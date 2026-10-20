> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# check_upgrade_record

## Purpose

Checks whether firmware upgrade records exist for a device or a list of devices (callers `AtsOtaLogic::getCheckUpgradeRecordApi`, `AnkerOTABaseLogic::getCheckUpgradeRecordApi`, `FirmwareUpdatesLogic::getCheckUpgradeRecord`) (asm-traced, caller chain in `data/endpoints.json`).

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
| `type` | int (Smi, w) | yes (stored in all three literals) | | `charging/http/http_request_repository_impl.dart @0x29138d0`, `@0x2913954`, `@0x2913994` |

Typing and caller values (asm-traced): the builder `HttpRequestControllerImpl::checkUpgradeRecord` (`charging/http/http_request_repository_impl.dart @0x2913854`, untyped `SetupParameters(dynamic _ ...)` `@0x2913860`) holds `type` as an unboxed integer parameter (`fp-0x28`) and tags it with `lsl x1, x2, #1` (`@0x29138dc`) before the 32-bit store into the literal (`@0x29138e0`), so the sent value is the integer itself. The `tbnz` at `@0x2913928` tests the boolean result of a dispatch-table call made on the `device_sns` parameter (`@0x2913914`, selector not named by Blutter; the test is on a list-like value): when that result is false (bit 4 set) the code jumps to the `{type}`-only literal (`@0x291397c`). Callers: `FirmwareUpdatesLogic.getCheckUpgradeRecord` (`charging/ui/page/user/firmware_updates/firmware_updates_page/firmware_updates_logic.dart @0x2913744`) passes no device argument (descriptor without named parameters `r4 = const [0, 0x3, 0, 0x3, null]` `@0x2913740`) and `type` = 3 (`r3 = 3` `@0x291373c`, an unboxed register, so real 3); `AtsOtaLogic.getCheckUpgradeRecordApi` (`charging/ui/page/device/anker_ota/ats_ota/ats_ota_logic.dart @0x3733f38`) passes the named argument `deviceSns` (`@0x3733f30`) and `type` = 1 (`r3 = 1` `@0x3733f2c`); `AnkerOtaBaseLogic.getCheckUpgradeRecordApi` (`charging/ui/page/device/anker_ota/base/anker_ota_base_logic.dart @0x3734424`) passes the named argument `deviceSn` (`@0x373441c`) and `type` = 1 (`r3 = 1` `@0x3734418`).

## `param_type`/`cmd`

n/a

## Response model (link)

- [`CheckUpgradeRecordModel`](../../../models/firmware.md#checkupgraderecordmodel), parsed by `CheckUpgradeRecordModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x2913a70`

## Response

(asm-traced) For each sender that parses a model, the keys below are the top-level keys of the model; that sender adds no wrapper fields of its own in the code read.

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

- Types of `device_sn` and `device_sns` (named arguments of two callers: `charging/ui/page/device/anker_ota/base/anker_ota_base_logic.dart @0x373441c`, `charging/ui/page/device/anker_ota/ats_ota/ats_ota_logic.dart @0x3733f30`) — attempted 2026-10-20 (two-hop not readable: both values come from field or dispatch-table reads with no declared type shown in the asm (`anker_ota_base_logic.dart @0x37343c0`..`@0x37343e0`). Header stays string-only)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
