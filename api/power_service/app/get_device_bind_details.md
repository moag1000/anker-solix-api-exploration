> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_device_bind_details

## Purpose

Reads which range-extender system each device is bound to (`RangeExtenderNetwork::getDeviceBindDetails`, `oe_a7320`); the callers are listed under "Callers in app"; the description itself comes from the function name (string-only).

## Upstream name

`get_device_bind_details` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/get_device_bind_details` (asm-traced): the builder `RangeExtenderNetwork::getDeviceBindDetails` (`oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x228efb0`) loads the path string at `@0x228f010` and calls `AkNetwork::requestHttp` (`@0x228f020`); that function builds the SDK command map with the literal `"POST"` (`base_service/util/ak_util/src/ak_network.dart @0x21c34fc`) and hands it to the handler `akiot.cloud_api` (`handle`, `@0x21c3544`). There is no `Method` object on this path.

## Encrypted?

Direct SDK call, path C (asm-traced), through the shared helper `AkNetwork::requestHttp`: the helper always sends `POST` and calls `handle` with `akiot.cloud_api` (`base_service/util/ak_util/src/ak_network.dart @0x21c3544`). The inventory flag `default-true (requestHttp)` does not apply: `AkNetwork::requestHttp` has no `needEncryption` switch and goes straight to the SDK; what the SDK encrypts is not visible in Dart (mechanics: [../../sdk_senders.md](../../sdk_senders.md#aknetworkrequesthttp), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)). The builder calls the helper at `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x228f020`.

## Request

(asm-traced) The body is one map literal passed as the named argument `params` (`r4 = const [0, 0x2, 0x1, 0x1, params, 0x1, null]` at `@0x228f018`); its type arguments are `<String, dynamic>` (`@0x228f000`), so the literal gives no value type.

Typing (two-hop, asm-traced): in `range_extender_network.dart` the builder's parameter is untyped (`SetupParameters(dynamic _ ...)`, `@0x228efbc`); its only caller, `ReSystemBiz.extenderSystemId` (`oe_a7320/src/oe_a7320/biz/re_system_biz.dart @0x228eef0`), builds the argument as a one-element growable list with type argument `<String>` (`@0x228eecc`, `AllocateGrowableArray` `@0x228eed0`), so the field is a list of strings.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn_list` | list (`<String>` growable list built by the caller) | yes | | `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x228efec` |

## `param_type`/`cmd`

n/a

## Response model (link)

- `oe_a7320::DeviceBindDetailsModel`, parsed by `DeviceBindDetailsModel.fromJson` at `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x228f054`

## Response

(asm-traced) For each sender that parses a model, the keys below are the top-level keys of the model; that sender adds no wrapper fields of its own in the code read.

- `DeviceBindDetailsModel` top-level keys (`data/models.json`, `oe_a7320::DeviceBindDetailsModel`): `result` (unknown), `DeviceBindDetailsModel` (List).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn_list": ["<device_sn>"]
}
```

Response: not synthesized (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `ReSystemBiz.extenderSystemId` (`oe_a7320/src/oe_a7320/biz/re_system_biz.dart @0x228eef0`)
- `oe_a7320/src/oe_a7320/network/range_extender_network.dart`: `getDeviceBindDetails` @0x228efb0 (`AkNetwork.requestHttp`, path C)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns


## Device-tested by

none
