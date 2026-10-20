> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# create_site

## Purpose

Creates a site: the A1782 and A17B1 electricity-scene logics (`createSite`), `OpenProcessLogic::create`, `CreateSystemLogic::create` and `SiteLogic::createSiteDirectly` call `createSiteRequest`.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/site/create_site` (asm-traced): URL string at `http_request_repository_impl.dart @0x27b28a4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x27b289c`, in `HttpRequestControllerImpl::createSiteRequest` (`http_request_repository_impl.dart @0x27b23f8`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is a 12-pair map literal typed `<String, dynamic>` (type arguments `@0x27b2828`, `AllocateArray r2 = 48` `@0x27b245c`) built in `createSiteRequest` (`http_request_repository_impl.dart @0x27b23f8`); `createSite` is logged first (`@0x27b2448`).

| field | type | required | example | source |
|---|---|---|---|---|
| `site_name` | ? | yes | | key `@0x27b2468`, value store `@0x27b2478` (stack parameter `fp+0x30`) |
| `site_img` | string | yes | `""` | key `@0x27b247c`, literal empty string `@0x27b2488`, store `@0x27b248c` |
| `solar_list` | list | yes | | key `@0x27b2490`, store `@0x27b24cc`; a null parameter (`cmp w1, NULL` `@0x27b24a0`) becomes an empty `<SiteDeviceModel>` list (`@0x27b24a8`) |
| `pps_list` | list | yes | | key `@0x27b24f0`, store `@0x27b2528`, null fallback `<SiteDeviceModel>` `@0x27b2504` |
| `solarbank_list` | list | yes | | key `@0x27b254c`, store `@0x27b2584`, null fallback `@0x27b2560` |
| `home_backup_system_list` | list | yes | | key `@0x27b25a8`, store `@0x27b25e0`, null fallback `@0x27b25bc` |
| `powerpanel_list` | list | yes | | key `@0x27b2604`, store `@0x27b263c`, null fallback `@0x27b2618` |
| `grid_list` | list | yes | | key `@0x27b2660`, store `@0x27b2698`, null fallback `@0x27b2674` |
| `solarbank_pps_list` | list | yes | | key `@0x27b26bc`, store `@0x27b26f4`, null fallback `@0x27b26d0` |
| `smartplug_list` | list | yes | | key `@0x27b2718`, store `@0x27b2750`, null fallback `@0x27b272c` |
| `combiner_box_list` | list | yes | | key `@0x27b2774`, store `@0x27b27ac`, null fallback `@0x27b2788` |
| `charging_pile_list` | list | yes | | key `@0x27b27d0`, store `@0x27b2804`, null fallback `@0x27b27e4` |
| `app_ability` | ? | optional | | key `@0x27b2858`, `[]=` `@0x27b2860`; added when the parameter at `fp-0x18` is non-null (`cmp w3, NULL` `@0x27b2844`) |

Elements of the ten lists (asm-traced): `SiteDeviceModel::toJson` (`charging/model/power_site/site_device_model.dart @0x225f4e8`) starts from an empty map and adds, with `Map.[]=` calls, the keys `device_sn` (`@0x225f534`), `device_name` (`@0x225f564`), `device_img` (`@0x225f594`), `generate_power` (`@0x225f5c4`), `power_unit` (`@0x225f5f4`), `status` (`@0x225f624`), `bind_site_status` (`@0x225f654`), `battery_power` (`@0x225f684`), `charging_power` (`@0x225f6b4`), `wireless_type` (`@0x225f6e4`), `priority_index` (`@0x225f714`), `device_pn` (`@0x225f744`), `initial_process` (`@0x225f774`), `bssid` (`@0x225f7a4`), `ssid` (`@0x225f7d4`), `password` (`@0x225f804`), `checked` (`@0x225f834`), `hardware_info` (`@0x225f864`), `hardware_main_sn` (`@0x225f894`), `hardware_status` (`@0x225f8c4`) and, only when a list field is not null (`cmp w3, NULL` `@0x225f8e8`), `bind_site_ids` (`@0x225f94c`). The declared types of `SiteDeviceModel.fromJson` (`data/models.json`, `charging::SiteDeviceModel`) are `String?` for all keys except `initial_process`, `hardware_info`, `hardware_status` (`int?`), `checked` (`bool?`) and `bind_site_ids` (`unknown`). The lists hold `SiteDeviceModel` objects (fallback `<SiteDeviceModel>` lists in the table), so each element carries these keys if the HTTP layer serialises the objects with `toJson`; that step is outside the Dart code read.

## `param_type`/`cmd`

n/a

## Response model (link)

`charging::CreateSiteResponseModel` (`data/models.json` key, no model page), parsed in the builder's success closure `http_request_repository_impl.dart @0x27b299c` by `CreateSiteResponseModel.fromJson`; the success path logs `"createSite success, data: "` and calls `exeSuccess()`.

## Response

Top-level keys of the model (from `data/models.json`, all nullable String): `site_id`, `site_name`, `exist_site_id`.

## Example request/response

Request, synthesized (type of `site_name` and `app_ability` unresolved; the ten lists default to empty)

```json
{"site_name": "<site_name>", "site_img": "", "solar_list": [], "pps_list": [], "solarbank_list": [], "home_backup_system_list": [], "powerpanel_list": [], "grid_list": [], "solarbank_pps_list": [], "smartplug_list": [], "combiner_box_list": [], "charging_pile_list": []}
```

## Errors seen

Several callers compare the failure code with a 32-bit compare, raw 44200, so 22100 (`a1782_electricity_scene_logic.dart @0x28d3540`, shared failure closure `@0x28d3528`) and show the text key `stationTips`; `SiteLogic::createSiteDirectly` handles failures with `handleNetErrorMsg`. Meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `createSiteRequest` @0x27b23f8 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::createSiteRequest`
- `charging/ui/page/device/a1782/station/electricity_scene/a1782_electricity_scene_logic.dart::createSite`
- `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart::createSite`
- `charging/ui/page/device/a17c1/open_process/open_process_logic.dart::create`
- `charging/ui/page/device/connect/create_join_device_to_system/create_system/create_system_logic.dart::create`
- `charging/ui/page/green_energy/site/site_logic.dart::createSiteDirectly`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- Type of `site_name` and of `app_ability` (parameters; the six callers were not followed). Header stays string-only. — attempted 2026-10-20 (two-hop not readable: `app_ability` is a named argument of three callers (`charging/ui/page/device/a17c1/open_process/open_process_logic.dart @0x28d2b28`, `charging/ui/page/device/connect/create_join_device_to_system/create_system/create_system_logic.dart @0x2924090`, `charging/ui/page/green_energy/site/site_logic.dart @0x27b1fa4`) and its value is read from fields; `site_name` is a positional argument whose source differs per caller (`r2 = Null` in `a1782_electricity_scene_logic.dart @0x28d3824`, `electricity_scene_logic.dart @0x3d079c8`); no declared types are shown)
- What `exist_site_id` carries the key name suggests the id of an existing site; not read. — reclassified: server

## Device-tested by

none
