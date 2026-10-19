> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# Template: BLE command page

Copy to a section (or page) of `ble/<pn>.md`, the owner of BLE opcodes and TLV. Tags (see `METHODOLOGY.md`): `asm-traced` · `string-only` · `upstream-confirmed` · `device-tested`. Integers from asm follow the Smi rule in [../../METHODOLOGY.md](../../METHODOLOGY.md); cite `file.dart @0xADDR` next to every number. A fact lives on one owner page (see [../STRUCTURE.md](../STRUCTURE.md)); other pages link. Section order is fixed.

## Status header

One line, first line of the page: `> Verified against: App 3.24.3 · Date: YYYY-MM-DD · Confidence: <tag> · Owner page: <path or "this page">`.

## Purpose

One sentence: what the command does. Tag: any.

## Upstream name

Upstream (AnkerSolixBLE / SolixBLE / mqttmap) name, or `none` (mark ours `(no upstream name)`). Tag: `upstream-confirmed` if matched.

## Opcode

Opcode as in Dart. A hex string (`"005e"`) is a string literal, not Smi; an int literal follows the Smi rule. Tag: `asm-traced` / `string-only`.

## Direction

`app→device`, `device→app` or `both`. Tag: `asm-traced`.

## Packet framing

Link to `ble/protocol.md`; never restate frame layout. Tag: per owner page.

## Handshake prerequisite

Link to `ble/handshake.md`; state only whether the command needs a completed handshake. Tag: per owner page.

## TLV tags

Table `tag | name | type | length | source`. Integers follow the Smi rule. Tag: per row.

## Example

Code block preceded by a label line `captured (client, version, date)` or `synthesized`. Tag: `device-tested` only if captured and accepted.

## Related API endpoint

Link to the `api/<service>/<endpoint>.md` owner, or the MQTT twin in `mqtt/<pn>.md`. Tag: none.

## Since/changed

3.18.0 to 3.24.3 change. Tag: `asm-traced` (3.24.3 side).

## Known unknowns

Bullet list of open questions. Tag: none.

## Device-tested by

Who, device PN and firmware, client and version, date; `none` if untested. Tag: `device-tested`.

Every BLE page carries this note line, verbatim: `BLE is unavailable while the device is on WiFi; see ble/protocol.md` (link to the `ble/protocol.md` owner; do not restate details here).

---

**Example skeleton — placeholders only, not a fact page**

> Verified against: App 3.24.3 · Date: YYYY-MM-DD · Confidence: <tag> · Owner page: <path or "this page">

# A17C1 opcode `005e`

## Status header

(see first line above)

## Purpose

<one sentence>

## Upstream name

`<upstream_name>` or `none`

## Opcode

`<opcode>` — `<file.dart @0xADDR>`

## Direction

<app→device / device→app / both>

## Packet framing

`ble/protocol.md`

## Handshake prerequisite

`ble/handshake.md` — <needed / not needed>

## TLV tags

| tag | name | type | length | source |
|---|---|---|---|---|
| `<tag>` | <name> | <type> | <N> | `<file.dart @0xADDR>` |

## Example

synthesized

```
<hex bytes>
```

## Related API endpoint

`api/<service>/<endpoint>.md`

## Since/changed

3.18.0: <state>. 3.24.3: <state>.

## Known unknowns

- <open question>

## Device-tested by

<who>, <PN> fw <version>, <client version>, <YYYY-MM-DD>

BLE is unavailable while the device is on WiFi; see `ble/protocol.md`.
