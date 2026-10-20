> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# GetSiteDeviceParamResponse

## Purpose

Carries the parsed `get_site_device_param` response for `param_type` 18 (station settings) and 26 (third-party PV settings), the decoded `param_data` object (`SiteDeviceParamData`) with its list elements, and the request-side object `SetSiteDeviceParamData` that the app serializes for `param_type` 18.

## Dart class + file

Package `charging`, directory `model/site_setting/`.

| class | role | method |
|---|---|---|
| `GetSiteDeviceParamResponse` | response wrapper, `get_site_device_param_model.dart` | `fromJson` `@0x2378060` |
| `SiteDeviceParamData` | decoded `param_data` object, `get_site_device_param_model.dart` | `fromJson` `@0x23781c0` |
| `SiteSocItem` | element of `soc_list`, `get_site_device_param_model.dart` | `fromJson` `@0x2378be0` |
| `FeedTimes` | element of `feed_times`, `get_site_device_param_model.dart` | `fromJson` `@0x2378a24` (written as a constructor, not as a `factory`) |
| `SetSiteDeviceParamData` | request object for type 18, `set_site_device_param_model.dart` | `toJson` `@0x23a0430` |

## Fields

Column `since`: `≤3.18.0` means the key is present in 3.18.0 (earlier versions not checked); `3.24.3` means it is absent in 3.18.0 and present in 3.24.3 (versions in between not checked). Column `nullable`: `yes` where the asm casts to a nullable type, `no` where it casts to a non-nullable type.

### GetSiteDeviceParamResponse

The server sends `data.param_data` as a String that contains JSON. `fromJson` reads it as `String?` (`@0x2378088`, cast `@0x23780c8`), substitutes `"{}"` when it is null (`@0x23780e4`), decodes it to a `Map<String, dynamic>` (cast `@0x2378108`) and passes the map to `SiteDeviceParamData.fromJson` (`@0x237818c`), which becomes the single field of the response (stored at field 0x7, `@0x237819c`). The string `"Warning: Failed to decode param_data: ..."` (`@0x2378138`) is built on the failure path, so a decode error yields an empty object instead of an exception.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `param_data` | `String?` (decoded into `SiteDeviceParamData`) | yes | ≤3.18.0 | `get_site_device_param_model.dart @0x2378088` |

### SiteDeviceParamData

Keys in `fromJson` order; `soc_list` elements are parsed with `SiteSocItem.fromJson` (`@0x2378bc8`, list built at `@0x2378264`), `feed_times` elements with `FeedTimes` (type argument `@0x2378394`).

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `soc_list` | `List<SiteSocItem>?` | yes | ≤3.18.0 | `get_site_device_param_model.dart @0x23781e4` |
| `feed_times` | `List<FeedTimes>?` | yes | 3.24.3 | `get_site_device_param_model.dart @0x23782f8` |
| `switch_0w` | `int?` | yes | ≤3.18.0 | `get_site_device_param_model.dart @0x2378404` |
| `enable_0w` | `int?` | yes | ≤3.18.0 | `get_site_device_param_model.dart @0x2378498` |
| `enable_0w_change` | `bool?` | yes | ≤3.18.0 | `get_site_device_param_model.dart @0x237852c` |
| `feed-in_power_limit` | `int?` | yes | ≤3.18.0 | `get_site_device_param_model.dart @0x23785b4` |
| `third_part_pv_setting` | `int?` | yes | ≤3.18.0 | `get_site_device_param_model.dart @0x237861c` |
| `charge_upper_limit` | `int?` | yes | 3.24.3 | `get_site_device_param_model.dart @0x23786b0` |
| `discharge_lower_limit` | `int?` | yes | 3.24.3 | `get_site_device_param_model.dart @0x2378718` |
| `backup_reserve_switch` | `int?` | yes | 3.24.3 | `get_site_device_param_model.dart @0x2378780` |
| `backup_reserve` | `int?` | yes | 3.24.3 | `get_site_device_param_model.dart @0x23787e8` |
| `cmd_type` | `int?` | yes | 3.24.3 | `get_site_device_param_model.dart @0x2378850` |

### SiteSocItem

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `id` | `int?` | yes | ≤3.18.0 | `get_site_device_param_model.dart @0x2378c0c` |
| `soc` | `int?` | yes | ≤3.18.0 | `get_site_device_param_model.dart @0x2378c90` |
| `is_selected` | `int?` | yes | ≤3.18.0 | `get_site_device_param_model.dart @0x2378d10` |

### FeedTimes

The class is new in 3.24.3 (no `FeedTimes` class in the 3.18.0 asm). `FeedTimes.defaultTime` (`@0x28f9610`) builds the default entry used by the feed-limit page.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `start_time` | `int?` | yes | 3.24.3 | `get_site_device_param_model.dart @0x2378a44` |
| `end_time` | `int?` | yes | 3.24.3 | `get_site_device_param_model.dart @0x2378ac8` |

### SetSiteDeviceParamData (request side, `toJson`)

`SetSiteDeviceParamData.toJson` (`@0x23a0430`) writes a key only when the corresponding field is non-null (each key store is preceded by `cmp w3, NULL`). The object is the `param_data` of `setSafetySocParams` (`param_type` 18, see [param_types.md](../api/param_types.md)). `soc_list` and `enable_0w_change` are not written; `id` and `soc` are written as scalars. `feed_times` is written as a list mapped through `FeedTimes.toJson` (closure `@0x23a07c4`).

| JSON key | source |
|---|---|
| `id` | `set_site_device_param_model.dart @0x23a0484` |
| `soc` | `set_site_device_param_model.dart @0x23a04bc` |
| `switch_0w` | `set_site_device_param_model.dart @0x23a04f4` |
| `enable_0w` | `set_site_device_param_model.dart @0x23a052c` |
| `feed-in_power_limit` | `set_site_device_param_model.dart @0x23a0564` |
| `third_part_pv_setting` | `set_site_device_param_model.dart @0x23a059c` |
| `feed_times` | `set_site_device_param_model.dart @0x23a0638` |
| `charge_upper_limit` | `set_site_device_param_model.dart @0x23a0670` |
| `discharge_lower_limit` | `set_site_device_param_model.dart @0x23a06a8` |
| `backup_reserve_switch` | `set_site_device_param_model.dart @0x23a06e0` |
| `backup_reserve` | `set_site_device_param_model.dart @0x23a0718` |
| `cmd_type` | `set_site_device_param_model.dart @0x23a0750` |

The only `cmd_type` value found at a caller is 1: the SOC-limit closure of `station_home_settings_logic.dart` (`@0x3ff10e4`) stores raw 2 (`mov x0, #2` at `@0x3ff11f0`) with a 32-bit store (`stur w0` at `@0x3ff11f4`) into the `cmd_type` field, Smi, so 1.

## Produced by

- Response: [`get_site_device_param`](../api/power_service/site/get_site_device_param.md) with `param_type` 18 (`getSafetySocParams`, `http_request_repository_impl.dart @0x2377e5c`; the success closure `@0x2377fa8` calls `GetSiteDeviceParamResponse.fromJson` at `@0x2377fd8`) and with `param_type` 26 (`getThreePvParam`, `http_request_repository_impl.dart @0x237dc80`; `SiteDeviceParamData.fromJson` is called directly at `@0x237df84` after `jsonDecode` `@0x237df58`). The `cmd` and request fields of both are in [param_types.md](../api/param_types.md).
- Request object: [`set_site_device_param`](../api/power_service/site/set_site_device_param.md) with `param_type` 18 (`setSafetySocParams`, `http_request_repository_impl.dart @0x23a0220`).

## Consumed by

- `getFeedLimitStatus` (`feed_network_limit_logic.dart @0x28f8a44`): the success closure (`@0x28f8b08`) takes a `GetSiteDeviceParamResponse`, reads fields of the decoded data, builds a `FeedNetWorkLimitEntity` (`@0x28f8d94`, see [feed_net_work_limit_entity.md](feed_net_work_limit_entity.md)) and saves it with `toJsonString` (`@0x28f8e44`). Which field of `SiteDeviceParamData` feeds which entity field is not traced.
- Other `getSafetySocParams` callers: `StationEnergySystemLogic._updateSafetySocStatus` (`station_energy_system_logic.dart @0x2377ce0`), `updateEquipmentFeedNetworkStatus` (`@0x237cb58`), `hasAE100FeederStatusChange` (`@0x239fd18`), `StationHomeSettingsLogic.updateSafetySocAndFeedNetworkStatus` (`station_home_settings_logic.dart @0x28b2534`). Field use is not traced.
- Type 26: `StationEnergySystemLogic.fetchThirdPvSetting` (`station_energy_system_logic.dart @0x237db2c`, call `@0x237dc54`).
- Request object: `station_home_settings_logic.dart` (`_executeSafetySocSave` `@0x3ff07bc`, SOC-limit closure `@0x3ff10e4`, closures `@0x3feed04` and `@0x3fef164`) and `FeedNetworkLimitLogic.setFeedNetworkLimitValue` (`feed_network_limit_logic.dart @0x28f967c`).

## Changed since 3.18.0

Compared with 3.18.0 (`GetSiteDeviceParamResponse.fromJson` 3.18.0 `@0x1a5615c`, `SiteDeviceParamData.fromJson` 3.18.0 `@0x1a562b4`, `SiteSocItem.fromJson` 3.18.0 `@0x1a56734`):

- added to `SiteDeviceParamData`: `feed_times`, `charge_upper_limit`, `discharge_lower_limit`, `backup_reserve_switch`, `backup_reserve`, `cmd_type`
- added class: `FeedTimes`
- no key removed; `GetSiteDeviceParamResponse` and `SiteSocItem` read the same keys in both versions

## Known unknowns

- The value sets and units of the keys (for example `switch_0w`, `enable_0w`, `cmd_type`); only the upstream-confirmed examples (`api/schedule.py` lines 227-229) show values.
- Which keys the server returns for `param_type` 26 (`third_part_pv_setting`, `show_third_party_pv_panel` per the upstream example) and whether `SiteDeviceParamData` reads them: `show_third_party_pv_panel` is not a key of this class.
- Whether `SetSiteDeviceParamData` fields not set by the traced callers are ever set by other callers of `setSafetySocParams`. — traced 2026-10-20: the dump has six call sites of `setSafetySocParams`: `station_energy_system_logic.dart @0x23a01f8` (object allocated `@0x23a0140`), `station_home_settings_logic.dart @0x3feef8c`, `@0x3fef290`, `@0x3ff0878`, `@0x3ff1294` and `feed_network_limit_logic.dart @0x28f97f4`. The `toJson` offsets are: `id` 0x7, `soc` 0xb, `switch_0w` 0xf, `enable_0w` 0x13, `charge_upper_limit` 0x27, `discharge_lower_limit` 0x2b, `backup_reserve_switch` 0x2f, `backup_reserve` 0x33, `cmd_type` 0x37 (loads in `toJson`, `set_site_device_param_model.dart @0x23a0484` to `@0x23a0750`). The closure at `@0x3ff1294` stores 0x27, 0x2b, 0x2f, 0x33 and 0x37 (`@0x3ff11c0` to `@0x3ff11f4`), the closure at `@0x3ff0878` stores 0x7 and 0xb (`@0x3ff0788`, `@0x3ff0790`); the other four sites store into closure contexts and objects whose offsets could not be separated by this scan, so the per-site field sets of those four were not decided.
