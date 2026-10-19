> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_upgrade_record

## Purpose

<!-- TODO -->

## Upstream name

`get_upgrade_record` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/app/get_upgrade_record`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x291210c`
(literal also at 2 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify" / `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `type` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x2912048` |
| `device_sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x2912048` |
| `site_id` | ? | ? | ? | `charging/ui/page/device/a5101/ota/a5101_base_ota_logic.dart @0x28d9db0` |

Rows are the union over 3 senders; `source` is the first sender that sets the key.

## `param_type`/`cmd`

n/a

## Response model (link)

<!-- TODO -->

## Response

<!-- TODO -->

## Example request/response

<!-- TODO -->

## Errors seen

`api/errors.md`: <!-- TODO -->

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getUpgradeRecord` @0x2912048 (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/device/a5101/ota/a5101_base_ota_logic.dart`: `getOtaUpgradeRecord` @0x28d9db0 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/ui/page/device/a5101/setting/firmware_update_record/firmware_update_record_logic.dart`: `_getOtaUpgradeRecord` @0x297165c (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from: `charging/http/http_request_repository.dart::getUpgradeRecord`, `charging/ui/page/device/a5101/setting/firmware_update_record/firmware_update_record_logic.dart::onReady`, `charging/ui/page/user/firmware_updates/firmware_updates_history/firmware_updates_history_logic.dart::getUpgradeRecordReq`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
