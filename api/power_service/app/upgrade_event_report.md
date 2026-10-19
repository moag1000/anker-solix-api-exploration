> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# upgrade_event_report

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/app/upgrade_event_report`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x34227b4`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3422678` |
| `device_pn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3422678` |
| `device_type` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3422678` |
| `upgrade_type` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3422678` |
| `after_version` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3422678` |
| `before_version` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3422678` |
| `upgrade_time` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3422678` |
| `site_id` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3422678` |
| `path` | ? | ? | ? | `ota_kit/src/services/ota_upgrade_record_reporter.dart @0x280a890` |
| `method` | ? | ? | ? | `ota_kit/src/services/ota_upgrade_record_reporter.dart @0x280a890` |
| `param` | ? | ? | ? | `ota_kit/src/services/ota_upgrade_record_reporter.dart @0x280a890` |

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

- `charging/http/http_request_repository_impl.dart`: `getReportBleUpgrade` @0x3422678 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `ota_kit/src/services/ota_upgrade_record_reporter.dart`: `_reportSingle` @0x280a890 (URL literal only, no `*Http*` call; sends in the same function (`AKIoTKitManagerImpl::handle`); resolved from the URL literal at `ota_kit/src/services/ota_upgrade_record_reporter.dart @0x280a8f4` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))

Called from:

- `charging/http/http_request_repository.dart::getReportBleUpgrade`
- `charging/ui/page/device/anker_ota/base/anker_ota_base_logic.dart::reportBleOtaRecord`
- `ota_kit/src/services/ota_upgrade_record_reporter.dart::report`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
