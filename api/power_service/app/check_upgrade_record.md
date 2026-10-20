> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# check_upgrade_record

## Purpose

Checks whether firmware upgrade records exist for a device or a list of devices (callers `AtsOtaLogic::getCheckUpgradeRecordApi`, `AnkerOtaBaseLogic::getCheckUpgradeRecordApi`, `FirmwareUpdatesLogic::getCheckUpgradeRecord`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`check_upgrade_record` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/check_upgrade_record` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x29139f4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x29139ec`, in `HttpRequestControllerImpl::checkUpgradeRecord` (`charging/http/http_request_repository_impl.dart @0x2913854`), sent through `encryptionRequestHttp` (`@0x2913a1c`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) The builder `HttpRequestControllerImpl::checkUpgradeRecord` (`charging/http/http_request_repository_impl.dart @0x2913854`) chooses one of three `<String, Object>` literals (`@0x29138e4`, `@0x2913968`, `@0x29139a8`) by null checks on its parameters (`cmp w0, NULL` `@0x29138a4`, `cmp w3, NULL` `@0x2913900`): `{device_sn, type}` when the device parameter is not null, else `{device_sns, type}` when the list parameter is not null (and `tbnz` `@0x2913928` passes), else `{type}` alone. All values are parameters of the builder.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | optional (parameter not null, guard `@0x29138a4`) | ? | `charging/http/http_request_repository_impl.dart @0x29138bc` |
| `device_sns` | ? | optional (list parameter not null, guard `@0x2913900`) | ? | `charging/http/http_request_repository_impl.dart @0x2913940` |
| `type` | ? | yes (stored in all three literals) | ? | `charging/http/http_request_repository_impl.dart @0x29138d0`, `@0x2913954`, `@0x2913994` |

## `param_type`/`cmd`

n/a

## Response model (link)

- [`CheckUpgradeRecordModel`](../../../models/firmware.md#checkupgraderecordmodel), parsed by `CheckUpgradeRecordModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x2913a70`

## Response

(asm-traced) All keys belong to the model page; this endpoint adds no wrapper fields of its own in the code read.

- `CheckUpgradeRecordModel` top-level keys (`data/models.json`, `charging::CheckUpgradeRecordModel`): `is_record` (bool?), `device_list` (List).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<?>",
  "type": "<?>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `checkUpgradeRecord` @0x2913854 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::checkUpgradeRecord`
- `charging/ui/page/device/anker_ota/ats_ota/ats_ota_logic.dart::getCheckUpgradeRecordApi`
- `charging/ui/page/device/anker_ota/base/anker_ota_base_logic.dart::getCheckUpgradeRecordApi`
- `charging/ui/page/user/firmware_updates/firmware_updates_page/firmware_updates_logic.dart::getCheckUpgradeRecord`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of `device_sn`, `device_sns` and `type` (all parameters; `<String, Object>` only says non-null) and which `type` values the three callers pass.
- The `tbnz` at `@0x2913928` (a boolean test between the list check and the second literal) was not attributed to a parameter name.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
