> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# set_evcharger_station_feature

## Purpose

Sets the station feature flags of an EV charger inside an HES station: whether the charger takes part in load balancing (`elbFlag`) or in solar-priority charging (`greenproFlag`).

## Upstream name

`none` (no upstream name). Upstream lists the URL without a key in `api/apitypes.py` (line 469, next to `set_station_evchargers`), and has the read side `get_evcharger_station_info` (line 238, upstream comment: "works as member, {\"evChargerSn\": deviceSn, \"featuretype\": 1}, featuretype [1,2]").

## Method+URL

`POST /charging_hes_svc/set_evcharger_station_feature` (asm-traced). Sender: `AKIotEVChargeCommand.setEvChargerHesStationFeature` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart` `@0x3960414`). The path literal has no leading slash (`@0x39605b8`), the method is the string `"POST"` (`@0x39605d0`), and the map keys `path`, `method`, `param` are stored at `@0x39605b0`, `@0x39605c4`, `@0x39605dc`.

## Encrypted?

Direct SDK call, path C (asm-traced): the command function calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ev_charge_command.dart @0x3960604`, call `@0x3960614`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../sdk_senders.md](../sdk_senders.md#the-common-envelope), background: [../encryption.md](../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a `<String, dynamic>` map. The function takes the charger serial, a page-type string and a named flag `isDelete` that defaults to true (`SetupParameters` `@0x3960420`, default `@0x3960468`). It always sends `evChargerSn`; it adds one flag, chosen by the page type, and the flag value is the negation of `isDelete`. For any other page type it sends only `evChargerSn`.

| field | type | required | example | source |
|---|---|---|---|---|
| `evChargerSn` | String | yes | `<charger sn>` | `ev_charge_command.dart @0x3960488`; value is the first argument |
| `elbFlag` | bool | only for page type `pageTypeLoadBalancing` | `true` | `ev_charge_command.dart @0x39604fc` (key), page-type compare string `@0x39604bc`; value `!isDelete` (`tbnz` on `isDelete`, `@0x39604dc` to `@0x39604e8`) |
| `greenproFlag` | bool | only for page type `pageTypeSolarCharging` | `true` | `ev_charge_command.dart @0x3960568` (key), page-type compare string `@0x3960524`; value `!isDelete` (`@0x3960544` to `@0x3960554`) |

So `isDelete: true` (the default, used when a charger is removed from the feature) sends `false`, and `isDelete: false` (adding the charger) sends `true`. The two page-type strings are `pageTypeLoadBalancing` and `pageTypeSolarCharging` (the strings are compared with `==`, `@0x39604d0`, `@0x396053c`). The callers are the load-balancing flows `LoadBalancingLogic.disConnectDevice` and `EvSelectStationLogic._executeSetStationEvChargers`. ELB is read as "energy load balancing" and `greenpro` as the solar-priority (green energy priority) feature from the other names in the same screens; the abbreviations themselves are not expanded in the app.

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): `handle` is called without a type argument.

## Response

Not parsed by the sender.

## Example request/response

Request, synthesized (adding a charger to load balancing)

```json
{ "evChargerSn": "<charger sn>", "elbFlag": true }
```

Request, synthesized (removing a charger from solar-priority charging)

```json
{ "evChargerSn": "<charger sn>", "greenproFlag": false }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../encryption.md](../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `LoadBalancingLogic.disConnectDevice` (`ev_charger/src/ev_charger/page/home/load_balancing/load_balancing_logic.dart @0x395fd68`)
- `EvSelectStationLogic._executeSetStationEvChargers` (`ev_charger/src/ev_charger/page/home/load_balancing/select_station/evselect_station_logic.dart @0x3964f04`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x83000`; the function is `setEvChargerHesStationFeature`); the sender function has the same sequence of string, integer and type literals in 3.18.0 (compared with a throwaway script, not committed). Not new in 3.24.3: the Task 3.1b inventory change (slashless URL literals) made the URL visible, nothing changed in the app. 3.24.3: present, unchanged. since: ≤3.18.0.

## Known unknowns

- The server-side meaning of the two flags and whether other `featuretype` values exist (upstream's read call has `featuretype` 1 and 2) are not known.

## Device-tested by

none
