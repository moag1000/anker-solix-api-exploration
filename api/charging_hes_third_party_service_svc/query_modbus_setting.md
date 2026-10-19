> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# query_modbus_setting

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_third_party_service_svc/query_modbus_setting`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/device/a17x8/a17x8setting/a17x8setting_logic.dart @0x2cd4ee8`
(literal also at 2 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `sn` | ? | ? | ? | `charging/ui/page/device/a17x8/a17x8setting/a17x8setting_logic.dart @0x2cd4e10` |
| `siteId` | ? | ? | ? | `charging/ui/widget/home_assitent/home_assistant_logic.dart @0x38db78c` |

Rows are the union over 3 senders; `source` is the first sender that sets the key.

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

- `charging/ui/page/device/a17x8/a17x8setting/a17x8setting_logic.dart`: `requestData` @0x2cd4e10 (encryptionRequestHttp; encrypted: true)
- `charging/ui/widget/home_assitent/home_assistant_logic.dart`: `requestData` @0x38db78c (encryptionRequestHttp; encrypted: true)
- `settings/src/common/menu_controller/communication_setting_menu_controller.dart`: `requestData` @0x2cd4c00 (encryptionRequestHttp; encrypted: true)

Called from: `charging/ui/page/device/a17x8/a17x8setting/a17x8setting_logic.dart::onInit`, `charging/ui/page/device/a17x8/a17x8setting/a17x8setting_logic.dart::tapEnterHA`, `charging/ui/widget/home_assitent/home_assistant_logic.dart::_retryFetchIp`, `settings/src/common/menu_controller/communication_setting_menu_controller.dart::onInit`, `settings/src/common/menu_controller/communication_setting_menu_controller.dart::onTapMenu`

## Since/changed

3.18.0: absent. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
