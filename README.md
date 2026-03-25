# Anker Solix API Exploration

> **⚠️ IMPORTANT DISCLAIMER**
>
> This reference was created through reverse engineering of the Anker App v3.18.0
> APK using Blutter (Dart AOT decompiler). **The analysis was heavily AI-assisted.**
> This means the content may be:
>
> - **Inaccurate** — field names extracted from compiled binary code may be
>   misattributed to the wrong endpoint or context
> - **Incomplete** — many values, types and constraints are compiled into native
>   ARM64 machine code and could not be recovered
> - **Fundamentally wrong in parts** — AI interpretation of decompiled assembly
>   can produce plausible-looking but incorrect conclusions
>
> **Do not rely on this as authoritative documentation.** Every claim should be
> verified against the live API or the mqtt_monitor tool before use in production
> code. Anker can change any endpoint, field name or behavior between app versions
> without notice.
>
> **No server-side impact analysis has been performed.** This exploration documents
> what the app *sends*, not what the server *expects* or *tolerates*. Sending
> malformed, unexpected, or excessive requests to Anker's API or MQTT infrastructure
> could have unintended consequences including but not limited to account restrictions,
> device malfunction, or infrastructure impact. **Anyone using this data does so
> entirely at their own risk and responsibility.** The authors accept no liability
> for any consequences arising from the use of this information.

---

## How this was built

| Source | Method | What it provides | Confidence |
|--------|--------|-----------------|------------|
| `libapp.so` (58MB ARM64 ELF) | [Blutter](https://github.com/worawit/blutter) AOT decompilation against Dart SDK 3.4.4 | Endpoint paths, function names, request params, response model fields, required/optional classification | Medium — string constants are reliable, param-to-endpoint attribution may have errors |
| `libapp.so` strings | `strings` extraction + pattern matching | MQTT field names, model `toString()` patterns, debug log messages | High for field names, low for interpretation |
| mqtt_monitor sessions | Live MQTT traffic capture on real devices (A17C1, A17X8) | Verified MQTT command fields, state change tracking | High — byte-for-byte verified |
| APK manifest + resources | Standard APK analysis | Device model codes, BLE UUIDs, app version | High |

**Dart SDK**: 3.4.4 (stable), snapshot hash `d20a1be77c3d3c41b2a5accaee1ce549`

**APK**: Anker App v3.18.0 (build 160), package `com.anker.charging`, from APKPure

---

## How to use this reference

### For API endpoint development
1. Find the endpoint in [endpoints/](endpoints/) by service prefix
2. Check the function name — it tells you the purpose (e.g., `getSafetySocParams` = get safety SOC parameters)
3. Check [REQUIRED_FIELDS.md](REQUIRED_FIELDS.md) for which params are required vs optional
4. Check the response model in [models/](models/) for expected response fields

### For adding new device controls
1. Check [VALIDATION_MODEL.md](VALIDATION_MODEL.md) for the GET→SET flow
2. The app always queries limits/options first (GET), then sets values (SET)
3. Validation ranges come from the server, not from the app — you must query them too

### For mqtt_monitor decoding sessions
1. Use the MQTT field name references to identify unknown hex fields
2. The Blutter-extracted field names tell you what to expect, but hex-to-field assignment requires live verification per [Discussion #222](https://github.com/thomluther/anker-solix-api/discussions/222)

---

## Statistics

- **243** function-to-endpoint mappings across **205** unique API endpoints
- **94** response models with field names
- **180** endpoints with required/optional field classification
- **33** device setting categories with complete GET→SET flows
- **82** BLE/IoT SDK action names (65 actions + 14 prop + 3 query)
- **234** cross-referenced field types with examples
- **60** unique product codes (44 IoT + 16 from message models)
- **30+** enum types with exact API integer values
- **71** real API response examples from thomluther's code
- **13** supported countries for dynamic pricing

---

## param_type Values

For `get_site_device_param` / `set_site_device_param`:

The type numbers are already listed in `apitypes.py` of [thomluther/anker-solix-api](https://github.com/thomluther/anker-solix-api). What Blutter adds is the **function name → purpose** mapping.

| type | Function (from Blutter) | Purpose | Status |
|------|------------------------|---------|-----------------|
| 1 | `getSiteGreenModeDeviceParam` | Green mode settings | Number known, **purpose new** |
| 2 | `getSitePeakTimeDeviceParam` | Peak/valley time params | Number known, **purpose new** |
| 3 | `getSiteEnablePeakDeviceParam` | Peak shaving enable | Number known, **purpose new** |
| 4 | *(native layer)* | SB1 schedule | Known (schedule.py has example data) |
| 5 | `getSiteLowerLimitDeviceParam` | Lower limit / min power | Number known, **purpose new** |
| 6 | *(native layer)* | SB2/SB3 schedule | Known (schedule.py has example data) |
| 7 | *(not in APK v3.18.0)* | Unknown | Number known, purpose unknown |
| 9 | *(native layer)* | SB1 in SB2 system schedule | Known (schedule.py) |
| 12 | *(native layer)* | SB3 TOU/dynamic price plan | Known (schedule.py) |
| 13 | *(native layer)* | SB3 system config | Known (schedule.py) |
| 16 | `getCombineBoxListData` | Combiner box / power dock | Known response, function name from Blutter |
| 18 | `getSafetySocParams` | Safety SOC parameters | Known response, function name from Blutter |
| 19 | `setSiteDevicePowerLimit` | Power limit (SET only) | Number **not in apitypes.py list**, purpose new |
| 20 | `get/setStationCountryCode` | Station country code | Number known, **purpose new** |
| 23 | *(not in APK v3.18.0)* | Switch config | Known (schedule.py, minimal) |
| 26 | `getThreePvParam` | 3rd-party PV params | Known response, function name from Blutter |

---

## Endpoints

| Service | File | Endpoints | Description |
|---------|------|-----------|-------------|
| power_service/v1/site/ | [power_service_site.md](endpoints/power_service_site.md) | 31 | Core site/station management |
| charging_hes_svc/ | [charging_hes_svc.md](endpoints/charging_hes_svc.md) | 28 | Home Energy System (X1, A5101) |
| mini_power/v1/ | [mini_power.md](endpoints/mini_power.md) | 27 | Prime Charger (A2345, A2687) |
| passport/ | [passport.md](endpoints/passport.md) | 24 | Authentication, account management |
| app/ | [app.md](endpoints/app.md) | 18 | Device management, help, OTA |
| power_service/v1/app/ | [power_service_app.md](endpoints/power_service_app.md) | 17 | Upgrade, sharing, device config |
| charging_energy_service/ | [charging_energy_service.md](endpoints/charging_energy_service.md) | 13 | Power Panel (A17B1) |
| power_service/v1/app/compatible/ | [power_service_compatible.md](endpoints/power_service_compatible.md) | 12 | OTA, solar compatibility |
| power_service/v1/ (other) | [power_service_other.md](endpoints/power_service_other.md) | 12 | Messages, currency, products |
| power_service/v1/app/device/ | [power_service_device.md](endpoints/power_service_device.md) | 8 | Device attributes, home load (21 functions, heavily overloaded) |
| power_service/v1/app/share_site/ | [power_service_share.md](endpoints/power_service_share.md) | 5 | Site member management |
| power_service/v1/dynamic_price/ | [power_service_dynamic_price.md](endpoints/power_service_dynamic_price.md) | 3 | Dynamic pricing (Nordpool, Tibber, Octopus) |
| charging_pv_svc/ | [charging_pv_svc.md](endpoints/charging_pv_svc.md) | 3 | Standalone inverters |
| power_service/v1/ai_ems/ | [power_service_ai_ems.md](endpoints/power_service_ai_ems.md) | 2 | AI Energy Management |
| charging_common_svc/ | [charging_common_svc.md](endpoints/charging_common_svc.md) | 1 | Location services |

---

## Validation Model

- [VALIDATION_MODEL.md](VALIDATION_MODEL.md) — GET→SET flow for 33 setting categories across API, MQTT and BLE

Covers: Power limits, home load, SOC reserve, usage modes, grid export, LED, temperature, cutoff, smart plug schedule/timer, EV charger, generator, heat pump, disaster preparedness, and more.

Key finding: **the app does not hardcode validation ranges.** It queries the server for device-specific min/max/step values and builds the UI dynamically. Developers must follow the same pattern.

## Field Types and Examples

- [FIELD_TYPES.md](FIELD_TYPES.md) — 234 fields with data types and example values, cross-referenced across Blutter (B), thomluther's API examples (U), and MQTT mappings (M)
- [DART_PYTHON_MAPPING.md](DART_PYTHON_MAPPING.md) — 35 confirmed Dart camelCase → JSON snake_case field name pairs

## Endpoint → Fields Direct Mapping

- [ENDPOINT_FIELDS.md](ENDPOINT_FIELDS.md) — 142 endpoints with request parameters and response model mapping (90 with identified response models)

## JSON Payloads and Examples

- [JSON_EXAMPLES.md](JSON_EXAMPLES.md) — 33 verified request payloads + 60 inferred + new parameter discoveries + enum constants + device-specific payload templates (EV charger, generator, SceneInfo feature flags)
- [RESPONSE_EXAMPLES.md](RESPONSE_EXAMPLES.md) — 71 real API response examples from 48 endpoints (extracted from thomluther's documented code)

## Enums, Constants, and Product Codes

- [ENUMS.md](ENUMS.md) — 30+ enum types with exact API integer values: EmsModeType (6 modes with API codes 1/4/5/8/9/10), 16-bit EnergyFlowType bitmask, AI mode codes, BLE status codes, MQTT command types, generator modes, PPS work status, price types, 60 product codes, 13 supported countries, TOU schedule templates

---

## Required vs Optional Fields

- [REQUIRED_FIELDS.md](REQUIRED_FIELDS.md) — Required/optional field classification for 180 endpoints

Derived from conditional branching patterns in decompiled Dart code: fields without a preceding branch instruction are always included in the request body (required), fields with a branch are conditionally added (optional/context-dependent).

97 endpoints have explicit required fields. 63 pass parameters via object construction not visible as string constants.

---

## Response Models

These are **Dart class names** from the decompiled APK, not Python classes from thomluther's API library.
The field names come from `fromJson` / `toJson` methods and represent the JSON keys in API responses.

| Category | File | Models | Description |
|----------|------|--------|-------------|
| Other | [models/other.md](models/other.md) | 28 | Banner, FAQ, messages, ranking, misc |
| Home Energy System | [models/hes.md](models/hes.md) | 14 | A5101/X1 disaster prep, commands, grid config |
| Account / Sharing | [models/account.md](models/account.md) | 10 | User, login, site members, validation |
| Firmware / OTA | [models/firmware.md](models/firmware.md) | 9 | Update status, batch device, upgrade records |
| Pricing / TOU | [models/pricing.md](models/pricing.md) | 7 | Dynamic price, TOU, currency |
| Solarbank | [models/solarbank.md](models/solarbank.md) | 5 | Home load, site consumption strategy, schedules |
| WiFi / Installation | [models/connectivity.md](models/connectivity.md) | 4 | WiFi info, installation inspection |
| Charger | [models/charger.md](models/charger.md) | 4 | A2345/A2687 charge modes, protocols |
| Device Management | [models/device.md](models/device.md) | 3 | Device list, auto-upgrade |
| Green Energy | [models/energy.md](models/energy.md) | 3 | Scene info, green PPS site detail |
| Products / Brands | [models/products.md](models/products.md) | 3 | Product categories, brands, Shelly platforms |
| Power Limits | [models/power.md](models/power.md) | 2 | Station power limit, device power limit |
| PPS | [models/pps.md](models/pps.md) | 2 | A5140 status, A1340 charging device |

---

## Cross-Reference: Response Model → Endpoint → Setting

Key models that carry validation information:

| Response Model | Endpoint Group | Provides |
|---------------|---------------|----------|
| `StationPowerLimitModel` | power_service_site | min, max, step, legal_limit, power_limit_option |
| `DevicePowerLimit` | power_service_site | min, max, step, legal_power_limit, region_power_limit |
| `SiteConsumptionStrategyModel` | power_service_site | mode_type, min_load, max_load, step, reserved_soc |
| `A17C1DeviceHomeLoadData` | power_service_device | min_load, max_load, step, ranges, schedule_mode |
| `SiteHomeLoadModel` | power_service_site | min_load, max_load, step, parallel_home_load |
| `AiModeStatusModel` | power_service_ai_ems | status, result, left_time |
| `CheckFunctionModel` | charging_hes_svc | auto_disaster, peak_shaving, support flags |
| `AutoDisasterPrepareStatusModel` | charging_hes_svc | code, disasterPrepareStatus, events |
| `DynamicPriceDetailModel` | power_service_dynamic_price | time, price, currency, avgPrice, trend |
| `TouDeviceAttrsModel` | power_service_device | attributes, prices, ranges, reserve_power |
| `GetSiteDeviceParamResponse` | power_service_site | param_data (JSON per param_type) |

---

## What this exploration IS and IS NOT

**This is useful as:**
- A **vocabulary / cheat sheet** for mqtt_monitor decoding sessions — knowing the field names that exist in the app helps identify unknown hex fields faster
- A **param_type purpose mapping** — types 1, 2, 3, 5, 19, 20 were previously undocumented
- A **validation flow guide** — understanding that the app always queries limits before setting values
- A **BLE action inventory** — 82 action/prop/query names tell you what controls exist, even if the payload format is unknown
- An **enum reference** — EMS modes, energy flow bitmasks, price types, device types, BLE status codes with their exact API integer values
- A **product code registry** — 60 known device model codes
- A **starting point** for device owners who want to contribute verified mappings

**This is NOT:**
- A replacement for [thomluther/anker-solix-api](https://github.com/thomluther/anker-solix-api) — that library has real, tested, working code
- A source of verified hex-to-field mappings — those require mqtt_monitor sessions per [Discussion #222](https://github.com/thomluther/anker-solix-api/discussions/222)
- Implementation-ready data — the field names are Dart class names (camelCase), not the snake_case JSON keys used in API responses. See [DART_PYTHON_MAPPING.md](DART_PYTHON_MAPPING.md) for 35 confirmed pairs, but coverage is incomplete.
- A complete API specification — most of the 205 endpoints listed here are already documented in `apitypes.py`. The incremental value is in the param_type mappings, response model fields, and required/optional classification.
- Reliable for required/optional — the branch-based detection has known false positives (see REQUIRED_FIELDS.md header)

## Known Limitations

- **Dart names ≠ JSON keys** — the response model fields are Dart property names (camelCase). The actual API JSON uses snake_case in most cases, but the mapping is not 1:1 — see [DART_PYTHON_MAPPING.md](DART_PYTHON_MAPPING.md) for 35 confirmed pairs
- **Flat field lists ≠ JSON structure** — fields are listed without nesting information. Real responses have objects, arrays, and optional fields that this reference does not capture
- **Example responses are from thomluther's code** — [RESPONSE_EXAMPLES.md](RESPONSE_EXAMPLES.md) has 71 examples, but these are copies from thomluther's docstrings, not independently captured
- **Field types** (int/string/bool/list) are not extractable — the TLV protocol carries type information in the data packets themselves, and the server responses use standard JSON typing
- **Validation ranges** are dynamic (from server), not hardcoded in the app — each device/region may have different min/max/step values
- **Error codes** are scattered throughout the code with no central registry found
- **Cooler devices** (A17A3-A5 EverFrost) have minimal logic in the Dart layer — most control appears to be BLE-only with limited decompilable structure
- **BLE action names without payload formats** — knowing `action_set_backup_strategy` exists does not help without the binary payload structure, which requires hardware testing
- **12 response models** yielded no field names due to generic deserialization patterns
- **25 of 205 endpoints** are not covered in REQUIRED_FIELDS.md (passport auth + misc)
- **param_type 7** is listed in apitypes.py but not found in APK v3.18.0

---

## Contributing

To improve this reference:

1. **Run mqtt_monitor sessions** on your device and compare unknown fields against the model field names listed here
2. **Test API endpoints** with the [anker-solix-api](https://github.com/thomluther/anker-solix-api) library and report actual response structures
3. **Report errors** — if you find a field attribution that is wrong, please flag it so it can be corrected
4. Follow the methodology described in [Discussion #222](https://github.com/thomluther/anker-solix-api/discussions/222)

---

## Trademarks

Anker, Solix, Solarbank, EverFrost, and related product names are trademarks of
Anker Innovations Limited. Shelly is a trademark of Allterco Robotics. Nordpool,
Tibber, Octopus Energy, Amazon, Alexa, and Google are trademarks of their
respective owners. OCPP is a standard by the Open Charge Alliance.

This project is not affiliated with, endorsed by, or connected to any of these
companies. All trademarks are used here solely for identification and
interoperability documentation purposes under fair use.
