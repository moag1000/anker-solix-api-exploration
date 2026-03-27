# Solarbank — A17C0, A17C1, A17C2, A17C3, A17C5

> **Priority**: P1 (Core) — largest user base, 70+ upstream issues
> Most actively developed device category in thomluther's integration

## Product Info

- **A17C0** — Solarbank E1600 (Gen 1)
- **A17C1** — Solarbank 2 E1600 Pro (Gen 2, flagship)
- **A17C2** — Solarbank 2 E1600 AC (AC-coupled)
- **A17C3** — Solarbank 2 E1600 Plus (budget Gen 2)
- **A17C5** — Solarbank 3 E2700 Pro (Gen 3, bidirectional)
- All consumer balcony solar, sold on anker.com / Amazon EU

## Related Files in This Repo

- [PARAM_DATA_STRUCTURES.md](../PARAM_DATA_STRUCTURES.md) — All param_type payload structures
- [VALIDATION_MODEL.md](../VALIDATION_MODEL.md) — 33 GET→SET flows (power limit, SOC, schedule, etc.)
- [ENDPOINT_FIELDS.md](../ENDPOINT_FIELDS.md#set_site_device_param) — set_site_device_param variants
- [ENDPOINT_FIELDS.md](../ENDPOINT_FIELDS.md#set_device_attrs) — set_device_attrs with confirmed nesting
- [FIELD_TYPES.md](../FIELD_TYPES.md) — 234+ field types with examples
- [FIELD_TYPES.md](../FIELD_TYPES.md#attributes-inner-fields-soc_modeldart--all-go-inside-attributes-dict) — Full attributes field list
- [ENUMS.md](../ENUMS.md) — EMS modes, usage modes, energy flow types
- [models/solarbank.md](../models/solarbank.md) — Response models
- [models/power.md](../models/power.md) — StationPowerLimitModel, DevicePowerLimit
- [RESPONSE_EXAMPLES.md](../RESPONSE_EXAMPLES.md) — 71 real API response examples
- [endpoints/power_service_site.md](../endpoints/power_service_site.md) — Site management endpoints
- [endpoints/power_service_device.md](../endpoints/power_service_device.md) — Device control endpoints

## param_type System

The core control mechanism. `get_site_device_param` / `set_site_device_param`
with numbered types. See [PARAM_DATA_STRUCTURES.md](../PARAM_DATA_STRUCTURES.md).

| type | Function | Purpose | Confidence |
|------|----------|---------|------------|
| 1 | `getSiteGreenModeDeviceParam` | Green mode settings | APK-extracted |
| 2 | `getSitePeakTimeDeviceParam` | Peak/valley time | APK-extracted |
| 3 | `getSiteEnablePeakDeviceParam` | Peak shaving enable | APK-extracted |
| 5 | `getSiteLowerLimitDeviceParam` | Lower limit / min power | APK-extracted |
| 6 | `set17C1SiteDeviceParam` | SB2/SB3 schedule | Upstream-confirmed |
| 18 | `setSafetySocParams` | Safety SOC | Upstream-confirmed |
| 19 | `setSiteDevicePowerLimit` | Power limit | Device-tested (thomluther, #423) |
| 20 | `get/setStationCountryCode` | Country/grid code | APK-extracted |
| 23 | — | Switch config | Upstream-confirmed |
| 26 | `getThreePvParam` | Third-party PV | Upstream-confirmed |

### param_type 6 — Schedule Structure (upstream-confirmed)
```json
{"mode_type": 3, "custom_rate_plan": [
  {"index": 0, "week": [0, 6], "ranges": [
    {"start_time": "00:00", "end_time": "24:00", "power": 110}
  ]}
]}
```

### param_type 18 — Safety SOC (upstream-confirmed)
```json
{"soc_list": [{"id": 1, "is_selected": 1, "soc": 10}],
 "switch_0w": 0, "enable_0w": 0, "feed-in_power_limit": 0}
```
Note: `feed-in_power_limit` uses a **HYPHEN** (not underscore).

### param_type 19 — Power Limit (device-tested by thomluther)
```json
{"power_limit": {"limit": 3600, "limit_real": 3600}}
```

## Usage Modes (from ENUMS)

| Value | Mode | Description |
|-------|------|-------------|
| 1 | `smartmeter` | Smart Meter driven |
| 2 | `smartplugs` | Smart Plug driven |
| 3 | `manual` | Manual fixed output |
| 4 | `backup` | Backup power |
| 5 | `use_time` | Time-of-use |
| 7 | `smart` | AI/smart mode |
| 8 | `time_slot` | Time slot schedule |

## MQTT Commands (device-tested on A17C1 FW 1.0.6.10)

| Cmd | Name | Fields | Tested |
|-----|------|--------|--------|
| `0050` | Temp Unit | a2: 0=Celsius, 1=Fahrenheit | mqtt_monitor |
| `0067` | Power Cutoff | a2=output_cutoff, a3=lowpower_input, a4=input_cutoff | mqtt_monitor |
| `005a` | Max Load | a2=max_load (W), a3=max_load_type | mqtt_monitor |
| `005e` | Usage Mode | a2=mode (1-8), complex multi-field | mqtt_monitor (modes 1+3) |
| `0068` | Inverter Type | a5=brand, a6=model, a7=min_load, a8=max_load | upstream |
| `0073` | AC Socket | a2: 0=off, 1=on | upstream |
| `0080` | Grid Export | a6=disable_switch, a9=export_limit | upstream |
| `0085` | 3rd Party PV | a2: 0=off, 1=on (cloud-driven) | upstream |

## Response Models

- `SiteConsumptionStrategyModel` — mode_type, min_load, max_load, step, reserved_soc, custom_rate_plan, ai_ems, exceed_alarm
- `A17C1DeviceHomeLoadData` — schedule_mode, ranges, charge_priority, appliance_loads, device_power_loads
- `GetSiteDeviceParamResponse` — param_data per param_type
- `StationPowerLimitModel` — min, max, step, legal_limit, power_limit_option

## Key Attributes (inside `attributes` dict)

Upstream confirms these go **inside** `{"device_sn": "...", "attributes": {...}}`:

| Field | Type | Notes |
|-------|------|-------|
| `pv_power_limit` | int | PV input limit (W) |
| `ac_power_limit` | int | AC input limit (W) |
| `power_limit` | int | AC output limit (W) |
| `switch_0w` | int | Grid export: 0=allow, 1=block |
| `enable_0w` | int | 0W mode enable |
| `feeder0w` | int | Feeder 0W setting |
| `pv_power_limit_option` | int | PV limit option |
| `user_power_limit` | int | User-set limit |

## MQTT Abbreviated Fields (A17B1 system context)

| Key | Meaning | Key | Meaning |
|-----|---------|-----|---------|
| `soc` | State of charge | `m` | Mode |
| `bp` | Battery power | `bpu` | Battery power unit |
| `pp` | PV power | `ppu` | PV power unit |
| `gp` | Grid power | `gpu` | Grid power unit |
| `lp` | Load power | `lpu` | Load power unit |
| `op` | Output power | `mps` | Master/parallel state |
| `p2bp` | PV→Battery | `p2lp` | PV→Load |
| `p2gp` | PV→Grid | `b2lp` | Battery→Load |
| `b2gp` | Battery→Grid | `g2bp` | Grid→Battery |
| `g2lp` | Grid→Load | `mpp` | Micro-inverter power |
