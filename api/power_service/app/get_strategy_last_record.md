> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_strategy_last_record

## Purpose

Reads the last strategy record of a range-extender system (`RangeExtenderNetwork::getStrategyLastRecord`, `oe_a7320`); the callers are listed under "Callers in app"; the description itself comes from the function name (string-only).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/get_strategy_last_record` (asm-traced): the builder `RangeExtenderNetwork::getStrategyLastRecord` (`oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x360a6ac`) loads the path string at `@0x360a744` and calls `AkNetwork::requestHttp` (`@0x360a754`); that function builds the SDK command map with the literal `"POST"` (`base_service/util/ak_util/src/ak_network.dart @0x21c34fc`) and hands it to the handler `akiot.cloud_api` (`handle`, `@0x21c3544`). There is no `Method` object on this path.

## Encrypted?

Direct SDK call, path C (asm-traced), through the shared helper `AkNetwork::requestHttp`: the helper always sends `POST` and calls `handle` with `akiot.cloud_api` (`base_service/util/ak_util/src/ak_network.dart @0x21c3544`). The inventory flag `default-true (requestHttp)` does not apply: `AkNetwork::requestHttp` has no `needEncryption` switch and goes straight to the SDK; what the SDK encrypts is not visible in Dart (mechanics: [../../sdk_senders.md](../../sdk_senders.md#aknetworkrequesthttp), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)). The builder calls the helper at `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x360a754`.

## Request

(asm-traced) The body is one map literal passed as the named argument `params` (`r4 = const [0, 0x2, 0x1, 0x1, params, 0x1, null]` at `@0x360a74c`); its type arguments are `<String, dynamic>` (`@0x360a734`), so the literal gives no value type.

Typing (two-hop, asm-traced): in `range_extender_network.dart` the builder's two parameters are untyped (`SetupParameters(dynamic _, dynamic _ ...)`, `@0x360a6b8`). `strategy_type` is read from the second parameter as an unboxed 64-bit field (`LoadField r5 = r4->field_13` `@0x360a718`, `BoxInt64Instr` `@0x360a71c`, store `@0x360a730`): the caller passes a `RangeExtenderStrategyType` enum object obtained from `RangeExtenderStrategyType::fromValue` (`oe_a7320/src/oe_a7320/page/range_extender_system/service/re_system_data_refresh_service.dart @0x360a428`, from an int read `@0x360a41c`), so the body carries the enum's integer field. `extender_system_id` is the first parameter of `ReSystemDataRefreshService._getStrategyRecordHistory`, itself untyped (`SetupParameters(dynamic _, dynamic _ ...)`, `@0x360a3c8`), and keeps `?`.

| field | type | required | example | source |
|---|---|---|---|---|
| `extender_system_id` | ? | yes | ? | `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x360a6f4` |
| `strategy_type` | int (unboxed, x) | yes | | `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x360a708` |

## `param_type`/`cmd`

n/a

## Response model (link)

- `oe_a7320::RangeExtenderStrategyRecordModel`, parsed by `RangeExtenderStrategyRecordModel.fromJson` at `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x360a788`

## Response

(asm-traced) For each sender that parses a model, the keys below are the top-level keys of the model; that sender adds no wrapper fields of its own in the code read.

- `RangeExtenderStrategyRecordModel` top-level keys (`data/models.json`, `oe_a7320::RangeExtenderStrategyRecordModel`): `extender_system_id` (String?), `strategy_type` (int?), `execution_time` (int?), `execution_result` (bool), `description` (int?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "extender_system_id": "<?>",
  "strategy_type": "<int>"
}
```

Response: not synthesized (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `ReSystemDataRefreshService._getStrategyRecordHistory` (`oe_a7320/src/oe_a7320/page/range_extender_system/service/re_system_data_refresh_service.dart @0x360a438`)
- `oe_a7320/src/oe_a7320/network/range_extender_network.dart`: `getStrategyLastRecord` @0x360a6ac (`AkNetwork.requestHttp`, path C)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Type of `extender_system_id`: forwarded from an untyped parameter of `ReSystemDataRefreshService._getStrategyRecordHistory` (`re_system_data_refresh_service.dart @0x360a3c8`) — attempted 2026-10-20 (two-hop not readable: the caller of that function was not followed; one more hop leaves the reader at an untyped parameter again (`@0x360a3c8`)). Header stays string-only.

## Device-tested by

none
