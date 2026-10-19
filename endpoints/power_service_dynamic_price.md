# Power Service Dynamic Price

> **Numbers under review (2026-10-19):** integers on this page that came from decompiled code were read without Smi decoding and may be 2× too large. Verified values: see docs/audit/endpoints.md; corrected facts live on their owner pages (docs/STRUCTURE.md).

> 3 function calls, 3 unique endpoints
>
> **Source**: Regenerated from ENDPOINT_FIELDS.md (authoritative reference)

## `/power_service/v1/dynamic_price/check_available`

- **postHasChangeCountry**(`*(no params in ENDPOINT_FIELDS.md)*`)

## `/power_service/v1/dynamic_price/price_detail`

- **getDynamicPriceDetail**(`company?, area, date, device_sn`) → `DynamicPriceDetailModel`

## `/power_service/v1/dynamic_price/support_option`

- **getDynamicPriceSupportOption**(`site_id?, device_pn`) → `DynamicPriceCountryAreaModel`
