# Changelog

## 2026-03-27 — Accuracy overhaul: upstream verification, breadth+depth APK scan

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
