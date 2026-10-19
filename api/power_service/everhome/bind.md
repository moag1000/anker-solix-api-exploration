> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# bind

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/everhome/bind`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/device/connect/third_party_platform_list/strategy/ever_home_navigation_strategy.dart @0x3f29df8`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `code` | ? | ? | ? | `charging/ui/page/device/connect/third_party_platform_list/strategy/ever_home_navigation_strategy.dart @0x3f29d24` |

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

- `charging/ui/page/device/connect/third_party_platform_list/strategy/ever_home_navigation_strategy.dart`: `bind2Cloud` @0x3f29d24 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/ui/page/device/connect/third_party_platform_list/strategy/ever_home_navigation_strategy.dart::addJsCallHandler`

## Since/changed

3.18.0: absent. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
