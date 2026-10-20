> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# quit_auto_disaster_prepare

## Purpose

Quits the auto disaster-preparedness mode of a station (callers `AutoDisasterTipsLogic::_quitAutoDisasterPrepareFromNet` and `onMessageDispatch`, through `HttpRequestControllerImpl::quitAutoDisasterPrepare`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/quit_auto_disaster_prepare` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x27ad66c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x27ad664`, in `HttpRequestControllerImpl::quitAutoDisasterPrepare` (`charging/http/http_request_repository_impl.dart @0x27ad518`), sent through `requestHttp` (`@0x27ad690`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `HttpRequestControllerImpl::quitAutoDisasterPrepare` (`charging/http/http_request_repository_impl.dart`, call `@0x27ad690`, argument list `@0x27ad688`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

`HttpRequestControllerImpl::quitAutoDisasterPrepare` (`charging/http/http_request_repository_impl.dart @0x27ad518`) stores 3 keys in a map literal with type arguments `<String, Object>` (`@0x27ad620`), which do not type the values. `unix` is boxed from an unboxed 64-bit integer (`BoxInt64Instr` `@0x27ad5f4`), so it is an integer; `station_id` and `far_field` are stored as received (`@0x27ad5e0`, `@0x27ad61c`). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | string | yes |  | `charging/http/http_request_repository_impl.dart @0x27ad5d0` |
| `unix` | int (unboxed, x) | yes |  | `charging/http/http_request_repository_impl.dart @0x27ad5e4` |
| `far_field` | bool | yes |  | `charging/http/http_request_repository_impl.dart @0x27ad60c` |

Callers (app side, traced 2026-10-20): `AutoDisasterTipsLogic::onMessageDispatch` (`charging/ui/page/family/auto_disaster/auto_disaster_tips_logic.dart @0x27acb48`) passes the constant `false` (`r2 = false` `@0x27acb40`) and `_quitAutoDisasterPrepareFromNet` (`@0x4369fec`..`@0x436a034`) passes the constant `true` (`@0x436a030`) as the first argument, which the sender stores as `far_field`, so it is a bool; both callers pass `stationId()` and `unix()` as the other two. `station_id` is the return value of `AutoDisasterTipsLogic::stationId` (`charging/ui/page/family/auto_disaster/auto_disaster_tips_logic.dart @0x23cd140`), which returns `field_7` of the value of `field_7f` of `Get.find<StationMainPageLogic>()` (`@0x23cd188`..`@0x23cd198`) or the empty string when null (`@0x23cd1a8`); `field_7` of that station model is the `String?` documented on [device_command.md](device_command.md#request), so the key is a string (two-hop, declared type read). `unix` is the getter `AutoDisasterTipsLogic::unix` (`@0x27ada3c`): `_getCurrentMicros` (`@0x27ada50`) divided twice by 1000 (`sdiv` `@0x27ada78`, `@0x27ada7c`, unboxed), the current time of the app clock in seconds. What the two values select on the server is not known from the app; the sibling key of [get_auto_disaster_prepare_detail.md](get_auto_disaster_prepare_detail.md) is `near_field`, a bool built from a negated field.

## `param_type`/`cmd`

n/a

## Response model (link)

- [`AutoDisasterQuitPrepareModel`](../../models/hes.md#autodisasterquitpreparemodel), parsed by `AutoDisasterQuitPrepareModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x27ad7b0` (success closure `@0x27ad744`, `bl` target `[package:charging/model/a5101/auto_disaster_quit_prepare_model.dart]`).

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::AutoDisasterQuitPrepareModel`): `success` (bool?), `message_id` (String?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "station_id": "<station_id>",
  "unix": "<unix>",
  "far_field": "<far_field>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`. The failure closure (`charging/http/http_request_repository_impl.dart @0x27ad6a4`) logs the code and message and completes the pending future with null (`@0x27ad728`) without comparing the code.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `quitAutoDisasterPrepare` @0x27ad518 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::quitAutoDisasterPrepare`
- `charging/ui/page/family/auto_disaster/auto_disaster_tips_logic.dart::_quitAutoDisasterPrepareFromNet`
- `charging/ui/page/family/auto_disaster/auto_disaster_tips_logic.dart::onMessageDispatch`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What `far_field` and the sibling key `near_field` select on the server: the app sends `far_field` = `true` from `_quitAutoDisasterPrepareFromNet` and `false` from `onMessageDispatch` (see Request); the meaning of the two values is not visible in the app — traced 2026-10-20.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call. — reclassified: device test row 150 (traced 2026-10-20: per call the SDK login state `AkIotKitFlutter::isLogin` and the base-URL predicate decide, `HttpEncryptionDecorator.dart @0x4869504`, `@0x4869544`; the predicate is a GDT dispatch whose selector the asm does not name, and the login state is runtime data)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
