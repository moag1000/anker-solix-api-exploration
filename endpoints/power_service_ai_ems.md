# Power Service AI EMS

> **Numbers under review (2026-10-19):** integers on this page that came from decompiled code were read without Smi decoding and may be 2× too large. Verified values: see docs/audit/endpoints.md; corrected facts live on their owner pages (docs/STRUCTURE.md).

> 2 function calls, 2 unique endpoints
>
> **Source**: Regenerated from ENDPOINT_FIELDS.md (authoritative reference)

## `/power_service/v1/ai_ems/get_status`

- **getAiModeStatusRequest**(`site_id?`) → `AiModeStatusModel`

## `/power_service/v1/ai_ems/profit`

- **getAiEmsProfit**(`site_id?, start_time, end_time, type`) → `AiEmsProfitModel`
