> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# Methodology

This page defines how every fact in this repository is gathered, how numbers read from the decompiled app are interpreted, and how confident a reader may be in a given statement. Every other page links here instead of repeating these rules.

## Sources and priority

Evidence comes from three sources, in this order of priority:

1. **Blutter asm of App 3.24.3** is the primary evidence. It is the current app, so a cited asm site (`file.dart @0xADDR`) is the strongest statement we can make about what the app does. Only this source can earn `asm-traced`; it can also earn `string-only`.
2. **Blutter asm of App 3.18.0** is used for diffs only, to say what changed since the previous version. It never confirms a fact about 3.24.3 on its own. Facts that exist only in 3.18.0 are history, not current behavior.
3. **Upstream code and live device tests** are used for confirmation. The code of [thomluther/anker-solix-api](https://github.com/thomluther/anker-solix-api) (community-tested on real devices) can earn `upstream-confirmed`. A request that someone actually sent to a real device, with the recorded response, can earn `device-tested`.

When sources disagree, the higher-priority source wins for what the app sends, and the disagreement is documented rather than silently resolved. When a device test contradicts the asm reading, the device result is recorded as `device-tested` and the asm reading stays as a note: the device is the final authority for what the server accepts, and asm is the authority for what the app sends. Upstream names (`apitypes.py` keys, `mqttmap` names) win over ours; a name of ours is marked `(no upstream name)`.

## Confidence tags

Every page carries one of exactly these four tags in its status header, and individual claims may carry them inline.

- `asm-traced`: the fact is backed by a cited asm site in the 3.24.3 Blutter output (`file.dart @0xADDR`), and the Smi rule below has been applied to any integer. Only 3.24.3 asm earns this tag; 3.18.0 asm never does.
- `string-only`: the string exists in the 3.24.3 binary (`pp.txt` or `strings`), but no call site in the 3.24.3 asm has been traced; a mere cross-reference without a traced caller still counts as string-only. Strings seen only in 3.18.0 are not documented as current facts at all; they appear only in "changed since" notes.
- `upstream-confirmed`: the fact matches code in thomluther/anker-solix-api that the community runs against real accounts and devices; name the upstream file and symbol.
- `device-tested`: a real device accepted or rejected the exact payload; any client counts (official app capture, upstream library, raw request), and the record must name client and version, device PN and firmware, date, and who tested.

The tags are ranked `device-tested` > `upstream-confirmed` > `asm-traced` > `string-only`. A fact can earn more than one tag over time, and the status-header tag of a page is the LOWEST tag among the facts on that page, i.e. the tag that covers every fact; stronger claims on a mixed page may carry their own tag inline.

## Smi rule: reading numbers from Blutter output

This rule originated in an internal audit note on 2026-10-19; this page is the authoritative copy, and it must be read before auditing any number.

Blutter prints register immediates RAW, e.g. `r16 = 246` for `mov x16, #0xf6`. Dart on arm64 stores small integers as **Smi = value << 1** (tagged). So a raw immediate that ends up in a *tagged* slot represents value/2.

### How to decide, per site

Look at the instructions right after the immediate.

| Evidence after `mov xN, #imm` | Meaning | Real value |
|---|---|---|
| `stur wN, [xM, #off]` / `str wN, ...` (32-bit store into object field or array slot) | tagged Smi | **imm / 2** |
| passed as array element / map literal value (AllocateArray + StoreField w) | tagged Smi | **imm / 2** |
| `cmp wN, #imm` against a loaded tagged field | tagged Smi | **imm / 2** |
| `r2 = N` right before `AllocateArray()` | array length (Smi) | **N / 2** elements |
| `stur xN, [xM, #off]` (64-bit store into unboxed int field) | unboxed | **imm** |
| used in arithmetic (`add/sub/mul/sbfx`) or `BoxInt64Instr(rN)` input | unboxed | **imm** |
| `LoadInt32Instr(rN)` = `sbfx x, w, #1, #0x1f` | untagging a Smi | the *result* is real |
| string literal `"19"` | string | as is |

An odd raw immediate in a tagged slot is impossible. If you see a raw odd value stored with `stur w`, re-check it: it is probably a pointer, bool or null, not an int.

### Verified examples (3.18.0 and 3.24.3 asm)

- `setSiteDeviceParam`: `mov x16, #0x22 (34)` + `stur w16` gives cmd = **17** (matches thomluther's community-tested cmd=17).
- `setSiteDevicePowerLimit`: `mov x16, #0xf6 (246)` + `stur w16` gives cmd = **123** (the old docs wrongly say 246).
- MQTT head in the old docs `cmd_status: 4, sign_code: 2, msg_seq: 2` versus upstream community-tested `cmd_status: 2, sign_code: 1, msg_seq: 1`: all of the old docs values were raw Smi (2x).
- `auto_disaster.dart`: `"disaster_type"` then `r17 = 4` + `stur w17` gives disaster_type = **2** (old docs say 4). `is_ble` raw 4 gives **2**.
- `showOutputPowerPicker`: `mov x0, #0x64` + `stur x0` (64-bit) gives min = **100** W (unboxed, real). `mov x1, #0xa` + `stur x1` gives step = **10** W.

### Consequence

EVERY number in the exploration docs that came from a Blutter immediate (cmd codes, enum ints, default values, type ids, flags, lengths, hardcoded ids) must be re-checked at the asm site, and the asm site is cited next to the number. Numbers that came from string literals ("19", "6"), from pp.txt strings, from live mqtt_monitor captures, or from upstream code are NOT affected.

## Known server tolerances

This section is intentionally empty for now. It will record cases where the server accepts values different from what the app sends (for example cmd 17 versus 123 for the power-limit call; to be recorded), each with the tag that earned it.
