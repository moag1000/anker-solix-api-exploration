> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_device_card_details

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_svc/get_device_card_details`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/device/a5101/device_home_page/device_home_http_reposity.dart @0x33c4d3c`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | ? | ? | ? | `charging/ui/page/device/a5101/device_home_page/device_home_http_reposity.dart @0x33c4c58` |
| `device_type` | ? | ? | ? | `charging/ui/page/device/a5101/device_home_page/device_home_http_reposity.dart @0x33c4c58` |
| `device_Sn` | ? | ? | ? | `charging/ui/page/device/a5101/device_home_page/device_home_http_reposity.dart @0x33c4c58` |

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

- `charging/ui/page/device/a5101/device_home_page/device_home_http_reposity.dart`: `getDeviceDetails` @0x33c4c58 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
