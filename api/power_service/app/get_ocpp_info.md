> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_ocpp_info

## Purpose

Reads which OCPP endpoint source a charger is linked to (source number, timestamp, time zone); the charging sessions screen and the OCPP settings use it.

## Upstream name

`get_device_ocpp_info` (upstream-confirmed, `api/apitypes.py` line 151; upstream comment: "works as member also for empty device SN, {\"device_sn\": deviceSn}, list device endpoint source number, default 0 if nothing found explicitly? (Useful only for EV charger devices)").

## Method+URL

`POST /power_service/v1/app/get_ocpp_info` (asm-traced). Sender: `OcppNetwork.getOcppInfo` (`ev_charger/src/ev_charger/page/home/setting/ocpp/network/ocpp_network.dart @0x284ad24`); the path literal is loaded at `@0x284adfc` and passed to `AkNetwork.requestHttp` (`@0x284ae0c`) with the named argument `params` (`r4 = const [0, 0x2, 0x1, 0x1, params, 0x1, null]`, `@0x284ae04`); the method is fixed to `POST` inside the helper.

## Encrypted?

Direct SDK call, path C (asm-traced), through the shared helper `AkNetwork.requestHttp` (`ocpp_network.dart`, call `@0x284ae0c`): the helper always sends `POST` and calls `handle` with `akiot.cloud_api` (`base_service/util/ak_util/src/ak_network.dart @0x21c3544`). The inventory row says `encrypted: false` with the note "plain callee; callee default needEncryption=true"; that note does not apply, because `AkNetwork.requestHttp` has no `needEncryption` switch and goes straight to the SDK (mechanics: [../../sdk_senders.md](../../sdk_senders.md#aknetworkrequesthttp), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a `<String, dynamic>` map built at `@0x284adb4` to `@0x284adbc` (`r2 = 4`, one pair).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | String | yes | `<device sn>` | `ocpp_network.dart @0x284ada0`; the value is the first argument (`@0x284adac`); upstream-confirmed (`apitypes.py` line 151) |
| `address` | String | no | `wss://ocpp.example/charger` | `ocpp_network.dart @0x284ade4`; added with `[]=` only when the optional named argument `address` is not null (`cmp w4, NULL` `@0x284adcc`) |

Upstream notes that the call also works with an empty device serial (it then reports source 0, default).

## `param_type`/`cmd`

n/a

## Response model (link)

`OCPPServerLinkInfoModel` ([../../../models/ev_charger_device_models.md](../../../models/ev_charger_device_models.md#ocppserverlinkinfomodel)): the sender allocates the model and calls `OCPPServerLinkInfoModel.fromJson` on the helper's result map (`ocpp_network.dart @0x284ae30`, `@0x284ae40`); return type `Future<OCPPServerLinkInfoModel?>` (`@0x284ad80`).

## Response

A null result gives `null` (`@0x284ae20` to `@0x284ae28`); an exception is logged as `getOcppInfo error: ...` (`@0x284ae9c`).

| field | type | required | example | source |
|---|---|---|---|---|
| `source`, `timestamp`, `time_zone` | int?, int?, String? | no | `{ "source": 0, "timestamp": 1760000000, "time_zone": "UTC+02:00" }` | `ocpp_server_link_info_model.dart @0x284afcc`, `@0x284b050`, `@0x284b0d8`; [model page](../../../models/ev_charger_device_models.md#ocppserverlinkinfomodel) |

## Example request/response

Request, synthesized

```json
{ "device_sn": "<device sn>" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../encryption.md](../../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `ChargeSessionsLogic._fetchOCPPInfo` (`ev_charger/src/ev_charger/page/home/charge_sessions/charge_sessions_logic.dart @0x2a42088`)
- `OcppBiz._init` (`ev_charger/src/ev_charger/page/home/setting/ocpp/biz/ocpp_biz.dart @0x284a338`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x84030`); the sender is not compared function by function. Not new in 3.24.3: the Task 3.1b inventory change (slashless URL literals) made the URL visible. 3.24.3: present. since: ≤3.18.0.

## Known unknowns

- The unit of `timestamp` and the format of `time_zone` are not shown by the model.
- Whether `address` selects the endpoint to query or the one to set is not known; the sender only reads the answer.

## Device-tested by

none
