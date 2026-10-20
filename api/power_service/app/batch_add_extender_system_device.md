> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# batch_add_extender_system_device

## Purpose

Adds devices to an existing range-extender system (`RangeExtenderNetwork::batchAddExtenderSystemDevice`, `oe_a7320`); purpose inferred from the function name (string-only).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/batch_add_extender_system_device` (asm-traced): the builder `RangeExtenderNetwork::batchAddExtenderSystemDevice` (`oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x43168f0`) loads the path string at `@0x431696c` and calls `AkNetwork::requestHttp` (`@0x431697c`); that function builds the SDK command map with the literal `"POST"` (`base_service/util/ak_util/src/ak_network.dart @0x21c34fc`) and hands it to the handler `akiot.cloud_api` (`handle`, `@0x21c3544`). There is no `Method` object on this path.

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) The body is one map literal passed as the named argument `params` (`r4 = const [0, 0x2, 0x1, 0x1, params, 0x1, null]` at `@0x4316974`); its type arguments are `<String, dynamic>` (`@0x431695c`), so the literal gives no value type. Values come from parameters of the builder; the asm carries no static parameter type.

| field | type | required | example | source |
|---|---|---|---|---|
| `extender_system_id` | ? | yes | ? | `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x4316934` |
| `device_list` | ? | yes | ? | `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x4316948` |

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
  "device_list": "<?>"
}
```

Response: not synthesized (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `oe_a7320/src/oe_a7320/network/range_extender_network.dart`: `batchAddExtenderSystemDevice` @0x43168f0 (requestHttp; encrypted: default-true (requestHttp) — verify)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Type of `extender_system_id`, `device_list`: parameter(s) of the builder; the map literal is `<String, dynamic>` and the asm carries no parameter type.
- Encryption: the call goes through `AkNetwork::requestHttp` and the SDK handler directly (path C in `api/encryption.md`); the "Encrypted?" line above is the inventory default.
- No UI caller is recorded for this builder in `data/endpoints.json`, so the purpose is inferred from the function name.

## Device-tested by

none
