> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# add_extender_system

## Purpose

Creates a range-extender system from a device list and returns its id (`RangeExtenderNetwork::addExtenderSystem`, `oe_a7320`); the callers are listed under "Callers in app"; the description itself comes from the function name (string-only).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/add_extender_system` (asm-traced): the builder `RangeExtenderNetwork::addExtenderSystem` (`oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x4316398`) loads the path string at `@0x43163f4` and calls `AkNetwork::requestHttp` (`@0x4316404`); that function builds the SDK command map with the literal `"POST"` (`base_service/util/ak_util/src/ak_network.dart @0x21c34fc`) and hands it to the handler `akiot.cloud_api` (`handle`, `@0x21c3544`). There is no `Method` object on this path.

## Encrypted?

Direct SDK call, path C (asm-traced), through the shared helper `AkNetwork::requestHttp`: the helper always sends `POST` and calls `handle` with `akiot.cloud_api` (`base_service/util/ak_util/src/ak_network.dart @0x21c3544`). The inventory flag `default-true (requestHttp)` does not apply: `AkNetwork::requestHttp` has no `needEncryption` switch and goes straight to the SDK; what the SDK encrypts is not visible in Dart (mechanics: [../../sdk_senders.md](../../sdk_senders.md#aknetworkrequesthttp), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)). The builder calls the helper at `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x4316404`.

## Request

(asm-traced) The body is one map literal passed as the named argument `params` (`r4 = const [0, 0x2, 0x1, 0x1, params, 0x1, null]` at `@0x43163fc`); its type arguments are `<String, dynamic>` (`@0x43163e4`), so the literal gives no value type.

Typing (two-hop, asm-traced): in `range_extender_network.dart` the builder's parameter is untyped (`SetupParameters(dynamic _ ...)`, `@0x43163a4`); the type below is read at its only caller, `ReSystemCreateLogic.createOrUpateExtenderSystem` (`oe_a7320/src/oe_a7320/page/range_system_create/re_system_create_logic.dart @0x4316100`), which passes the result of `_creattingDeviceJsonList` (`@0x4316014`): a growable list with type argument `<Map<String, dynamic>>` (`@0x4316a28`, `_GrowableList` `@0x4316a30`) whose elements include the `toJson()` results (`@0x4316a58`, `@0x4316a80`) of two device objects held in the logic (fields `field_43`, `field_47`); the element keys are those models' `toJson` (not read here).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_list` | list (`<Map<String, dynamic>>` growable list built by the caller) | yes | | `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x43163d0` |

## `param_type`/`cmd`

n/a

## Response model (link)

no model class: the builder reads the key `extender_system_id` from the awaited response map (string literal `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x4316438`, index call `@0x4316440`) and casts it to `String?` (`@0x431647c`); the return type is `Future<String?>` (type argument `@0x43163a8` region).

## Response

| field | type | required | example | source |
|---|---|---|---|---|
| `extender_system_id` | string (nullable, cast to `String?`) | optional | `"<id>"` | `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x4316438` |

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_list": ["<object>"]
}
```

Response, synthesized (key read by the builder; value is a placeholder)

```json
{
  "data": {
    "extender_system_id": "<id>"
  }
}
```

Whether the key sits at the top of `data` or of the whole body is not shown here: the builder indexes the object it awaited (`@0x4316440`).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `ReSystemCreateLogic.createOrUpateExtenderSystem` (`oe_a7320/src/oe_a7320/page/range_system_create/re_system_create_logic.dart @0x4316100`)
- `oe_a7320/src/oe_a7320/network/range_extender_network.dart`: `addExtenderSystem` @0x4316398 (`AkNetwork.requestHttp`, path C)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Whether `AkNetwork::requestHttp` returns the `data` object or the whole body to this builder (the `extender_system_id` index `@0x4316440` is applied to it).
- Element keys of `device_list`: the elements are the `toJson()` maps of two device objects (`re_system_create_logic.dart @0x4316a58`, `@0x4316a80`); the element keys are written by those models' `toJson` and are not listed on this page.

## Device-tested by

none
