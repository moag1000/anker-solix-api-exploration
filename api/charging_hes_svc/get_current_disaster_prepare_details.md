> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_current_disaster_prepare_details

## Purpose

Reads the current disaster-preparedness details of a station (callers `SystemPolicyLogic::deviceToAutoDisasterStatus` and `AutoDisasterTipsLogic::_quitAutoDisasterPrepareFromDevice`, through `HttpRequestControllerImpl::getCurrentDisasterPrepareDetails`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_current_disaster_prepare_details` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x3ebe778`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3ebe770`, in `HttpRequestControllerImpl::getCurrentDisasterPrepareDetails` (`charging/http/http_request_repository_impl.dart @0x3ebe5d8`), sent through `requestHttp` (`@0x3ebe79c`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `HttpRequestControllerImpl::getCurrentDisasterPrepareDetails` (`charging/http/http_request_repository_impl.dart`, call `@0x3ebe79c`, argument list `@0x3ebe794`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

`HttpRequestControllerImpl::getCurrentDisasterPrepareDetails` (`charging/http/http_request_repository_impl.dart @0x3ebe5d8`) starts from an empty map literal with type arguments `<String, Object>` (`@0x3ebe68c`) and adds keys with `[]=`. `station_id` is added as received (`@0x3ebe6c0`), `unix` after `BoxInt64Instr` (`@0x3ebe6d0`, an unboxed 64-bit integer), and `auto_disaster_enable` only when its parameter is non-null (`cmp w3, NULL` `@0x3ebe714`, branch `@0x3ebe718`); its value is stored as received (`@0x3ebe734`).

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | string | yes |  | `charging/http/http_request_repository_impl.dart @0x3ebe6b8` |
| `unix` | int (unboxed, x) | yes |  | `charging/http/http_request_repository_impl.dart @0x3ebe6fc` |
| `auto_disaster_enable` | bool | optional |  | `charging/http/http_request_repository_impl.dart @0x3ebe72c` |

Callers (app side, traced 2026-10-20): `SystemPolicyLogic::deviceToAutoDisasterStatus` (`charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart @0x3ebd418`) passes `stationId()` (`@0x3ebd3f8`, the getter `AutoDisasterTipsLogic::stationId` `@0x23cd140`), a seconds value it computes inline from `_getCurrentMicros` (`@0x3ebd3c0`, two `sdiv` by 1000 `@0x3ebd3e8`, `@0x3ebd3ec`) and the named argument `autoDisasterEnable` (`@0x3ebd410`) from its own parameter; the function that calls `deviceToAutoDisasterStatus` (`@0x3ebd380`, with the same value also passed to `netToSetAutoDisasterStatus` `@0x3ebd374`) type-checks that value as `bool` (`r8 = bool` `@0x3ebd30c`, class-id test `@0x3ebd304`) and stores it with `value=` (`@0x3ebd324`); so `auto_disaster_enable` is a bool. `AutoDisasterTipsLogic::_quitAutoDisasterPrepareFromDevice` (`charging/ui/page/family/auto_disaster/auto_disaster_tips_logic.dart @0x4369e08`) passes `stationId()` and `unix()` and no named argument, so the key is omitted there (the null guard of the sender). `station_id` is the return value of `AutoDisasterTipsLogic::stationId` (`charging/ui/page/family/auto_disaster/auto_disaster_tips_logic.dart @0x23cd140`), which returns `field_7` of the value of `field_7f` of `Get.find<StationMainPageLogic>()` (`@0x23cd188`..`@0x23cd198`) or the empty string when null (`@0x23cd1a8`); `field_7` of that station model is the `String?` documented on [device_command.md](device_command.md#request), so the key is a string (two-hop, declared type read). `unix` is the getter `AutoDisasterTipsLogic::unix` (`@0x27ada3c`): `_getCurrentMicros` (`@0x27ada50`) divided twice by 1000 (`sdiv` `@0x27ada78`, `@0x27ada7c`, unboxed), the current time of the app clock in seconds.

## `param_type`/`cmd`

n/a

## Response model (link)

- [`DisasterPrepareDetailsModel`](../../models/hes.md#disasterpreparedetailsmodel), parsed by `DisasterPrepareDetailsModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x3ebe8bc` (success closure `@0x3ebe850`, `bl` target `[package:charging/model/a5101/disaster_prepare_details_model.dart]`).

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::DisasterPrepareDetailsModel`): `details` (unknown).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "station_id": "<station_id>",
  "unix": "<unix>",
  "auto_disaster_enable": "<auto_disaster_enable>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getCurrentDisasterPrepareDetails` @0x3ebe5d8 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::getCurrentDisasterPrepareDetails`
- `charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart::deviceToAutoDisasterStatus`
- `charging/ui/page/family/auto_disaster/auto_disaster_tips_logic.dart::_quitAutoDisasterPrepareFromDevice`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What the server returns when `auto_disaster_enable` is absent: the app omits the key for a null parameter.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call. — reclassified: device test row 150 (traced 2026-10-20: per call the SDK login state `AkIotKitFlutter::isLogin` and the base-URL predicate decide, `HttpEncryptionDecorator.dart @0x4869504`, `@0x4869544`; the predicate is a GDT dispatch whose selector the asm does not name, and the login state is runtime data)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
