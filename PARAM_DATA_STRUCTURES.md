# param_data JSON Structures

> Extracted from Blutter decompilation by tracing Map construction patterns
> near `jsonEncode()` calls and `set_site_device_param` invocations.
>
> **Important:** `param_data` is always a **JSON string** (not a nested object).
> The API expects: `{"param_data": "{\"key\":{\"nested\":\"value\"}}"}` — a string
> containing JSON, not a nested object directly.
>
> Device-tested example from upstream (param_type 19):
> ```json
> {"site_id": "<id>", "param_type": "19", "cmd": 17,
>  "param_data": "{\"power_limit\":{\"limit\":3600,\"limit_real\":3600}}"}
> ```

## param_type 19 — Power Limit (SET only)

Function: `setSiteDevicePowerLimit`

Device-tested by thomluther ([Issue #423](https://github.com/thomluther/ha-anker-solix/issues/423#issuecomment-4135301109)):

```json
{
  "site_id": "<siteid>",
  "param_type": "19",
  "cmd": 17,
  "param_data": "{\"power_limit\":{\"limit\":3600,\"limit_real\":3600}}"
}
```

Nesting from Blutter: `Map<String, Map<String, int>>`
- Outer key: `power_limit`
- Inner keys: `limit` (int), `limit_real` (int)
- Values must match `get_power_limit` response options

## param_type 18 — Safety SOC Parameters

Function: `setSafetySocParams`

From Blutter + upstream schedule.py example:

```json
{
  "site_id": "<siteid>",
  "param_type": "18",
  "cmd": 17,
  "param_data": "{\"soc_list\":[{\"id\":1,\"is_selected\":1,\"soc\":10},{\"id\":2,\"is_selected\":0,\"soc\":5}],\"switch_0w\":0,\"enable_0w\":0,\"enable_0w_change\":false,\"feed-in_power_limit\":0}"
}
```

Related fields from `a17c1setting_logic.dart`:
`ip_region, region_microinverter_limit, switch_0w, enable_0w, power_limit_option_real, pv_power_limit_option`

## param_type 20 — Station Country Code

Function: `get/setStationCountryCode`

From Blutter `grid_code_model.dart`:

```json
{
  "site_id": "<siteid>",
  "param_type": "20",
  "cmd": 17,
  "param_data": "{\"state_name\":\"...\",\"grid_code\":\"...\"}"
}
```

Type: `Map<String, dynamic>`

## param_type 26 — Third-Party PV

Function: `getThreePvParam` / `setThreePvInstallSwitch`

From upstream schedule.py:

```json
{
  "site_id": "<siteid>",
  "param_type": "26",
  "cmd": 17,
  "param_data": "{\"third_part_pv_setting\":1,\"show_third_party_pv_panel\":1}"
}
```

## param_type 6 — SB2/SB3 Schedule

Function: `set17C1SiteDeviceParam`

From upstream schedule.py + Blutter:

```json
{
  "site_id": "<siteid>",
  "param_type": "6",
  "cmd": 17,
  "param_data": "{\"mode_type\":3,\"custom_rate_plan\":[{\"index\":0,\"week\":[0,6],\"ranges\":[{\"start_time\":\"00:00\",\"end_time\":\"24:00\",\"power\":110}]}]}"
}
```

Nesting: `mode_type` (int) + `custom_rate_plan` (list of objects with `index`, `week`, `ranges`)

## param_type 23 — Switch Config

From upstream schedule.py:

```json
{
  "site_id": "<siteid>",
  "param_type": "23",
  "cmd": 17,
  "param_data": "{\"switch\":0}"
}
```

## param_type 1 — Green Mode Device Params

Function: `getSiteGreenModeDeviceParam`

Structure: unknown (GET only observed, no SET example)

## param_type 2 — Peak/Valley Time Params

Function: `getSitePeakTimeDeviceParam`

Structure: unknown (GET only observed)

## param_type 3 — Peak Shaving Enable

Function: `getSiteEnablePeakDeviceParam`

Structure: unknown (GET only observed)

## param_type 5 — Lower Limit / Min Power

Function: `getSiteLowerLimitDeviceParam`

Structure: unknown (GET only observed)

---

## Key Pattern

All `set_site_device_param` calls follow:
```json
{
  "site_id": "<siteid>",
  "param_type": "<N>",
  "cmd": 17,
  "param_data": "<JSON string>"
}
```

Where `cmd: 17` appears to be a constant for SET operations (from thomluther's verification).
The `param_data` value is always a **JSON-encoded string**, not a nested object.

---

## Additional Nested Structures (from Map TypeArguments)

### getDeviceInfos (charging_energy_service)
```json
{"main_sn": "<sn>", "device_rom_versions": [{"sn": "<sn1>"}, {"sn": "<sn2>"}]}
```
Type: `Map<String, List<String>>`

### getDeviceJoinSiteList
```json
{"devices": [{"device_sn": "...", "device_model": "...", ...}]}
```
Type: `Map<String, List<DeviceJoinSiteModel>>`

### getHeatPumpTimePlan (charging_hes_svc)
```json
{"heat_pump_plan": [{"start_time": "...", "end_time": "...", "mode": "...", ...}]}
```
Type: `Map<String, List<Map<String, dynamic>>>`

---

## Technique Used

The nested structures were identified by tracing:
1. `Map._fromLiteral()` calls in decompiled Dart
2. `TypeArguments` annotations that show the generic types (e.g., `<String, Map<String, int>>`)
3. String constants (`r17 = "field_name"`) set via `StoreField` before the Map construction
4. `jsonEncode()` calls that serialize the Map into the `param_data` JSON string

This technique can reveal nesting that flat field name extraction misses.

---

## Comprehensive Nested Structure Extraction (660 findings)

Extracted using 4 methods: Map._fromLiteral + TypeArguments, jsonEncode tracing,
json.dumps patterns, and StoreField nesting analysis across the entire codebase.

### set_device_attrs — Confirmed Nesting Pattern

The `set_device_attrs` endpoint uses `device_sn` + `attributes` dict. **Upstream confirms**
that additional fields like `switch_0w`, `pv_power_limit` go **inside** the `attributes`
dict, NOT alongside it:

```json
{"device_sn": "...", "attributes": {"pv_power_limit": 800, "switch_0w": 0}}
```

Per-function attribute keys (all go inside `attributes`):
```
setDevicePowerOptionsReq:     attributes: {power_limit?, ac_power_limit?, pv_power_limit?}
setTouElectricAttrs:          attributes: {pps_use_time}
getCurrencySetDeviceAttrs:    attributes: {currency}
setSolarName:                 device_pn + attributes: {}
setDeviceFeedGridSwitch:      attributes: {switch_0w}        ← 0=allow grid, 1=block
setDevicePvPowerOptionsReq:   attributes: {pv_power_limit}   ← in Watts
setLocationTag:               attributes: {tag}
setDeviceGameStatus:          attributes: {init_status}
setPpsSolarName:              device_pn + attributes: {}
```

### Shelly Device Control

```json
{"device_sn": "...", "op_type": "parameter", "toggle": "...", "value": "..."}
```

### Power Limit Region Config (deeply nested)

```
power_limit_option
  └─ user_power_limit
  └─ region_power_limit
       └─ ip_region
       └─ regulation_code
       └─ region_microinverter_limit
  └─ legal_power_limit
  └─ enable_0w
       └─ switch_0w
```

### Extender System Operations

```
addExtenderSystem:              {"device_list": [...]}
delExtenderSystem:              {"extender_system_id": "..."}
setExtenderSystemName:          {"extender_system_id": "...", "extender_system_name": "..."}
updateExtenderSystemStrategy:   {"extender_system_id": "...", "extender_system_params": {...}}
batchAddDevice:                 {"extender_system_id": "...", "device_list": [...]}
batchDelDevice:                 {"extender_system_id": "...", "device_sn_list": [...]}
getStrategyLastRecord:          {"extender_system_id": "...", "strategy_type": 1}
```

### AX170 IoT Action Payloads

All AX170 BLE/IoT actions use the pattern:
```json
{"id": "<action_name>", "deviceSn": "<sn>", "param": {<action-specific params>}}
```

Examples:
```
action_set_backup_strategy:          {"id": "action_set_backup_strategy", "param": {...}}
action_set_standby_oil_machine_params: {"id": "action_set_standby_oil_machine_params", "param": {...}}
action_set_custom_branch:            {"id": "action_set_custom_branch", "param": {"custom_branches": [...]}}
action_set_biggest_frequency:        {"id": "action_set_biggest_frequency", "param": {...}}
action_set_connection_sensitivity:   {"id": "action_set_connection_sensitivity", "param": {...}}
action_manual_set_oil_machine_params: {"id": "action_manual_set_oil_machine_params", "param": {...}}
```

### Init Flow Actions

```
action_set_distribution_box:         {"id": "action_set_distribution_box", "param": {...}}
action_set_power_limit_country_code: {"id": "action_set_power_limit_country_code", "param": {...}}
action_set_standby_rated_power:      {"id": "action_set_standby_rated_power", "param": {...}}
action_set_third_oil_type:           {"id": "action_set_third_oil_type", "param": {...}}
action_set_third_party_pv:           {"id": "action_set_third_party_pv", "param": {...}}
action_set_system_self_check:        {"id": "action_set_system_self_check"}
```

### EV Charger Operations

```
addChargingDevice:    {"site_id": "...", "ev_charger": {...}, "device_sn": "..."}
getStationEvChargers: {"site_id": "...", "charging_pile_list": [...]}
shareDevice:          {"device_sn": "...", "sub_devices": [...]}
setRfidCard:          {"device_sn": "...", "card_number": "...", "alias_name": "..."}
```

### Smart Charging (EV)

```json
{"switch_smart_charging": true, "price_type": "...", "fixed_price": "...",
 "currency": "...", "site_price_info": {...}}
```

Driving plan:
```json
{"driving_plan": [{"vehicleId": "...", "targetSoc": 80, "departureTime": "08:00",
  "everyday": false, "weekday": true, "weekend": false}]}
```

### Disaster Preparedness

```
setDisaster:     {"type": 2, "identifier_id": "<siteid>", "manual_disaster_switch": 1,
                  "start_time": "...", "end_time": "..."}
autoDisaster:    {"type": 2, "identifier_id": "<siteid>", "auto_disaster_switch": 1}
quitDisaster:    {"type": 2, "identifier_id": "<siteid>"}
```

### Message/Notification Control

```json
{"disturb_scenes": [...], "start_charging": true, "stop_charging": true,
 "paused_charging": true, "paused_car_charging": true,
 "restore_charging": true, "smart_charging": true, "boost_charging": true}
```

### A7320 Generator Maintenance

```
setOilReminder:    {"device_sn": "...", "interval_period_month": 2, "interval_period_week": 0}
setExercisePlan:   {"device_sn": "...", "effective_mode": 4,
                    "automatic_exercise": {...}, "manual_exercise": {...}}
batchMaintain:     {"device_sn": "...", "maintenance_items": [{"item_id": "...", "item_name": "...", "description": "..."}]}
setNoticeSwitch:   {"device_sn": "...", "notice_switch": 1}
```

### User Params

```json
{"user_params": [{"param_type": "...", "param_value": "..."}]}
```

### Station Energy Data Flow Grouping

```
all_input = {home_usage, solarbank, grid}
all_input = {pv_input, third_party_pv_input, diesel_input, third_party_diesel_input}
home_usage = {branch_load, other_load}
```

---

## Notes on Accuracy

### Confidence Levels

| Level | Description | Examples |
|-------|-------------|---------|
| **Device-tested** | Tested on real devices by specific community member | param_type 19 power_limit (thomluther, Issue #423) |
| **Upstream-confirmed** | From upstream's community-tested code | param_type 18, 26, 6, 23; set_device_attrs nesting |
| **Structurally inferred** | Consistent Blutter decompilation / toJson() analysis | disturb_scenes nesting, home_load_data nesting |
| **Heuristic** | StoreField pattern, may conflate sequential assignments with nesting | Some nested structures |

### Known Issues

- **param_type 19** structure is **device-tested** by thomluther (Issue #423)
- **param_type 18, 26, 6, 23** structures are from **upstream schedule.py examples** (high confidence)
- **set_device_attrs nesting RESOLVED**: Upstream confirms `switch_0w`, `pv_power_limit`, `tag` etc.
  go **inside** the `attributes` dict: `{"device_sn": "...", "attributes": {"switch_0w": 0}}`
- **`setDeviceHomeLoadRes` missing `site_id`**: Upstream confirms `site_id` is sent (now fixed)
- **Missing from APK extraction**: `set_power_cutoff` and `set_aps_power` — added from upstream
- **AX170 IoT actions** include `deviceSn` alongside `id` and `param` (corrected from
  initial documentation that showed only `{id, param}`)
- **StoreField nesting** analysis may sometimes conflate sequential field assignments
  with nested object construction — treat as hints, not specifications
- **`endpoints/*.md` files** had a systematic parameter-shifting bug (now fixed): parameters
  from one function were incorrectly assigned to adjacent functions. All 16 files have been
  regenerated from `ENDPOINT_FIELDS.md`. Use `ENDPOINT_FIELDS.md` as the authoritative source
- **camelCase HES endpoints**: `bindUnX1Charger` and `updatePeakAndValley` use camelCase
  field names (`stationId`, `evChargers`, `siteId`, `peakValleyPriceSeason`), unlike
  the snake_case convention used by most power_service endpoints

---

## Remaining SET Function Payloads (31 functions)

Extracted from `http_request_repository_impl.dart`. Endpoint paths are in
[ENDPOINT_FIELDS.md](ENDPOINT_FIELDS.md) — keys here show the request body structure.

### Home Load
- **set17C1DeviceHomeLoadRes**: `device_sn, mode_type, custom_rate_plan?, home_load_data?`
- **setDeviceHomeLoadRes**: `site_id, device_sn, home_load_data` (upstream confirms site_id is required)

### Site/Device Param (generic)
- **setSiteDeviceParam**: `site_id, param_type, cmd, param_data`
- **setDynamicPrice**: `site_id, param_type, cmd, param_data` (for dynamic pricing)

### Site Management
- **createSiteRequest**: `site_name, site_img, solar_list, pps_list?, solarbank_list?, ...`
- **updateSiteDevices**: `site_id, pps_list`
- **updateSitePriceRequest**: `site_id, price, site_co2?, site_price_unit?, price_type?, current_mode?, accuracy?, dynamic_price?`
  - `dynamic_price` nested: `{"country": "...", "company": "Nordpool", "area": "GER", "pct": float?, "adjust_coef": float?}`

### OTA/Firmware
- **setThirdOta**: `device_sn, solar_pn, insert_sn, rollback_install_mode`
- **saveThirdOtaInfo**: `solarbank_sn, ota_complete_status`
- **saveCompatibleSolarApi**: (via model serialization)
- **setAutoUpgrade**: `main_switch, device_list`
- **syncInstallation**: `sn, page, errors`

### Prime Charger (A2345/A2687)
- **addCustomChargeMode**: `device_sn, name, number, total_power, max_total_power, auto_exit, has_charge_protocol, power_settings?`
- **updateCustomChargeMode**: `id, name, total_power, max_total_power, auto_exit, has_charge_protocol, power_settings?`
- **deleteCustomChargeMode**: `id`
- **saveCustomChargeModeSetting**: `device_sn, charging_mode_status`
- **saveCompatibilityStatusSetting**: `device_sn, compatibility_status`
- **setA2687ModeSubStatus**: `device_sn, mode, protocol_key, status`
- **setA2687ProtocolAgreementStatus**: `device_sn, protocol_status`
- **setA2687ChargingDeviceModelIdentityStatus**: `device_sn, charging_device_identity_status`
- **setA2687StandardChargingDeviceModelIdentityStatus**: `device_sn, charging_device_identity_new_status`
- **setA2345DeviceIdentityStatus**: `device_sn, charging_device_identity_status_default_true`
- **setPortRemark**: `device_sn, port_name, remark`
- **addA2345CustomClockScreenSavers**: `sn, img_url, hash_code`
- **deleteA2345CustomClockScreenSavers**: `id`
- **addEasterEggStatusRecord**: `device_sn, egg_type, report_time?`

### HES/Energy Service
- **changePriceUnit**: `station_id, price_unit`
- **changeA17B1PriceUnit**: (same pattern for A17B1)
- **dealUtilityRatePlanData**: `peak_sessions` (endpoint: `/charging_energy_service/preprocess_utility_rate_plan`)
- **deleteAndRestartPeakValley**: `station_id, far_field_model`
- **reportHesEvents**: `station_id, pn, language, event`
- **bindUnX1Charger**: `stationId, evChargers, deleteFlag, forceBindFlag` (uses **camelCase**)
- **updateWiFiConfig**: `ssid, sn, rssi, encryption`

### Device Management
- **updateDeviceName**: `device_sn, device_mac, alias_name`
- **updateDeviceInfo**: `device_sn, ble_mac, product_code, device_name, main_sw_version, sec_sw_version`
- **removeParamConfigKey**: `site_id, device_sn, remove_key, use_time`

### Smart Plug
- **setRemainPluginStatus**: (payload from setDeviceFeature — `site_id, smart_plug` list)

### Notifications
- **setEvChargerPushMessage**: `disturb_scenes` (nested object containing: `stop_charging, start_charging, paused_charging, paused_car_charging, restore_charging, smart_charging, boost_charging`)
- **setMessageDisturb**: `start_time, end_time, disturb_switch`

### Pricing
- **updateUserTieredElecPrice**: (via CurrencyElecModel — `sn, currencyUnit, tieredElecPrices`)
- **updatePeakAndValley**: `siteId, peakValleyPriceSeason` (camelCase! — endpoint: `/charging_hes_svc/update_hes_utility_rate_plan`)
  - ⚠️ This is a **HES-specific endpoint**, NOT a `set_site_device_param` wrapper
  - Previously incorrectly documented with `power_limit, limit, limit_real` — those belong to `setSiteDevicePowerLimit`
