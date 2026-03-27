# Power Service Other

> 13 function calls, 12 unique endpoints
>
> **Source**: Regenerated from ENDPOINT_FIELDS.md (authoritative reference)

## `/power_service/v1/add_message`

- **addMessage**(`*(no params in ENDPOINT_FIELDS.md)*`)

## `/power_service/v1/currency/get_list`

- **getCurrencyGetList**(`counrty?`) → `CurrencyInfo`

## `/power_service/v1/del_message`

- **delMessage**(`*(no params in ENDPOINT_FIELDS.md)*`)

## `/power_service/v1/get_all_service_config`

- **getAllQaEnvConfig**(`*(no params in ENDPOINT_FIELDS.md)*`)

## `/power_service/v1/get_message`

- **getMessage**(`last_time?, device_sns?, limit?, message_type, last_msg_id?`) → `MsgHttpModel`

## `/power_service/v1/get_message_not_disturb`

- **getMessageDisturb**(`*(none extracted)*`) → `MsgDisturbHttpModel`

## `/power_service/v1/get_message_sn_list`

- **getMessageSnList**(`*(no params in ENDPOINT_FIELDS.md)*`)

## `/power_service/v1/get_message_unread`

- **getMessageUnread**(`*(no params in ENDPOINT_FIELDS.md)*`)

## `/power_service/v1/message_not_disturb`

- **setEvChargerPushMessage**(`disturb_scenes`)
  - `disturb_scenes` is a nested object: `{stop_charging, start_charging, paused_charging, ...}`
- **setMessageDisturb**(`start_time?, end_time?, disturb_switch?`)

## `/power_service/v1/product_accessories`

- **getProductAccessories**(`*(no params in ENDPOINT_FIELDS.md)*`)

## `/power_service/v1/product_categories`

- **getProductCategories**(`*(no params in ENDPOINT_FIELDS.md)*`)

## `/power_service/v1/read_message`

- **setMessageRead**(`*(no params in ENDPOINT_FIELDS.md)*`)
