> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# confirm_permissions_settings

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/app/compatible/confirm_permissions_settings`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x2444f8c`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_model` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x2444ebc` |
| `confirm_type` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x2444ebc` |

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

- `charging/http/http_request_repository_impl.dart`: `getConfirmPermissionsSettingsApi` @0x2444ebc (encryptionRequestHttp; encrypted: true)

Called from: `charging/http/http_request_repository.dart::getConfirmPermissionsSettingsApi`, `charging/ui/page/device/a17c0/select_brand/select_brand_logic.dart::getConfirmPermissionsSettings`, `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::getSolarBankParticleData`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
