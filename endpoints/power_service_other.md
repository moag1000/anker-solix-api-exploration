# Power Service Other

> 13 function calls, 12 unique endpoints

## `/power_service/v1/add_message`

- **addMessage**(`device_sn, product_code, device_name, bt_ble_id, bt_ble_mac, firmware_version, wifi_name, parent_device_sn, parent_device_pn`)

## `/power_service/v1/currency/get_list`

- **getCurrencyGetList**(`solar_bank_sn, solar_sn`) → `CurrencyInfo`

## `/power_service/v1/del_message`

- **delMessage**(`token`)

## `/power_service/v1/get_all_service_config`

- **getAllQaEnvConfig**(`*(no params extracted)*`)

## `/power_service/v1/get_message`

- **getMessage**(`*(no params extracted)*`) → `MsgHttpModel`

## `/power_service/v1/get_message_not_disturb`

- **getMessageDisturb**(`*(no params extracted)*`) → `GdprLinkResponseModel`

## `/power_service/v1/get_message_sn_list`

- **getMessageSnList**(`last_time, device_sns, limit, message_type, last_msg_id`)

## `/power_service/v1/get_message_unread`

- **getMessageUnread**(`*(no params extracted)*`)

## `/power_service/v1/message_not_disturb`

- **setEvChargerPushMessage**(`start_time, end_time, disturb_switch`)
- **setMessageDisturb**(`*(no params extracted)*`)

## `/power_service/v1/product_accessories`

- **getProductAccessories**(`device_model, device_sn, brand_id`)

## `/power_service/v1/product_categories`

- **getProductCategories**(`*(no params extracted)*`)

## `/power_service/v1/read_message`

- **setMessageRead**(`disturb_scenes, start_charging, stop_charging, paused_charging, paused_car_charging, restore_charging, smart_charging, boost_charging`)

