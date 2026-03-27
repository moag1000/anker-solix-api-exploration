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
