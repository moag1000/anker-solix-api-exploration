> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# Anker Solix API Exploration

> **⚠️ IMPORTANT DISCLAIMER**
>
> This reference was created through reverse engineering of the Anker App 3.24.3
> APK (rework in progress on branch `rework/3.24.3`, 2026-10-19; the previous
> 3.18.0 reference is tagged `v2026.04-app3.18.0`) using Blutter (Dart AOT decompiler).
> **The analysis was heavily AI-assisted.** Before polling the cloud with a library, read [docs/SAFE_USAGE.md](docs/SAFE_USAGE.md).
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

## Start here by role

Pick the line that matches what you want to do. Each links to a persona section (who it is for, reading path) and to the first page you need. Details are in [docs/PERSONAS.md](docs/PERSONAS.md).

- **Library maintainer** ("what exactly does the app send?"): [persona](docs/PERSONAS.md#1-library-maintainer), first pages [api/README.md](api/README.md) (one page per endpoint), [api/param_types.md](api/param_types.md) and [api/sdk_senders.md](api/sdk_senders.md).
- **Home Assistant integration developer** ("which setting, which flow, which ranges?"): [persona](docs/PERSONAS.md#2-home-assistant-integration-developer), first pages [flows/](flows/README.md) and [api/param_types.md](api/param_types.md).
- **mqtt_monitor user** ("what is field a8 / cmd 0x7c?"): [persona](docs/PERSONAS.md#3-mqtt_monitor-user), first pages [mqtt/README.md](mqtt/README.md) (one decoder page per product number) and [mqtt/envelope.md](mqtt/envelope.md) (frame and envelope).
- **BLE project developer** ("opcode, TLV, handshake?"): [persona](docs/PERSONAS.md#4-ble-project-developer), the [ble/](ble/README.md) pages are planned (Task 3.7/4.x, nothing there yet); the shared TLV frame and the per-product command tags are in [mqtt/envelope.md](mqtt/envelope.md) and [mqtt/README.md](mqtt/README.md). BLE is a local channel only; it is not a live fallback for the cloud.
- **Curious user / newcomer** ("what can be controlled, what is a site?"): [persona](docs/PERSONAS.md#5-curious-user--newcomer), start with [How to use this reference](#how-to-use-this-reference) and [METHODOLOGY.md](METHODOLOGY.md); the [glossary](GLOSSARY.md).

The layout and the owner of every kind of fact are described in [docs/STRUCTURE.md](docs/STRUCTURE.md); the old root pages are still present and are marked as superseded below.

Coverage and statistics are generated from the data files, see [Statistics and coverage](#statistics-and-coverage).

---

## How this was built

| Source | Method | What it provides | Confidence (3.18.0-era judgement; the tags of [METHODOLOGY.md](METHODOLOGY.md) are authoritative) |
|--------|--------|-----------------|------------|
| `libapp.so` (78 MB ARM64 ELF) | [Blutter](https://github.com/worawit/blutter) AOT decompilation against Dart SDK 3.11.0 | Endpoint paths, function names, request params, response model fields, required/optional classification | Medium — string constants are reliable, param-to-endpoint attribution may have errors |
| `libapp.so` strings | `strings` extraction + pattern matching | MQTT field names, model `toString()` patterns, debug log messages | High for field names, low for interpretation |
| mqtt_monitor sessions | Live MQTT traffic capture on real devices (A17C1, A17X8) | Verified MQTT command fields, state change tracking | Device-tested only where a page records client, version, PN/FW, date and tester (see [METHODOLOGY.md](METHODOLOGY.md)); not re-verified for 3.24.3 |
| APK manifest + resources | Standard APK analysis | Device model codes, BLE UUIDs, app version | High |
| Model `toJson()` methods | class scan of all model classes (count: see Statistics) | Exact request body nesting, field names per model | High — compiler-generated serialization |
| Device-specific logic | `ui/page/device/*/` + helper classes scan | Additional endpoints not in the central repository (counted in Statistics) | Medium — device-specific, may not be available to all accounts |
| Upstream cross-reference | thomluther/anker-solix-api code comparison | Nesting verification, missing fields, confirmed constants | High — upstream code is community-tested on real devices |

**Dart SDK**: 3.11.0 (stable), snapshot: `78da37fed6bf1489361a312568249f3f`

**APK**: Anker App v3.24.3 (versionCode 237), package `com.anker.charging`, XAPK sha256 `7d6d0deab4834515c41aa5e8bafff03f9735e883f15c4f8d5b7194e871ff6ba5`

**History**: previously built on App v3.18.0 (build 160), Dart SDK 3.4.4, snapshot: `d20a1be77c3d3c41b2a5accaee1ce549`.

> This repo is mid-rework (branch `rework/3.24.3`, 2026-10-19). Re-verified against App 3.24.3: [api/](api/README.md), the dedicated pages in [models/](models/README.md), [mqtt/](mqtt/README.md), [flows/](flows/README.md), [devices/a17c5.md](devices/a17c5.md), [devices/modbus.md](devices/modbus.md), [reference/iot_kit_channels.md](reference/iot_kit_channels.md) (90 `akiot.*` IoT-Kit identifiers, 22 new in 3.24.3), the BLE section [ble/](ble/README.md) (protocol, handshake, 30 product pages), [reference/enums.md](reference/enums.md), [reference/business_rules.md](reference/business_rules.md), [reference/validation_model.md](reference/validation_model.md), [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) (native libs, hosts, channels) and the audit tables in [docs/audit/](docs/audit/). Every root page and old section marked "3.18.0 reference, superseded — kept until Task 4.9" below still carries 3.18.0 content and numbers. See [METHODOLOGY.md](METHODOLOGY.md) for the rules and confidence tags used.

---

## How to use this reference

### For API endpoint development
1. Find the endpoint page in [api/](api/README.md): `api/<service>/<endpoint>.md` (service = first URL segment)
2. Check the function name — it tells you the purpose (e.g., `getSafetySocParams` = get safety SOC parameters)
3. The endpoint page owns the request parameters (the old [REQUIRED_FIELDS.md](REQUIRED_FIELDS.md) is a 3.18.0 reference, superseded)
4. Check the response model in [models/README.md](models/README.md) for expected response fields

### For adding new device controls
1. Check [flows/](flows/README.md) for the traced flows and [VALIDATION_MODEL.md](VALIDATION_MODEL.md) for the GET→SET pattern (3.18.0 reference, numbers under review; `reference/validation_model.md` is planned)
2. The app always queries limits/options first (GET), then sets values (SET)
3. Validation ranges come from the server, not from the app — you must query them too

### For mqtt_monitor decoding sessions
1. Use the per-product decoder pages in [mqtt/README.md](mqtt/README.md) to identify unknown hex fields
2. The Blutter-extracted field names tell you what to expect, but hex-to-field assignment requires live verification per [Discussion #222](https://github.com/thomluther/anker-solix-api/discussions/222)

---

## Statistics and coverage

<!-- readme_stats:begin -->
This block is the data snapshot 2026-10-19, generated by `tools/readme_stats.py` from `data/*.json` and the files on disk; do not edit by hand (run the tool again).

**Coverage**

- Endpoint pages: 450 of 450 distinct URLs in `data/endpoints.json` have a page (439 with a code reference in 3.24.3, 9 only in the 3.24.3 object pool with no code reference, 2 only in 3.18.0), plus 3 hand-written pages with no inventory row; 453 endpoint pages in total.
- Of these pages, 124 are hand-written and 329 are skeletons (`Confidence: string-only` with unfilled `<!-- TODO -->` purpose); the skeletons carry only what `data/endpoints.json` knows.

**Statistics**

- 24 API services (directories under [api/](api/README.md))
- 1032 model classes in `data/models.json` (1016 with fields), 53 pages in [models/](models/README.md)
- 24 distinct param_type values sent by 3.24.3 (`data/param_types.json`, owner page [api/param_types.md](api/param_types.md))
- 21 MQTT pages in [mqtt/](mqtt/README.md), 6 flow pages in [flows/](flows/README.md)
- Smi audit of the old root pages ([docs/audit/](docs/audit/)): 1460 audited claims in 15 tables, of which 182 are WRONG (the real value is in each table)
<!-- readme_stats:end -->

The per-service endpoint counts are in the [service index of api/README.md](api/README.md#service-index); the old hand-typed statistics and prefix table were 3.18.0 snapshots and are removed.

---

## param_type Values

The `param_type` values of `get_site_device_param` / `set_site_device_param`, with the sending function, `cmd` and upstream name for every type that App 3.24.3 sends, are owned by [api/param_types.md](api/param_types.md); this README does not repeat them. The type numbers are also listed in `apitypes.py` of [thomluther/anker-solix-api](https://github.com/thomluther/anker-solix-api), which wins on naming.

---

## Command Flows

Now: the traced flows are owned by [flows/](flows/README.md): [flows/system_output_limit.md](flows/system_output_limit.md), [flows/encrypted_request.md](flows/encrypted_request.md) and [flows/modbus_setup.md](flows/modbus_setup.md).
The old page below (3.18.0 reference, superseded — kept until Task 4.9): its slot count, tag and state numbers were Smi misreads; the corrected values are in the [Errata of the CHANGELOG](CHANGELOG.md#errata-2026-10-smi-decoding) and in [docs/audit/FLOWS.md](docs/audit/FLOWS.md).

- [FLOWS.md](FLOWS.md) — step traces from UI button to wire bytes for the solarbank schedule, EV charger start, smart plug timer and schedule, and the solarbank power limit (numbers under review, do not copy them)

---

## Business Rules

Now: planned owner `reference/business_rules.md` (not written yet); the Smi audit of this page is [docs/audit/BUSINESS_RULES.md](docs/audit/BUSINESS_RULES.md). The old page below (3.18.0 reference, superseded — kept until Task 4.9), numbers under review.

- [BUSINESS_RULES.md](BUSINESS_RULES.md) — When SET commands are allowed, what values are valid, what guards exist

Extracted from APK controller assembly. These are the conditions the Anker app checks
before sending a command — device connectivity, charge priority blocking schedules,
value-unchanged skip, SOC defaults, the schedule slot limit and several power limit paths.
**This information is not obtainable from mqtt_monitor or API responses.**

---

## Device Pages

Start here if you own a specific device:

| Device | Page | Upstream Issue | Status |
|--------|------|---------------|--------|
| Solarbank 2 (A17C1) | [devices/solarbank.md](devices/solarbank.md) | [70+ issues](https://github.com/thomluther/ha-anker-solix/issues?q=solarbank) | Core supported |
| Smart Plug (A17X8) | [devices/smart_plug.md](devices/smart_plug.md) | [#150](https://github.com/thomluther/ha-anker-solix/issues/150) | Switch in v3.5.0, timer open |
| Solarbank 3 (A17C5) | [devices/a17c5.md](devices/a17c5.md) | | App 3.24.3 page |
| Modbus (third-party control) | [devices/modbus.md](devices/modbus.md) | | App 3.24.3 page, feature not a PN |
| EV Charger V1 (A5191) | [devices/ev_charger.md](devices/ev_charger.md) | [#322](https://github.com/thomluther/ha-anker-solix/issues/322) | Not yet supported |
| X1 HES / E10 (A5101) | [devices/x1_hes_e10.md](devices/x1_hes_e10.md) | [#274](https://github.com/thomluther/anker-solix-api/issues/274) | Basic monitoring |

---

## Endpoints

Now: every endpoint has its own page under [api/](api/README.md) (service index with page counts and purposes); the machine-readable inventory is [data/endpoints.json](data/endpoints.json).
The old per-file counts and links below are 3.18.0 data and do not add up to the current inventory.
The old content below (3.18.0 reference, superseded — kept until Task 4.9).

| Service | File | Endpoints | Description |
|---------|------|-----------|-------------|
| power_service/v1/site/ | [power_service_site.md](endpoints/power_service_site.md) | 31 | Core site/station management |
| charging_hes_svc/ | [charging_hes_svc.md](endpoints/charging_hes_svc.md) | 28 | Home Energy System (X1, A5101) |
| mini_power/v1/ | [mini_power.md](endpoints/mini_power.md) | 27 | Prime Charger (A2345, A2687) |
| passport/ | [passport.md](endpoints/passport.md) | 24 | Authentication, account management |
| app/ | [app.md](endpoints/app.md) | 18 | Device management, help, OTA |
| power_service/v1/app/ | [power_service_app.md](endpoints/power_service_app.md) | 17 | Upgrade, sharing, device config |
| charging_energy_service/ | [charging_energy_service.md](endpoints/charging_energy_service.md) | 10 | Power Panel (A17B1) |
| power_service/v1/app/compatible/ | [power_service_compatible.md](endpoints/power_service_compatible.md) | 12 | OTA, solar compatibility |
| power_service/v1/ (other) | [power_service_other.md](endpoints/power_service_other.md) | 12 | Messages, currency, products |
| power_service/v1/app/device/ | [power_service_device.md](endpoints/power_service_device.md) | 8 | Device attributes, home load (21 functions, heavily overloaded) |
| power_service/v1/app/share_site/ | [power_service_share.md](endpoints/power_service_share.md) | 5 | Site member management |
| power_service/v1/dynamic_price/ | [power_service_dynamic_price.md](endpoints/power_service_dynamic_price.md) | 3 | Dynamic pricing (Nordpool, Tibber, Octopus) |
| charging_pv_svc/ | [charging_pv_svc.md](endpoints/charging_pv_svc.md) | 4 | Standalone inverters |
| power_service/v1/ai_ems/ | [power_service_ai_ems.md](endpoints/power_service_ai_ems.md) | 2 | AI Energy Management |
| charging_common_svc/ | [charging_common_svc.md](endpoints/charging_common_svc.md) | 1 | Location services |
| *(device-specific)* | [device_specific.md](endpoints/device_specific.md) | 95 | EV Charger, Generator, HES, Storm Guard, AI, etc. |

---

## BLE/MQTT Command Map

Now: MQTT field maps and command tags are in [mqtt/README.md](mqtt/README.md) (per product number, plus [mqtt/envelope.md](mqtt/envelope.md) and [mqtt/upstream_commands.md](mqtt/upstream_commands.md)); BLE pages are planned in [ble/](ble/README.md). Line-by-line audit of the old page: [docs/audit/BLE_COMMAND_MAP.md](docs/audit/BLE_COMMAND_MAP.md).
The claims below ("100% match rate", "20+ new commands") were 3.18.0-era statements and were not re-checked.
The old content below (3.18.0 reference, superseded — kept until Task 4.9).

- [BLE_COMMAND_MAP.md](BLE_COMMAND_MAP.md) — Cross-reference of APK command builders with upstream TLV tag assignments

**New methodology**: By tracing the decompiled command builder functions (field order + Dart Smi
constants) and cross-referencing with thomluther's device-tested `mqttcmdmap.py`, we can infer
which APK field name maps to which TLV hex tag — **without needing a physical device**.

Validated on 5 confirmed commands (A17X8 + A17C1) with 100% match rate. This does NOT replace
device testing — it generates hypotheses that device owners can verify in one mqtt_monitor session.

Covers: A17C1/C5 (Solarbank), A17X8 (Smart Plug), A17C0 (SB Gen1), PPS family, A1790 (F3800),
A5190 (EV Charger), A5101 (X1 HES), EverFrost, Prime Charger. Includes 20+ NEW commands not in upstream.

---

## Validation Model

Now: planned owner `reference/validation_model.md` (not written yet); flows that use the ranges are in [flows/](flows/README.md); audit of the old page: [docs/audit/VALIDATION_MODEL.md](docs/audit/VALIDATION_MODEL.md).
The category count below is a 3.18.0 number.
The old content below (3.18.0 reference, superseded — kept until Task 4.9).

- [VALIDATION_MODEL.md](VALIDATION_MODEL.md) — GET→SET flow for 33 setting categories across API, MQTT and BLE

Covers: Power limits, home load, SOC reserve, usage modes, grid export, LED, temperature, cutoff, smart plug schedule/timer, EV charger, generator, heat pump, disaster preparedness, and more.

Key finding: **the app does not hardcode validation ranges.** It queries the server for device-specific min/max/step values and builds the UI dynamically. Developers must follow the same pattern.

## Field Types and Examples

Now: field lists live on the model pages ([models/README.md](models/README.md)) and in [data/models.json](data/models.json).
The counts below are 3.18.0 numbers.
The old content below (3.18.0 reference, superseded — kept until Task 4.9).

- [FIELD_TYPES.md](FIELD_TYPES.md) — 234 fields with data types and example values, cross-referenced across Blutter (B), thomluther's API examples (U), and MQTT mappings (M)
- [DART_PYTHON_MAPPING.md](DART_PYTHON_MAPPING.md) — 35 confirmed Dart camelCase → JSON snake_case field name pairs

## Endpoint → Fields Direct Mapping

Now: param_type structures are owned by [api/param_types.md](api/param_types.md); request parameters and response models per endpoint are on the endpoint pages in [api/](api/README.md).
The endpoint count below is a 3.18.0 number.
The old content below (3.18.0 reference, superseded — kept until Task 4.9).

- [PARAM_DATA_STRUCTURES.md](PARAM_DATA_STRUCTURES.md) — Nested JSON structures for param_data per param_type (cross-referenced with thomluther's Issue #423 device findings)
- [ENDPOINT_FIELDS.md](ENDPOINT_FIELDS.md) — ~150 endpoints with request parameters and response model mapping (91 with identified response models), plus nesting corrections from 460 toJson() class analysis

## JSON Payloads and Examples

Now: examples belong to the owning endpoint page in [api/](api/README.md); audits of the old pages: [docs/audit/JSON_EXAMPLES.md](docs/audit/JSON_EXAMPLES.md), [docs/audit/RESPONSE_EXAMPLES.md](docs/audit/RESPONSE_EXAMPLES.md).
The example counts below are 3.18.0 numbers.
The old content below (3.18.0 reference, superseded — kept until Task 4.9).

- [JSON_EXAMPLES.md](JSON_EXAMPLES.md) — 33 upstream-sourced request payloads + 60 inferred + new parameter discoveries + enum constants + device-specific payload templates (EV charger, generator, SceneInfo feature flags)
- [RESPONSE_EXAMPLES.md](RESPONSE_EXAMPLES.md) — 71 real API response examples from 48 endpoints (extracted from thomluther's documented code)

## Enums, Constants, and Product Codes

Now: planned owner `reference/enums.md` (not written yet); audit of the old page: [docs/audit/ENUMS.md](docs/audit/ENUMS.md).
The counts and code lists below are 3.18.0 content.
The old content below (3.18.0 reference, superseded — kept until Task 4.9).

- [ENUMS.md](ENUMS.md) — 30+ enum types with exact API integer values: EmsModeType (6 modes with API codes 1/4/5/8/9/10), 16-bit EnergyFlowType bitmask, AI mode codes, BLE status codes, MQTT command types, generator modes, PPS work status, price types, 60 product codes, 13 supported countries, TOU schedule templates

---

## Required vs Optional Fields

Now: required/optional flags belong in the parameter table of each endpoint page in [api/](api/README.md).
The numbers below are 3.18.0 counts.
The old content below (3.18.0 reference, superseded — kept until Task 4.9).

- [REQUIRED_FIELDS.md](REQUIRED_FIELDS.md) — Required/optional field classification for 180 endpoints

Derived from conditional branching patterns in decompiled Dart code: fields without a preceding branch instruction are always included in the request body (required), fields with a branch are conditionally added (optional/context-dependent).

97 endpoints have explicit required fields. 63 pass parameters via object construction not visible as string constants.

---

## Response Models

Now: [models/README.md](models/README.md) is the index of all model pages (dedicated pages per class plus legacy group pages); the field lists are generated into [data/models.json](data/models.json).
The group table below lists legacy pages only; several classes have since moved to dedicated pages, so its model counts were dropped.
The old content below (3.18.0 reference, superseded — kept until Task 4.9).

These are **Dart class names** from the decompiled APK, not Python classes from thomluther's API library.
The field names come from `fromJson` / `toJson` methods and represent the JSON keys in API responses.

| Category | File | Description |
|----------|------|-------------|
| Other | [models/other.md](models/other.md) | Banner, FAQ, messages, ranking, misc |
| Home Energy System | [models/hes.md](models/hes.md) | A5101/X1 disaster prep, commands, grid config |
| Account / Sharing | [models/account.md](models/account.md) | User, login, site members, validation |
| Firmware / OTA | [models/firmware.md](models/firmware.md) | Update status, batch device, upgrade records |
| Pricing / TOU | [models/pricing.md](models/pricing.md) | Dynamic price, TOU, currency |
| Solarbank | [models/solarbank.md](models/solarbank.md) | Home load, site consumption strategy, schedules |
| WiFi / Installation | [models/connectivity.md](models/connectivity.md) | WiFi info, installation inspection |
| Charger | [models/charger.md](models/charger.md) | A2345/A2687 charge modes, protocols |
| Device Management | [models/device.md](models/device.md) | Device list, auto-upgrade |
| Green Energy | [models/energy.md](models/energy.md) | Scene info, green PPS site detail |
| Products / Brands | [models/products.md](models/products.md) | Product categories, brands, Shelly platforms |
| Power Limits | [models/power.md](models/power.md) | Station power limit, device power limit |
| PPS | [models/pps.md](models/pps.md) | A5140 status, A1340 charging device |

---

## Cross-Reference: Response Model → Endpoint → Setting

Now: the model pages ([models/station_power_limit.md](models/station_power_limit.md), [models/get_site_device_param_response.md](models/get_site_device_param_response.md), others in [models/README.md](models/README.md)) link to the endpoints that carry them; endpoint pages are in [api/](api/README.md).
The endpoint-group names below are the old file names.
The old content below (3.18.0 reference, superseded — kept until Task 4.9).

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

This section (3.18.0 reference, superseded — kept until Task 4.9): the counts and claims in it are 3.18.0-era and were not re-checked (current counts: [Statistics and coverage](#statistics-and-coverage)).

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
- **Partial nesting information** — key SET functions now have upstream-confirmed nesting (set_device_attrs, param_data) and structurally inferred nesting from toJson() analysis (disturb_scenes, home_load_data), but many GET response structures still lack full nesting detail
- **Example responses are from thomluther's code** — [RESPONSE_EXAMPLES.md](RESPONSE_EXAMPLES.md) has 71 examples, but these are copies from thomluther's docstrings, not independently captured
- **Field types** (int/string/bool/list) are not extractable — the TLV protocol carries type information in the data packets themselves, and the server responses use standard JSON typing
- **Validation ranges** are dynamic (from server), not hardcoded in the app — each device/region may have different min/max/step values
- **Error codes** are scattered throughout the code; a catalog is planned (`api/errors.md`, not written yet)
- **Cooler devices** (A17A3-A5 EverFrost) have minimal logic in the Dart layer — most control appears to be BLE-only with limited decompilable structure
- **BLE action names without payload formats** — knowing `action_set_backup_strategy` exists does not help without the binary payload structure, which requires hardware testing
- **12 response models** yielded no field names due to generic deserialization patterns
- **25 of 205 endpoints** are not covered in REQUIRED_FIELDS.md (passport auth + misc)
- **param_type 7** is listed in apitypes.py but App 3.24.3 sends no such `param_type` literal (see [api/param_types.md](api/param_types.md))

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the device-tested record template, how to report a contradiction, and the checks a change must pass (issue templates: `device-tested`, `correction`).

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
