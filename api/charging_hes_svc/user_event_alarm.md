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
| `station_id` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x23ce3e8` |
| `pn` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x23ce3fc` |
| `language` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x23ce410` |
| `event` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x23ce424` |

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

- The types of all four keys: the values are parameters stored without conversion.
- What `event` carries (an event name or number): the callers were not decoded.
- The failure handling: the failure callback could not be read.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
