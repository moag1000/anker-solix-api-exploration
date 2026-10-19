> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_site_list

## Purpose

<!-- TODO -->

## Upstream name

`site_list` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/site/get_site_list`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x28c2ffc`
(literal also at 2 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `/power_service/v1/site/get_site_list` | ? | ? | ? | `charging/ui/page/home/home_base_http_reposity.dart @0x238e380` |
| `path` | ? | ? | ? | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2aaea38` |
| `method` | ? | ? | ? | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2aaea38` |
| `param` | ? | ? | ? | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2aaea38` |

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

- `charging/http/http_request_repository_impl.dart`: `getUserSiteList` @0x28c2f6c (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/home/home_base_http_reposity.dart`: `querySiteList` @0x238e380 (encryptionRequestHttp; encrypted: true)
- `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart`: `getUserSiteList` @0x2aaea38 (URL literal only, no `*Http*` call; sends in the same function (`AKIoTKitManagerImpl::handle`); resolved from the URL literal at `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2aaea8c` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))

Called from:

- `charging/http/http_request_repository.dart::getUserSiteList`
- `charging/ui/page/device/a17c0/select_station/select_station_logic.dart::getUserSiteListReq`
- `charging/ui/page/device/connect/zx_config_wifi/zx_config_wifi_logic.dart::parseBleResponseData`
- `charging/ui/page/device/connect/zx_connect_ble_success/zx_connect_ble_success_logic.dart::_updateDeviceName`
- `charging/ui/page/green_energy/site/site_logic.dart::onReady`
- `charging/ui/page/home/home_base_logic.dart::quierySiteList`
- `charging/ui/page/user/share_site/manage_system/manage_system_logic.dart::getUserSiteListReq`
- `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart::fetchHesSites`
- `ev_charger/src/ev_charger/page/home/load_balancing/select_station/evselect_station_logic.dart::getUserStation`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
