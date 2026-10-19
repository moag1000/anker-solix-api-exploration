> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Page type: audit table · Owner page: this page

# Audit: endpoints/*.md (17 pages; charging_disaster_prepared.md audited in batch C1) (Smi sweep)

Every integer in the assigned documents that could have come from a Blutter immediate, checked against the asm. Method and verdict meanings: [../../METHODOLOGY.md](../../METHODOLOGY.md) (Smi rule). Asm roots: 3.24.3 `v3.24.3/blutter_output/asm`, 3.18.0 `blutter_output/asm`; `pp.txt` entries are pool objects and are already untagged (pool `List<int>(2)` opcode lists and `Obj!<Enum>` values are real). Addresses are `file.dart @0xADDR` relative to the asm root. `data/param_types.json`, `data/endpoints.json` and `data/models.json` were used as cross-checks only. The documents themselves are left unchanged except for the banner under their titles.

Line basis: doc line numbers refer to the files BEFORE the banner was added (pre-banner commit 50c80cc); in the current files add 2.

Verdicts: `OK`, `WRONG` (real value in the note), `NOT-FROM-ASM` (string, upstream, captured/device test, example or prose count), `UNVERIFIABLE` (site not found; search listed), `CHANGED-IN-3.24.3` (doc matches 3.18.0 but not 3.24.3). Byte offsets (`0xNNN`, `r17 = N`), class sizes and pool offsets are real values printed by Blutter and are not Smi-affected; they are checked only for presence. Notes that start with `not Smi:` are semantic corrections (not a doubled integer).

Rows: 42. NOT-FROM-ASM 40, OK 1, WRONG 1.

Sections (one per audited file or entry):

- `endpoints/app.md`: 2 rows (NOT-FROM-ASM 2)
- `endpoints/charging_common_svc.md`: 2 rows (NOT-FROM-ASM 2)
- `endpoints/charging_energy_service.md`: 4 rows (NOT-FROM-ASM 4)
- `endpoints/charging_hes_svc.md`: 2 rows (NOT-FROM-ASM 2)
- `endpoints/charging_pv_svc.md`: 2 rows (NOT-FROM-ASM 2)
- `endpoints/device_specific.md`: 8 rows (NOT-FROM-ASM 7, WRONG 1)
- `endpoints/mini_power.md`: 2 rows (NOT-FROM-ASM 2)
- `endpoints/other.md`: 2 rows (NOT-FROM-ASM 2)
- `endpoints/passport.md`: 2 rows (NOT-FROM-ASM 2)
- `endpoints/power_service_ai_ems.md`: 2 rows (NOT-FROM-ASM 2)
- `endpoints/power_service_app.md`: 2 rows (NOT-FROM-ASM 2)
- `endpoints/power_service_compatible.md`: 2 rows (NOT-FROM-ASM 2)
- `endpoints/power_service_device.md`: 2 rows (NOT-FROM-ASM 2)
- `endpoints/power_service_dynamic_price.md`: 2 rows (NOT-FROM-ASM 2)
- `endpoints/power_service_other.md`: 2 rows (NOT-FROM-ASM 2)
- `endpoints/power_service_share.md`: 2 rows (NOT-FROM-ASM 2)
- `endpoints/power_service_site.md`: 2 rows (NOT-FROM-ASM 1, OK 1)

## endpoints/app.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| header "20 function calls, 18 unique endpoints" | 3 | data/endpoints.json (generated from the 3.24.3 asm with a 3.18.0 diff) | - | - | NOT-FROM-ASM | Prose counts. The page names 18 distinct endpoint paths, 18 of them found in `data/endpoints.json`, which holds 40 function rows for those URLs (18 of the URLs exist since 3.18.0 or earlier only). |
| NOT-FROM-ASM (whole file: endpoint paths, function names and parameter names only) | 1-84 | - | - | - | NOT-FROM-ASM | `grep -nE "0x[0-9a-f]+\|[=:] ?-?[0-9]+\|[0-9]+ ?(or\|/\|-) ?[0-9]+" endpoints/app.md` (header line excluded) has no hit; the only digits are inside identifiers such as `17C1`, `A2345`, `A17B1`. |

## endpoints/charging_common_svc.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| header "1 function call, 1 unique endpoint" | 3 | data/endpoints.json (generated from the 3.24.3 asm with a 3.18.0 diff) | - | - | NOT-FROM-ASM | Prose counts. The page names 1 distinct endpoint paths, 1 of them found in `data/endpoints.json`, which holds 2 function rows for those URLs (1 of the URLs exist since 3.18.0 or earlier only). |
| NOT-FROM-ASM (whole file: endpoint paths, function names and parameter names only) | 1-12 | - | - | - | NOT-FROM-ASM | `grep -nE "0x[0-9a-f]+\|[=:] ?-?[0-9]+\|[0-9]+ ?(or\|/\|-) ?[0-9]+" endpoints/charging_common_svc.md` (header line excluded) has no hit; the only digits are inside identifiers such as `17C1`, `A2345`, `A17B1`. |

## endpoints/charging_energy_service.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| header "11+ function calls, 10+ unique endpoints" | 3 | data/endpoints.json (generated from the 3.24.3 asm with a 3.18.0 diff) | - | - | NOT-FROM-ASM | Prose counts. The page names 17 distinct endpoint paths, 17 of them found in `data/endpoints.json`, which holds 18 function rows for those URLs (17 of the URLs exist since 3.18.0 or earlier only). "N+" claims are lower bounds. |
| "Implemented in `powerpanel.py` lines 518-581" and "lines 860-922" | 60, 76 | upstream anker-solix-api/api/powerpanel.py | - | - | NOT-FROM-ASM | Upstream line numbers of an older snapshot; in the current checkout `get_system_running_info` starts at line 620 and `energy_statistics` at line 982. |
| `control`: 0 or 1 (report_device_data) | 88 | upstream anker-solix-api/api/apitypes.py API_CHARGING_ENDPOINTS comment `ctrol [0 1]` | - | - | NOT-FROM-ASM | Upstream comment, not an asm constant. |
| Example `{"main_sn": ..., "macs": [...]}` | 94 | upstream apitypes.py comment | - | - | NOT-FROM-ASM | Example payload. |

## endpoints/charging_hes_svc.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| header "28+ function calls, 28+ unique endpoints" | 3 | data/endpoints.json (generated from the 3.24.3 asm with a 3.18.0 diff) | - | - | NOT-FROM-ASM | Prose counts. The page names 50 distinct endpoint paths, 50 of them found in `data/endpoints.json`, which holds 71 function rows for those URLs (50 of the URLs exist since 3.18.0 or earlier only). "N+" claims are lower bounds. |
| NOT-FROM-ASM (whole file: endpoint paths, function names and parameter names only) | 1-248 | - | - | - | NOT-FROM-ASM | `grep -nE "0x[0-9a-f]+\|[=:] ?-?[0-9]+\|[0-9]+ ?(or\|/\|-) ?[0-9]+" endpoints/charging_hes_svc.md` (header line excluded) has no hit; the only digits are inside identifiers such as `17C1`, `A2345`, `A17B1`. |

## endpoints/charging_pv_svc.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| header "4 function calls, 4 unique endpoints" | 3 | data/endpoints.json (generated from the 3.24.3 asm with a 3.18.0 diff) | - | - | NOT-FROM-ASM | Prose counts. The page names 4 distinct endpoint paths, 4 of them found in `data/endpoints.json`, which holds 4 function rows for those URLs (4 of the URLs exist since 3.18.0 or earlier only). |
| Upstream-confirmed example `tieredElecPrices` `[{"from": "00:00", "to": "23:59", "price": 0.30}]` | 17 | - | - | - | NOT-FROM-ASM | Upstream example payload. |

## endpoints/device_specific.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| page has no header count | - | - | - | - | NOT-FROM-ASM | device_specific.md carries a priority table instead of a count header (next rows). |
| priority table issue counts "70+" | 15 | - | - | - | NOT-FROM-ASM | Community issue/demand counts, not asm values. |
| priority table issue counts "20+" | 16 | - | - | - | NOT-FROM-ASM | Community issue/demand counts, not asm values. |
| priority table issue counts "15+" | 17 | - | - | - | NOT-FROM-ASM | Community issue/demand counts, not asm values. |
| priority table issue counts "1-2" | 18 | - | - | - | NOT-FROM-ASM | Community issue/demand counts, not asm values. |
| `afterSaleMarkSn(after_sale_type=2, device_sns, mark_type=2)` | 233 | charging/http/http_business_impl.dart afterSaleMarkSn map literal @0x28606e0, @0x2860710 (3.24.3); @0x20b5bcc, @0x20b5bfc (3.18.0) | 2 / 2 | `mov x16,#2` / `stur w16,[x0,#0x13]` and `stur w16,[x0,#0x23]` (map-literal slots in a `r2 = 12` array, 6 slots = 3 pairs) | WRONG -> after_sale_type=1, mark_type=1 | Both values are raw 2 stored with `stur w`, i.e. the Smi 1. Same raw values in 3.18.0 (@0x20b5bd0 and @0x20b5c00 for the stores). |
| Section endpoint counts implied by headings (EV 42, Generator 29, HES/X1 31, Dynamic Pricing 6, Disaster 6, Anka AI 4) | 25 | - | - | - | NOT-FROM-ASM | The page has no numeric claims about these sections; the counts are the number of endpoint lines per section and are used to cross-check the prose counts in devices/ev_charger.md and CHANGELOG.md. |
| "Device tags" `[A5190]`, `[A5101]`, `[A17B1]`, `[A1782]` ... | 6 | - | - | - | NOT-FROM-ASM | Product codes (identifiers), not integers. |

## endpoints/mini_power.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| header "28 function calls, 27 unique endpoints" | 3 | data/endpoints.json (generated from the 3.24.3 asm with a 3.18.0 diff) | - | - | NOT-FROM-ASM | Prose counts. The page names 27 distinct endpoint paths, 27 of them found in `data/endpoints.json`, which holds 33 function rows for those URLs (27 of the URLs exist since 3.18.0 or earlier only). |
| NOT-FROM-ASM (whole file: endpoint paths, function names and parameter names only) | 1-119 | - | - | - | NOT-FROM-ASM | `grep -nE "0x[0-9a-f]+\|[=:] ?-?[0-9]+\|[0-9]+ ?(or\|/\|-) ?[0-9]+" endpoints/mini_power.md` (header line excluded) has no hit; the only digits are inside identifiers such as `17C1`, `A2345`, `A17B1`. |

## endpoints/other.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| header "1 function call, 1 unique endpoint" | 3 | data/endpoints.json (generated from the 3.24.3 asm with a 3.18.0 diff) | - | - | NOT-FROM-ASM | Prose counts. The page names 1 distinct endpoint paths, 1 of them found in `data/endpoints.json`, which holds 1 function rows for those URLs (1 of the URLs exist since 3.18.0 or earlier only). |
| NOT-FROM-ASM (whole file: endpoint paths, function names and parameter names only) | 1-12 | - | - | - | NOT-FROM-ASM | `grep -nE "0x[0-9a-f]+\|[=:] ?-?[0-9]+\|[0-9]+ ?(or\|/\|-) ?[0-9]+" endpoints/other.md` (header line excluded) has no hit; the only digits are inside identifiers such as `17C1`, `A2345`, `A17B1`. |

## endpoints/passport.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| header "25 function calls, 24 unique endpoints" | 3 | data/endpoints.json (generated from the 3.24.3 asm with a 3.18.0 diff) | - | - | NOT-FROM-ASM | Prose counts. The page names 24 distinct endpoint paths, 24 of them found in `data/endpoints.json`, which holds 26 function rows for those URLs (24 of the URLs exist since 3.18.0 or earlier only). |
| NOT-FROM-ASM (whole file: endpoint paths, function names and parameter names only) | 1-108 | - | - | - | NOT-FROM-ASM | `grep -nE "0x[0-9a-f]+\|[=:] ?-?[0-9]+\|[0-9]+ ?(or\|/\|-) ?[0-9]+" endpoints/passport.md` (header line excluded) has no hit; the only digits are inside identifiers such as `17C1`, `A2345`, `A17B1`. |

## endpoints/power_service_ai_ems.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| header "2 function calls, 2 unique endpoints" | 3 | data/endpoints.json (generated from the 3.24.3 asm with a 3.18.0 diff) | - | - | NOT-FROM-ASM | Prose counts. The page names 2 distinct endpoint paths, 2 of them found in `data/endpoints.json`, which holds 3 function rows for those URLs (2 of the URLs exist since 3.18.0 or earlier only). |
| NOT-FROM-ASM (whole file: endpoint paths, function names and parameter names only) | 1-14 | - | - | - | NOT-FROM-ASM | `grep -nE "0x[0-9a-f]+\|[=:] ?-?[0-9]+\|[0-9]+ ?(or\|/\|-) ?[0-9]+" endpoints/power_service_ai_ems.md` (header line excluded) has no hit; the only digits are inside identifiers such as `17C1`, `A2345`, `A17B1`. |

## endpoints/power_service_app.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| header "17 function calls, 17 unique endpoints" | 3 | data/endpoints.json (generated from the 3.24.3 asm with a 3.18.0 diff) | - | - | NOT-FROM-ASM | Prose counts. The page names 17 distinct endpoint paths, 17 of them found in `data/endpoints.json`, which holds 25 function rows for those URLs (17 of the URLs exist since 3.18.0 or earlier only). |
| NOT-FROM-ASM (whole file: endpoint paths, function names and parameter names only) | 1-74 | - | - | - | NOT-FROM-ASM | `grep -nE "0x[0-9a-f]+\|[=:] ?-?[0-9]+\|[0-9]+ ?(or\|/\|-) ?[0-9]+" endpoints/power_service_app.md` (header line excluded) has no hit; the only digits are inside identifiers such as `17C1`, `A2345`, `A17B1`. |

## endpoints/power_service_compatible.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| header "12 function calls, 12 unique endpoints" | 3 | data/endpoints.json (generated from the 3.24.3 asm with a 3.18.0 diff) | - | - | NOT-FROM-ASM | Prose counts. The page names 13 distinct endpoint paths, 13 of them found in `data/endpoints.json`, which holds 16 function rows for those URLs (13 of the URLs exist since 3.18.0 or earlier only). The extra path is an upstream-confirmed endpoint "missing from APK extraction" (set_power_cutoff). |
| NOT-FROM-ASM (whole file: endpoint paths, function names and parameter names only) | 1-59 | - | - | - | NOT-FROM-ASM | `grep -nE "0x[0-9a-f]+\|[=:] ?-?[0-9]+\|[0-9]+ ?(or\|/\|-) ?[0-9]+" endpoints/power_service_compatible.md` (header line excluded) has no hit; the only digits are inside identifiers such as `17C1`, `A2345`, `A17B1`. |

## endpoints/power_service_device.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| header "21 function calls, 8 unique endpoints" | 3 | data/endpoints.json (generated from the 3.24.3 asm with a 3.18.0 diff) | - | - | NOT-FROM-ASM | Prose counts. The page names 8 distinct endpoint paths, 8 of them found in `data/endpoints.json`, which holds 73 function rows for those URLs (8 of the URLs exist since 3.18.0 or earlier only). |
| Upstream example `{"pv_power_limit": 800, "switch_0w": 0}` | 38 | - | - | - | NOT-FROM-ASM | Upstream example payload. |

## endpoints/power_service_dynamic_price.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| header "3 function calls, 3 unique endpoints" | 3 | data/endpoints.json (generated from the 3.24.3 asm with a 3.18.0 diff) | - | - | NOT-FROM-ASM | Prose counts. The page names 3 distinct endpoint paths, 3 of them found in `data/endpoints.json`, which holds 3 function rows for those URLs (3 of the URLs exist since 3.18.0 or earlier only). |
| NOT-FROM-ASM (whole file: endpoint paths, function names and parameter names only) | 1-18 | - | - | - | NOT-FROM-ASM | `grep -nE "0x[0-9a-f]+\|[=:] ?-?[0-9]+\|[0-9]+ ?(or\|/\|-) ?[0-9]+" endpoints/power_service_dynamic_price.md` (header line excluded) has no hit; the only digits are inside identifiers such as `17C1`, `A2345`, `A17B1`. |

## endpoints/power_service_other.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| header "13 function calls, 12 unique endpoints" | 3 | data/endpoints.json (generated from the 3.24.3 asm with a 3.18.0 diff) | - | - | NOT-FROM-ASM | Prose counts. The page names 12 distinct endpoint paths, 12 of them found in `data/endpoints.json`, which holds 14 function rows for those URLs (12 of the URLs exist since 3.18.0 or earlier only). |
| NOT-FROM-ASM (whole file: endpoint paths, function names and parameter names only) | 1-56 | - | - | - | NOT-FROM-ASM | `grep -nE "0x[0-9a-f]+\|[=:] ?-?[0-9]+\|[0-9]+ ?(or\|/\|-) ?[0-9]+" endpoints/power_service_other.md` (header line excluded) has no hit; the only digits are inside identifiers such as `17C1`, `A2345`, `A17B1`. |

## endpoints/power_service_share.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| header "5 function calls, 5 unique endpoints" | 3 | data/endpoints.json (generated from the 3.24.3 asm with a 3.18.0 diff) | - | - | NOT-FROM-ASM | Prose counts. The page names 5 distinct endpoint paths, 5 of them found in `data/endpoints.json`, which holds 6 function rows for those URLs (5 of the URLs exist since 3.18.0 or earlier only). |
| NOT-FROM-ASM (whole file: endpoint paths, function names and parameter names only) | 1-26 | - | - | - | NOT-FROM-ASM | `grep -nE "0x[0-9a-f]+\|[=:] ?-?[0-9]+\|[0-9]+ ?(or\|/\|-) ?[0-9]+" endpoints/power_service_share.md` (header line excluded) has no hit; the only digits are inside identifiers such as `17C1`, `A2345`, `A17B1`. |

## endpoints/power_service_site.md

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| header "51 function calls, 31 unique endpoints" | 3 | data/endpoints.json (generated from the 3.24.3 asm with a 3.18.0 diff) | - | - | NOT-FROM-ASM | Prose counts. The page names 31 distinct endpoint paths, 31 of them found in `data/endpoints.json`, which holds 139 function rows for those URLs (31 of the URLs exist since 3.18.0 or earlier only). |
| set_site_device_param power limit: app sends cmd 123, upstream sends cmd 17 | 129 | charging/http/http_request_repository_impl.dart setSiteDevicePowerLimit @0x43558c4 (3.24.3) | 246 | `mov x16,#0xf6` / `stur w16` (map-literal slot) -> 123 | OK | Already corrected in the text; owner page `api/power_service/site/set_site_device_param.md`. |
