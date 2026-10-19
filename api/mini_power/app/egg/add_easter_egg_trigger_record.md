> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# add_easter_egg_trigger_record

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/mini_power/v1/app/egg/add_easter_egg_trigger_record`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_business_impl.dart @0x3b2d694`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `charging/http/http_business_impl.dart @0x3b2d58c` |
| `egg_type` | ? | ? | ? | `charging/http/http_business_impl.dart @0x3b2d58c` |
| `trigger_time` | ? | ? | ? | `charging/http/http_business_impl.dart @0x3b2d58c` |

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

- `charging/http/http_business_impl.dart`: `addEasterEggRecord` @0x3b2d58c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/ble/device/A2345/a2345_device_commands.dart::parseUploadEasterEggTrigger`
- `charging/ble/device/A91B2/a91b2_device_commands.dart::parseUploadEasterEggTrigger`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
