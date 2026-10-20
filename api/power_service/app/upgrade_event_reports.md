> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# upgrade_event_reports

## Purpose

Reports the results of several firmware upgrades at once: `getReportsBleUpgrade` is called from `AnkerOtaBaseLogic::handleA17A3BleOtaRecords`, `WifiBleOtaLogic::handleOtaRecordResult` and `WifiBleParallelOtaLogic::handleOtaRecordResult`; the OTA kit reporter `OTAUpgradeRecordReporter::_reportBatch` (`ota_kit/src/services/ota_upgrade_record_reporter.dart @0x280a11c`) sends the same URL through the IoT kit.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/upgrade_event_reports` (asm-traced): URL string at `http_request_repository_impl.dart @0x3423438`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3423430`, in `HttpRequestControllerImpl::getReportsBleUpgrade` (`http_request_repository_impl.dart @0x3423398`).

The IoT-kit sender `OTAUpgradeRecordReporter::_reportBatch` puts the path `"/power_service/v1/app/upgrade_event_reports"` (`ota_kit/src/services/ota_upgrade_record_reporter.dart @0x280a210`), the string literal `"POST"` (`@0x280a228`) and a `param` entry into a command map for `akIoTKitManager.handle` (`@0x280a358`); the method there is a string literal, not a `Method` pool object.

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `upgrade_even_device_infos` | ? | yes | | key `http_request_repository_impl.dart @0x34233e0` (sic `even`) in the repository sender `getReportsBleUpgrade` (function `@0x3423398`): 1-pair map literal (`AllocateArray r2 = 4` `@0x34233d8`, no printed type arguments), value store `@0x34233f0` (parameter at `fp-0x10`) |
| `upgrade_even_device_infos` | list | yes | | IoT-kit sender `_reportBatch`: key `ota_kit/src/services/ota_upgrade_record_reporter.dart @0x280a250`, `param` map typed `<String, List<Map<String, dynamic>>>` (`@0x280a2f4`); the elements are `<Map<String, dynamic>>` (`@0x280a278`) |

## `param_type`/`cmd`

n/a

## Response model (link)

None: the response body is not parsed. The repository sender passes the forwarding template `rx_workers.dart @0x228e574`; the callers' shared success callback `anker_ota_base_logic.dart @0x3423588` loads no argument and logs `"======多包上报成功========="` before `exeSuccess()`. Not read for the IoT-kit sender.

## Response

No response key is read by the repository sender's callers.

## Example request/response

Request, synthesized (IoT-kit sender; element keys unknown)

```json
{"upgrade_even_device_infos": [{}]}
```

Response: none parsed.

## Errors seen

None traced. No compare was found in the callbacks read. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getReportsBleUpgrade` @0x3423398 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `ota_kit/src/services/ota_upgrade_record_reporter.dart`: `_reportBatch` @0x280a11c (URL literal only, no `*Http*` call; sends in the same function (`AKIoTKitManagerImpl::handle`); resolved from the URL literal at `ota_kit/src/services/ota_upgrade_record_reporter.dart @0x280a210` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))

Called from:

- `charging/http/http_request_repository.dart::getReportsBleUpgrade`
- `charging/ui/page/device/a1780p/ota/wifi_ble_ota_logic.dart::handleOtaRecordResult`
- `charging/ui/page/device/a1780p/parallel_ota/wifi_ble_parallel_ota_logic.dart::handleOtaRecordResult`
- `charging/ui/page/device/anker_ota/base/anker_ota_base_logic.dart::handleA17A3BleOtaRecords`
- `ota_kit/src/services/ota_upgrade_record_reporter.dart::report`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. `tools/out/diff_3.18.0_3.24.3.md` (changed params) lists `method`, `param.upgrade_even_device_infos` and `path` as added: these are the key names of the IoT-kit command map of `_reportBatch` (`@0x280a208`..`@0x280a250`).

## Known unknowns

- Type and element keys of the repository sender's `upgrade_even_device_infos` parameter (the three callers were not followed). Header stays string-only. — attempted 2026-10-20 (two-hop not readable: the three callers (`WifiBleParallelOtaLogic.handleOtaRecordResult`, `WifiBleOtaLogic.handleOtaRecordResult`, `AnkerOTABaseLogic.handleA17A3BleOtaRecords`) log the string " maps = " and pass maps built locally; their element keys were not followed)
- Whether the element keys equal those of [upgrade_event_report](upgrade_event_report.md) (the batch maps are `Map<String, dynamic>`). — traced 2026-10-20: not decoded in this pass (element keys of the batch maps); the reason given in the bullet stands
- The response body: not read. — reclassified: server

## Device-tested by

none
