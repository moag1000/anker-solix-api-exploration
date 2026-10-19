> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# mini_power

Service index for the URL prefix `/mini_power/`. Each endpoint page is the single owner of its request, response and tags; a skeleton page (status "skeleton", purpose TODO) carries only what `data/endpoints.json` knows and has `Confidence: string-only` until a human reads the asm. Upstream keys are `API_ENDPOINTS` keys of `api/apitypes.py`.

| endpoint | purpose | upstream key | status |
|---|---|---|---|
| [`/mini_power/v1/app/charging/add_charging_mode`](app/charging/add_charging_mode.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/charging/delete_charging_mode`](app/charging/delete_charging_mode.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/charging/get_charging_mode_list`](app/charging/get_charging_mode_list.md) | TODO | `charger_get_charging_modes` | skeleton |
| [`/mini_power/v1/app/charging/update_charging_mode`](app/charging/update_charging_mode.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/egg/add_easter_egg_trigger_record`](app/egg/add_easter_egg_trigger_record.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/egg/get_easter_egg_trigger_list`](app/egg/get_easter_egg_trigger_list.md) | TODO | `charger_get_triggers` | skeleton |
| [`/mini_power/v1/app/egg/report_easter_egg_trigger_status`](app/egg/report_easter_egg_trigger_status.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/power/get_day_power_data`](app/power/get_day_power_data.md) | TODO | `charger_get_statistics` | skeleton |
| [`/mini_power/v1/app/reminder/del_reminder`](app/reminder/del_reminder.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/reminder/get_reminder_list`](app/reminder/get_reminder_list.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/reminder/set_reminder`](app/reminder/set_reminder.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/setting/get_charging_device_identity_new_status`](app/setting/get_charging_device_identity_new_status.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/setting/get_charging_device_identity_status_default_true`](app/setting/get_charging_device_identity_status_default_true.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/setting/get_device_setting`](app/setting/get_device_setting.md) | TODO | `charger_get_device_setting` | skeleton |
| [`/mini_power/v1/app/setting/get_port_protocol_status`](app/setting/get_port_protocol_status.md) | TODO | - | removed in 3.24.3, skeleton |
| [`/mini_power/v1/app/setting/get_port_remarks`](app/setting/get_port_remarks.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/setting/get_power_range_support_protocols`](app/setting/get_power_range_support_protocols.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/setting/get_protocol_status`](app/setting/get_protocol_status.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/setting/set_charging_device_identity_new_status`](app/setting/set_charging_device_identity_new_status.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/setting/set_charging_device_identity_status`](app/setting/set_charging_device_identity_status.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/setting/set_charging_device_identity_status_default_true`](app/setting/set_charging_device_identity_status_default_true.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/setting/set_charging_mode_status`](app/setting/set_charging_mode_status.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/setting/set_compatibility_status`](app/setting/set_compatibility_status.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/setting/set_mode_sub_status`](app/setting/set_mode_sub_status.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/setting/set_port_protocol_status`](app/setting/set_port_protocol_status.md) | TODO | - | removed in 3.24.3, skeleton |
| [`/mini_power/v1/app/setting/set_port_remark`](app/setting/set_port_remark.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/setting/set_protocol_status`](app/setting/set_protocol_status.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/style/add_manual_clock_screensavers`](app/style/add_manual_clock_screensavers.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/style/delete_manual_clock_screensavers`](app/style/delete_manual_clock_screensavers.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/style/get_clock_screensavers`](app/style/get_clock_screensavers.md) | TODO | `charger_get_screensavers` | skeleton |
| [`/mini_power/v1/app/style/get_manual_clock_screensavers`](app/style/get_manual_clock_screensavers.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/style/get_screensaver_img_url`](app/style/get_screensaver_img_url.md) | TODO | - | removed in 3.24.3, skeleton |
| [`/mini_power/v1/app/style/get_url`](app/style/get_url.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/style/set_manual_clock_screensaver_name`](app/style/set_manual_clock_screensaver_name.md) | TODO | - | skeleton |

Not here: MQTT or BLE facts (see [../../mqtt/README.md](../../mqtt/README.md), [../../ble/README.md](../../ble/README.md)), step-by-step flows ([../../flows/README.md](../../flows/README.md)); ownership rules are in [../../docs/STRUCTURE.md](../../docs/STRUCTURE.md).
