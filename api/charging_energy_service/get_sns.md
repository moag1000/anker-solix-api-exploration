> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_sns

## Purpose

Resolves device serial numbers from Bluetooth MAC addresses during the A17B1 firmware check (caller `FirmwareUpdateState::getDeviceSnByMac`, reached from `CheckUpdateLogic::matchDeviceMac`) (string-only: the meaning is taken from the function names).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_energy_service/get_sns` (asm-traced): URL string `@0x36dd76c`, method object `Method.post` (pool entry `pp+0xa7e0`) `@0x36dd764`, in `FirmwareUpdateState::getDeviceSnByMac` (`charging/ui/page/device/a17b1/check_update/check_update_logic.dart @0x36dd6a0`), sent through `BaseGetController::requestHttp` (`@0x36dd790`; argument descriptor `@0x36dd788` names `fail` and `success`).

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(string-only: both field types are not read) One sender. The map literal has the type arguments `<String, Object>` (`charging/ui/page/device/a17b1/check_update/check_update_logic.dart @0x36dd720`), which name no value type; both keys are stored without a guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `main_sn` | ? | yes | `"<main_sn>"` | `charging/ui/page/device/a17b1/check_update/check_update_logic.dart @0x36dd6f8` (value store `@0x36dd708`, parameter) |
| `macs` | ? | yes | `["<mac>"]` | `charging/ui/page/device/a17b1/check_update/check_update_logic.dart @0x36dd70c` (value store `@0x36dd71c`, parameter) |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed in this function: the success closure (`charging/ui/page/device/a17b1/check_update/check_update_logic.dart @0x36dd818`) passes its argument unchanged to a stored callback (dispatch-table call `@0x36dd860`) and reads no key; `CheckUpdateLogic::matchDeviceMac` was not read.

## Response

No response key is read by the sender (see Response model).

Parse (traced 2026-10-20, app side): the success closure of `CheckUpdateLogic::matchDeviceMac` (`charging/ui/page/device/a17b1/check_update/check_update_logic.dart @0x36dd8c4`, argument `dynamic`) cancels a timer field (`cancel` `@0x36dd904`), requires the answer to be a `Map` (`r8 = Map` `@0x36dd99c`) and reads the key `mac_sn_map` (`@0x36dd9d8`) as a `Map` (`@0x36dd9fc`) from MAC to serial number; it then walks that map (`@0x36dda1c`..`@0x36ddb30`, texts `scanXXDevice`) and builds a list (`toList` `@0x36ddba4`). The failure closure (`@0x36dd87c`) calls `resetState` (`@0x36dd8a8`).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "main_sn": "<main_sn>",
  "macs": ["<mac>"]
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure only logs `code` and `msg`). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/device/a17b1/check_update/check_update_logic.dart`: `getDeviceSnByMac` @0x36dd6a0 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/ui/page/device/a17b1/check_update/check_update_logic.dart::matchDeviceMac`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of `main_sn` and `macs`: parameters; the literal `<String, Object>` names no value type. `macs` as a list of MAC strings follows from the function name only. — attempted 2026-10-20 (two-hop not readable: `matchDeviceMac` (`charging/ui/page/device/a17b1/check_update/check_update_logic.dart @0x36dd654`) pass slots or fields of their own frames; no literal or declared type in the argument setups)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
