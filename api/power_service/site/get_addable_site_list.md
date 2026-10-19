> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_addable_site_list

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/site/get_addable_site_list`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_business_impl.dart @0x239ba44`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `charging/http/http_business_impl.dart @0x239b964` |
| `device_model` | ? | ? | ? | `charging/http/http_business_impl.dart @0x239b964` |

Rows are the union over 2 senders; `source` is the first sender that sets the key.

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

- `charging/http/http_business_impl.dart`: `getDeviceIsJoinedSite` @0x239b964 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/http/http_request_repository_impl.dart`: `getAddableSiteList` @0x262e088 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::getAddableSiteList`
- `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart::_getAddableSiteList`
- `charging/ui/page/device/a17b1/system_policy/system_policy_logic.dart::_getSiteConfig`
- `charging/ui/page/device/a17c0/a17c0SwitchMode/a17c0_switch_mode_logic.dart::deviceConnect`
- `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart::getUserSiteListReq`
- `charging/ui/page/device/connect/create_join_device_to_system/join_system/join_system_logic.dart::queryExistSystems`
- `charging/ui/page/device/main/sitation_energy_system/create_site_progress_handler/create_site_progress_handler.dart::checkCreateSiteProgressIsComplete`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
