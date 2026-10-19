> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_relate_and_bind_devices

## Purpose

<!-- TODO -->

## Upstream name

`bind_devices` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/app/get_relate_and_bind_devices`, method: not extracted by the inventory <!-- TODO -->; string-only: `base_service/service/business_service.dart @0x2ac45d8`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No request keys found by the extractor. <!-- TODO -->

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

- `base_service/service/business_service.dart`: `fetchDevicesListDirect` @0x2ac44b8 (encryptionRequestHttp; encrypted: true)
- `charging/http/http_request_repository_impl.dart`: `getDevicesList` @0x2289700 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getDevicesList`
- `charging/ui/page/device/a17b1/check_update/check_update_logic.dart::getDeviceList`
- `charging/ui/page/device/anker_ota/base/anker_ota_base_logic.dart::specialHandleOta`
- `charging/ui/page/device/connect/scan_logic.dart::getDeviceList`
- `charging/ui/page/device/main/sitation_energy_system/scan_appoint_device/scan_appoint_device_logic.dart::getDeviceList`
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::getDeviceList`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
