> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_station_evchargers

## Purpose

Loads the EV chargers bound to a station for the EV charger manager (`EvChargerManagerLogic::_getBindList` through `HttpRequestControllerImpl::getX1BindChargerList`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_station_evchargers` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x28e0bd4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x28e0bcc`, in `HttpRequestControllerImpl::getX1BindChargerList` (`charging/http/http_request_repository_impl.dart @0x28e0b20`), sent through `encryptionRequestHttp` (`@0x28e0bfc`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- `encryptionRequestHttp` forwards `needEncryption` with its default true to `requestHttp` (`api/encryption.md`): `HttpRequestControllerImpl::getX1BindChargerList` (`charging/http/http_request_repository_impl.dart`, call `@0x28e0bfc`).

## Request

(asm-traced) Each sender stores its keys in one map literal with type arguments `<String, String>` read at the cited address, so every value is a String: `HttpRequestControllerImpl::getX1BindChargerList` (`charging/http/http_request_repository_impl.dart @0x28e0b88`, 1 key). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `stationId` | string | yes | `"<stationId>"` | `charging/http/http_request_repository_impl.dart @0x28e0b74` |

## `param_type`/`cmd`

n/a

## Response model (link)

- [`A5101EvChargerListModel`](../../models/hes.md#a5101evchargerlistmodel), parsed by `A5101EvChargerListModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x2268404` (success closure `@0x22683cc`, `bl` target `[package:charging/model/a5101/a5101_ev_charger_list_model.dart]`). The two callbacks are passed as positional arguments (the argument list `@0x28e0bf4` names only `showLoading`); the closure holding the parse is shared (identical code folded) with `getX1BindUserUnbindChargerList`, takes the response as `Map<String, dynamic>` and hands the model to the callback stored in the builder context (`LoadField` `@0x226840c`).

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::A5101EvChargerListModel`): `evChargers` (List), `userBindEvChargersCount` (int?).

App side use (traced 2026-10-20): the success callback of `EvChargerManagerLogic::_getBindList` (`charging/ui/page/device/a5101/setting/device_manager/ev_charger/ev_charger_manager_logic.dart`, sender call `@0x28e0aa4`, closure `@0x28e0c18`) reads `evChargers` (`field_7`) and appends all elements to a list field of the logic (`addAll` `@0x28e0c68`) that the function first cleared (`clear` `@0x28e0a5c`), then sets an observable (`value=` `@0x28e0cac`). The shared parse closure also serves the sender of [get_user_bind_and_not_in_station_evchargers](get_user_bind_and_not_in_station_evchargers.md), whose page lists the same two model keys.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "stationId": "<stationId>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getX1BindChargerList` @0x28e0b20 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getX1BindChargerList`
- `charging/ui/page/device/a5101/setting/device_manager/ev_charger/ev_charger_manager_logic.dart::_getBindList`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
