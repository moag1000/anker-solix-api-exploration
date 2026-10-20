> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

3.24.3: string present in the object pool, no code reference found (present in 3.18.0 with a sender)

# set_port_protocol_status

## Purpose

Saves the per-port protocol selection of a charger from the custom-protocol manager (callers `saveToAllPorts` in `CustomProtocolManagerLogic` and the A2345 protocol-manage logic) (string-only: the sender body is not in the asm dump; the caller names are read, the meaning comes from names only).

## Upstream name

`none` (no upstream name)

## Method+URL

`/mini_power/v1/app/setting/set_port_protocol_status`, method: not extracted (string-only). The 3.24.3 object pool holds the URL string (`pp+0xa3890`), but no decoded function references it: the senders are mixin-deduplicated functions (`[dart:mixin_deduplication]`) whose bodies Blutter did not write to the asm dump, so neither the method object nor the key stores can be read. Call sites in 3.24.3:

- `small_charging_platform/src/custom_protocol/page/custom_protocol_manager_logic.dart`: `saveToAllPorts` (`@0x3a7764c`) calls the mixin function at `@0x3a77738`, passing an instance of `PortProtocolSetType` (`@0x3a77730`); a second call is at `@0x3a78360`.
- `charging/ui/page/device/a2345/a2345prococol_manage/a2345protocol_manage_logic.dart`: calls at `@0x3e646c8` and `@0x3e65558`.

## Encrypted?

encrypted: `true` per the 3.18.0 inventory (`encryptionRequestHttp`); not re-read in 3.24.3 because the sender body is not in the asm dump. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

Not re-read in 3.24.3: the sender is a mixin-deduplicated function whose body is not in the asm dump (see Method+URL), so the keys below are the 3.18.0 inventory rows (`data/endpoints.json`); their addresses do not exist in the 3.24.3 asm and are therefore not cited. No type, requiredness or value is read.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | 3.18.0 inventory row, not present in the 3.24.3 asm |
| `version` | ? | ? | ? | 3.18.0 inventory row, not present in the 3.24.3 asm |
| `type` | ? | ? | ? | 3.18.0 inventory row, not present in the 3.24.3 asm |
| `port_list` | ? | ? | ? | 3.18.0 inventory row, not present in the 3.24.3 asm |

## `param_type`/`cmd`

n/a

## Response model (link)

not extracted: the sender body is not in the asm dump, so the response handling cannot be read (the callbacks passed at the call site are closures `@0x3a77ae8` and `@0x3a77a0c` of `small_charging_platform/src/custom_protocol/page/custom_protocol_manager_logic.dart`, not read).

## Response

No response key is confirmed read (see Response model).

## Example request/response

Request: not synthesized (the keys are not re-read in 3.24.3, see Request).

Response: not synthesized (no capture exists for this endpoint).

## Errors seen

none traced: the sender body is not in the asm dump, so the failure path of the request is not readable. Code meanings are owned by `api/errors.md`.

## Callers in app

- `small_charging_platform/src/custom_protocol/page/custom_protocol_manager_logic.dart`: `setPortProtocolStatus` (3.18.0 inventory, encryptionRequestHttp; address not present in the 3.24.3 asm)

## Since/changed

3.18.0: present (with a sender in the inventory). 3.24.3: the URL string is in the object pool (`pp+0xa3890`) and the callers listed under Method+URL still call the sender, but the sender body is not in the asm dump; `tools/out/diff_3.18.0_3.24.3.md` lists the URL under Removed endpoints (string-level). since: <=3.18.0. Treat the URL as still in use (the callers exist) until a capture says otherwise.

## Known unknowns

- The method, the request keys, their types and whether they are required: the sender body is not in the asm dump. The inventory rows are 3.18.0 data. The model `small_charging_platform::PortProtocolStatusResponse` has `toJson` (`small_charging_platform/src/custom_protocol/model/port_protocol_status_model.dart @0x2859c40`) and the manager logic calls it (`small_charging_platform/src/custom_protocol/page/custom_protocol_manager_logic.dart @0x2a24f9c`), which fits the keys `version` and `port_list`, but the link to this body was not read.
- What `type` takes (the call site `small_charging_platform/src/custom_protocol/page/custom_protocol_manager_logic.dart @0x3a77730` passes `Instance_PortProtocolSetType`); the enum values were not decoded.
- How the answer is used: the callbacks were not read.
- Header stays `string-only` because Method, request types and response handling are missing.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
