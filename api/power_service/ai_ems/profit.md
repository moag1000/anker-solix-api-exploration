> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# profit

## Purpose

<!-- TODO -->

## Upstream name

`get_ai_ems_profit` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/ai_ems/profit`, method: not extracted by the inventory <!-- TODO -->; string-only: `ak_soft_ems/aiems/api/ai_ems_request.dart @0x27e21ec`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | ? | ? | `ak_soft_ems/aiems/api/ai_ems_request.dart @0x27e20b4` |
| `start_time` | ? | ? | ? | `ak_soft_ems/aiems/api/ai_ems_request.dart @0x27e20b4` |
| `end_time` | ? | ? | ? | `ak_soft_ems/aiems/api/ai_ems_request.dart @0x27e20b4` |
| `type` | ? | ? | ? | `ak_soft_ems/aiems/api/ai_ems_request.dart @0x27e20b4` |

Rows are the union over 2 senders; `source` is the first sender that sets the key.

## `param_type`/`cmd`

n/a

## Response model (link)

<!-- TODO -->

## Response

<!-- TODO -->

## Example request/response

<!-- TODO -->

## Errors seen

`api/errors.md`: <!-- TODO -->

## Callers in app

- `ak_soft_ems/aiems/api/ai_ems_request.dart`: `getProfitInfo` @0x27e20b4 (URL literal only, no `*Http*` call)
- `charging/http/http_request_repository_impl.dart`: `getAiEmsProfit` @0x2925858 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getAiEmsProfit`
- `charging/ui/page/device/a17c1/cost_savings/cost_savings_logic.dart::getAiProfit`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
