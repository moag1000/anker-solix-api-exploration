> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Page type: audit table · Owner page: this page

# Audit: ENDPOINT_FIELDS.md, REQUIRED_FIELDS.md, FIELD_TYPES.md, DART_PYTHON_MAPPING.md (Smi sweep)

Every integer in the assigned documents that could have come from a Blutter immediate, checked against the asm. Method and verdict meanings: [../../METHODOLOGY.md](../../METHODOLOGY.md) (Smi rule). Asm roots: 3.24.3 `v3.24.3/blutter_output/asm`, 3.18.0 `blutter_output/asm`; `pp.txt` entries are pool objects and are already untagged (pool `List<int>(2)` opcode lists and `Obj!<Enum>` values are real). Addresses are `file.dart @0xADDR` relative to the asm root. `data/param_types.json`, `data/endpoints.json` and `data/models.json` were used as cross-checks only. The documents themselves are left unchanged except for the banner under their titles.

Line basis: doc line numbers refer to the files BEFORE the banner was added (pre-banner commit 50c80cc); in the current files add 2.

Verdicts: `OK`, `WRONG` (real value in the note), `NOT-FROM-ASM` (string, upstream, captured/device test, example or prose count), `UNVERIFIABLE` (site not found; search listed), `CHANGED-IN-3.24.3` (doc matches 3.18.0 but not 3.24.3). Byte offsets (`0xNNN`, `r17 = N`), class sizes and pool offsets are real values printed by Blutter and are not Smi-affected; they are checked only for presence. Notes that start with `not Smi:` are semantic corrections (not a doubled integer).

Rows: 37. NOT-FROM-ASM 30, OK 5, UNVERIFIABLE 2.

Sections (one per audited file or entry):

- `ENDPOINT_FIELDS.md`: 11 rows (NOT-FROM-ASM 7, OK 3, UNVERIFIABLE 1)
- `REQUIRED_FIELDS.md`: 3 rows (NOT-FROM-ASM 2, OK 1)
- `FIELD_TYPES.md`: 21 rows (NOT-FROM-ASM 19, OK 1, UNVERIFIABLE 1)
- `DART_PYTHON_MAPPING.md`: 2 rows (NOT-FROM-ASM 2)

## ENDPOINT_FIELDS.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| set_site_device_param `setSiteDevicePowerLimit`: app sends cmd 123, upstream library sends cmd 17 | 776 | charging/http/http_request_repository_impl.dart setSiteDevicePowerLimit @0x43558c4 (3.24.3) | 246 | `mov x16,#0xf6` / `stur w16,[x0,#0x23]` -> 123 | OK | Already corrected in the text; owner page `api/power_service/site/set_site_device_param.md`. |
| `cmd` as a parameter of `set17C1SiteDeviceParam`, `setSafetySocParams`, `setSiteDeviceParam`, ... (no value given) | 769 | charging/http/http_request_repository_impl.dart set17C1SiteDeviceParam @0x238cca8, setSiteDeviceParam @0x2404444 (3.24.3) | 246 / 34 | `stur w` map-literal slot -> 123 / 17 | OK | The page lists `cmd` as a name only. Real values: 123 for the 17C1/dynamic-price/power-limit wrappers, 17 for `setSiteDeviceParam` (see `data/param_types.json` and the FLOWS audit). |
| `updateSitePriceRequest(... accuracy?, ...)`: parameter name only | 791 | charging/http/http_request_repository.dart updateSitePriceRequest @0x279df00, default `mov x6,#2` @0x279df50 (3.24.3) | 2 | default of a named parameter, loaded untagged (`sbfx x6,x1,#1` on the passed value; `mov x6,#2` otherwise) | OK | No number on the page; the real default is 2, matching the FIELD_TYPES example `accuracy 2`. |
| `getDeviceCommand(station_id?, accuracy)` and the nested `dynamic_price` object (`"pct": float?`) | 182 | charging/http/http_request_repository.dart (3.24.3) | - | - | NOT-FROM-ASM | Parameter and key names only. (For the real `accuracy` values sent by the HES calls see the models audit: raw 10 -> 5.) |
| home_load_data example `"id": 0`, `"power_setting_mode": 1`, `"charge_priority": 80`, `"priority_discharge_switch": 0`, `"power": 100`, `"number": 1`, `"power": 50` | 823, 824 | charging/model/.../HomeRangesModel toJson (3.18.0 scan); asm map keys only | - | - | NOT-FROM-ASM | The nesting and the key names come from `toJson()` of the model; the values are invented example values (a model class has no constants). Compare the schedule payloads in the FLOWS audit (`charge_priority` 2/1). |
| param_data inner fields (`id, soc, switch_0w, enable_0w, feed-in_power_limit, third_part_pv_setting`); `enable_0w_change` | 817 | - | - | - | NOT-FROM-ASM | Key names only. |
| Upstream pattern `{"pv_power_limit": 800, "switch_0w": 0}` | 547 | - | - | - | NOT-FROM-ASM | Upstream example. |
| Statistics: "148 endpoints from `http_request_repository_impl.dart`", "+95 endpoints", "~243 total", "10+ API service prefixes", "6 new API service prefixes", "91 endpoints with identified response models", "148 endpoints. 90 with identified response models" (last line) | 853, 854, 855, 857, 858, 862 | data/endpoints.json (rows with dart_file http_request_repository_impl.dart) | - | - | NOT-FROM-ASM | Tallies of an earlier extraction. `data/endpoints.json` now has 250 function rows (213 distinct URLs) for `http_request_repository_impl.dart`, 207 of them since 3.18.0 or earlier. The 91 vs 90 difference between the two statistics blocks is internal to the page. |
| "460 toJson() classes scanned" | 814, 856 | `grep -rhoE "Map<String, dynamic> toJson\([A-Za-z0-9_]+\)"` over both trees | - | - | UNVERIFIABLE | Not reproducible: distinct `toJson(<Class>)` implementations are 415 under charging/ (3.18.0; 418 in 3.24.3), 744 in the whole 3.18.0 tree and 884 in the whole 3.24.3 tree. The scope that gave 460 is unknown. |
| "Nesting corrections" paragraph: FeatureSwitch `new flags`, SiteConsumptionStrategyModel (`reserved_soc`, `ai_ems: {status}`, `exceed_alarm`) | 846, 843 | - | - | - | NOT-FROM-ASM | Key names only. |
| Other lines: identifiers containing digits (`17C1`, `A2345`, `A17B1`, `A5101`, `A2687`, `X1`) | - | - | - | - | NOT-FROM-ASM | `python3` scan of the file with backticked spans removed: only the statistics block and the examples above carry numbers. |

## REQUIRED_FIELDS.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| set17C1SiteDeviceParam power-limit correction: cmd 123 (app) vs cmd 17 (upstream) | 977 | charging/http/http_request_repository_impl.dart setSiteDevicePowerLimit @0x43558c4 (3.24.3) | 246 | `stur w16` map-literal slot -> 123 | OK | Already corrected in the text; owner page `api/power_service/site/set_site_device_param.md`. |
| Upstream pattern `{"switch_0w": 0, "pv_power_limit": 800}`; `switch_0w` 0=allow, 1=block | 607, 625 | - | - | - | NOT-FROM-ASM | Upstream example and semantics. |
| NOT-FROM-ASM (whole file: required/optional parameter names only) | 1-1003 | - | - | - | NOT-FROM-ASM | `grep -nE "0x[0-9a-f]+\|[=:] ?-?[0-9]+\|[0-9]+ ?(or\|/\|-) ?[0-9]+" REQUIRED_FIELDS.md` shows only the two lines above, the `charging_device_identity_status_default_true` identifiers and example JSON. The digits in the remaining lines are part of identifiers (`17C1`, `A2345`, `A17B1`, `A5101`, `A2687`). |

## FIELD_TYPES.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| "**234** fields with type information or cross-source confirmation" | 7 | FIELD_TYPES.md first table (`awk` count of `\| \`` rows between the first header and the "Fields discovered from toJson()" heading) | 234 | - | NOT-FROM-ASM | Prose count; the first table has exactly 234 rows (258 table rows in the whole file). |
| "scanning 460 toJson() class implementations" | 250 | `grep -rhoE "Map<String, dynamic> toJson\([A-Za-z0-9_]+\)"` over both trees | - | - | UNVERIFIABLE | Same finding as in ENDPOINT_FIELDS (415 under charging/ in 3.18.0, 744 whole tree). |
| `accuracy` example 2 | 14 | charging/http/http_request_repository.dart updateSitePriceRequest @0x279df50 (3.24.3) | 2 | `mov x6,#2` (unboxed default of the named parameter) | OK | Upstream example; the app default is the same real 2. |
| Example column of the 227 rows (counted by script) whose Sources contain `U` (upstream examples) | 11 | upstream API response examples (thomluther) | - | - | NOT-FROM-ASM | Values such as `1200`, `800`, `"75"`, `7` (`current_mode`) come from real upstream responses (U) or mqtt_monitor (M); they are not asm constants. |
| `enable_0w` example `0` (source B only) | 257 | toJson() of the owning model (key names only) | - | - | NOT-FROM-ASM | Source `B` means the key was found in a `toJson()`; a model class holds no constants, so the example integer is not an asm value. |
| `feeder0w` example `0` (source B only) | 263 | toJson() of the owning model (key names only) | - | - | NOT-FROM-ASM | Source `B` means the key was found in a `toJson()`; a model class holds no constants, so the example integer is not an asm value. |
| `pv_power_limit_option` example `2000` (source B only) | 264 | toJson() of the owning model (key names only) | - | - | NOT-FROM-ASM | Source `B` means the key was found in a `toJson()`; a model class holds no constants, so the example integer is not an asm value. |
| `user_power_limit` example `800` (source B only) | 265 | toJson() of the owning model (key names only) | - | - | NOT-FROM-ASM | Source `B` means the key was found in a `toJson()`; a model class holds no constants, so the example integer is not an asm value. |
| `legal_power_limit` example `800` (source B only) | 266 | toJson() of the owning model (key names only) | - | - | NOT-FROM-ASM | Source `B` means the key was found in a `toJson()`; a model class holds no constants, so the example integer is not an asm value. |
| `region_power_limit` example `800` (source B only) | 267 | toJson() of the owning model (key names only) | - | - | NOT-FROM-ASM | Source `B` means the key was found in a `toJson()`; a model class holds no constants, so the example integer is not an asm value. |
| `power_limit_option` example `800` (source B only) | 268 | toJson() of the owning model (key names only) | - | - | NOT-FROM-ASM | Source `B` means the key was found in a `toJson()`; a model class holds no constants, so the example integer is not an asm value. |
| `region_microinverter_limit` example `800` (source B only) | 271 | toJson() of the owning model (key names only) | - | - | NOT-FROM-ASM | Source `B` means the key was found in a `toJson()`; a model class holds no constants, so the example integer is not an asm value. |
| `power_setting_mode` example `1` (source B only) | 276 | toJson() of the owning model (key names only) | - | - | NOT-FROM-ASM | Source `B` means the key was found in a `toJson()`; a model class holds no constants, so the example integer is not an asm value. |
| `priority_discharge_switch` example `0` (source B only) | 277 | toJson() of the owning model (key names only) | - | - | NOT-FROM-ASM | Source `B` means the key was found in a `toJson()`; a model class holds no constants, so the example integer is not an asm value. |
| `reserved_soc` example `10` (source B only) | 293 | toJson() of the owning model (key names only) | - | - | NOT-FROM-ASM | Source `B` means the key was found in a `toJson()`; a model class holds no constants, so the example integer is not an asm value. |
| `exceed_alarm` example `0` (source B only) | 294 | toJson() of the owning model (key names only) | - | - | NOT-FROM-ASM | Source `B` means the key was found in a `toJson()`; a model class holds no constants, so the example integer is not an asm value. |
| `feed-in_power_limit` example `4500` (source B only) | 256 | toJson() of the owning model (key names only) | - | - | NOT-FROM-ASM | Source `B` means the key was found in a `toJson()`; a model class holds no constants, so the example integer is not an asm value. |
| Feature flags `enable_aiems_v2`, `grid_to_ev`, `meter_self_testing`, `power_limit_status`, `power_saving_mode` (bool `false`) | 284 | charging/model/green_energy/station/scene_info.dart FeatureSwitch (3.24.3) | - | key names are pool strings | NOT-FROM-ASM | Booleans, not integers. All five keys occur in `FeatureSwitch` (3.24.3 class size 0x88 = 32 field slots; 3.18.0: 0x60 = 22). |
| Example arrays `{name, power, number, id}`, `{device_sn, power}` | 278 | - | - | - | NOT-FROM-ASM | Key lists, no numbers. |
| `ai_ems` example `{"status": 0}` | 295 | - | - | - | NOT-FROM-ASM | Example value. |
| Remaining table rows (identifier, string, bool, array and null examples) | 1-296 | - | - | - | NOT-FROM-ASM | Strings, booleans, arrays and `null` are not integers; UUIDs, URLs and MACs in the Example column are upstream data. |

## DART_PYTHON_MAPPING.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| "**35** cross-referenced camelCase<->snake_case pairs" | 7 | DART_PYTHON_MAPPING.md table (row count) | 35 | - | NOT-FROM-ASM | Prose count; the table has exactly 35 data rows. |
| NOT-FROM-ASM (whole file: field-name pairs only) | 1-46 | - | - | - | NOT-FROM-ASM | `grep -nE "[0-9]" DART_PYTHON_MAPPING.md` hits only the count line above. |
