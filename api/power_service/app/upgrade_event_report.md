> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# upgrade_event_report

## Purpose

Reports the result of one firmware upgrade: `AnkerOtaBaseLogic::reportBleOtaRecord` (`anker_ota_base_logic.dart @0x342243c`) calls `getReportBleUpgrade`, and the OTA kit reporter `OTAUpgradeRecordReporter::_reportSingle` (`ota_upgrade_record_reporter.dart @0x280a890`, called from `report`) sends the same URL through the IoT kit.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/upgrade_event_report` (asm-traced): URL string at `http_request_repository_impl.dart @0x34227b4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x34227ac`, in `HttpRequestControllerImpl::getReportBleUpgrade` (`http_request_repository_impl.dart @0x3422678`).

The IoT-kit sender `OTAUpgradeRecordReporter::_reportSingle` puts the path `"/power_service/v1/app/upgrade_event_report"` (`ota_kit/src/services/ota_upgrade_record_reporter.dart @0x280a8f4`), the string literal `"POST"` (`@0x280a90c`) and a `param` entry into a command map for `akIoTKitManager.handle` (`@0x280a97c`); the method there is a string literal, not a `Method` pool object.

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The repository sender `getReportBleUpgrade` (`http_request_repository_impl.dart @0x3422678`) builds an 8-pair map literal (`AllocateArray r2 = 32` `@0x34226c4`); the map has no printed type arguments, so the value types come from the parameters.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | yes | | key `@0x34226cc`, value store `@0x34226dc` (parameter at `fp-0x10`) |
| `device_pn` | ? | yes | | key `@0x34226e0`, value store `@0x34226f0` (parameter at `fp-0x18`) |
| `device_type` | ? | yes | | key `@0x34226f4`, value store `@0x3422704` (stack parameter `fp+0x20`) |
| `upgrade_type` | int (Smi, w) | yes | | key `@0x3422708`, `lsl x2, x1, #1` `@0x3422718` Smi-tags the unboxed stack parameter, store `@0x342271c` |
| `after_version` | ? | yes | | key `@0x3422720`, value store `@0x3422730` (parameter at `fp-0x20`) |
| `before_version` | ? | yes | | key `@0x3422734`, value store `@0x3422744` (parameter at `fp-0x28`) |
| `upgrade_time` | ? | yes | | key `@0x3422748`, value store `@0x3422758` (parameter at `fp-0x30`) |
| `site_id` | string | yes | `""` | key `@0x342275c`, literal empty string `@0x3422768`, store `@0x342276c` |

The IoT-kit sender's `param` entry is the result of `toMap()` on a record object (`ota_kit/src/services/ota_upgrade_record_reporter.dart @0x280a928`); its keys were not read.

## `param_type`/`cmd`

n/a

## Response model (link)

None: the response body is not parsed. The repository sender passes the forwarding template `rx_workers.dart @0x228e574`; the caller's success callback `anker_ota_base_logic.dart @0x34227f8` loads no argument and logs `"======上报成功========="` before `exeSuccess()`. Not read for the IoT-kit sender.

## Response

No response key is read by the repository sender's caller.

## Example request/response

Request, synthesized (types of the parameters unresolved)

```json
{"device_sn": "<device_sn>", "device_pn": "<device_pn>", "device_type": "<device_type>", "upgrade_type": "<upgrade_type>", "after_version": "<after_version>", "before_version": "<before_version>", "upgrade_time": "<upgrade_time>", "site_id": ""}
```

Response: none parsed.

## Errors seen

None traced. No compare was found in the callbacks read. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getReportBleUpgrade` @0x3422678 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `ota_kit/src/services/ota_upgrade_record_reporter.dart`: `_reportSingle` @0x280a890 (URL literal only, no `*Http*` call; sends in the same function (`AKIoTKitManagerImpl::handle`); resolved from the URL literal at `ota_kit/src/services/ota_upgrade_record_reporter.dart @0x280a8f4` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))

Called from:

- `charging/http/http_request_repository.dart::getReportBleUpgrade`
- `charging/ui/page/device/anker_ota/base/anker_ota_base_logic.dart::reportBleOtaRecord`
- `ota_kit/src/services/ota_upgrade_record_reporter.dart::report`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. `tools/out/diff_3.18.0_3.24.3.md` (changed params) lists `method`, `param` and `path` as added: these are the key names of the IoT-kit command map of `_reportSingle` (`@0x280a8ec`..`@0x280a918`).

## Known unknowns

- Types of `device_sn`, `device_pn`, `device_type`, `after_version`, `before_version` and `upgrade_time` (parameters; `reportBleOtaRecord` was not followed). Header stays string-only. — attempted 2026-10-20 (two-hop not readable: the only caller, `AnkerOTABaseLogic.reportBleOtaRecord` (`charging/ui/page/device/anker_ota/base/anker_ota_base_logic.dart @0x34225f0`), passes values with `""` defaults and an integer, but the slot-to-key mapping was not followed. Header stays string-only)
- The `toMap()` keys of the IoT-kit record and whether they equal the repository keys. — traced 2026-10-20: not decoded in this pass (IoT-kit `toMap()`); the reason given in the bullet stands
- The response body: not read by the repository caller; the IoT-kit callback was not read. — reclassified: server (the app does not read the body in the traced callers; its keys are not visible)

## Device-tested by

none
