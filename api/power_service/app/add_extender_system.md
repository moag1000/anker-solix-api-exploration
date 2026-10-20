> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# add_extender_system

## Purpose

Creates a range-extender system from a device list and returns its id (`RangeExtenderNetwork::addExtenderSystem`, `oe_a7320`); no UI caller is recorded in `data/endpoints.json`, so the purpose is inferred from the function name (string-only).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/add_extender_system` (asm-traced): the builder `RangeExtenderNetwork::addExtenderSystem` (`oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x4316398`) loads the path string at `@0x43163f4` and calls `AkNetwork::requestHttp` (`@0x4316404`); that function builds the SDK command map with the literal `"POST"` (`base_service/util/ak_util/src/ak_network.dart @0x21c34fc`) and hands it to the handler `akiot.cloud_api` (`handle`, `@0x21c3544`). There is no `Method` object on this path.

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) The body is one map literal passed as the named argument `params` (`r4 = const [0, 0x2, 0x1, 0x1, params, 0x1, null]` at `@0x43163fc`); its type arguments are `<String, dynamic>` (`@0x43163e4`), so the literal gives no value type. Values come from parameters of the builder; the asm carries no static parameter type.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_list` | ? | yes | ? | `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x43163d0` |

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
  "device_list": "<?>"
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

- `oe_a7320/src/oe_a7320/network/range_extender_network.dart`: `addExtenderSystem` @0x4316398 (requestHttp; encrypted: default-true (requestHttp) — verify)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Type and element shape of `device_list`: a parameter of the builder (`fp-0x60`, `@0x43163d0`); the map literal is `<String, dynamic>` (`@0x43163e4`) and the asm carries no parameter type.
- Whether `AkNetwork::requestHttp` returns the `data` object or the whole body to this builder (the `extender_system_id` index `@0x4316440` is applied to it).
- No UI caller is recorded for this builder in `data/endpoints.json`.
- Encryption: the call goes through `AkNetwork::requestHttp` and the SDK handler directly (path C in `api/encryption.md`), not through `encryptionRequestHttp`; the "Encrypted?" line above is the inventory default.

## Device-tested by

none
