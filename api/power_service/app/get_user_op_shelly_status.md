> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_user_op_shelly_status

## Purpose

<!-- TODO -->

## Upstream name

`get_shelly_status` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/app/get_user_op_shelly_status`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x3f2aa7c`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `token` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3f2a9d4` |

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

- `charging/http/http_request_repository_impl.dart`: `checkIsGrantedDeviceChanged` @0x3f2a9d4 (encryptionRequestHttp; encrypted: true)

Called from: `charging/http/http_request_repository.dart::checkIsGrantedDeviceChanged`, `charging/ui/page/device/connect/third_party_platform/third_party_platform_logic.dart::selectDone`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
