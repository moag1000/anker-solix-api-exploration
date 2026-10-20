> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# set_station_evchargers

## Purpose

Binds EV chargers to a station or unbinds them (callers `AddEvChargerLogic::pushToStation`, `EvChargerManagerLogic::unBindEvCharger` and the load-balancing station logic of the EV charger package); two senders were read, `HttpRequestControllerImpl::bindUnX1Charger` and the SDK command `AKIotEVChargeCommand::setStationEvChargers` (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/set_station_evchargers` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x226c47c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x226c474`, in `HttpRequestControllerImpl::bindUnX1Charger` (`charging/http/http_request_repository_impl.dart @0x226c334`), sent through `encryptionRequestHttp` (`@0x226c4a4`).

Second sender (SDK path, no `Method` object): `AKIotEVChargeCommand::setStationEvChargers` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x3961580`) wraps the body in a map with the string `path` = `charging_hes_svc/set_station_evchargers` (key `@0x396176c`, value `@0x3961774`), the string `method` = `POST` (key `@0x3961780`, value `@0x3961788`) and `param` (key `@0x3961798`), and passes it to `handle` with the identifier `akiot.cloud_api` (`@0x39617c0`, call `@0x39617d0`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- `encryptionRequestHttp` forwards `needEncryption` with its default true to `requestHttp` (`api/encryption.md`): `HttpRequestControllerImpl::bindUnX1Charger` (`charging/http/http_request_repository_impl.dart`, call `@0x226c4a4`).

## Request

First sender `HttpRequestControllerImpl::bindUnX1Charger` (`charging/http/http_request_repository_impl.dart @0x226c334`): 4 keys in a map literal with type arguments `<String, dynamic>` (`@0x226c3dc`), which do not type the values (all stored as received, `@0x226c39c`..`@0x226c3d8`), then `elbFlag` and `greenproFlag` are added with `[]=` as the constant `true` (`@0x226c410`, `@0x226c438`) only when the `deleteFlag` parameter is false (`tbz w0, #4` `@0x226c3f4` skips both when it is true). Second sender `AKIotEVChargeCommand::setStationEvChargers` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x3961580`): the same keys in a `<String, dynamic>` literal (`@0x39616dc`), with `evChargers` built as a one-element growable list of strings (`<String>` `@0x39616a4`, length `@0x39616bc`) and `elbFlag` and `greenproFlag` added unconditionally as `true` (`@0x3961708`, `@0x3961730`); the body is wrapped in `{path, method, param}` (below).

| field | type | required | example | source |
|---|---|---|---|---|
| `stationId` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x226c38c` |
| `evChargers` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x226c3a0`; `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x3961684`;  `@0x39616a4` |
| `deleteFlag` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x226c3b4` |
| `forceBindFlag` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x226c3c8` |
| `elbFlag` | bool | optional (first sender: only when `deleteFlag` is false) | `true` | `charging/http/http_request_repository_impl.dart @0x226c404` |
| `greenproFlag` | bool | optional (first sender: only when `deleteFlag` is false) | `true` | `charging/http/http_request_repository_impl.dart @0x226c42c` |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the senders (asm-traced): the success closure of `bindUnX1Charger` (`charging/http/http_request_repository_impl.dart @0x226c4c0`) passes the empty string to the callback stored in the context (`r16 = ""` `@0x226c4ec`, `ClosureCall` `@0x226c4f4`) and reads no key; `AKIotEVChargeCommand::setStationEvChargers` returns the result of `handle` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x39617d0`) without reading it in the same function.

## Response

No response key is read in the senders.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "stationId": "<stationId>",
  "evChargers": "<evChargers>",
  "deleteFlag": "<deleteFlag>",
  "forceBindFlag": "<forceBindFlag>",
  "elbFlag": "<elbFlag>",
  "greenproFlag": "<greenproFlag>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `bindUnX1Charger` @0x226c334 (encryptionRequestHttp; encrypted: true)
- `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart`: `setStationEvChargers` @0x3961580 (URL literal only, no `*Http*` call; sends in the same function (`AKIoTKitManagerImpl::handle`); resolved from the URL literal at `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x3961774` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))

Called from:

- `charging/http/http_request_repository.dart::bindUnX1Charger`
- `charging/ui/page/device/a5101/setting/device_manager/ev_charger/add_ev_charger_logic.dart::pushToStation`
- `charging/ui/page/device/a5101/setting/device_manager/ev_charger/ev_charger_manager_logic.dart::unBindEvCharger`
- `ev_charger/src/ev_charger/page/home/load_balancing/load_balancing_logic.dart::_executeStationDisconnect`
- `ev_charger/src/ev_charger/page/home/load_balancing/select_station/evselect_station_logic.dart::_executeSetStationEvChargers`
- `ev_charger/src/ev_charger/page/home/load_balancing/select_station/evselect_station_logic.dart::removeFromStationAndBind`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The types of `stationId`, `evChargers`, `deleteFlag` and `forceBindFlag` in the first sender: the map is `<String, dynamic>` and the values are parameters stored without conversion.
- Whether the server treats `elbFlag` and `greenproFlag` as filters on the bound chargers: only the keys and the constant `true` were read.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
