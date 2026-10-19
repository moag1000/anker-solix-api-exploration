> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# set_station_evchargers

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_svc/set_station_evchargers`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x226c47c`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `stationId` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x226c334` |
| `evChargers` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x226c334` |
| `deleteFlag` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x226c334` |
| `forceBindFlag` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x226c334` |
| `path` | ? | ? | ? | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x3961580` |
| `method` | ? | ? | ? | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x3961580` |
| `param` | ? | ? | ? | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x3961580` |

Rows are the union over 2 senders; `source` is the first sender that sets the key.

## `param_type`/`cmd`

n/a

## Response model (link)

<!-- TODO -->

## Response

<!-- TODO -->

## Example request/response

<!-- TODO -->

## Errors seen

`api/errors.md`: <!-- TODO -->

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `bindUnX1Charger` @0x226c334 (encryptionRequestHttp; encrypted: true)
- `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart`: `setStationEvChargers` @0x3961580 (URL literal only, no `*Http*` call)

Called from:

- `charging/http/http_request_repository.dart::bindUnX1Charger`
- `charging/ui/page/device/a5101/setting/device_manager/ev_charger/add_ev_charger_logic.dart::pushToStation`
- `charging/ui/page/device/a5101/setting/device_manager/ev_charger/ev_charger_manager_logic.dart::unBindEvCharger`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
