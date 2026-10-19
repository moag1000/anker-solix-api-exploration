> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_message

## Purpose

<!-- TODO -->

## Upstream name

`get_message` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/get_message`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x297c524`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `last_time` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x297c340` |
| `device_sns` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x297c340` |
| `limit` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x297c340` |
| `message_type` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x297c340` |
| `last_msg_id` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x297c340` |

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

- `charging/http/http_request_repository_impl.dart`: `getMessage` @0x297c340 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getMessage`
- `charging/ui/page/message/Main/message_main_logic.dart::requestCloudMessage`
- `charging/ui/page/message/Main/message_main_logic.dart::requestOtherCloudMessage`
- `charging/ui/page/message/system/message_system_logic.dart::requestCloudMessage`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
