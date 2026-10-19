> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# remove_param_config_key

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/app/device/remove_param_config_key`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x428bae0`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x428b9e4` |
| `device_sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x428b9e4` |
| `remove_key` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x428b9e4` |

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

- `charging/http/http_request_repository_impl.dart`: `removeParamConfigKey` @0x428b9e4 (encryptionRequestHttp; encrypted: true)

Called from: `charging/feature/peak_valley/confirm/confirm_peak_valley_logic.dart::onDeletePeakValleyClick`, `charging/http/http_request_repository.dart::removeParamConfigKey`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
