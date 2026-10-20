> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_extender_system_cumulative_data

## Purpose

Reads the accumulated energy data of a range-extender system (`RangeExtenderNetwork::getExtenderSystemCumulativeData`, `oe_a7320`); no UI caller is recorded in `data/endpoints.json`, so the purpose is inferred from the function name (string-only).

## Upstream name

`get_extender_system_cumulative_data` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/get_extender_system_cumulative_data` (asm-traced): the builder `RangeExtenderNetwork::getExtenderSystemCumulativeData` (`oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x3608d24`) loads the path string at `@0x3608d84` and calls `AkNetwork::requestHttp` (`@0x3608d94`); that function builds the SDK command map with the literal `"POST"` (`base_service/util/ak_util/src/ak_network.dart @0x21c34fc`) and hands it to the handler `akiot.cloud_api` (`handle`, `@0x21c3544`). There is no `Method` object on this path.

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) The body is one map literal passed as the named argument `params` (`r4 = const [0, 0x2, 0x1, 0x1, params, 0x1, null]` at `@0x3608d8c`); its type arguments are `<String, dynamic>` (`@0x3608d74`), so the literal gives no value type. Values come from parameters or object fields of the builder; the asm carries no static type.

| field | type | required | example | source |
|---|---|---|---|---|
| `extender_system_id` | ? | yes | ? | `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x3608d60` |

## `param_type`/`cmd`

n/a

## Response model (link)

- `oe_a7320::ExtenderSystemCumulativeDataModel`, parsed by `ExtenderSystemCumulativeDataModel.fromJson` at `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x3608dc8`

## Response

(asm-traced) For each sender that parses a model, the keys below are the top-level keys of the model; that sender adds no wrapper fields of its own in the code read.

- `ExtenderSystemCumulativeDataModel` top-level keys (`data/models.json`, `oe_a7320::ExtenderSystemCumulativeDataModel`): `total_power_generation` (int?), `consumption_gas` (int?), `consumption_lpg` (int?), `consumption_ng` (int?).

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

- `oe_a7320/src/oe_a7320/network/range_extender_network.dart`: `getExtenderSystemCumulativeData` @0x3608d24 (requestHttp; encrypted: default-true (requestHttp) — verify)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Type of `extender_system_id`: parameter or object field read by the builder; the map literal is `<String, dynamic>` and the asm carries no static type.
- Encryption: the call goes through `AkNetwork::requestHttp` and the SDK handler directly (path C in `api/encryption.md`); the "Encrypted?" line above is the inventory default.
- No UI caller is recorded for this builder in `data/endpoints.json`, so the purpose is inferred from the function name.

## Device-tested by

none
