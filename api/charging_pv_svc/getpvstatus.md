> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# getPvStatus

## Purpose

<!-- TODO -->

## Upstream name

`get_device_pv_status` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/charging_pv_svc/getPvStatus`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x2446fe0`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `sns` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x2446f1c` |

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

- `charging/http/http_request_repository_impl.dart`: `getPvStatus` @0x2446f1c (encryptionRequestHttp; encrypted: true)

Called from: `charging/http/http_request_repository.dart::getPvStatus`, `charging/ui/page/device/a5140/a5140home/a5140home_logic.dart::_isOffline`, `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::getDeviceList`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
