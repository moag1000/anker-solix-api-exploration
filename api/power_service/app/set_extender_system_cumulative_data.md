> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# set_extender_system_cumulative_data

## Purpose

Uploads the accumulated energy data of a range-extender system (`RangeExtenderNetwork::setExtenderSystemCumulativeData`, `oe_a7320`); the callers are listed under "Callers in app"; the description itself comes from the function name (string-only).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/set_extender_system_cumulative_data` (asm-traced): the builder `RangeExtenderNetwork::setExtenderSystemCumulativeData` (`oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x33b8ce8`) loads the path string at `@0x33b8d9c` and calls `AkNetwork::requestHttp` (`@0x33b8dac`); that function builds the SDK command map with the literal `"POST"` (`base_service/util/ak_util/src/ak_network.dart @0x21c34fc`) and hands it to the handler `akiot.cloud_api` (`handle`, `@0x21c3544`). There is no `Method` object on this path.

## Encrypted?

Direct SDK call, path C (asm-traced), through the shared helper `AkNetwork::requestHttp`: the helper always sends `POST` and calls `handle` with `akiot.cloud_api` (`base_service/util/ak_util/src/ak_network.dart @0x21c3544`). The inventory flag `default-true (requestHttp)` does not apply: `AkNetwork::requestHttp` has no `needEncryption` switch and goes straight to the SDK; what the SDK encrypts is not visible in Dart (mechanics: [../../sdk_senders.md](../../sdk_senders.md#aknetworkrequesthttp), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)). The builder calls the helper at `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x33b8dac`.

## Request

(asm-traced) The body is one map literal passed as the named argument `params` (`r4 = const [0, 0x2, 0x1, 0x1, params, 0x1, null]` at `@0x33b8da4`); its type arguments are `<String, dynamic>` (`@0x33b8d70`), so the literal gives no value type. Values come from parameters or object fields of the builder; the asm carries no static type.

| field | type | required | example | source |
|---|---|---|---|---|
| `extender_system_id` | ? | yes | ? | `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x33b8d5c` |
| `total_power_generation` | int (declared `int?`) | optional (null-guarded, `@0x33b8e7c`) | | `oe_a7320/src/oe_a7320/network/models/src/extender_system_cumulative_data.dart @0x33b8e90` |
| `consumption_gas` | int (declared `int?`) | optional (null-guarded, `@0x33b8eb4`) | | `extender_system_cumulative_data.dart @0x33b8ec8` |
| `consumption_lpg` | int (declared `int?`) | optional (null-guarded, `@0x33b8eec`) | | `extender_system_cumulative_data.dart @0x33b8f00` |
| `consumption_ng` | int (declared `int?`) | optional (null-guarded, `@0x33b8f24`) | | `extender_system_cumulative_data.dart @0x33b8f38` |

The four lower rows are the keys of `ExtenderSystemCumulativeDataModel::toJson` (`oe_a7320/src/oe_a7320/network/models/src/extender_system_cumulative_data.dart @0x33b8e3c`); each is written only when the model field is not null. Their types are the declared `int?` of the model fields (`data/models.json`, `oe_a7320::ExtenderSystemCumulativeDataModel`); the width of the stored number is not shown by `toJson`. The builder merges the map into the body with `addAll` (`range_extender_network.dart @0x33b8d84`, `@0x33b8d90`).

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the builder awaits `AkNetwork::requestHttp` (`@0x33b8dac`) and returns `Future<void?>`; it reads no key.

## Response

No response key is read.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "extender_system_id": "<?>"
}
```

Response: not synthesized (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `RangeExtenderSystemLogic.onClose` (`oe_a7320/src/oe_a7320/page/range_extender_system/range_extender_system_logic.dart @0x33b8cbc`)
- `RangeExtenderSystemLogic.onPaused` (`oe_a7320/src/oe_a7320/page/range_extender_system/range_extender_system_logic.dart @0x3afc048`)
- `oe_a7320/src/oe_a7320/network/range_extender_network.dart`: `setExtenderSystemCumulativeData` @0x33b8ce8 (`AkNetwork.requestHttp`, path C)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Type of `extender_system_id`: `RangeExtenderSystemLogic.onClose` and `onPaused` pass `field_43?.field_2f ?? field_57` of the logic object (`range_extender_system_logic.dart @0x33b8c74..@0x33b8c90`) — attempted 2026-10-20 (two-hop not readable: the field types are not shown in the asm (`range_extender_system_logic.dart @0x33b8c90`)). Header stays string-only.

## Device-tested by

none
