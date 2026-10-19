> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# upgrade_event_reports

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/app/upgrade_event_reports`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x3423438`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `upgrade_even_device_infos` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3423398` |
| `path` | ? | ? | ? | `ota_kit/src/services/ota_upgrade_record_reporter.dart @0x280a11c` |
| `param.upgrade_even_device_infos` | ? | ? | ? | `ota_kit/src/services/ota_upgrade_record_reporter.dart @0x280a11c` |

Rows are the union over 2 senders; `source` is the first sender that sets the key.

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

- `charging/http/http_request_repository_impl.dart`: `getReportsBleUpgrade` @0x3423398 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `ota_kit/src/services/ota_upgrade_record_reporter.dart`: `_reportBatch` @0x280a11c (URL literal only, no `*Http*` call)

Called from:

- `charging/http/http_request_repository.dart::getReportsBleUpgrade`
- `charging/ui/page/device/a1780p/ota/wifi_ble_ota_logic.dart::handleOtaRecordResult`
- `charging/ui/page/device/a1780p/parallel_ota/wifi_ble_parallel_ota_logic.dart::handleOtaRecordResult`
- `charging/ui/page/device/anker_ota/base/anker_ota_base_logic.dart::handleA17A3BleOtaRecords`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
