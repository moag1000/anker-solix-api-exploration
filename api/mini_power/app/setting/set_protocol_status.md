> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# set_protocol_status

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/mini_power/v1/app/setting/set_protocol_status`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x35407c4`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x35406a8` |
| `protocol_status` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x35406a8` |

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

- `charging/http/http_request_repository_impl.dart`: `setA2687ProtocolAgreementStatus` @0x35406a8 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/ak_iot_kit/business/A2687/service/a2687_device_info_service.dart::<anonymous closure>@0x3540538`
- `charging/ak_iot_kit/business/A2687/service/a2687_device_info_service.dart::<anonymous closure>@0x3540844`
- `charging/ui/page/device/a2687/a2687setting/a2687_lab_function/a2687_lab_function_logic.dart::setProtocolAgreementStatus`
- `charging/ui/page/device/a2687/a2687setting/a2687_lab_function/a2687_new_lab_function_logic.dart::setProtocolAgreementStatus`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
