# param_data JSON Structures

> Extracted from Blutter decompilation by tracing Map construction patterns
> near `jsonEncode()` calls and `set_site_device_param` invocations.
>
> **Important:** `param_data` is always a **JSON string** (not a nested object).
> The API expects: `{"param_data": "{\"key\":{\"nested\":\"value\"}}"}` — a string
> containing JSON, not a nested object directly.
>
> Verified example from thomluther (param_type 19):
> ```json
> {"site_id": "<id>", "param_type": "19", "cmd": 17,
>  "param_data": "{\"power_limit\":{\"limit\":3600,\"limit_real\":3600}}"}
> ```

## param_type 19 — Power Limit (SET only)

Function: `setSiteDevicePowerLimit`

Verified by thomluther ([Issue #423](https://github.com/thomluther/ha-anker-solix/issues/423#issuecomment-4135301109)):

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

### set_device_attrs — 9 Different Payload Patterns

The `set_device_attrs` endpoint uses `device_sn` + `attributes` as base, with
different additional fields per use case:

```
setDevicePowerOptionsReq:     {"device_sn": "...", "attributes": {...}, "enable_0w_v2": true}
setTouElectricAttrs:          {"device_sn": "...", "attributes": {...}, "pps_use_time": "..."}
getCurrencySetDeviceAttrs:    {"device_sn": "...", "attributes": {...}, "currency": "..."}
setSolarName:                 {"device_sn": "...", "device_pn": "...", "attributes": {...}}
setDeviceFeedGridSwitch:      {"device_sn": "...", "attributes": {...}, "switch_0w": 0}
setDevicePvPowerOptionsReq:   {"device_sn": "...", "attributes": {...}, "pv_power_limit": 800}
setLocationTag:               {"device_sn": "...", "attributes": {...}, "tag": "..."}
setDeviceGameStatus:          {"device_sn": "...", "attributes": {...}, "init_status": "..."}
setPpsSolarName:              {"device_sn": "...", "device_pn": "...", "attributes": {...}}
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

- **param_type 19** structure is **verified** by thomluther (Issue #423)
- **param_type 18, 26, 6, 23** structures are from **upstream schedule.py examples** (high confidence)
- **set_device_attrs patterns** show `switch_0w`, `pv_power_limit`, `tag` etc. as separate
  keys alongside `attributes` in the decompiled code. Upstream confirms this pattern for
  `{"attributes": {"pv_power_limit": 800}}`. Whether additional keys like `switch_0w` are
  at the same level or inside `attributes` needs API testing to confirm.
- **AX170 IoT actions** include `deviceSn` alongside `id` and `param` (corrected from
  initial documentation that showed only `{id, param}`)
- **StoreField nesting** analysis may sometimes conflate sequential field assignments
  with nested object construction — treat as hints, not specifications
