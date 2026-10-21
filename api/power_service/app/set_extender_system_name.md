> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# set_extender_system_name

## Purpose

Renames a range-extender system (`RangeExtenderNetwork::setExtenderSystemName`, `oe_a7320`); the description comes from the function name (string-only); the callers are listed under "Callers in app".

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/set_extender_system_name` (asm-traced): the builder `RangeExtenderNetwork::setExtenderSystemName` (`oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x2d178f4`) loads the path string at `@0x2d17970` and calls `AkNetwork::requestHttp` (`@0x2d17980`); that function builds the SDK command map with the literal `"POST"` (`base_service/util/ak_util/src/ak_network.dart @0x21c34fc`) and hands it to the handler `akiot.cloud_api` (`handle`, `@0x21c3544`). There is no `Method` object on this path.

## Encrypted?

Direct SDK call, path C (asm-traced), through the shared helper `AkNetwork::requestHttp`: the helper always sends `POST` and calls `handle` with `akiot.cloud_api` (`base_service/util/ak_util/src/ak_network.dart @0x21c3544`). The inventory flag `default-true (requestHttp)` does not apply: `AkNetwork::requestHttp` has no `needEncryption` switch and goes straight to the SDK; what the SDK encrypts is not visible in Dart (mechanics: [../../sdk_senders.md](../../sdk_senders.md#aknetworkrequesthttp), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)). The builder calls the helper at `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x2d17980`.

## Request

(asm-traced) The body is one map literal passed as the named argument `params` (`r4 = const [0, 0x2, 0x1, 0x1, params, 0x1, null]` at `@0x2d17978`); its type arguments are `<String, dynamic>` (`@0x2d17960`), so the literal gives no value type. Values come from parameters or object fields of the builder; the asm carries no static type.

| field | type | required | example | source |
|---|---|---|---|---|
| `extender_system_id` | ? | yes | ? | `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x2d17938` |
| `extender_system_name` | ? | yes | ? | `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x2d1794c` |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the builder awaits `AkNetwork::requestHttp` (`@0x2d17980`), logs the result between the strings `"setExtenderSystemName=="` and `"====="` and reads no key.

## Response

No response key is read.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "extender_system_id": "<?>",
  "extender_system_name": "<?>"
}
```

Response: not synthesized (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `SystemNameController.Future<Null> <anonymous closure>` (`oe_a7320/src/oe_a7320/page/range_extender_settings/menu_controller/system_name_controller.dart @0x2d178b0`)
- `oe_a7320/src/oe_a7320/network/range_extender_network.dart`: `setExtenderSystemName` @0x2d178f4 (`AkNetwork.requestHttp`, path C)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Type of `extender_system_id`, `extender_system_name`: the only caller (a closure of `SystemNameController`, `system_name_controller.dart @0x2d178b0`) passes a null-checked field read (`@0x2d1789c`) and `field_f` of its context (`@0x2d178a8`) — attempted 2026-10-20 (two-hop not readable: the field types are not shown in the asm (`system_name_controller.dart @0x2d17894`, `@0x2d178a8`)). Header stays string-only.

## Device-tested by

none
