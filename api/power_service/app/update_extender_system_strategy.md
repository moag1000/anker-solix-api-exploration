> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# update_extender_system_strategy

## Purpose

Saves the strategy of an A7320 range extender system: `RangeExtenderStrategyLogic::updateRangeExtenderSystem` (`range_extender_strategy_logic.dart @0x39d99a8`) calls `RangeExtenderNetwork::updateExtenderSystemStrategy`, then writes the strategy to the device (`_setupExtendedRangeStrategyToDevice`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/update_extender_system_strategy` (asm-traced): the sender `RangeExtenderNetwork::updateExtenderSystemStrategy` (`range_extender_network.dart @0x39dadbc`) has the URL string at `@0x39dae70` and calls `AkNetwork::requestHttp` (`@0x39dae80`); that helper (`base_service/util/ak_util/src/ak_network.dart @0x21c3444`) builds a command map with the string literal `"POST"` (`@0x21c34fc`) and sends it through `akIoTKitManager.handle` (`@0x21c3544`). The method is a string literal, not a `Method` pool object.

## Encrypted?

Direct SDK call, path C (asm-traced), through the shared helper `AkNetwork::requestHttp`: the helper always sends `POST` and calls `handle` with `akiot.cloud_api` (`base_service/util/ak_util/src/ak_network.dart @0x21c3544`). The inventory flag `default-true (requestHttp)` does not apply: `AkNetwork::requestHttp` has no `needEncryption` switch and goes straight to the SDK; what the SDK encrypts is not visible in Dart (mechanics: [../../sdk_senders.md](../../sdk_senders.md#aknetworkrequesthttp), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)). The builder calls the helper at `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x39dae80`.

## Request

The body is a 2-pair map literal typed `<String, dynamic>` (type arguments `@0x39dae5c`, `AllocateArray r2 = 8` `@0x39dae00`) passed to `AkNetwork::requestHttp` as the `params` argument.

| field | type | required | example | source |
|---|---|---|---|---|
| `extender_system_id` | ? | yes | | key `range_extender_network.dart @0x39dae0c`, value store `@0x39dae1c` (parameter at `fp-0x68`); the caller reads fields of its state objects just before the call (`range_extender_strategy_logic.dart @0x39d9b70`..`@0x39d9ba4`), the type is not given there |
| `extender_system_params` | object | yes | | key `range_extender_network.dart @0x39dae20`, value store `@0x39dae38`; the value is the result of `RangeExtenderStrategyParamsModel::toJson` (call `@0x39dae30`, `range_extender_system_detail.dart`); keys of that model (from `data/models.json`): `effective_strategy` (int), `by_time_strategy`, `by_soc_strategy` |

Inner structures of `extender_system_params` (asm-traced, `toJson` of the three models in `oe_a7320/src/oe_a7320/network/models/src/range_extender_system_detail.dart`; each key is written only when its model field is not null unless noted): `RangeExtenderStrategyParamsModel::toJson` (`@0x22917a8`) writes `effective_strategy` (`@0x22917fc`), `by_time_strategy` (`@0x2291844`, nested `RangeExtenderByTimeStrategyModel::toJson` `@0x2291b30`) and `by_soc_strategy` (`@0x229188c`, nested `RangeExtenderBySocStrategyModel::toJson` `@0x2291900`). The by-time object has `strategy_type` (`@0x2291b84`), `generator_start_time` (`@0x2291bbc`), `stop_soc` (`@0x2291bf4`) and `ranges` (key `@0x2291c74`, a list built by `map` `@0x2291c48` over the closure `@0x2291ab8` and `_GrowableList.of` `@0x2291c58`; written only when the list is not empty: `cbz` on its length, `@0x2291c1c`); the by-soc object has `strategy_type` (`@0x2291954`), `start_soc` (`@0x229198c`), `stop_soc` (`@0x22919c4`) and `ranges` (key `@0x2291a44`, built the same way, length test `@0x22919ec`). Each `ranges` element is a `RangeExtenderGeneratorModeModel::toJson` map (`@0x2290ea0`) with `end_time` (`@0x2290ef4`), `start_time` (`@0x2290f2c`) and `generator_mode` (`@0x2290f64`). Field types are the declared ones in `data/models.json`: `int?` for the strategy and SoC keys and `generator_mode`; the types of the times and of `ranges` are `unknown` there.

## `param_type`/`cmd`

n/a

## Response model (link)

None: the response body is not parsed. `updateExtenderSystemStrategy` returns the awaited `Map<String, dynamic>?` of `AkNetwork::requestHttp`; the caller awaits it (`Await` `range_extender_strategy_logic.dart @0x39d9bd0`) and discards the result before `defaultOtherMode` (`@0x39d9bd8`). The extractor's response class `RangeExtenderStrategyParamsModel` is the request model, not a parsed answer.

## Response

No response key is read by the app.

## Example request/response

Request, synthesized (type of `extender_system_id` unresolved)

```json
{"extender_system_id": "<extender_system_id>", "extender_system_params": "<RangeExtenderStrategyParamsModel.toJson()>"}
```

Response: none parsed.

## Errors seen

None traced as codes. `updateExtenderSystemStrategy` catches an `AkNetworkException` (class-id test `cmp x, x17` with 6337 `range_extender_network.dart @0x39daeb0`, a type test, not an error code), logs `"updateExtenderSystemStrategy error: "` and rethrows it as a `RangeExtenderException` (`errorToRangeExtenderException` `@0x39daf90`). Error codes are catalogued in `api/errors.md`.

## Callers in app

- `oe_a7320/src/oe_a7320/network/range_extender_network.dart`: `updateExtenderSystemStrategy` @0x39dadbc (`AkNetwork.requestHttp`, path C)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- Type of `extender_system_id`: a field read of the logic's state objects (`range_extender_strategy_logic.dart @0x39d9b70..@0x39d9ba4`) — attempted 2026-10-20 (two-hop not readable: the field declaration is not shown in the asm (`range_extender_strategy_logic.dart @0x39d9b70`)). Header stays string-only.
- Whether the server echoes the stored strategy: the app drops the answer.

## Device-tested by

none
