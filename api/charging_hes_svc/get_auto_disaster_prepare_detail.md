> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_auto_disaster_prepare_detail

## Purpose

Reads the detail of the auto disaster-preparedness plan for the family page tips (`AutoDisasterTipsLogic::clickAutoDisasterTips` through `HttpRequestControllerImpl::getAutoDisasterPrepareDetail`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_auto_disaster_prepare_detail` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x43695f8`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x43695f0`, in `HttpRequestControllerImpl::getAutoDisasterPrepareDetail` (`charging/http/http_request_repository_impl.dart @0x43694a4`), sent through `requestHttp` (`@0x4369620`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `HttpRequestControllerImpl::getAutoDisasterPrepareDetail` (`charging/http/http_request_repository_impl.dart`, call `@0x4369620`, argument list `@0x4369618`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

`HttpRequestControllerImpl::getAutoDisasterPrepareDetail` (`charging/http/http_request_repository_impl.dart @0x43694a4`) stores 3 keys in a map literal with type arguments `<String, Object>` (`@0x43695ac`), which do not type the values. `unix` is boxed from an unboxed 64-bit integer (`BoxInt64Instr` `@0x4369580`), so it is an integer; `station_id` and `near_field` are stored as received (`@0x436956c`, `@0x43695a8`). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | string | yes |  | `charging/http/http_request_repository_impl.dart @0x436955c` |
| `unix` | int (unboxed, x) | yes |  | `charging/http/http_request_repository_impl.dart @0x4369570` |
| `near_field` | bool | yes |  | `charging/http/http_request_repository_impl.dart @0x4369598` |

Callers (app side, traced 2026-10-20): the only caller `AutoDisasterTipsLogic::clickAutoDisasterTips` (`charging/ui/page/family/auto_disaster/auto_disaster_tips_logic.dart @0x4367f54`) passes `stationId()` (`@0x4367ee4`), `unix()` (`@0x4367ef0`) and, as `near_field`, the boolean negation (`eor x, x, #0x10` `@0x4367f44`) of a bool field (`field_93` of the object at `field_83`, read only when its `field_2b` flag is true, else `false`, `@0x4367f30`..`@0x4367f40`), so `near_field` is a bool. `station_id` is the return value of `AutoDisasterTipsLogic::stationId` (`charging/ui/page/family/auto_disaster/auto_disaster_tips_logic.dart @0x23cd140`), which returns `field_7` of the value of `field_7f` of `Get.find<StationMainPageLogic>()` (`@0x23cd188`..`@0x23cd198`) or the empty string when null (`@0x23cd1a8`); `field_7` of that station model is the `String?` documented on [device_command.md](device_command.md#request), so the key is a string (two-hop, declared type read). `unix` is the getter `AutoDisasterTipsLogic::unix` (`@0x27ada3c`): `_getCurrentMicros` (`@0x27ada50`) divided twice by 1000 (`sdiv` `@0x27ada78`, `@0x27ada7c`, unboxed), the current time of the app clock in seconds.

## `param_type`/`cmd`

n/a

## Response model (link)

- [`AutoDisasterDetailModel`](../../models/hes.md#autodisasterdetailmodel), parsed by `AutoDisasterDetailModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x4369740` (success closure `@0x43696d4`, `bl` target `[package:charging/model/a5101/auto_disaster_detail_model.dart]`). The success closure also calls `isErrorData` (`@0x4369748`) on the model before it completes the future.

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::AutoDisasterDetailModel`): `uuid` (String?), `event` (String?), `start` (int?), `end` (int?).

`AutoDisasterDetailModel.isErrorData` (`charging/model/a5101/auto_disaster_detail_model.dart @0x43697a0`) is true when the tagged field `field_f` (`start`) is 0 (`cbnz` `@0x43697a8`) or `field_13` (`end`) is 0 (`cbz` `@0x43697bc`); the success closure calls it right after `fromJson` (`charging/http/http_request_repository_impl.dart @0x4369748`).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "station_id": "<station_id>",
  "unix": "<unix>",
  "near_field": "<near_field>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getAutoDisasterPrepareDetail` @0x43694a4 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::getAutoDisasterPrepareDetail`
- `charging/ui/page/family/auto_disaster/auto_disaster_tips_logic.dart::clickAutoDisasterTips`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call. — reclassified: device test row 150 (traced 2026-10-20: per call the SDK login state `AkIotKitFlutter::isLogin` and the base-URL predicate decide, `HttpEncryptionDecorator.dart @0x4869504`, `@0x4869544`; the predicate is a GDT dispatch whose selector the asm does not name, and the login state is runtime data)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
