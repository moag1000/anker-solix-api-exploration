> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# create_site

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/site/create_site`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x27b28a4`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `site_name` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x27b23f8` |
| `site_img` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x27b23f8` |
| `solar_list` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x27b23f8` |
| `pps_list` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x27b23f8` |
| `solarbank_list` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x27b23f8` |
| `home_backup_system_list` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x27b23f8` |
| `powerpanel_list` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x27b23f8` |
| `grid_list` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x27b23f8` |
| `solarbank_pps_list` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x27b23f8` |
| `smartplug_list` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x27b23f8` |
| `combiner_box_list` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x27b23f8` |
| `charging_pile_list` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x27b23f8` |

## `param_type`/`cmd`

n/a

## Response model (link)

<!-- TODO -->

## Response

<!-- TODO -->

## Example request/response

<!-- TODO -->

## Errors seen

`api/errors.md`: <!-- TODO -->

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

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
