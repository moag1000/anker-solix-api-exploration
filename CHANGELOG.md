# Changelog

## 2026-03-28 — BLE/MQTT Protocol Reference (2350 lines), device pages, API findings

### Concrete NEW API/Protocol Findings (not previously known)

**Wire protocol details** (from ZXCommandTransformer/ZXCmdUtil assembly):
- TLV frame: `0xA1` marker, `0x02` version, direction byte `0x42`/`0x44`
- Direction detection: `(byte[0] & 0x0F) >> 3` — bit 3 = response
- Data type codes: 1=ui(1B), 2=int(2B), 3=variable, 4=int(4B)
- Checksum: XOR of all bytes
- Timestamps: Unix seconds (not ms) via `DateTime.now().toUtc().microsecondsSinceEpoch / 1e6`

**MQTT envelope** (from MqttCommandTransformer):
- `sess_id` and `msg_seq` are HARDCODED ("1" and 2) — not dynamic sequence numbers
- Topic pattern: `cmd/anker_power/{product_key}/{device_sn}/req` (publish), 3 subscribe topics
- 8 MqttCommandType values with cmd codes (0x22=normal, 0x0C=OTA, 0x18=unbind, etc.)
- Payloads are base64-encoded, optional GZip (0x1F8B magic), then JSON

**A17X7 Smart Meter** (entirely unmapped in upstream):
- 11 status tags: grid_power, grid_import/export, totals, firmware, OTA status
- Debug strings confirm: "fromGrid", "toGrid", "fromGridSum", "toGridSum"

**A17C1 Solarbank 2 — 11 new status tags** (not in upstream 0405 mapping):
- `ae`=ac_socket_switch, `af`=schedule_enabled, `b8`=ac_input_power
- `ba`=cutoff_power, `bb`=heating_power (upstream comment confirmed)
- `fc`=extended_status_flags bitfield ([2]=parallel, [10]=export, [14]=schedule, [18]=config)
- Divisors from assembly: `ab`÷10, `ac`÷10, `b0`÷100, `b7`÷100, `c8`÷10, `d3`÷10

**A17C2 Hybrid Inverter — 8 tags with Chinese debug labels**:
- `ac`="电池充放电功率" (bat charge/discharge power)
- `ae`="并网口功率" (grid-connected port power), `af`="离网口功率" (off-grid port power)
- `d3`="标识当前是否0溃网" (grid collapse flag)

**A17C5 Solarbank 3 — 15+ extra tags vs A17C1**:
- Extra commands: AC socket (0x73), device timeout (0x9A), PV limit, usage mode (0x5E)
- Multi-system messages: 0420/0421/0428

**EV Charger field→TLV tag mapping** (cross-referenced APK field names with upstream tags):
- 12 confirmed tag assignments (controlType→a2, carChargerLockStatus→a3, etc.)
- 3 NEW commands: `ioDetection*`, `disconnectFunction`, `initSettings`
- Only start/stop/boost use encoding_type=2

**A1790 F3800**:
- `b3` uses `bytesToHexString` (NOT listToInt) = battery_serial_hex
- `f8` uses DeviceSavingModeEnum (1=normal, 2=smart, 4=custom)

**A1771/A1753 PPS** — 5 new tags from Chinese debug strings:
- `df`="绿电模式" (green energy mode), `e0`="绿电充电功率上限" (green charge limit)
- `e2`="是否启用波峰波谷" (peak/valley enabled), `e4`="波峰波谷数据"

**Data structures with byte-level layouts**:
- CountDownInfo: 8-byte min payload, remaining = max(0, total - elapsed)
- TimingInfo: 5 fixed bytes + variable weekdays (NOT bitmask, sequential 1-7)
- OutputPortInfo (A2345): portIndex, voltage(mV), current(mA), power(mW)
- SubBatteryInfo (A1790): 17 fields including SOC, health, heating, error

**10 complete enum tables** with API integer values:
- EmsModeType: 1/4/5/8/9/10
- EvChargerDeviceStatus: 0-8 (OCPP-aligned)
- GeneratorMode: 0-6 (silentDc through dcExercise)
- StartWayEnum: 1-8 (wifi/ble/touch/rfid/plug/timed/autoResume/modbus)

**22 FeatureSwitch flags** from SceneInfo:
- New: `enable_aiems_v2`, `grid_to_ev`, `meter_self_testing`, `power_saving_mode`

**Device→Command Matrix**: Which of thomluther's 53 CMD_* each device supports.

**Unreleased device A17D0** discovered in A17B1 parser (4 references).

### BLE_COMMAND_MAP.md growth
From 0 to 2350 lines covering:
- Wire protocol + MQTT envelope + compression + encryption
- TLV parsing internals + value encoding (scaling, signed, sub-byte)
- ~80 SET commands + ~200 STATUS tags across 13 device families
- 10 enum tables + 5 GET→SET flows + 30 value range definitions
- 6 complete API response model structures
- Device→Command matrix for all upstream devices
- 10 byte-level data structure layouts
- 37 missing upstream CMD_* cross-referenced

---

## 2026-03-28 — BLE/MQTT command map, device pages, protocol cross-reference (Part 2 original)

### BLE/MQTT Command Map (new methodology)

Cross-referenced decompiled APK command builder functions with thomluther's device-tested
TLV tag assignments. Validated on 5 confirmed commands (Smart Plug 007a/007c/007e,
Solarbank 005e/0080) — 100% match rate on field order and types.

Key insight: Dart Smi encoding means assembly constant >> 1 = actual hex tag value.

Coverage:
- **A17C1/C5 (Solarbank 2/3)**: 17 commands, 6 NEW (electricity price, self-test,
  micro power limit)
- **A17X8 (Smart Plug)**: 7 commands, 3 NEW (momentary switch, countdown variant)
- **PPS family**: 17 commands, 3 NEW (light wait time, locale, port memory)
- **A1790 (F3800)**: 3 NEW (generator ATS params, sub-battery switches)
- **A5190 (EV Charger)**: Full field→tag mapping (12 confirmed, 3 NEW: ioDetection,
  disconnect, initSettings)
- **A5101 (X1 HES)**: Different protocol (att_id + JSON, not TLV) — entirely unmapped
- **EverFrost**: 12 commands, ALL NEW (entirely unmapped in upstream)
- **Prime Charger / A91B2**: 9 commands, ALL NEW

### Device pages

Added `devices/` directory with per-device reference pages:
- `solarbank.md` — param_types, usage modes, MQTT commands, abbreviated fields
- `smart_plug.md` — verified MQTT commands, timer fields
- `ev_charger.md` — 35 API endpoints, BLE actions, field→TLV tag mapping
- `x1_hes_e10.md` — 65 A5101DataCodeType MQTT field names with hex codes

Each page links to upstream community issues and all relevant files in this repo.

### Community demand priority

Added P1-P4 priority tags based on thomluther/ha-anker-solix issue analysis.
Tagged non-relevant endpoints (AIOT popups, AI chat, screen savers, easter eggs).

### Confidence language audit

Replaced "verified" with device-tested / upstream-confirmed / structurally inferred
throughout all documentation.

---

## 2026-03-27 — Accuracy overhaul: upstream verification, breadth+depth APK scan (Part 1)

### Critical fixes

- **`set_device_attrs` nesting resolved**: Upstream confirms `switch_0w`, `pv_power_limit`,
  `power_limit`, `ac_power_limit`, `tag`, `init_status` etc. go **inside** `attributes` dict,
  not alongside it. Pattern: `{"device_sn": "...", "attributes": {"switch_0w": 0}}`
- **`setSiteDevicePowerLimit` nesting fixed**: `power_limit`, `limit`, `limit_real` are
  **inside** the JSON-encoded `param_data` string, not top-level request fields
- **`updatePeakAndValley` completely wrong → fixed**: Was documented as `set_site_device_param`
  wrapper with `power_limit, limit, limit_real`. Actually a HES-specific endpoint
  (`/charging_hes_svc/update_hes_utility_rate_plan`) with camelCase fields
  `siteId, peakValleyPriceSeason`
- **`disturb_scenes` nesting fixed**: Boolean fields (`start_charging`, `stop_charging`, etc.)
  go **inside** the `disturb_scenes` object, not at the same level
- **`setDeviceHomeLoadRes` missing `site_id`**: Upstream confirms `site_id` is sent in request
- **`dealUtilityRatePlanData` wrong params**: Had shifted params from `setDeviceFeedGridSwitch`,
  corrected to `peak_sessions`

### endpoints/*.md parameter-shifting bug (150+ functions affected)

All 16 endpoint files had a systematic bug where parameters from one function were
incorrectly assigned to an adjacent function (off-by-one in extraction). All files
regenerated from the authoritative `ENDPOINT_FIELDS.md`.

### Breadth scan: 95 new endpoints from device-specific logic

Scanned device logic files outside `http_request_repository_impl.dart`:
- **6 new API service prefixes**: `/smart_service/v1/`, `/charging_imsg_svc/`,
  `/charging_hes_dynamic_price_svc/`, `/charging_disaster_prepared/`,
  `/charging_common_svc/location/`, `/power_service/v2/`
- **A5190 (EV Charger)**: 35 endpoints — RFID, OCPP, Vehicle, Orders, Sharing
- **A7320 (Generator)**: 32 endpoints — Extender System CRUD, Oil Maintenance, Exercise
- **A5101 (HES/X1)**: 25+ endpoints — AI-EMS, Self-Check, Energy Stats, OTA, Backup
- **Dynamic Pricing**: 6 endpoints
- **Storm Guard / Disaster**: 5 endpoints
- **Anka AI Agent**: 3 endpoints
- All documented in new `endpoints/device_specific.md` with device tags

### Depth scan: 460 toJson() classes analyzed

- **`feed-in_power_limit`** uses a HYPHEN (not underscore!) — discovered in param_data
- **`home_load_data`** has deep nesting: `appliance_loads: [{name, power, number, id}]`
  and `device_power_loads: [{device_sn, power}]`
- **Attributes** contains 6 additional fields: `feeder0w`, `pv_power_limit_option`,
  `user_power_limit`, `legal_power_limit`, `region_power_limit`, `ip_region`
- **Feature flags**: `enable_aiems_v2`, `grid_to_ev`, `meter_self_testing`,
  `power_limit_status`, `power_saving_mode`
- **`reserved_soc`** and **`exceed_alarm`** in SiteConsumptionStrategy

### Upstream cross-reference

- **`cmd=17`** confirmed as SET constant
- **`param_data`** confirmed as JSON string (not nested object)
- **2 missing endpoints added**: `set_power_cutoff` (`device_sn, cutoff_data_id`),
  `set_aps_power` (`sn, power`)
- **`switch_0w` semantics**: 0=allow grid export, 1=block (inverted!)
- **`updateSitePriceRequest`** missing `dynamic_price` nested structure — added

### Minor fixes

- Typo: `counrty` → `country` in getCurrencyGetList
- Response model count: 90 → 91
- `power_limit_option_real` type conflict: null → int (from toJson evidence)
- Function count: "32 functions" → 31 (actual count)
- `bindUnX1Charger` camelCase fields added to REQUIRED_FIELDS

### Confidence language audit

Systematic review of all "verified", "confirmed" claims across 12 files:
- Replaced "verified" with "device-tested" (for mqtt_monitor results)
- Replaced "verified" with "upstream-confirmed" (for thomluther/community-tested code)
- Replaced "confirmed" with "structurally inferred" (for toJson() decompilation evidence)
- Split confidence table: Device-tested / Upstream-confirmed / Structurally inferred / Heuristic
- Credit "upstream community" (not just thomluther) for device testing — except
  Issue #423 which thomluther specifically tested

### HA relevance tagging

- Added community demand priority table (P1-P4) to `device_specific.md`
  based on thomluther/ha-anker-solix issue analysis
- Tagged sections not relevant for HA integration: AIOT popups, Anka AI,
  passport (except login), screen savers, easter eggs, app help/FAQ
- All Anker Solix devices are consumer products (no commercial-only line);
  X1 HES requires installer but is user-owned

### Files changed

- 25 files modified, 2 new files (`endpoints/device_specific.md`, `CHANGELOG.md`)
- Total repo: ~7500 lines across 41 files
