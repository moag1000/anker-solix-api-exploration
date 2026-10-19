> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Page type: audit table · Owner page: this page

# Audit: models/*.md (13 legacy pages; station_power_limit.md excluded) (Smi sweep)

Every integer in the assigned documents that could have come from a Blutter immediate, checked against the asm. Method and verdict meanings: [../../METHODOLOGY.md](../../METHODOLOGY.md) (Smi rule). Asm roots: 3.24.3 `v3.24.3/blutter_output/asm`, 3.18.0 `blutter_output/asm`; `pp.txt` entries are pool objects and are already untagged (pool `List<int>(2)` opcode lists and `Obj!<Enum>` values are real). Addresses are `file.dart @0xADDR` relative to the asm root. `data/param_types.json`, `data/endpoints.json` and `data/models.json` were used as cross-checks only. The documents themselves are left unchanged except for the banner under their titles.

Line basis: doc line numbers refer to the files BEFORE the banner was added (pre-banner commit 50c80cc); in the current files add 2.

Verdicts: `OK`, `WRONG` (real value in the note), `NOT-FROM-ASM` (string, upstream, captured/device test, example or prose count), `UNVERIFIABLE` (site not found; search listed), `CHANGED-IN-3.24.3` (doc matches 3.18.0 but not 3.24.3). Byte offsets (`0xNNN`, `r17 = N`), class sizes and pool offsets are real values printed by Blutter and are not Smi-affected; they are checked only for presence. Notes that start with `not Smi:` are semantic corrections (not a doubled integer).

Rows: 39. NOT-FROM-ASM 30, OK 7, WRONG 2.

Sections (one per audited file or entry):

- `models/account.md`: 2 rows (NOT-FROM-ASM 2)
- `models/charger.md`: 2 rows (NOT-FROM-ASM 2)
- `models/connectivity.md`: 2 rows (NOT-FROM-ASM 2)
- `models/device.md`: 2 rows (NOT-FROM-ASM 2)
- `models/energy.md`: 2 rows (NOT-FROM-ASM 2)
- `models/firmware.md`: 2 rows (NOT-FROM-ASM 2)
- `models/hes.md`: 15 rows (NOT-FROM-ASM 6, OK 7, WRONG 2)
- `models/other.md`: 2 rows (NOT-FROM-ASM 2)
- `models/power.md`: 2 rows (NOT-FROM-ASM 2)
- `models/pps.md`: 2 rows (NOT-FROM-ASM 2)
- `models/pricing.md`: 2 rows (NOT-FROM-ASM 2)
- `models/products.md`: 2 rows (NOT-FROM-ASM 2)
- `models/solarbank.md`: 2 rows (NOT-FROM-ASM 2)

## models/account.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| header count "10 models" | 3 | asm class declarations (`grep -rhoE "^class [A-Za-z0-9_]+"` over the 3.24.3 tree) | - | - | NOT-FROM-ASM | Prose count equal to the 10 level-2 headings of the page. All 10 class names exist as classes in the 3.24.3 asm. |
| NOT-FROM-ASM (whole file: field names and source paths only) | 1-92 | - | - | - | NOT-FROM-ASM | `grep -nE "0x[0-9a-f]+\|alloc\|size\|Fixed\|default\|enum\|[0-9]+ (fields\|models\|params\|parameters\|keys\|elements)" models/account.md` shows only the header count above. Field names and Dart types are not integers; the field lists are owned by the Phase 1 model pages and `data/models.json`. |

## models/charger.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| header count "4 models" | 3 | asm class declarations (`grep -rhoE "^class [A-Za-z0-9_]+"` over the 3.24.3 tree) | - | - | NOT-FROM-ASM | Prose count equal to the 4 level-2 headings of the page. All 4 class names exist as classes in the 3.24.3 asm. |
| NOT-FROM-ASM (whole file: field names and source paths only) | 1-29 | - | - | - | NOT-FROM-ASM | `grep -nE "0x[0-9a-f]+\|alloc\|size\|Fixed\|default\|enum\|[0-9]+ (fields\|models\|params\|parameters\|keys\|elements)" models/charger.md` shows only the header count above. Field names and Dart types are not integers; the field lists are owned by the Phase 1 model pages and `data/models.json`. |

## models/connectivity.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| header count "4 models" | 3 | asm class declarations (`grep -rhoE "^class [A-Za-z0-9_]+"` over the 3.24.3 tree) | - | - | NOT-FROM-ASM | Prose count equal to the 4 level-2 headings of the page. All 4 class names exist as classes in the 3.24.3 asm. |
| NOT-FROM-ASM (whole file: field names and source paths only) | 1-45 | - | - | - | NOT-FROM-ASM | `grep -nE "0x[0-9a-f]+\|alloc\|size\|Fixed\|default\|enum\|[0-9]+ (fields\|models\|params\|parameters\|keys\|elements)" models/connectivity.md` shows only the header count above. Field names and Dart types are not integers; the field lists are owned by the Phase 1 model pages and `data/models.json`. |

## models/device.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| header count "3 models" | 3 | asm class declarations (`grep -rhoE "^class [A-Za-z0-9_]+"` over the 3.24.3 tree) | - | - | NOT-FROM-ASM | Prose count equal to the 3 level-2 headings of the page. All 3 class names exist as classes in the 3.24.3 asm. |
| NOT-FROM-ASM (whole file: field names and source paths only) | 1-35 | - | - | - | NOT-FROM-ASM | `grep -nE "0x[0-9a-f]+\|alloc\|size\|Fixed\|default\|enum\|[0-9]+ (fields\|models\|params\|parameters\|keys\|elements)" models/device.md` shows only the header count above. Field names and Dart types are not integers; the field lists are owned by the Phase 1 model pages and `data/models.json`. |

## models/energy.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| header count "3 models" | 3 | asm class declarations (`grep -rhoE "^class [A-Za-z0-9_]+"` over the 3.24.3 tree) | - | - | NOT-FROM-ASM | Prose count equal to the 3 level-2 headings of the page. All 3 class names exist as classes in the 3.24.3 asm. |
| NOT-FROM-ASM (whole file: field names and source paths only) | 1-31 | - | - | - | NOT-FROM-ASM | `grep -nE "0x[0-9a-f]+\|alloc\|size\|Fixed\|default\|enum\|[0-9]+ (fields\|models\|params\|parameters\|keys\|elements)" models/energy.md` shows only the header count above. Field names and Dart types are not integers; the field lists are owned by the Phase 1 model pages and `data/models.json`. |

## models/firmware.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| header count "9 models" | 3 | asm class declarations (`grep -rhoE "^class [A-Za-z0-9_]+"` over the 3.24.3 tree) | - | - | NOT-FROM-ASM | Prose count equal to the 9 level-2 headings of the page. All 9 class names exist as classes in the 3.24.3 asm. |
| NOT-FROM-ASM (whole file: field names and source paths only) | 1-93 | - | - | - | NOT-FROM-ASM | `grep -nE "0x[0-9a-f]+\|alloc\|size\|Fixed\|default\|enum\|[0-9]+ (fields\|models\|params\|parameters\|keys\|elements)" models/firmware.md` shows only the header count above and field names containing the words `default` / `size` (`default_charge_priority`, `file_size`, `size`). Field names and Dart types are not integers; the field lists are owned by the Phase 1 model pages and `data/models.json`. |

## models/hes.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| header count "14+ models" | 3 | asm class declarations (`grep -rhoE "^class [A-Za-z0-9_]+"` over the 3.24.3 tree) | - | - | NOT-FROM-ASM | Prose count equal to the 14 level-2 headings of the page. All 14 class names exist as classes in the 3.24.3 asm. |
| "28 parameters allocated (60-element array)" in the SET request to `device_command` | 26 | charging/http/http_request_repository_impl.dart sendDeviceCommand @0x24a0aa8, AllocateArray @0x24a0b78 (3.24.3); @0x1d59d24 (3.18.0) | 60 | `r2 = 60` (`mov x2,#0x3c`) before AllocateArray: 60 / 2 = 30 slots = 15 key/value pairs | WRONG -> 15 key/value pairs (30 slots) | The immediate is the Smi-tagged length. The map has 15 pairs: station_id, main_sn, time, electricity_strategy, add_diesel, screen_setting, utility_rate_plan, ack_peak_valley, advanced_setting, heat_pump_setting, accuracy, cls_reset, off_grid_switching, evcharger_setting, version, which are exactly the 15 listed in the doc block. |
| `accuracy` "Fixed value: 10" | 39 | charging/http/http_request_repository_impl.dart sendDeviceCommand @0x24a0d6c (3.24.3); @0x1d59f14 (3.18.0); ui/page/device/a5101/setting/homeSetting/save_tou_plan_logic.dart sendPeakValleyData @0x249e12c (3.24.3) | 10 | `mov x16,#0xa` / `stur w16,[x2,#0x3b]` (map-literal slot, key `"accuracy"` @0x249e120) | WRONG -> 5 | Raw 10 stored with `stur w` is the Smi 5. (The Dart default of the named parameter `accuracy` in `updateSitePriceRequest`, `mov x6,#2` @0x279df50, is unboxed and really is 2; a5101 `_getUtilityRatePlan` also sends `accuracy` raw 10 -> 5 @0x24a54f0.) |
| SET request key set (`ack_peak_valley`, `cls_reset`, `accuracy`, ...) | 36 | charging/http/http_request_repository_impl.dart sendDeviceCommand (3.24.3) | - | - | OK | Key names match the pool strings (`"ack_peak_valley"` [pp+0x90fa8], `"cls_reset"` [pp+0x90fb0], `"version"` [pp+0x13760]); no integer is given for them. |
| ElectricityStrategy `mode` value `1` = selfConsumption | 70 | pp.txt Obj!EmsModeType selfConsumption [pp+0x6aee0] (3.24.3) | off_14: int(1) | pool enum object (untagged) | OK | Same as [ENUMS audit](ENUMS.md) ("EMS Mode Type API values"). |
| ElectricityStrategy `mode` value `4` = manualPowerBackup | 71 | pp.txt Obj!EmsModeType manualPowerBackup [pp+0x1a120] (3.24.3) | off_14: int(4) | pool enum object (untagged) | OK | Same as [ENUMS audit](ENUMS.md) ("EMS Mode Type API values"). |
| ElectricityStrategy `mode` value `5` = timeOfUse | 72 | pp.txt Obj!EmsModeType timeOfUse [pp+0x6af00] (3.24.3) | off_14: int(5) | pool enum object (untagged) | OK | Same as [ENUMS audit](ENUMS.md) ("EMS Mode Type API values"). |
| ElectricityStrategy `mode` value `8` = onlyBackupPower | 73 | pp.txt Obj!EmsModeType onlyBackupPower [pp+0x1a758] (3.24.3) | off_14: int(8) | pool enum object (untagged) | OK | Same as [ENUMS audit](ENUMS.md) ("EMS Mode Type API values"). |
| ElectricityStrategy `mode` value `9` = severeWeatherMode | 74 | pp.txt Obj!EmsModeType severeWeatherMode [pp+0x1a100] (3.24.3) | off_14: int(9) | pool enum object (untagged) | OK | Same as [ENUMS audit](ENUMS.md) ("EMS Mode Type API values"). |
| ElectricityStrategy `mode` value `10` = offGrid | 75 | pp.txt Obj!EmsModeType offGrid [pp+0xe7d10] (3.24.3) | off_14: int(10) | pool enum object (untagged) | OK | Same as [ENUMS audit](ENUMS.md) ("EMS Mode Type API values"). |
| ElectricityStrategy example `"conserve_percent": 20`, `"mode": 1`; range `(0-100)` | 60, 12 | - | - | - | NOT-FROM-ASM | Example payload and UI range hint. |
| OffGridSwitching example `"off_grid_enable": 1`, `"off_grid_sensitivity": 3` | 82 | - | - | - | NOT-FROM-ASM | Example payload. |
| HeatPumpModel example values (`heat_pump_state` 0, `heat_pump_power` 0, `min_launch_time` 0, `min_running_time` 0) | 91 | - | - | - | NOT-FROM-ASM | Default/example values; the key names are present in the asm (a5101_device_command_model.dart HeatPumpModel toJson @0x277e2b8). |
| `soc` "State of charge (0-100)" | 20 | - | - | - | NOT-FROM-ASM | Range hint. |
| `version` string "1.0.0" | 43 | pp.txt String (3.24.3) | - | String literal | NOT-FROM-ASM | String, not an integer. |

## models/other.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| header count "28 models" | 3 | asm class declarations (`grep -rhoE "^class [A-Za-z0-9_]+"` over the 3.24.3 tree) | - | - | NOT-FROM-ASM | Prose count equal to the 28 level-2 headings of the page. All 28 class names exist as classes in the 3.24.3 asm. |
| NOT-FROM-ASM (whole file: field names and source paths only) | 1-224 | - | - | - | NOT-FROM-ASM | `grep -nE "0x[0-9a-f]+\|alloc\|size\|Fixed\|default\|enum\|[0-9]+ (fields\|models\|params\|parameters\|keys\|elements)" models/other.md` shows only the header count above. Field names and Dart types are not integers; the field lists are owned by the Phase 1 model pages and `data/models.json`. |

## models/power.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| header count "2 models" | 3 | asm class declarations (`grep -rhoE "^class [A-Za-z0-9_]+"` over the 3.24.3 tree) | - | - | NOT-FROM-ASM | Prose count equal to the 2 level-2 headings of the page. All 2 class names exist as classes in the 3.24.3 asm. |
| NOT-FROM-ASM (whole file: field names and source paths only) | 1-29 | - | - | - | NOT-FROM-ASM | `grep -nE "0x[0-9a-f]+\|alloc\|size\|Fixed\|default\|enum\|[0-9]+ (fields\|models\|params\|parameters\|keys\|elements)" models/power.md` shows only the header count above. Field names and Dart types are not integers; the field lists are owned by the Phase 1 model pages and `data/models.json`. |

## models/pps.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| header count "2 models" | 3 | asm class declarations (`grep -rhoE "^class [A-Za-z0-9_]+"` over the 3.24.3 tree) | - | - | NOT-FROM-ASM | Prose count equal to the 2 level-2 headings of the page. All 2 class names exist as classes in the 3.24.3 asm. |
| NOT-FROM-ASM (whole file: field names and source paths only) | 1-23 | - | - | - | NOT-FROM-ASM | `grep -nE "0x[0-9a-f]+\|alloc\|size\|Fixed\|default\|enum\|[0-9]+ (fields\|models\|params\|parameters\|keys\|elements)" models/pps.md` shows only the header count above. Field names and Dart types are not integers; the field lists are owned by the Phase 1 model pages and `data/models.json`. |

## models/pricing.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| header count "7 models" | 3 | asm class declarations (`grep -rhoE "^class [A-Za-z0-9_]+"` over the 3.24.3 tree) | - | - | NOT-FROM-ASM | Prose count equal to the 7 level-2 headings of the page. All 7 class names exist as classes in the 3.24.3 asm. |
| NOT-FROM-ASM (whole file: field names and source paths only) | 1-60 | - | - | - | NOT-FROM-ASM | `grep -nE "0x[0-9a-f]+\|alloc\|size\|Fixed\|default\|enum\|[0-9]+ (fields\|models\|params\|parameters\|keys\|elements)" models/pricing.md` shows only the header count above. Field names and Dart types are not integers; the field lists are owned by the Phase 1 model pages and `data/models.json`. |

## models/products.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| header count "3 models" | 3 | asm class declarations (`grep -rhoE "^class [A-Za-z0-9_]+"` over the 3.24.3 tree) | - | - | NOT-FROM-ASM | Prose count equal to the 3 level-2 headings of the page. All 3 class names exist as classes in the 3.24.3 asm. |
| NOT-FROM-ASM (whole file: field names and source paths only) | 1-38 | - | - | - | NOT-FROM-ASM | `grep -nE "0x[0-9a-f]+\|alloc\|size\|Fixed\|default\|enum\|[0-9]+ (fields\|models\|params\|parameters\|keys\|elements)" models/products.md` shows only the header count above. Field names and Dart types are not integers; the field lists are owned by the Phase 1 model pages and `data/models.json`. |

## models/solarbank.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| header count "5 models" | 3 | asm class declarations (`grep -rhoE "^class [A-Za-z0-9_]+"` over the 3.24.3 tree) | - | - | NOT-FROM-ASM | Prose count equal to the 5 level-2 headings of the page. All 5 class names exist as classes in the 3.24.3 asm. |
| NOT-FROM-ASM (whole file: field names and source paths only) | 1-61 | - | - | - | NOT-FROM-ASM | `grep -nE "0x[0-9a-f]+\|alloc\|size\|Fixed\|default\|enum\|[0-9]+ (fields\|models\|params\|parameters\|keys\|elements)" models/solarbank.md` shows only the header count above and field names containing the words `default` / `size` (`default_charge_priority`, `file_size`, `size`). Field names and Dart types are not integers; the field lists are owned by the Phase 1 model pages and `data/models.json`. |
