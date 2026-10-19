> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_vpp_check_code

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_svc/get_vpp_check_code`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x292c70c`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify" / `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x292c5a0` |
| `get_code` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x292c5a0` |
| `current_version` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x292c5a0` |

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

- `charging/http/http_request_repository_impl.dart`: `getVppInfo` @0x292c5a0 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `settings/src/common/menu_controller/vpp_menu_controller.dart`: `checkSupport` @0x367abf4 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getVppInfo`
- `charging/ui/page/device/a5101/setting/homeSetting/home_setting_logic.dart::requestVppInfo`
- `charging/ui/page/device/a5101/setting/vpp/controller.dart::requestVppInfo`
- `settings/src/common/menu_controller/vpp_menu_controller.dart::onInit`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
