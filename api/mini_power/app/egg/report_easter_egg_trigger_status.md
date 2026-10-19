> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# report_easter_egg_trigger_status

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/mini_power/v1/app/egg/report_easter_egg_trigger_status`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x3e3c0ac`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3e3bf9c` |
| `egg_type` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3e3bf9c` |
| `report_time` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3e3bf9c` |

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

- `charging/http/http_request_repository_impl.dart`: `addEasterEggStatusRecord` @0x3e3bf9c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::addEasterEggStatusRecord`
- `charging/ui/page/device/a2345/a2345easter_egg/a2345easter_egg_logic.dart::requestAddEasterEggStatusRecord`
- `charging/ui/page/device/a91b2/a91b2easter_egg/a91b2easter_egg_logic.dart::requestAddEasterEggStatusRecord`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
