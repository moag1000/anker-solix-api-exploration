> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# visualization

## Purpose

Reads the AI EMS strategy visualization of a site: the planned energy chart (solar, battery, home load and grid per period with the strategy type), the current strategy and the price chart; the AI strategy page and the A5101 system policy page use it.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /ems/v1/strategy/visualization` (asm-traced). Sender: `AiEmsRequest.getVisualizationDetail` (`ak_soft_ems/aiems/api/ai_ems_request.dart @0x24a40fc`); the URL literal is loaded at `@0x24a41f8`, the method is `Method.post` (pool entry `pp+0xa7e0`, `@0x24a41e0`), both passed to `HttpHelper.getDataFromService` (`ak_soft_ems/http/http_helper.dart @0x22ba2bc`, call `@0x24a420c`).

## Encrypted?

Yes by wrapper (asm-traced): `getDataFromService` (`ak_soft_ems/http/http_helper.dart @0x22ba2bc`) calls `HttpServiceImpl.encryptionRequestHttp` (`http_helper.dart @0x22ba418`) with the named arguments `complete`, `fail`, `showLoading` and `success` (`@0x22ba410`) and without `needEncryption`, so the default `true` applies ([encryption.md](../../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time ([encryption.md](../../encryption.md)); asm alone does not decide it. The inventory lists this URL as a URL provider because the `*Http*` call is in the helper, not in the function that holds the literal.

## Request

Body is a `<String, dynamic>` map of one pair (`r2 = 4`, `@0x24a4190`).

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | String | yes | `<site id>` | `ai_ems_request.dart @0x24a4198`; the argument |

## `param_type`/`cmd`

n/a

## Response model (link)

`StrategyVisualizationDetail` ([../../../models/strategy_visualization_models.md](../../../models/strategy_visualization_models.md#strategyvisualizationdetail)): the function's future is typed `StrategyVisualizationDetail?` (`@0x24a411c`); the success closure (`@0x24a42c8`) calls `StrategyVisualizationDetail.fromJson` on the data (`@0x24a4320`) and completes the future (`@0x24a4330`).

## Response

The sender completes an `_AsyncCompleter<StrategyVisualizationDetail?>` (`@0x24a4160`) through two static closures: the failure closure (`@0x24a4228`) logs `StrategyApi.getVisualizationDetail failed code=... msg=...` (`@0x24a425c`), the success closure (`@0x24a42c8`) checks that the data is a `Map<String, dynamic>` (`@0x24a4308`) and parses it.

| field | type | required | example | source |
|---|---|---|---|---|
| `energy_chart_data`, `current_strategy`, `price_unit`, `energy_unit`, `price_chart_data` | see model page | no | `{ "energy_chart_data": [ ... ], "current_strategy": { ... }, "price_unit": "...", "energy_unit": "kWh", "price_chart_data": { "buy_real_prices": [ ... ], "sell_real_prices": [ ... ] } }` | `strategy_visualization_model.dart @0x24a43d4`, `@0x24a441c`, `@0x24a44c4`, `@0x24a4540`, `@0x24a46e0`; [model page](../../../models/strategy_visualization_models.md#strategyvisualizationdetail) |

Failure path (traced 2026-10-20, app side): after logging with `exeError` (`ak_soft_ems/aiems/api/ai_ems_request.dart @0x24a4294`) the failure closure completes the completer with `null` (`complete(null)`, `@0x24a429c`..`@0x24a42ac`), so a failed call yields a null `StrategyVisualizationDetail?`, not an exception.

## Example request/response

Request, synthesized

```json
{ "site_id": "<site id>" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../encryption.md](../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../errors.md).

## Callers in app

- `AiEmsStrategyController._fetchStrategyData` (`ak_soft_ems/aiems/aiems_strategy_controller.dart @0x363cfa8`)
- `SystemPolicyLogic.fetchAndUpdateSmartModeSubtitle` (`charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart @0x24a3f58`)

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 object pool). 3.24.3: present (pool `pp+0x91520`). since: 3.24.3.

## Known unknowns

- Whether the server returns an object for sites without an AI EMS strategy is not known (the future is nullable).

## Device-tested by

none
