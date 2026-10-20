> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# update_extender_system_strategy

## Purpose

Saves the strategy of an A7320 range extender system: `RangeExtenderStrategyLogic::updateRangeExtenderSystem` (`range_extender_strategy_logic.dart @0x39d99a8`) calls `RangeExtenderNetwork::updateExtenderSystemStrategy`, then writes the strategy to the device (`_setupExtendedRangeStrategyToDevice`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/update_extender_system_strategy` (asm-traced): the sender `RangeExtenderNetwork::updateExtenderSystemStrategy` (`range_extender_network.dart @0x39dadbc`) has the URL string at `@0x39dae70` and calls `AkNetwork::requestHttp` (`@0x39dae80`); that helper (`base_service/util/ak_util/src/ak_network.dart @0x21c3444`) builds a command map with the string literal `"POST"` (`@0x21c34fc`) and sends it through `akIoTKitManager.handle` (`@0x21c3544`). The method is a string literal, not a `Method` pool object.

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is a 2-pair map literal typed `<String, dynamic>` (type arguments `@0x39dae5c`, `AllocateArray r2 = 8` `@0x39dae00`) passed to `AkNetwork::requestHttp` as the `params` argument.

| field | type | required | example | source |
|---|---|---|---|---|
| `extender_system_id` | ? | yes | | key `@0x39dae0c`, value store `@0x39dae1c` (parameter at `fp-0x68`); the caller reads fields of its state objects just before the call (`range_extender_strategy_logic.dart @0x39d9b70`..`@0x39d9ba4`), the type is not given there |
| `extender_system_params` | object | yes | | key `@0x39dae20`, value store `@0x39dae38`; the value is the result of `RangeExtenderStrategyParamsModel::toJson` (call `@0x39dae30`, `range_extender_system_detail.dart`); keys of that model (from `data/models.json`): `effective_strategy` (int), `by_time_strategy`, `by_soc_strategy` |

## `param_type`/`cmd`

n/a

## Response model (link)

None: the response body is not parsed. `updateExtenderSystemStrategy` returns the awaited `Map<String, dynamic>?` of `AkNetwork::requestHttp`; the caller awaits it (`Await` `@0x39d9bd0`) and discards the result before `defaultOtherMode` (`@0x39d9bd8`). The extractor's response class `RangeExtenderStrategyParamsModel` is the request model, not a parsed answer.

## Response

No response key is read by the app.

## Example request/response

Request, synthesized (type of `extender_system_id` unresolved)

```json
{"extender_system_id": "<extender_system_id>", "extender_system_params": {"effective_strategy": 0, "by_time_strategy": {}, "by_soc_strategy": {}}}
```

Response: none parsed.

## Errors seen

None traced as codes. `updateExtenderSystemStrategy` catches an `AkNetworkException` (class-id test `cmp x, x17` with 6337 `@0x39daeb0`, a type test, not an error code), logs `"updateExtenderSystemStrategy error: "` and rethrows it as a `RangeExtenderException` (`errorToRangeExtenderException` `@0x39daf90`). Error codes are catalogued in `api/errors.md`.

## Callers in app

- `oe_a7320/src/oe_a7320/network/range_extender_network.dart`: `updateExtenderSystemStrategy` @0x39dadbc (requestHttp; encrypted: default-true (requestHttp) — verify)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- Type of `extender_system_id` (a field read of the logic's state objects). Header stays string-only.
- The inner structures `by_time_strategy` and `by_soc_strategy` (their `toJson` was not followed).
- Whether the server echoes the stored strategy: the app drops the answer.

## Device-tested by

none
