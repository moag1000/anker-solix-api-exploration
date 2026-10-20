> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# profit

## Purpose

Reads the AI-EMS profit figures of a site for a time range (callers `AiemsStrategyController::_fetchRevenueData`, `AiSmartModeCardLogic::_fetchRevenue` and `CostSavingsLogic::getAiProfit`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`get_ai_ems_profit` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/ai_ems/profit` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x292594c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2925944`, in `HttpRequestControllerImpl::getAiEmsProfit` (`charging/http/http_request_repository_impl.dart @0x2925858`), sent through `encryptionRequestHttp` (`@0x2925974`).

Same URL and method object in the other sender(s) read:

- `POST /power_service/v1/ai_ems/profit` (asm-traced): URL string at `ak_soft_ems/aiems/api/ai_ems_request.dart @0x27e21ec`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x27e21d4`, in `AiEmsRequest::getProfitInfo` (`ak_soft_ems/aiems/api/ai_ems_request.dart @0x27e20b4`), sent through `getDataFromService` (`@0x27e2200`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) Two senders. `HttpRequestControllerImpl::getAiEmsProfit` stores four keys from parameters in one map literal with type arguments `<String, String>` (`@0x2925900`), so all four values are Strings. `AiEmsRequest::getProfitInfo` (`ak_soft_ems/aiems/api/ai_ems_request.dart @0x27e20b4`) builds the same four keys in a `<String, dynamic>` literal (`@0x27e21a0`) with `site_id` from a parameter and the constants `start_time = ""` (`@0x27e2170`), `end_time = ""` (`@0x27e2184`), `type = "lifetime"` (`@0x27e2194`). 

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | string | yes | `"<site_id>"` | `charging/http/http_request_repository_impl.dart @0x29258b4` |
| `start_time` | string | yes | `"<start_time>"` | `charging/http/http_request_repository_impl.dart @0x29258c8` |
| `end_time` | string | yes | `"<end_time>"` | `charging/http/http_request_repository_impl.dart @0x29258dc` |
| `type` | string | yes | `"lifetime"` (constant in `AiEmsRequest::getProfitInfo`) | `charging/http/http_request_repository_impl.dart @0x29258f0` (value from parameter); constant at `ak_soft_ems/aiems/api/ai_ems_request.dart @0x27e2194` |

## `param_type`/`cmd`

n/a

## Response model (link)

- [`AiEmsProfitModel`](../../../models/other.md#aiemsprofitmodel), parsed by `AiEmsProfitModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x29259c8`. Parsed by the `HttpRequestControllerImpl` sender. The `AiEmsRequest` sender returns a `Future<RevenueData?>` (type argument `@0x27e20d4`); its parser is not read here.

## Response

(asm-traced) All keys belong to the model page; this endpoint adds no wrapper fields of its own in the code read.

- `AiEmsProfitModel` top-level keys (`data/models.json`, `charging::AiEmsProfitModel`): `price_unit` (String?), `running_time` (int?), `self_use_diff_percent` (String?), `aiems_lifetime_profit` (String?), `aiems_profit_total` (String?), `aiems_profit` (unknown), `type` (String?), `show_percentage` (bool?), `aiems_self_use_diff` (String?), `schedule_day` (int?), `ss_income` (String?), `ss_chg_energy` (String?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "site_id": "<site_id>",
  "start_time": "<start_time>",
  "end_time": "<end_time>",
  "type": "lifetime"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `ak_soft_ems/aiems/api/ai_ems_request.dart`: `getProfitInfo` @0x27e20b4 (URL literal only, no `*Http*` call; sender `HttpHelper::getDataFromService` (`ak_soft_ems/http/http_helper.dart @0x22ba2bc`) (HTTP helper wrapper), called from the same function; resolved from the URL literal at `ak_soft_ems/aiems/api/ai_ems_request.dart @0x27e21ec` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))
- `charging/http/http_request_repository_impl.dart`: `getAiEmsProfit` @0x2925858 (encryptionRequestHttp; encrypted: true)

Called from:

- `ak_soft_ems/aiems/aiems_strategy_controller.dart::_fetchRevenueData`
- `ak_soft_ems/aiems/public_widget/ai_smart_mode_card_logic.dart::_fetchRevenue`
- `charging/http/http_request_repository.dart::getAiEmsProfit`
- `charging/ui/page/device/a17c1/cost_savings/cost_savings_logic.dart::getAiProfit`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Which values of `type` other than `"lifetime"` the callers of `getAiEmsProfit` pass: the value is a parameter (`@0x29258f0`) and the three callers were not decoded for it.
- The format of `start_time` and `end_time` (the `AiEmsRequest` sender sends empty strings for both).
- The `RevenueData` parser of the `AiEmsRequest` sender (`ak_soft_ems`) was not read.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
