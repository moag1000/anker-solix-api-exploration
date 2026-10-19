> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_charging_device

## Purpose

<!-- TODO -->

## Upstream name

`charging_devices` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/site/get_charging_device`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x286b044`

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

- `charging/http/http_request_repository_impl.dart`: `getChargingDeviceRequest` @0x286afb8 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getChargingDeviceRequest`
- `charging/ui/page/device/a1340/a1340charge_device/a1340charge_device_logic.dart::getA1340ChargeDeviceListForOther`
- `charging/ui/page/device/a1340/a1340home/a1340home_logic.dart::_getA1340ChargeDeviceListForOther`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
