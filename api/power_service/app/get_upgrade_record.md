> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_upgrade_record

## Purpose

Reads the firmware upgrade history for the firmware update record pages (callers `FirmwareUpdateRecordLogic::onReady`, `FirmwareUpdatesHistoryLogic::getUpgradeRecordReq`, `A5101BaseOTALogic::getOtaUpgradeRecord`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`get_upgrade_record` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/get_upgrade_record` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x291210c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2912104`, in `HttpRequestControllerImpl::getUpgradeRecord` (`charging/http/http_request_repository_impl.dart @0x2912048`), sent through `encryptionRequestHttp` (`@0x2912134`).

Same URL and method object in the other sender(s) read:

- `POST /power_service/v1/app/get_upgrade_record` (asm-traced): URL string at `charging/ui/page/device/a5101/ota/a5101_base_ota_logic.dart @0x28d9ed8`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x28d9ed0`, in `A5101BaseOTALogic::getOtaUpgradeRecord` (`charging/ui/page/device/a5101/ota/a5101_base_ota_logic.dart @0x28d9db0`), sent through `requestHttp` (`@0x28d9efc`).
- `POST /power_service/v1/app/get_upgrade_record` (asm-traced): URL string at `charging/ui/page/device/a5101/setting/firmware_update_record/firmware_update_record_logic.dart @0x2971784`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x297177c`, in `FirmwareUpdateRecordLogic::_getOtaUpgradeRecord` (`charging/ui/page/device/a5101/setting/firmware_update_record/firmware_update_record_logic.dart @0x297165c`), sent through `requestHttp` (`@0x29717ac`).

## Encrypted?

Three senders (asm-traced). `getUpgradeRecord` (`charging/http/http_request_repository_impl.dart @0x2912048`) goes through `encryptionRequestHttp`. The two A5101 senders call the plain wrapper `BaseGetController::requestHttp` (`charging/base/get/getx_controller.dart @0x230eaa8`): `getOtaUpgradeRecord` at `charging/ui/page/device/a5101/ota/a5101_base_ota_logic.dart @0x28d9efc` and `_getOtaUpgradeRecord` at `charging/ui/page/device/a5101/setting/firmware_update_record/firmware_update_record_logic.dart @0x29717ac`, both without a `needEncryption` argument. In all three the default `needEncryption: true` applies and rule 3 of [encryption.md](../../encryption.md#rule-and-resulting-counts) holds: the SDK path is taken whenever the SDK reports a logged-in state and the URL passes the base-URL predicate, otherwise the plain Dio path; that is decided at run time by `HttpEncryptionDecorator::request` (`charging/http/HttpEncryptionDecorator.dart @0x4868ff4`), not by this page.

## Request

(asm-traced) Three senders, each with one `<String, Object>` literal (type arguments `@0x29120c0`, `charging/ui/page/device/a5101/ota/a5101_base_ota_logic.dart @0x28d9e88`, `charging/ui/page/device/a5101/setting/firmware_update_record/firmware_update_record_logic.dart @0x2971734`). `HttpRequestControllerImpl::getUpgradeRecord` (`charging/http/http_request_repository_impl.dart @0x2912048`) sends `{type, device_sn}` with `type` = the constant raw 2, so 1 (`@0x29120a4`). `A5101BaseOTALogic::getOtaUpgradeRecord` and `FirmwareUpdateRecordLogic::_getOtaUpgradeRecord` send `{type, site_id}` with `type` = the constant raw 4, so 2 (`@0x28d9dfc`, `@0x29716a8`); `site_id` is a field of the `A5101MqttLogic` object they look up with `safeFind`.

| field | type | required | example | source |
|---|---|---|---|---|
| `type` | int (Smi, w) | yes | `1` (`getUpgradeRecord`), `2` (the two A5101 senders) | `charging/http/http_request_repository_impl.dart @0x291209c`; `charging/ui/page/device/a5101/ota/a5101_base_ota_logic.dart @0x28d9df4`; `charging/ui/page/device/a5101/setting/firmware_update_record/firmware_update_record_logic.dart @0x29716a0` |
| `device_sn` | ? | yes (`getUpgradeRecord` only) | ? | `charging/http/http_request_repository_impl.dart @0x29120ac` |
| `site_id` | ? | yes (A5101 senders only) | ? | `charging/ui/page/device/a5101/ota/a5101_base_ota_logic.dart @0x28d9e04` |

## `param_type`/`cmd`

n/a

## Response model (link)

- [`UpgradeRecordModel`](../../../models/firmware.md#upgraderecordmodel), parsed by `UpgradeRecordModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x2912188`. Model of `getUpgradeRecord`.
- `charging::OtaUpgradeRecordListModel`, parsed by `OtaUpgradeRecordListModel.fromJson` at `charging/ui/page/device/a5101/ota/a5101_base_ota_logic.dart @0x28d9fb4`. Model of the two A5101 senders (`charging::OtaUpgradeRecordListModel`, no models page): the second sender parses it in its closure `@0x29717c8` (`charging/ui/page/device/a5101/setting/firmware_update_record/firmware_update_record_logic.dart @0x2971800`).

## Response

(asm-traced) For each sender that parses a model, the keys below are the top-level keys of the model; that sender adds no wrapper fields of its own in the code read.

- `UpgradeRecordModel` top-level keys (`data/models.json`, `charging::UpgradeRecordModel`): `device_sn` (String?), `site_id` (String?), `upgrade_record_list` (List).
- `OtaUpgradeRecordListModel` top-level keys (`data/models.json`, `charging::OtaUpgradeRecordListModel`): `device_sn` (String?), `site_id` (String?), `upgrade_record_list` (unknown).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "type": 1,
  "device_sn": "<?>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint). The A5101 senders send `{"type": 2, "site_id": "<?>"}`.

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getUpgradeRecord` @0x2912048 (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/device/a5101/ota/a5101_base_ota_logic.dart`: `getOtaUpgradeRecord` @0x28d9db0 (requestHttp, default `needEncryption: true`)
- `charging/ui/page/device/a5101/setting/firmware_update_record/firmware_update_record_logic.dart`: `_getOtaUpgradeRecord` @0x297165c (requestHttp, default `needEncryption: true`)

Called from:

- `charging/http/http_request_repository.dart::getUpgradeRecord`
- `charging/ui/page/device/a5101/setting/firmware_update_record/firmware_update_record_logic.dart::onReady`
- `charging/ui/page/user/firmware_updates/firmware_updates_history/firmware_updates_history_logic.dart::getUpgradeRecordReq`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of `device_sn` and `site_id` (a parameter and an object field; `<String, Object>` only says non-null).
- What the `type` values 1 and 2 select on the server (the senders send constants).
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
