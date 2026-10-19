> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_charging_device_identity_status_default_true

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/mini_power/v1/app/setting/get_charging_device_identity_status_default_true`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x28d8340`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x28d828c` |

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

- `charging/http/http_request_repository_impl.dart`: `getA2345DeviceIdentityStatus` @0x28d828c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getA2345DeviceIdentityStatus`
- `charging/ui/page/device/a2345/a2345home/a2345home_logic.dart::getDeviceIdentityStatusSwitch`
- `charging/ui/page/device/a2345/a2345laboratory/a2345laboratory_logic.dart::getDeviceIdentityStatusSwitch`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
