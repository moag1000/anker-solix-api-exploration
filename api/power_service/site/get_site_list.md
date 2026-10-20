> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_site_list

## Purpose

Lists the sites of the logged-in user: `HttpRequestControllerImpl::getUserSiteList` and `HomeBaseHttpReposity::querySiteList` (home page) send it from the app, and `AKIotEVChargeCommand::getUserSiteList` (EV charger load-balancing station picker) sends it through the IoT kit.

## Upstream name

`site_list` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/site/get_site_list` (asm-traced) at the senders that load a `Method` object next to the URL string (pool entry `pp+0xa7e0`, `Method.post`):

- `HttpRequestControllerImpl::getUserSiteList` (`http_request_repository_impl.dart @0x28c2f6c`): URL string `@0x28c2ffc`, method object `Method.post` (`pp+0xa7e0`) `@0x28c2ff4`.
- `HomeBaseHttpReposity::querySiteList` (`home_base_http_reposity.dart @0x238e380`): URL string `@0x238e580`, method object `Method.post` (`pp+0xa7e0`) `@0x238e578`.

The IoT-kit sender `AKIotEVChargeCommand::getUserSiteList` (`ev_charge_command.dart @0x2aaea38`) uses the path `"power_service/v1/site/get_site_list"` (`@0x2aaea8c`, without a leading slash) and the string literal `"POST"` (`@0x2aaeaa4`) in a command map for `akIoTKitManager.handle` (`@0x2aaeb18`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No request keys: all three senders send an empty body.

- `HttpRequestControllerImpl::getUserSiteList` (`http_request_repository_impl.dart @0x28c2f6c`): an empty map literal (`empty_array`, `Map._fromLiteral`), no `[]=` call.
- `HomeBaseHttpReposity::querySiteList` (`home_base_http_reposity.dart @0x238e380`): an empty `<String, String>` map (`@0x238e51c`, `empty_array` `@0x238e524`, `Map._fromLiteral` `@0x238e52c`); the call also carries a `cacheKey` argument built from the URL and the user id (`getUserId` `@0x238e488`).
- `AKIotEVChargeCommand::getUserSiteList`: the `param` entry of the command map is an empty map (`empty_array` `@0x2aaeabc`, `Map._fromLiteral` `@0x2aaeac4`).

## `param_type`/`cmd`

n/a

## Response model (link)

Per sender. `getUserSiteList`: `charging::UserSiteListModel` (`data/models.json` key; fields on [`models/account.md`](../../../models/account.md#usersitelistmodel)), parsed per list element in the success closure `http_request_repository_impl.dart @0x28c3040` (key string `site_list`). `querySiteList`: its callbacks (`home_base_http_reposity.dart @0x238fa00`, `@0x238f974`) call `_onQuerySiteListSuccess` (`@0x238e5d4`), which reads the key `site_list` (`@0x238e63c`) and parses every element with `StationModel.fromJson` (`@0x238e724`, resolves to `base_service/ak_iot_kit/business/basic/model/station_model.dart`; fields on [`models/other.md`](../../../models/other.md#stationmodel)). IoT-kit sender: the caller `EvselectStationLogic::getUserStation` (`evselect_station_logic.dart @0x2aae588`) reads the keys `data` (`@0x2aae678`) and `site_list` (`@0x2aae6e4`); its element parsing was not read.

## Response

The response data carries the list under `site_list`. Keys of one `UserSiteListModel` element (from `data/models.json`): `site_id`, `site_name`, `site_img` (String), `device_type_list` (Iterable), `ms_type`, `power_site_type` (int), `is_allow_delete` (bool), `support_device_models` (Iterable), `init_status` (int). `StationModel` has more keys: see its model page.

## Example request/response

Request, synthesized

```json
{}
```

Response keys: see Response; no capture.

## Errors seen

None traced. The builders' failure callbacks (`postJML` template `@0x226824c`, `home_base_http_reposity.dart @0x238fa00`/`@0x238f974` which call `_onQuerySiteListSuccess` for both outcomes) compare no code. Error codes are catalogued in `api/errors.md`.

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

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- How the IoT-kit sender's caller parses `site_list` (not read). Header stays string-only.
- Why the two app senders parse the same key into two different model classes (`UserSiteListModel` vs `StationModel`).
- What `cacheKey` does to the request: it is an argument of `requestHttp` (`@0x238e5ac`), not part of the body.

## Device-tested by

none
