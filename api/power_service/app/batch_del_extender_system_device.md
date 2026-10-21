> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# batch_del_extender_system_device

## Purpose

Removes devices from a range-extender system (`RangeExtenderNetwork::batchDelExtenderSystemDevice`, `oe_a7320`); the description comes from the function name (string-only); the callers are listed under "Callers in app".

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/batch_del_extender_system_device` (asm-traced): the builder `RangeExtenderNetwork::batchDelExtenderSystemDevice` (`oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x3a223b0`) loads the path string at `@0x3a2242c` and calls `AkNetwork::requestHttp` (`@0x3a2243c`); that function builds the SDK command map with the literal `"POST"` (`base_service/util/ak_util/src/ak_network.dart @0x21c34fc`) and hands it to the handler `akiot.cloud_api` (`handle`, `@0x21c3544`). There is no `Method` object on this path.

## Encrypted?

Direct SDK call, path C (asm-traced), through the shared helper `AkNetwork::requestHttp`: the helper always sends `POST` and calls `handle` with `akiot.cloud_api` (`base_service/util/ak_util/src/ak_network.dart @0x21c3544`). The inventory flag `default-true (requestHttp)` does not apply: `AkNetwork::requestHttp` has no `needEncryption` switch and goes straight to the SDK; what the SDK encrypts is not visible in Dart (mechanics: [../../sdk_senders.md](../../sdk_senders.md#aknetworkrequesthttp), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)). The builder calls the helper at `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x3a2243c`.

## Request

(asm-traced) The body is one map literal passed as the named argument `params` (`r4 = const [0, 0x2, 0x1, 0x1, params, 0x1, null]` at `@0x3a22434`); its type arguments are `<String, dynamic>` (`@0x3a2241c`), so the literal gives no value type.

Typing (two-hop, asm-traced): in `range_extender_network.dart` the builder's two parameters are untyped (`SetupParameters(dynamic _, dynamic _ ...)`). `device_sn_list` is typed at the caller `ReSystemUnbindTools._unbindFromCloud` (`oe_a7320/src/oe_a7320/page/range_system_create/unbind_tools/re_system_unbind_tools.dart @0x43148e8`): a one-element growable list with type argument `<String>` (`@0x43148c8`, `AllocateGrowableArray` `@0x43148cc`); the other caller, `ManageDevicesLogic._batchDeleteDevices` (`manage_devices_logic.dart @0x3a22340`), passes a closure-context field. `extender_system_id` is a `field_f` read of the unbind-tools object (`@0x43148e4`) and keeps `?`.

| field | type | required | example | source |
|---|---|---|---|---|
| `extender_system_id` | ? | yes | ? | `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x3a223f4` |
| `device_sn_list` | list (`<String>` growable list at one caller) | yes | | `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x3a22408` |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the builder awaits `AkNetwork::requestHttp` (`@0x3a2243c`), only logs the strings `"batchDelExtenderSystemDevice=="` and the result (`@0x3a2245c..`) and reads no key.

## Response

No response key is read.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "extender_system_id": "<?>",
  "device_sn_list": "<?>"
}
```

Response: not synthesized (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `ManageDevicesLogic._batchDeleteDevices` (`oe_a7320/src/oe_a7320/page/range_extender_settings/manage_devices/manage_devices_logic.dart @0x3a22340`)
- `ReSystemUnbindTools._unbindFromCloud` (`oe_a7320/src/oe_a7320/page/range_system_create/unbind_tools/re_system_unbind_tools.dart @0x43148e8`)
- `oe_a7320/src/oe_a7320/network/range_extender_network.dart`: `batchDelExtenderSystemDevice` @0x3a223b0 (`AkNetwork.requestHttp`, path C)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Type of `extender_system_id`: a `field_f` read of `ReSystemUnbindTools` (`re_system_unbind_tools.dart @0x43148e4`) and a closure-context field in `ManageDevicesLogic._batchDeleteDevices` (`@0x3a22338`) — attempted 2026-10-20 (two-hop not readable: both callers pass fields whose declared type is not shown in the asm (`re_system_unbind_tools.dart @0x43148e4`, `manage_devices_logic.dart @0x3a22338`)). Header stays string-only.

## Device-tested by

none
