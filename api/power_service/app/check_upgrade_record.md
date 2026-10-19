> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# check_upgrade_record

## Purpose

<!-- TODO -->

## Upstream name

`check_upgrade_record` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/app/check_upgrade_record`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x29139f4`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x2913854` |
| `type` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x2913854` |
| `device_sns` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x2913854` |

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

- `charging/http/http_request_repository_impl.dart`: `checkUpgradeRecord` @0x2913854 (encryptionRequestHttp; encrypted: true)

Called from: `charging/http/http_request_repository.dart::checkUpgradeRecord`, `charging/ui/page/device/anker_ota/ats_ota/ats_ota_logic.dart::getCheckUpgradeRecordApi`, `charging/ui/page/device/anker_ota/base/anker_ota_base_logic.dart::getCheckUpgradeRecordApi`, `charging/ui/page/user/firmware_updates/firmware_updates_page/firmware_updates_logic.dart::getCheckUpgradeRecord`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
