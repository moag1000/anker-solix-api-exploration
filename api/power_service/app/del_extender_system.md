> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# del_extender_system

## Purpose

Deletes a range-extender system (`RangeExtenderNetwork::delExtenderSystem`, `oe_a7320`); the description comes from the function name (string-only); the callers are listed under "Callers in app".

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/del_extender_system` (asm-traced): the builder `RangeExtenderNetwork::delExtenderSystem` (`oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x471ce1c`) loads the path string at `@0x471ce78` and calls `AkNetwork::requestHttp` (`@0x471ce88`); that function builds the SDK command map with the literal `"POST"` (`base_service/util/ak_util/src/ak_network.dart @0x21c34fc`) and hands it to the handler `akiot.cloud_api` (`handle`, `@0x21c3544`). There is no `Method` object on this path.

## Encrypted?

Direct SDK call, path C (asm-traced), through the shared helper `AkNetwork::requestHttp`: the helper always sends `POST` and calls `handle` with `akiot.cloud_api` (`base_service/util/ak_util/src/ak_network.dart @0x21c3544`). The inventory flag `default-true (requestHttp)` does not apply: `AkNetwork::requestHttp` has no `needEncryption` switch and goes straight to the SDK; what the SDK encrypts is not visible in Dart (mechanics: [../../sdk_senders.md](../../sdk_senders.md#aknetworkrequesthttp), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)). The builder calls the helper at `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x471ce88`.

## Request

(asm-traced) The body is one map literal passed as the named argument `params` (`r4 = const [0, 0x2, 0x1, 0x1, params, 0x1, null]` at `@0x471ce80`); its type arguments are `<String, dynamic>` (`@0x471ce68`), so the literal gives no value type. Values come from parameters or object fields of the builder; the asm carries no static type.

| field | type | required | example | source |
|---|---|---|---|---|
| `extender_system_id` | ? | yes | ? | `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x471ce54` |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the builder is an async function returning `Future<void?>` (`InitAsync` `@0x471ce3c`) and reads no key from the awaited result.

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

- `RemoveSystemController._handleDeviceRemoval` (`oe_a7320/src/oe_a7320/page/range_extender_settings/menu_controller/remove_system_controller.dart @0x471c9d8`)
- `oe_a7320/src/oe_a7320/network/range_extender_network.dart`: `delExtenderSystem` @0x471ce1c (`AkNetwork.requestHttp`, path C)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Type of `extender_system_id`: the only caller, `RemoveSystemController._handleDeviceRemoval`, passes a null-checked `field_7` of an Rx `value` (`remove_system_controller.dart @0x471c9bc..@0x471c9d4`) — attempted 2026-10-20 (two-hop not readable: the field type is not shown in the asm (`remove_system_controller.dart @0x471c9c0`)).

## Device-tested by

none
