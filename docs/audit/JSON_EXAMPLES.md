> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Page type: audit table · Owner page: this page

# Audit: JSON_EXAMPLES.md (Smi sweep)

Every integer in `JSON_EXAMPLES.md` that the doc could attribute to the asm. The upstream-sourced blocks are Python snippets from the upstream library, the inferred blocks carry placeholders only, and most remaining examples are synthesized values; each is classified below. Only the constants tables are asm-derived.

Doc line numbers refer to the file BEFORE the banner was added (commit f105769); in the current file add 2.

Verdicts: `OK`, `WRONG` (real value in the note), `NOT-FROM-ASM` (string, upstream, captured/device test, example or prose count), `UNVERIFIABLE` (site not found; search listed), `CHANGED-IN-3.24.3` (doc matches 3.18.0 but not 3.24.3). Byte offsets (`0xNNN`, `r17 = N`) and class ids/sizes are real values printed by Blutter and are not Smi-affected; they are only checked for presence. `not Smi:` in a WRONG note marks a correction that is not a doubled integer.

Rows: 17. NOT-FROM-ASM 15, OK 2.

| claim (as written) | doc line | asm site (file.dart @0xADDR, version) | raw | store/compare instruction | verdict | note |
|---|---|---|---|---|---|---|
| Upstream-sourced request blocks (`check_upgrade_record` ... `wifi_list`, 33 blocks) | 10-243 | upstream api.py / energy.py / apibase.py (thomluther) | - | - | NOT-FROM-ASM | Python snippets copied from the upstream library. They contain no integer literals that came from asm (only `site_id`, `device_sn`, `accuracy`/`decimals` variables). |
| `(sb.get("generation") or 0) <= 1` / `>= 2` in the `set_device_load` and `set_device_parm` snippets | 198, 205 | upstream api.py (thomluther) | - | - | NOT-FROM-ASM | Upstream solarbank-generation split (SB1 vs SB2+); Python, not asm. |
| Inferred Requests: all fields are placeholders `"..."` (`add_charging_mode`, `get_configs`, ..., 60 blocks) | 245-672 | - | - | - | NOT-FROM-ASM | The section states "Field values are placeholders"; there are no integers. Function names with digits (`addA2345...`, `getA2687...`) are identifiers. |
| `getDeviceAttrs` extra `enable_0w_v2` flag | 443, 685-687 | - | - | - | NOT-FROM-ASM | Boolean flag name; the digits are part of the key. No integer. |
| "`set_device_attrs` ... is used by **9 different functions**" | 713 | - | - | - | NOT-FROM-ASM | Prose count; the nine functions listed under it (and in PARAM_DATA_STRUCTURES lines 190-198) are consistent. |
| `{"power_limit": 800, "ac_power_limit": 1200, "pv_power_limit": 3600}` | 717 | upstream api.py `set_device_attributes` example | - | - | NOT-FROM-ASM | Upstream example values. |
| `{"switch_0w": 0}` and "0=allow grid export, 1=block" | 741, 743 | upstream apitypes.py / device-tested semantics | - | - | NOT-FROM-ASM | Same finding as the BLE_COMMAND_MAP audit row for `switch_0w` (upstream semantics). |
| `{"pv_power_limit": 800}` | 747 | upstream | - | - | NOT-FROM-ASM | Upstream example value. |
| `{"init_status": "1"}` | 759 | - | - | - | NOT-FROM-ASM | String value in the example; setDeviceGameStatus argument, not an asm immediate. |
| Peak/Valley price types `{"peak": 1, "normal": 2, "valley": 3, "super_valley": 4}` | 777 | pp.txt Map<String,int>(4) [pp+0xeb970] / [pp+0xfbd88] (3.24.3); [pp+0xb7970] (3.18.0) | 0x1, 0x2, 0x3, 0x4 | pool constant map (untagged) | OK | Already verified in `docs/audit/ENUMS.md` (row "Peak/Valley Price Types", which cites this line). The `ElectricityIntervalEnum` indices are 0..3; 1..4 are the map values. |
| "All Known Product Codes (53 models)" | 802 | - | - | - | NOT-FROM-ASM | Prose count; the list below the heading contains 53 codes. Strings, no integers. |
| EV Charger Schedule Defaults (A5190): `"08:00"`, `"22:00"`, `false`, `[]` | 815-830 | ev_charger/src/ev_charger/sdk/model (3.24.3) | - | - | NOT-FROM-ASM | Times are strings and the rest are booleans; no integers. Header says "Defaults" but the block is a shape template. |
| Range Extender Strategy `"bysocData": {"startSoc": 20, "targetSoc": 80}`, `"bytimeData": {"startTime": "08:00", "targetSoc": 80}` | 839-840 | oe_a7320/src/oe_a7320/page/range_extender_system/local/range_extender_local.dart (3.24.3); charging/model/a5101/a5101_diesel_model.dart | - | - | NOT-FROM-ASM | Illustrative values. The only hits for `startSoc` in these files are the key and a translation lookup (`startSoc()` -> `Trans.tr`); no 20/80 constants (raw 40/160) are stored next to the keys. |
| EV Charger Control `"carChargerLockStatus": 0`, `"maximumCurrentLimit": 16`, `"lightBrightness": 100` | 856-859 | ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2ce0b20, @0x398170c (BoxInt64Instr of a parameter) (3.24.3) | variable | `BoxInt64Instr(r3)` of an unboxed argument | NOT-FROM-ASM | The command builders take these values from their parameters; 16 and 100 are illustrative, not constants. |
| Dynamic price fields `"today_avg_price": 0.15`, `"tomorrow_avg_price": 0.12`, `"batteryReserve": 10` | 895-899 | base_service/bean/dynamic_price_detail_model.dart (3.24.3) | - | - | NOT-FROM-ASM | Illustrative response values (double fields); no constants at the field sites. |
| akiot.cloud_api bridge `"param_type": "18"` | 914 | data/param_types.json row 18 @0x2aa91bc (3.24.3) | string "18" | String literal | OK | param_type 18 = getSafetySocParams / setSafetySocParams. String, matches the decoded row. |
| SceneInfo flags `"exceed_power": "0"`, `"power_limit_status": 0` | 928, 937 | charging/model/green_energy/station/scene_info.dart fromJson @0x225e52c (3.24.3) | - | no immediates beside the key strings | NOT-FROM-ASM | Field names from the model; the `0` values are illustrative (the fromJson reads carry no defaults). |
