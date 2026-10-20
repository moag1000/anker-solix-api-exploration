> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# user_event_alarm

## Purpose

Reports an auto disaster-preparedness event of a station (callers `AutoDisasterTipsLogic::enterLowPowerEvent` and `updateSpecialEvent`, through `HttpRequestControllerImpl::reportHesEvents`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/user_event_alarm` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x23ce484`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x23ce47c`, in `HttpRequestControllerImpl::reportHesEvents` (`charging/http/http_request_repository_impl.dart @0x23ce394`), sent through `requestHttp` (`@0x23ce4a8`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `HttpRequestControllerImpl::reportHesEvents` (`charging/http/http_request_repository_impl.dart`, call `@0x23ce4a8`, argument list `@0x23ce4a0`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

`HttpRequestControllerImpl::reportHesEvents` (`charging/http/http_request_repository_impl.dart @0x23ce394`) stores 4 keys in a map literal with type arguments `<String, Object>` (`@0x23ce438`), which do not type the values; all four are stored as received (`@0x23ce3f8`, `@0x23ce40c`, `@0x23ce420`, `@0x23ce434`). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | string | yes |  | `charging/http/http_request_repository_impl.dart @0x23ce3e8` |
| `pn` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x23ce3fc` |
| `language` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x23ce410` |
| `event` | list | yes |  | `charging/http/http_request_repository_impl.dart @0x23ce424` |

Caller arguments (traced 2026-10-20, app side): both callers pass `station_id` from `AutoDisasterTipsLogic::stationId` (`charging/ui/page/family/auto_disaster/auto_disaster_tips_logic.dart`, `@0x23cd028`, `@0x23d4304`; a `String` with the fallback `""`), `language` from `getDefault()` mapped through a constant map of 78 entries with the fallback to the unmapped value (`@0x23cd0c0`..`@0x23cd0f0`, `@0x23d439c`..), `pn` as `field_d3` of the `A5101StationLogic` object with the fallback constant `"A5341"` in `enterLowPowerEvent` (`@0x23cd0ac`) and the constant `"A5101"` in `updateSpecialEvent` (`@0x23d4388`), and `event` as a growable list with the type argument `<Map<String, dynamic>>` and one element (`@0x23cd04c`; `@0x23d4100`..). The element map has the keys `code`, `sn`, `subSn`, `deviceType`, `localTime` and `payLoad` (a map with the key `control`): in `updateSpecialEvent` `code` is a growable `<int>` list with the single value 32 (raw 64 in a 32-bit store, Smi rule, `@0x23d4120`), `deviceType` is `"ems"` (`@0x23d4234`), `sn` and `subSn` are `field_6b` of a device object (`@0x23d4184`..`@0x23d41f0`) and `localTime` is an integer in seconds (`BoxInt64Instr` after `sdiv` `@0x23d40f0`, `@0x23d424c`); in `enterLowPowerEvent` `code` is `field_23` of the parameter object (`@0x23ccf10`) and `deviceType` is `field_13` of it. Both callers pass only the `success` callback (named argument list `@0x23cd11c`), no `fail`.

## `param_type`/`cmd`

n/a

## Response model (link)

- [`A5101EventsSetModel`](../../models/hes.md#a5101eventssetmodel), parsed by `A5101EventsSetModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x23ce518` (success closure `@0x23ce4c4`, `bl` target `[package:charging/model/a5101/auto_disaster_prepare_status_model.dart]`).

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::A5101EventsSetModel`): `events` (unknown).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "station_id": "<station_id>",
  "pn": "<pn>",
  "language": "<language>",
  "event": "<event>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`. The failure callback comes from a pool entry labelled `[dart:ui] _NativeScene::_NativeScene._` (`charging/http/http_request_repository_impl.dart @0x23ce45c`, the same label as in `remove_user_fault_info`), so it could not be read.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `reportHesEvents` @0x23ce394 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::reportHesEvents`
- `charging/ui/page/family/auto_disaster/auto_disaster_tips_logic.dart::enterLowPowerEvent`
- `charging/ui/page/family/auto_disaster/auto_disaster_tips_logic.dart::updateSpecialEvent`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The types of `pn` and `language`: `pn` is a field value with a string constant as fallback and `language` the result of a constant-map lookup with a fallback (see Request); no declared type is read. `station_id` (string) and `event` (list) are typed under Request. — attempted 2026-10-20 (two-hop not readable for `pn`, `language`: `auto_disaster_tips_logic.dart @0x23cd084`, `@0x23cd0c4`)
- The failure handling inside the sender: both callers pass only `success` (see Request), so any failure path is the default of `requestHttp` / the sender and was not read — traced 2026-10-20
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call. — reclassified: device test row 150 (traced 2026-10-20: per call the SDK login state `AkIotKitFlutter::isLogin` and the base-URL predicate decide, `HttpEncryptionDecorator.dart @0x4869504`, `@0x4869544`; the predicate is a GDT dispatch whose selector the asm does not name, and the login state is runtime data)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
