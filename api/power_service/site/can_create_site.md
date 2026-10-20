> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# can_create_site

## Purpose

Asks the server whether a new site can be created and which device lists a site may hold: `StationMainPageLogic::checkCanCreateStation` calls `checkCanCreateSite`; `SiteLogic::createSiteHome` (and `_deleteGroupDevices`) call `createSiteHomeRequest`, which sends the same URL.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/site/can_create_site` (asm-traced) at the senders that load a `Method` object next to the URL string (pool entry `pp+0xa7e0`, `Method.post`):

- `HttpRequestControllerImpl::checkCanCreateSite` (`http_request_repository_impl.dart @0x2902144`): URL string `@0x2902200`, method object `Method.post` (`pp+0xa7e0`) `@0x29021f8`.
- `HttpRequestControllerImpl::createSiteHomeRequest` (`http_request_repository_impl.dart @0x290487c`): URL string `@0x2904908`, method object `Method.post` (`pp+0xa7e0`) `@0x2904900`.

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No request keys. Two builders, both with an empty body and no `[]=` call: `checkCanCreateSite` (`http_request_repository_impl.dart @0x2902144`): empty array (`ldr x16, [THR, #0xa8]`) `@0x29021b8`, `Map._fromLiteral` `@0x29021c0`, sent with `encryptionRequestHttp` `@0x2902220`; `createSiteHomeRequest` (`http_request_repository_impl.dart @0x290487c`): empty array `@0x29048c0`, `Map._fromLiteral` `@0x29048c8`, `encryptionRequestHttp` `@0x2904930`.

## `param_type`/`cmd`

n/a

## Response model (link)

`charging::CanCreateSiteModel` (`data/models.json` key; fields on [`models/other.md`](../../../models/other.md#cancreatesitemodel)), parsed in the success closure `http_request_repository_impl.dart @0x29022fc` by `CanCreateSiteModel.fromJson`, followed by `setEnableCreateSite` and the local solar and PPS list setters. `createSiteHomeRequest` references the same closure code (identical pool closure `@0x29022fc`).

## Response

Top-level keys of the model (from `data/models.json`): `can_create_site` (String), `grid_list`, `smartplug_list`, `solar_list`, `pps_list`, `solarbank_list`, `powerpanel_list`, `combiner_box_list`, `solarbank_pps_list`, `charging_pile_list`, `home_backup_system_list` (element types not resolved there).

## Example request/response

Request, synthesized

```json
{}
```

Response keys: see Response; no capture.

## Errors seen

None traced. The failure callback `@0x2902248` logs `"checkCanCreateSite failed, code: "` and the message, then calls `exeError()`; no code is compared. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `checkCanCreateSite` @0x2902144 (encryptionRequestHttp; encrypted: true); `createSiteHomeRequest` @0x290487c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::checkCanCreateSite`
- `charging/http/http_request_repository.dart::createSiteHomeRequest`
- `charging/ui/page/device/main/station_device_home/station_main_page/station_main_page_logic.dart::checkCanCreateStation`
- `charging/ui/page/green_energy/site/site_logic.dart::_deleteGroupDevices`
- `charging/ui/page/green_energy/site/site_logic.dart::createSiteHome`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta. The model `CanCreateSiteModel` is `≤3.18.0` in `data/models.json`.

## Known unknowns

- Why `createSiteHomeRequest` shares this URL and closure with the check: only the shared pool closure is read; whether the server treats the two calls differently is not derivable (the body is empty in both).
- Element structures of the `*_list` keys (the model keeps them untyped).
- The server rule behind `can_create_site` (a String in the model): not visible in the app.

## Device-tested by

none
