> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# upload_pb_events

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/app/logging/upload_pb_events`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x263e918`

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `pb` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x263e8c4` |
| `tlv` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x263e8c4` |
| `params.payload` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x263e8c4` |
| `device_sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x263e8c4` |
| `version` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x263e8c4` |
| `local_time` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x263e8c4` |
| `device_model` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x263e8c4` |
| `events` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x263e8c4` |

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

- `charging/http/http_request_repository_impl.dart`: `postEventData` @0x263e8c4 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/ble/base_ble_controller.dart::postEventDataRequest`
- `charging/ble/device/iot_anker_controller.dart::_handleResponse`
- `charging/http/http_request_repository.dart::postEventData`
- `charging/impl/http_service_impl.dart::postEventData`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
