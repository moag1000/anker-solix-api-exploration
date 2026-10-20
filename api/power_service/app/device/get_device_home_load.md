> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_device_home_load

## Purpose

Reads the home-load (backup/priority load) configuration of a device or site for the A17C0 and A17C1 pages (callers `A17c0SwitchModeLogic::deviceConnect`, `A17c0energyPlanLogic::getDeviceHomeLoadData`, `A17c0homeLogic::getDeviceHomeLoad` and others) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`get_device_load` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/device/get_device_home_load` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x262c194`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x262c18c`, in `HttpRequestControllerImpl::get17C1DeviceHomeLoadPort` (`charging/http/http_request_repository_impl.dart @0x262c0b0`), sent through `encryptionRequestHttp` (`@0x262c1bc`).

Same URL and method object in the other sender(s) read:

- `POST /power_service/v1/app/device/get_device_home_load` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x26744d4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x26744cc`, in `HttpRequestControllerImpl::getDeviceHomeLoadPort` (`charging/http/http_request_repository_impl.dart @0x2674420`), sent through `encryptionRequestHttp` (`@0x26744fc`).
- `POST /power_service/v1/app/device/get_device_home_load` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x274a840`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x274a838`, in `HttpRequestControllerImpl::getDeviceHomeLoadRes` (`charging/http/http_request_repository_impl.dart @0x274a794`), sent through `encryptionRequestHttp` (`@0x274a868`).

## Encrypted?

encrypted: "default-true (requestHttp) — verify" / `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) 12 senders were found for this URL; the three `HttpRequestControllerImpl` senders were read. `getDeviceHomeLoadPort` (`charging/http/http_request_repository_impl.dart @0x2674420`) and `getDeviceHomeLoadRes` (`@0x274a794`) send `{device_sn}` in a `<String, String>` literal (`@0x2674488`, `@0x274a7f4`), so the value is a String. `get17C1DeviceHomeLoadPort` (`@0x262c0b0`) sends `{device_sn, param_type, device_pn}` in a `<String, Object>` literal (`@0x262c148`); `param_type` is the constant raw 2, so 1 (`@0x262c12c`). Other senders (`TouHttpService::getDeviceHomeLoad`, `TOUPlanLogic::getDataFromAPi`, `A5190HomeLogic::_fetchDeviceStationInfo`, `ElectricityUsageHelper` functions) send the same `device_sn` or add `site_id`/`accuracy`; they were not decoded.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | `charging/http/http_request_repository_impl.dart @0x2674474` |
| `param_type` | int (Smi, w) | yes (`get17C1DeviceHomeLoadPort` and `TouHttpService::getDeviceHomeLoad` only) | `1` | `charging/http/http_request_repository_impl.dart @0x262c120` (raw 2 stored by 32-bit store, so 1) |
| `device_pn` | ? | yes (`get17C1DeviceHomeLoadPort` only) | ? | `charging/http/http_request_repository_impl.dart @0x262c134` |

## `param_type`/`cmd`

see `api/param_types.md`

param_type is a variable at this sender (traced by heuristic — verify against the callers in `data/param_types.json`).

## Response model (link)

- [`A17C1DeviceHomeLoadData`](../../../../models/solarbank.md#a17c1devicehomeloaddata), parsed by `A17C1DeviceHomeLoadData.fromJson` at `charging/http/http_request_repository_impl.dart @0x262c210`
- [`StationModel`](../../../../models/other.md#stationmodel), parsed by `StationModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x267455c`. Parsed by `getDeviceHomeLoadPort`.
- [`SiteHomeLoadModel`](../../../../models/solarbank.md#sitehomeloadmodel), parsed by `SiteHomeLoadModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x274a940`

## Response

Model per sender: `get17C1DeviceHomeLoadPort` parses `A17C1DeviceHomeLoadData`, `getDeviceHomeLoadPort` parses `StationModel`, `getDeviceHomeLoadRes` parses `SiteHomeLoadModel` (worksheet `response_class`; the `fromJson` addresses are listed above where found). `ElectricityUsageHelper::getCurEmsModeType` parses `EmsModeModel` (not read here).

(asm-traced) For each sender that parses a model, the keys below are the top-level keys of the model; that sender adds no wrapper fields of its own in the code read.

- `A17C1DeviceHomeLoadData` top-level keys (`data/models.json`, `charging::A17C1DeviceHomeLoadData`): `site_id` (String?), `current_home_load` (String?), `home_load_data` (String), `parallel_home_load` (String?), `parallel_display` (bool?).
- `StationModel` top-level keys (`data/models.json`, `base_service::StationModel`): `site_id` (String?), `site_name` (String?), `site_img` (String?), `current_home_load` (String?), `parallel_home_load` (String?), `parallel_display` (bool?), `device_type_list` (Iterable), `support_device_models` (Iterable), `current_site_device_models` (Iterable), `ms_type` (int?), `power_site_type` (int?), `display_priority_discharge_tips` (int?), `priority_discharge_switch` (int?), `is_show_priority_discharge` (int?), `site_device_list` (Iterable), `init_status` (int?), `reason_code` (int?), `is_site_created_by_installer` (bool?), `is_allow_delete` (bool?), `not_allow_delete_reason` (Iterable), `not_allow_device_add_remove` (int?).
- `SiteHomeLoadModel` top-level keys (`data/models.json`, `charging::SiteHomeLoadModel`): `step` (int?), `schedule_mode` (unknown), `last_select_mode` (num?), `max_load` (int?), `min_load` (int?), `is_charge_priority` (int?), `default_charge_priority` (int?), `is_zero_output_tips` (int?), `is_show_install_mode` (int?), `advanced_mode_min_load` (int?), `display_advanced_mode` (int?), `priority_discharge_upgrade_devices` (String?), `ranges` (List), `display_priority_discharge_tips` (int?), `is_show_priority_discharge` (int?), `default_home_load` (int?), `switch` (int?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<device_sn>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint). The 17C1 sender adds `"param_type": 1` and `"device_pn": "<?>"`.

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `get17C1DeviceHomeLoadPort` @0x262c0b0 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`); `getDeviceHomeLoadPort` @0x2674420 (encryptionRequestHttp; encrypted: true); `getDeviceHomeLoadRes` @0x274a794 (encryptionRequestHttp; encrypted: true)
- `electricity_price/components/electricity_price_common/electricity_usage_helper.dart`: `<anonymous closure> in ElectricityUsageHelper::getCurEmsModeType` @0x292e774 (URL literal only, no `*Http*` call; sends in the same function (`HttpServiceImpl::encryptionRequestHttp`); resolved from the URL literal at `electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x292e7e4` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md)); `<anonymous closure> in ElectricityUsageHelper::getManualSetTOUDetailWithUrl` @0x2c4fdfc (URL literal only, no `*Http*` call; sends in the same function (`HttpServiceImpl::encryptionRequestHttp`); resolved from the URL literal at `electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x2c4ff38` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md)); `assembleRemoteApiParametersWidthGetDetail` @0x2c4f694 (URL literal only, no `*Http*` call; no sender within 3 caller levels); `getCurEmsModeType` @0x292e1f4 (encryptionRequestHttp; encrypted: true); `getElectricityUsagePolicyUrl` @0x292e5e8 (URL literal only, no `*Http*` call; sender `ElectricityUsageHelper::getCurEmsModeType` (`electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x292e1f4`), reached through callers `ElectricityUsageHelper::getCurEmsModeType` (`electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x292e1f4`); resolved from the URL literal at `electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x292e634` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))
- `electricity_price/components/electricity_price_common/view/tou_plan_logic.dart`: `<anonymous closure> in TOUPlanLogic::getDataFromAPi` @0x2c49658 (URL literal only, no `*Http*` call; no sender within 3 caller levels); `getDataFromAPi` @0x2c49144 (encryptionRequestHttp; encrypted: true)
- `electricity_price/components/tou/impl_v2/service/tou_http_service.dart`: `getDeviceHomeLoad` @0x4878c74 (request; encrypted: default-true (requestHttp) — verify, param_type/cmd: see `api/param_types.md`)
- `ev_charger/src/ev_charger/page/home/a5190_home_logic.dart`: `_fetchDeviceStationInfo` @0x3504e80 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::get17C1DeviceHomeLoadPort`
- `charging/http/http_request_repository.dart::getDeviceHomeLoadPort`
- `charging/http/http_request_repository.dart::getDeviceHomeLoadRes`
- `charging/ui/page/device/a17c0/a17c0SwitchMode/a17c0_switch_mode_logic.dart::deviceConnect`
- `charging/ui/page/device/a17c0/a17c0energyPlan/a17c0energy_plan_logic.dart::getDeviceHomeLoadData`
- `charging/ui/page/device/a17c0/a17c0home/a17c0home_logic.dart::getDeviceHomeLoad`
- `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart::onInit`
- `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart::_preloadHomeLoadData`
- `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart::getDeviceHomeLoad`
- `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart::_ensureHomeLoadData`
- `charging/ui/page/device/a17c1/energy_plan/energy_plan_logic.dart::getHomeLoadSiteParam`
- `charging/ui/page/device/a17x7/a17x7home/a17x7home_logic.dart::_fetchDeviceStationInfo`
- `charging/ui/page/device/a17x8/a17x8home/a17x8home_logic.dart::_fetchDeviceStationInfo`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/merge_system_energy/merge_system_energy_plan_logic.dart::getHomeLoadSiteParam`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/power_usage_scenario/power_usage_scenario_logic.dart::getHomeLoadDeviceParam`
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::detectionDeviceJoinSystem`
- `electricity_price/components/electricity_module/electricity_price_serviceImpl.dart::getCurEmsModeType`
- `electricity_price/components/electricity_price_common/electricity_usage_helper.dart::getCurEmsModeType`
- `electricity_price/components/electricity_price_common/electricity_usage_helper.dart::getManualSetTOUDetail`
- `electricity_price/components/electricity_price_common/view/tou_plan_logic.dart::parserRouterInfo`
- `electricity_price/components/electricity_price_common/view/tou_plan_logic.dart::updateData`
- `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart::onReady`
- `electricity_price/components/tou/impl_v2/repository/charging_pile_tou_repository.dart::getTouDetail`
- `ev_charger/src/ev_charger/page/home/a5190_home_logic.dart::onInit`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of `device_pn` and of `device_sn` in the `<String, Object>` sender. — attempted 2026-10-20 (two-hop not readable: the `<String, Object>` sender's callers were not followed in this pass; header stays string-only)
- The seven senders not read (`TouHttpService`, `TOUPlanLogic`, `A5190HomeLogic`, `ElectricityUsageHelper` x3 closures/functions): bodies and parsers were not decoded. — traced 2026-10-20: not decoded in this pass (seven senders); the reason given in the bullet stands
- Which model each caller expects for which device type (server data decides the keys).
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
