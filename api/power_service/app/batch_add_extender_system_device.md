> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# batch_add_extender_system_device

## Purpose

Adds devices to an existing range-extender system (`RangeExtenderNetwork::batchAddExtenderSystemDevice`, `oe_a7320`); the description comes from the function name (string-only); the callers are listed under "Callers in app".

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/batch_add_extender_system_device` (asm-traced): the builder `RangeExtenderNetwork::batchAddExtenderSystemDevice` (`oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x43168f0`) loads the path string at `@0x431696c` and calls `AkNetwork::requestHttp` (`@0x431697c`); that function builds the SDK command map with the literal `"POST"` (`base_service/util/ak_util/src/ak_network.dart @0x21c34fc`) and hands it to the handler `akiot.cloud_api` (`handle`, `@0x21c3544`). There is no `Method` object on this path.

## Encrypted?

Direct SDK call, path C (asm-traced), through the shared helper `AkNetwork::requestHttp`: the helper always sends `POST` and calls `handle` with `akiot.cloud_api` (`base_service/util/ak_util/src/ak_network.dart @0x21c3544`). The inventory flag `default-true (requestHttp)` does not apply: `AkNetwork::requestHttp` has no `needEncryption` switch and goes straight to the SDK; what the SDK encrypts is not visible in Dart (mechanics: [../../sdk_senders.md](../../sdk_senders.md#aknetworkrequesthttp), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)). The builder calls the helper at `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x431697c`.

## Request

(asm-traced) The body is one map literal passed as the named argument `params` (`r4 = const [0, 0x2, 0x1, 0x1, params, 0x1, null]` at `@0x4316974`); its type arguments are `<String, dynamic>` (`@0x431695c`), so the literal gives no value type.

Typing (two-hop, asm-traced): in `range_extender_network.dart` the builder's two parameters are untyped (`SetupParameters(dynamic _, dynamic _ ...)`); `device_list` is typed at the caller `ReSystemCreateLogic.createOrUpateExtenderSystem` (`oe_a7320/src/oe_a7320/page/range_system_create/re_system_create_logic.dart @0x4316074`), which passes the result of `_creattingDeviceJsonList` (`@0x4316014`): a growable list with type argument `<Map<String, dynamic>>` (`@0x4316a28`, `_GrowableList` `@0x4316a30`). `extender_system_id` is passed from a null-checked field read (`field_67`, `@0x4316058`, `@0x4316064`) and keeps `?`.

| field | type | required | example | source |
|---|---|---|---|---|
| `extender_system_id` | ? | yes | ? | `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x4316934` |
| `device_list` | list (`<Map<String, dynamic>>` growable list built by the caller) | yes | | `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x4316948` |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the builder awaits `AkNetwork::requestHttp` and returns without indexing the result (no key string or `fromJson` after `Await` in `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x43168f0..`).

## Response

No response key is read.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "extender_system_id": "<?>",
  "device_list": ["<object>"]
}
```

Response: not synthesized (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `ReSystemCreateLogic.createOrUpateExtenderSystem` (`oe_a7320/src/oe_a7320/page/range_system_create/re_system_create_logic.dart @0x4316074`)
- `oe_a7320/src/oe_a7320/network/range_extender_network.dart`: `batchAddExtenderSystemDevice` @0x43168f0 (`AkNetwork.requestHttp`, path C)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Type of `extender_system_id`: the only caller passes a `field_67` read of `ReSystemCreateLogic` (`re_system_create_logic.dart @0x4316058`) and the asm carries no field declaration — attempted 2026-10-20 (two-hop not readable: `re_system_create_logic.dart @0x4316058`, field type not shown in the asm). Header stays string-only.

## Device-tested by

none
