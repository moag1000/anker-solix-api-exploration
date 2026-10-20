> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

3.24.3: string present in the object pool, no code reference found (present in 3.18.0 with a sender)

# get_port_protocol_status

## Purpose

Reads the per-port protocol status of a charger for the custom-protocol manager and the online listener (callers `_fetchPortsData` in `CustomProtocolManagerLogic`, `_getPortProtocolStatusWithRetry` in `CustomProtocolDeviceOnlineListener` and the A2345 protocol-manage logic) (string-only: the sender body is not in the asm dump; the caller names are read, the meaning of the status comes from names only).

## Upstream name

`none` (no upstream name)

## Method+URL

`/mini_power/v1/app/setting/get_port_protocol_status`, method: not extracted (string-only). The 3.24.3 object pool holds the URL string (`pp+0x5b990`), but no decoded function references it: the senders are mixin-deduplicated functions (`[dart:mixin_deduplication]`) whose bodies Blutter did not write to the asm dump, so neither the method object nor the key stores can be read. Call sites in 3.24.3:

- `small_charging_platform/src/custom_protocol/page/custom_protocol_manager_logic.dart`: `_fetchPortsData` (`@0x2a24a1c`) calls the mixin function at `@0x2a24ad0`.
- `small_charging_platform/src/custom_protocol/device_online_listener.dart`: `_getPortProtocolStatusWithRetry` (`@0x285874c`) calls it at `@0x2858888`.
- `charging/ui/page/device/a2345/a2345prococol_manage/a2345protocol_manage_logic.dart`: call at `@0x28667b4`.
- `charging/ble/device/A2345/a2345_device_controller.dart`: call at `@0x3b2f868`.

## Encrypted?

encrypted: `true` per the 3.18.0 inventory (`encryptionRequestHttp`); not re-read in 3.24.3 because the sender body is not in the asm dump. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

Not re-read in 3.24.3: the sender is a mixin-deduplicated function whose body is not in the asm dump (see Method+URL), so the keys below are the 3.18.0 inventory rows (`data/endpoints.json`); their addresses do not exist in the 3.24.3 asm and are therefore not cited. No type, requiredness or value is read.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | 3.18.0 inventory row, not present in the 3.24.3 asm |
| `version` | ? | ? | ? | 3.18.0 inventory row, not present in the 3.24.3 asm |

## `param_type`/`cmd`

n/a

## Response model (link)

- `small_charging_platform::PortProtocolStatusResponse` (`data/models.json`; no page under `models/`), applied to the response by the success callback of the online listener: `PortProtocolStatusResponse.fromJson` at `small_charging_platform/src/custom_protocol/device_online_listener.dart @0x2858ba4` (callback closure `@0x2858b0c`, argument cast `Map<String, dynamic>?` `@0x2858b98`), and by the manager logic at `small_charging_platform/src/custom_protocol/page/custom_protocol_manager_logic.dart @0x2a246b0` (string-only for this URL: the sender body, which would show that the callbacks receive this endpoint's body unchanged, is not in the dump).

## Response

Keys of the model the callbacks apply (`data/models.json`, `small_charging_platform::PortProtocolStatusResponse`): `version` (String?) and `port_list` (field type not extracted).

## Example request/response

Request: not synthesized (the keys are not re-read in 3.24.3, see Request).

Response: not synthesized (no capture exists for this endpoint).

## Errors seen

none traced: the sender body is not in the asm dump, so the failure path of the request is not readable. Code meanings are owned by `api/errors.md`.

## Callers in app

- `small_charging_platform/src/custom_protocol/device_online_listener.dart`: `getPortProtocolStatus` (3.18.0 inventory, encryptionRequestHttp; address not present in the 3.24.3 asm)
- `small_charging_platform/src/custom_protocol/page/custom_protocol_manager_logic.dart`: `getPortProtocolStatus` (3.18.0 inventory, encryptionRequestHttp; address not present in the 3.24.3 asm)

## Since/changed

3.18.0: present (with a sender in the inventory). 3.24.3: the URL string is in the object pool (`pp+0x5b990`) and the callers listed under Method+URL still call the sender, but the sender body is not in the asm dump; `tools/out/diff_3.18.0_3.24.3.md` lists the URL under Removed endpoints (string-level: the inventory finds no code reference). since: <=3.18.0. Treat the URL as still in use (the callers exist) until a capture says otherwise.

## Known unknowns

- The method, the request keys, their types and whether they are required: the sender body is not in the asm dump (mixin-deduplicated function). The inventory rows `device_sn` and `version` are 3.18.0 data.
- Whether the callbacks receive the response body unchanged: the sender body was not read, so `PortProtocolStatusResponse` is only the model the callers apply.
- Why the diff lists the URL under "Removed endpoints": the inventory finds no code reference to the string in 3.24.3, while the callers still `bl` into the mixin function.
- The element shape of `port_list` (`unknown` in `data/models.json`).
- Header stays `string-only` because Method and request types are missing. — rechecked 2026-10-20: still true; the typing attempts are recorded on the bullets of this section
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
