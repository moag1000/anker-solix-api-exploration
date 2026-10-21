> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# product_tutorial_search

## Purpose

Searches the user manuals by keyword or by product numbers; sent by `SearchDeviceUserManualsLogic::searchDeviceNameList` and `::searchDeviceUserManualsList` and by `StationUsermanualsLogic::_getDevicesList` (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /app/help/product_tutorial_search` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x291a65c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x291a654`, in `HttpRequestControllerImpl::searchUserManualsDeviceDataList` (`charging/http/http_request_repository_impl.dart @0x291a52c`), sent through `encryptionRequestHttp` (`@0x291a68c`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The sender builds the body at run time: an empty map literal (`Map._fromLiteral` `@0x291a58c`) is filled with `[]=` calls, each behind a guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `keyword` | string | optional (inserted only when a length field read from an argument is non-zero, `cbz` `@0x291a5a0`) | ? | `charging/http/http_request_repository_impl.dart @0x291a5b0` (`[]=` call `@0x291a5b8`) |
| `pns` | list | optional (inserted only when a list length read from an argument is non-zero, `cbnz` `@0x291a5e0`) | ? | `charging/http/http_request_repository_impl.dart @0x291a610` (`[]=` call `@0x291a618`) |

The literal has no type arguments recorded; the guards read a string-like length for `keyword` (`field_7`) and a list-like length for `pns` (`field_b`), which is not a type proof.

Caller arguments (traced 2026-10-20, app side): the sender takes `keyword` and `pns` as named parameters and each caller passes one of them (named argument list `@0x291a420`, `@0x34b25cc`). `SearchDeviceUserManualsLogic::searchDeviceNameList` (`charging/ui/page/user/userManuals/searchDeviceUserManuals/search_device_user_manuals_logic.dart @0x291a358`) passes `keyword`; it reads the length field of the text (`field_7` as `LoadInt32Instr` `@0x291a3cc`..`@0x291a3d0`) and returns without a request when the length is not greater than 1 (`cmp x2, #1` `@0x291a3d4`), so `keyword` is a String of at least 2 characters when sent (a text field value). `StationUsermanualsLogic::_getDevicesList` (`charging/ui/page/device/main/station_device_home/StationUsermanuals/station_usermanuals_logic.dart @0x34b25d4`) passes `pns`, built as a growable list from `map<String>` over the station's product lists (`<String>` `@0x34b2564`, `map` `@0x34b2578`, `_GrowableList.of` `@0x34b2588`), so `pns` is a list of strings; the source lists are the station product lists (`PpsList`, `ProductInfoModel`, `SolarList`, `SolarbankList` types, `@0x34b1f28`..`@0x34b2374`), so the entries are product identifiers taken from those lists (the mapped field is `field_1b` of each element, see Known unknowns). The sender sends an empty body only when `pns` is an empty list or the call has neither argument; the `keyword` caller cannot produce an empty body (length guard).

## `param_type`/`cmd`

n/a

## Response model (link)

[`SearchUserManualsModel`](../../../models/account.md#searchusermanualsmodel), parsed by `SearchUserManualsModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x291a6e0` in the success closure `@0x291a6a8` (call target `#0x291a720`).

## Response

(asm-traced) Top-level keys of `charging::SearchUserManualsModel` (`data/models.json`): `trace_id` (String?), `products` (List). The closure passes the model to the callback (`ClosureCall` `@0x291a6fc`).

## Example request/response

Request: the keys are listed under Request; the values are parameters, so no body is synthesized. Response: not synthesized; no capture exists for this endpoint.

## Errors seen

none traced: no numeric error code is compared in the sender, its closures or the caller functions read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `searchUserManualsDeviceDataList` @0x291a52c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::searchUserManualsDeviceDataList`
- `charging/ui/page/device/main/station_device_home/StationUsermanuals/station_usermanuals_logic.dart::_getDevicesList`
- `charging/ui/page/user/userManuals/searchDeviceUserManuals/search_device_user_manuals_logic.dart::searchDeviceNameList`
- `charging/ui/page/user/userManuals/searchDeviceUserManuals/search_device_user_manuals_logic.dart::searchDeviceUserManualsList`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Which field of each station product ends in `pns`: the mapping closure `@0x34b296c` (code shared with another page, `small_charging_platform/src/screen_setting/clock_style/custom_screensaver/page/clock_style_manage_logic.dart`) returns `field_1b` of its argument or `""` when that is null (`@0x34b2970`..`@0x34b2980`); that `field_1b` is a product number is the reading of the key name, not read from the asm — traced 2026-10-20
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
