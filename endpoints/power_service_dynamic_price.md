# Power Service Dynamic Price

> 3 function calls, 3 unique endpoints

## `/power_service/v1/dynamic_price/check_available`

- **postHasChangeCountry**(`is_notification_enable, token`)

## `/power_service/v1/dynamic_price/price_detail`

- **getDynamicPriceDetail**(`pb, tlv, device_sn, version, local_time, device_type, protobuf_name, events, payload, device_model, sns`) → `DynamicPriceDetailModel`

## `/power_service/v1/dynamic_price/support_option`

- **getDynamicPriceSupportOption**(`site_id`) → `DynamicPriceCountryAreaModel`

