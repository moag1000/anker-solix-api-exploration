> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_extender_system_detail

## Purpose

Reads the detail of one range-extender system (`RangeExtenderNetwork::getExtenderSystemDetail`, `oe_a7320`); the callers are listed under "Callers in app"; the description itself comes from the function name (string-only).

## Upstream name

`get_extender_system_detail` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/get_extender_system_detail` (asm-traced): the builder `RangeExtenderNetwork::getExtenderSystemDetail` (`oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x2290fb0`) loads the path string at `@0x2291010` and calls `AkNetwork::requestHttp` (`@0x2291020`); that function builds the SDK command map with the literal `"POST"` (`base_service/util/ak_util/src/ak_network.dart @0x21c34fc`) and hands it to the handler `akiot.cloud_api` (`handle`, `@0x21c3544`). There is no `Method` object on this path.

## Encrypted?

Direct SDK call, path C (asm-traced), through the shared helper `AkNetwork::requestHttp`: the helper always sends `POST` and calls `handle` with `akiot.cloud_api` (`base_service/util/ak_util/src/ak_network.dart @0x21c3544`). The inventory flag `default-true (requestHttp)` does not apply: `AkNetwork::requestHttp` has no `needEncryption` switch and goes straight to the SDK; what the SDK encrypts is not visible in Dart (mechanics: [../../sdk_senders.md](../../sdk_senders.md#aknetworkrequesthttp), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)). The builder calls the helper at `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x2291020`.

## Request

(asm-traced) The body is one map literal passed as the named argument `params` (`r4 = const [0, 0x2, 0x1, 0x1, params, 0x1, null]` at `@0x2291018`); its type arguments are `<String, dynamic>` (`@0x2291000`), so the literal gives no value type.

Typing (two-hop, asm-traced): in `range_extender_network.dart` the builder's parameter is untyped (`SetupParameters(dynamic _ ...)`, `@0x2290fbc`); the type is read at the caller `ManageDevicesLogic.refreshData` (`oe_a7320/src/oe_a7320/page/range_extender_settings/manage_devices/manage_devices_logic.dart @0x2adcbb0`): the argument is a nullable value that is replaced by the String literal `""` when null (`r2 = ""` `@0x2adcb9c`, pool string `[pp+0xb00]`), so the field is a string.

| field | type | required | example | source |
|---|---|---|---|---|
| `extender_system_id` | string | yes | | `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x2290fec` |

## `param_type`/`cmd`

n/a

## Response model (link)

- `oe_a7320::RangeExtenderSystemDetailModel`, parsed by `RangeExtenderSystemDetailModel.fromJson` at `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x2291054`

## Response

(asm-traced) For each sender that parses a model, the keys below are the top-level keys of the model; that sender adds no wrapper fields of its own in the code read.

- `RangeExtenderSystemDetailModel` top-level keys (`data/models.json`, `oe_a7320::RangeExtenderSystemDetailModel`): `extender_system_id` (String?), `extender_system_name` (String?), `extender_system_img` (String?), `total_power_generation` (int?), `consumption_gas` (int?), `consumption_lpg` (int?), `consumption_ng` (int?), `device_list` (unknown), `extender_system_params` (RangeExtenderStrategyParamsModel?) (the extractor also lists an element-parser entry `[Class]` of type List, omitted here).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "extender_system_id": "<extender_system_id>"
}
```

Response: not synthesized (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `ManageDevicesLogic.refreshData` (`oe_a7320/src/oe_a7320/page/range_extender_settings/manage_devices/manage_devices_logic.dart @0x2adcbb0`)
- `ReSystemStatusController._getSystemDetail` (`oe_a7320/src/oe_a7320/page/range_extender_system/controller/re_system_status_controller.dart @0x22a2470`)
- `ReSystemBiz._syncExtendedRangeStrategy` (`oe_a7320/src/oe_a7320/biz/re_system_biz.dart @0x228fb34`)
- `ReSystemBiz._syncExtendedRangeRelsOnlyGeneratorOnline` (`oe_a7320/src/oe_a7320/biz/re_system_biz.dart @0x2292880`)
- `ReSystemBiz.closeExtendedRangeStrategy` (`oe_a7320/src/oe_a7320/biz/re_system_biz.dart @0x4975688`)
- `A1782DeviceLogic.refreshExtenderSystemState` (`charging/ui/page/device/a1782/home/a1782_home_logic.dart @0x3578c38`)
- `A1790homeLogic.refreshExtenderSystemState` (`charging/ui/page/device/a1790/a1790home_logic.dart @0x2868774`)
- `oe_a7320/src/oe_a7320/network/range_extender_network.dart`: `getExtenderSystemDetail` @0x2290fb0 (`AkNetwork.requestHttp`, path C)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The element structure of `device_list` (the model lists it as `unknown`). — reclassified: server (not visible in the app: the model keeps it untyped)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
