> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_hardware_relation

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v2/app/get_hardware_relation`, method: not extracted by the inventory <!-- TODO -->; string-only: `base_service/ak_iot_kit/business/basic/model/station_device_relation.dart @0x22a49c4`
(literal also at 3 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `sn_list` | ? | ? | ? | `base_service/ak_iot_kit/business/basic/model/station_device_relation.dart @0x22a4864` |
| `path` | ? | ? | ? | `ota_kit/src/providers/sub_package_info_provider.dart @0x2b0b4ec` |
| `param.sn_list` | ? | ? | ? | `ota_kit/src/providers/sub_package_info_provider.dart @0x2b0b4ec` |

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

- `base_service/ak_iot_kit/business/basic/model/station_device_relation.dart`: `<anonymous closure>@0x22a4a08` @0x22a4a08 (URL literal only, no `*Http*` call); `<anonymous closure>@0x22a4ab8` @0x22a4ab8 (URL literal only, no `*Http*` call); `requestHardwareRelation` @0x22a4864 (encryptionRequestHttp; encrypted: true)
- `ota_kit/src/providers/sub_package_info_provider.dart`: `getHardwareRelation` @0x2b0b4ec (URL literal only, no `*Http*` call)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
