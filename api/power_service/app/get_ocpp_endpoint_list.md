> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_ocpp_endpoint_list

## Purpose

Lists the OCPP back-end endpoints that Anker offers for an EV charger (name, address, certificate, icon and a source number per endpoint); the OCPP settings of the charger use it to let the user pick a server.

## Upstream name

`get_ocpp_endpoint_list` (upstream-confirmed, `api/apitypes.py` line 150; upstream comment: "lists ocpp endpoints used by Anker, including source number per endpoint").

## Method+URL

`POST /power_service/v1/app/get_ocpp_endpoint_list` (asm-traced). Sender: `OcppNetwork.getOcppEndpointList` (`ev_charger/src/ev_charger/page/home/setting/ocpp/network/ocpp_network.dart @0x284a584`); the path literal is loaded at `@0x284a5ac` and passed to `AkNetwork.requestHttp` (`@0x284a5b8`); the method is fixed to `POST` inside the helper (`base_service/util/ak_util/src/ak_network.dart @0x21c34fc`).

## Encrypted?

Direct SDK call, path C (asm-traced), through the shared helper `AkNetwork.requestHttp` (`ocpp_network.dart`, call `@0x284a5b8`): the helper always sends `POST` and calls `handle` with `akiot.cloud_api` (`base_service/util/ak_util/src/ak_network.dart @0x21c3544`). The inventory row says `encrypted: false` with the note "plain callee; callee default needEncryption=true"; that note does not apply, because `AkNetwork.requestHttp` has no `needEncryption` switch and goes straight to the SDK (mechanics: [../../sdk_senders.md](../../sdk_senders.md#aknetworkrequesthttp), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)).

## Request

No body: the call is made without the named argument `params` (`r4 = const [0, 0x1, 0, 0x1, null]`, `@0x284a5b4`), so `param` is `null` in the envelope.

## `param_type`/`cmd`

n/a

## Response model (link)

`OcppListModel` ([../../../models/ev_charger_device_models.md](../../../models/ev_charger_device_models.md#ocpplistmodel)): `OcppListModel.fromJson` is called on the map returned by the helper (`ocpp_network.dart @0x284a5e4`); the function's return type is `Future<OcppListModel?>` (`InitAsync`, `@0x284a5a0`).

## Response

The helper returns the value of the key `data` of the SDK result as a map (`null` when absent); the sender returns `null` for a null result (`@0x284a5cc`). An exception is logged as `getOcppEndpointList error: ...` (`@0x284a61c`) and `null` is returned.

| field | type | required | example | source |
|---|---|---|---|---|
| `list` | list of `OcppItemModel` | no | `[ { "id": 1, "name": "...", "address": "wss://...", "certificate": "...", "icon": "...", "source": 0 } ]` | `ocpp_list_model.dart @0x284a6d0`; item keys `id`, `name`, `address`, `certificate`, `icon`, `source` on the [model page](../../../models/ev_charger_device_models.md#ocppitemmodel) |

## Example request/response

Request, synthesized

```json
{ "path": "power_service/v1/app/get_ocpp_endpoint_list", "method": "POST", "param": null }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../encryption.md](../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../errors.md).

## Callers in app

- `OcppBiz._init` (`ev_charger/src/ev_charger/page/home/setting/ocpp/biz/ocpp_biz.dart @0x284a3d8`)
- `OcppBiz.getInternalOcppServer` (`ocpp_biz.dart @0x284b41c`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x81dc0`); the sender is not compared function by function. Not new in 3.24.3: the inventory learned URL literals without a leading slash, which made the URL visible. 3.24.3: present. since: ≤3.18.0.

## Known unknowns

- The meaning of the `source` number per endpoint (upstream: "source number per endpoint") is not decoded; `get_ocpp_info` returns the source number the charger currently uses.
- Whether the list depends on the account's region is not known.
- No response was captured.

## Device-tested by

none
