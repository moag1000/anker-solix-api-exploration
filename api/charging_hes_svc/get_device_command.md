> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_device_command

## Purpose

Reads the stored system settings of an A5101 site (`A5101DeviceCommandModel`) for 13 settings pages (callers include `AdvancedConfigLogic::getAdvancedConfigStateFromCloud`, `ClsSettingLogic::_getCLSState`, `DeviceManagerLogic::getDeviceData`, `EvChargerManagerLogic::_getData`, `ManageDevicesLogic::_getData`, through `HttpRequestControllerImpl::getDeviceCommand`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_device_command` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x277cbc8`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x277cbc0`, in `HttpRequestControllerImpl::getDeviceCommand` (`charging/http/http_request_repository_impl.dart @0x277caa0`), sent through `requestHttp` (`@0x277cbf0`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `HttpRequestControllerImpl::getDeviceCommand` (`charging/http/http_request_repository_impl.dart`, call `@0x277cbf0`, argument list `@0x277cbe8`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

`HttpRequestControllerImpl::getDeviceCommand` (`charging/http/http_request_repository_impl.dart @0x277caa0`) stores 2 keys in a map literal with type arguments `<String, Object>` (`@0x277cb7c`), which do not type the values. `accuracy` is a constant: `r16 = 10` (`@0x277cb74`), a tagged immediate stored without a guard (`@0x277cb78`), so the Smi 5. `station_id` is `field_7` of the value of `StationMainPageLogic` (load `@0x277cb28`, fallback `""` `@0x277cb38`). `StationMainPageLogic` holds an `Rx<StationModel>` (`charging/ui/page/device/main/station_device_home/station_main_page/station_main_page_logic.dart @0x22597b0`, stored `@0x22597cc`); `StationModel.field_7` is declared `String?` (cast `r8 = String?` `@0x238e858`, store `@0x238e870` in `base_service/ak_iot_kit/business/basic/model/station_model.dart`, key `site_id` `@0x238e808`), so the value is a String with the empty string as fallback.

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | string | yes | `"<station_id>"` | `charging/http/http_request_repository_impl.dart @0x277cb54` |
| `accuracy` | int (Smi, w) | yes | `5` | `charging/http/http_request_repository_impl.dart @0x277cb68` |

## `param_type`/`cmd`

n/a

## Response model (link)

- [`A5101DeviceCommandModel`](../../models/hes.md#a5101devicecommandmodel), parsed by `A5101DeviceCommandModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x277cc44` (success closure `@0x277cc0c`, `bl` target `[package:charging/model/a5101/a5101_device_command_model.dart]`).

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::A5101DeviceCommandModel`): `main_sn` (String?), `electricity_strategy` (ElectricityStrategy?), `diesel` (A5101Diesel?), `screen_setting` (ScreenSetting?), `utility_rate_plan` (UtilityRatePlan?), `fixed_price` (FixedRate?), `real_grid` (int?), `advanced_setting` (AdvancedSetting?), `heat_pump_setting` (HeatPumpModel?), `time_zone` (String?), `cls_status` (int?), `grid_code` (int?), `off_grid_switching` (OffGridSwitching?), `price_source_type` (int?), `price_source_sub_type` (int?), `history_schedule_mode` (HistoryScheduleMode?), `evcharger_setting` (unknown), `evcharger_enable` (int?), `showBatterySetting` (bool?), `battertySetting` (BattertySetting?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "station_id": "<station_id>",
  "accuracy": 5
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`. The failure closure is the folded closure `charging/http/http_request_repository_impl.dart @0x238cda4`, which forwards the code and the message to the stored callback (`ClosureCall` `@0x238cde8`).

## Callers in app

- `ak_soft_ems/http/ems_api.dart`: `getDeviceCommand` @0x2a31618 (URL literal only, no `*Http*` call; sender `EmsAiModeConditionLogic::_getLargeAuthorizationStatus` (`ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x2a31278`), reached through callers `EmsAiModeConditionLogic::_getLargeAuthorizationStatus` (`ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x2a31278`); resolved from the URL literal at `ak_soft_ems/http/ems_api.dart @0x2a31630` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))
- `charging/http/http_request_repository_impl.dart`: `getDeviceCommand` @0x277caa0 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::getDeviceCommand`
- `charging/ui/page/device/a5101/setting/advanced_config/advanced_config_logic.dart::getAdvancedConfigStateFromCloud`
- `charging/ui/page/device/a5101/setting/bluetooth_control/bleTest/peak_valley_test/peak_valley_test_logic.dart::onReady`
- `charging/ui/page/device/a5101/setting/cls_setting/cls_setting_logic.dart::_getCLSState`
- `charging/ui/page/device/a5101/setting/device_manager/device_manager_logic.dart::getDeviceData`
- `charging/ui/page/device/a5101/setting/device_manager/ev_charger/ev_charger_manager_logic.dart::_getData`
- `charging/ui/page/device/a5101/setting/device_manager/oil_engine/manage_devices_logic.dart::_getData`
- `charging/ui/page/device/a5101/setting/grid_sensitivity/a5101_grid_sensitivity_logic.dart::_getOffGridState`
- `charging/ui/page/device/a5101/setting/homeSetting/home_setting_logic.dart::_getCLSState`
- `charging/ui/page/device/a5101/setting/screen_timeout/screen_timeout_logic.dart::getRadarAndScreenConfig`
- `charging/ui/page/device/a5101/setting/smartMode/smart_mode_logic.dart::_getSmartModeAuthorizationStatus`
- `charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart::_getSystemPolicySetting`
- `charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart::_updateRemainingChargeTime`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What `accuracy` selects on the server: the app sends the constant Smi 5.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call. — reclassified: device test row 150 (traced 2026-10-20: per call the SDK login state `AkIotKitFlutter::isLogin` and the base-URL predicate decide, `HttpEncryptionDecorator.dart @0x4869504`, `@0x4869544`; the predicate is a GDT dispatch whose selector the asm does not name, and the login state is runtime data)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
