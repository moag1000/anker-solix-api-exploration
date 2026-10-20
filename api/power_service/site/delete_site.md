> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# delete_site

## Purpose

Deletes a site: the four delete-site confirmations build the body and call `deleteSite`: `SystemInfoLogic` of the A17B1 and of the station-home-settings page, `StationHomeInfoLogic::deleteSiteRes` and `HomeCenterLogic::deleteSiteRes`.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/site/delete_site` (asm-traced): URL string at `http_request_repository_impl.dart @0x30c5424`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x30c541c`, in `HttpRequestControllerImpl::deleteSite` (`http_request_repository_impl.dart @0x30c53a0`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The builder `deleteSite` (`http_request_repository_impl.dart @0x30c53a0`) has no map literal; each of the four callers builds a 1-pair map typed `<String, String>`, so `site_id` is a String in all of them.

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | string | yes | `"<site_id>"` | a17b1 `system_info_logic.dart`: key `@0x3d45eec`, store `@0x3d45f04`, type arguments `@0x3d45f08`; station-home-settings `system_info_logic.dart`: key `@0x3ff4168`, store `@0x3ff4180`, type arguments `@0x3ff4184`; `station_home_info_logic.dart`: key `@0x30c5238`, store `@0x30c5268`, type arguments `@0x30c528c`; `home_center_logic.dart`: key `@0x405eee0`, store `@0x405eef0`, type arguments `@0x405eef4` |

## `param_type`/`cmd`

n/a

## Response model (link)

None: no model is parsed. The builder passes forwarding template closures (`pp` entries printed in `rx_workers.dart @0x228e574` and `http_request_repository_impl.dart @0x2375ad8`); the callers' success callbacks (`system_info_logic.dart @0x3d45f88` and `@0x3ff4288`, `station_home_info_logic.dart @0x30c62f4`, `home_center_logic.dart @0x405f0b0`) load no response argument and contain no `fromJson` call; they close pages and refresh the site list (`getSiteList`, `processDeleteStation`, `_deleteSiteSuccess`).

## Response

No response key is read by the app.

## Example request/response

Request, synthesized (decrypted body as built by the four callers)

```json
{"site_id": "<site_id>"}
```

Response: none parsed.

## Errors seen

None traced. The shared failure callback `station_home_info_logic.dart @0x30c5468` and `system_info_logic.dart @0x3ff4208` show the `commonOK` dialog; no code is compared. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `deleteSite` @0x30c53a0 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::deleteSite`
- `charging/ui/page/device/a17b1/system_info/system_info_logic.dart::deleteSiteRes`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/system_info/system_info_logic.dart::deleteSiteRes`
- `charging/ui/page/device/main/station_device_home/station_home_info/controller/station_home_info_logic.dart::deleteSiteRes`
- `charging/ui/page/user/share_site/home_center/home_center_logic.dart::deleteSiteRes`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- Whether the server deletes only the site or also detaches its devices: the app sends only `site_id`; device removal is a separate call ([delete_site_devices](delete_site_devices.md)).
- The response body: not read by the app, so its keys are unknown.

## Device-tested by

none
