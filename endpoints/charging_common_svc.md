# Charging Common Svc

> **Numbers under review (2026-10-19):** integers on this page that came from decompiled code were read without Smi decoding and may be 2× too large. Verified values: see docs/audit/endpoints.md; corrected facts live on their owner pages (docs/STRUCTURE.md).

> 1 function call, 1 unique endpoint
>
> **Source**: Regenerated from ENDPOINT_FIELDS.md (authoritative reference)
>
> Note: Additional endpoints `location/get` and `location/set` are known from thomluther/anker-solix-api but not found in the Blutter Dart HTTP layer — they may use the native AKIoT SDK bridge.

## `/charging_common_svc/location/support`

- **getLocationSupport**(`business_type?, identifier_type, identifier_id`) → `SupportLocation`
