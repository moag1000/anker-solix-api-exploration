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
| [`/mini_power/v1/app/reminder/del_reminder`](app/reminder/del_reminder.md) | Deletes one custom reminder of a Prime-class charger by id. | - | owner |
| [`/mini_power/v1/app/reminder/get_reminder_list`](app/reminder/get_reminder_list.md) | Lists the custom reminders of a Prime-class charger (small charging platform), or fetches one reminder by id; the reminder manager, the editor's schedule-conflict check and the reminder image generator call it. | - | owner |
| [`/mini_power/v1/app/reminder/set_reminder`](app/reminder/set_reminder.md) | Creates or changes one custom reminder of a Prime-class charger (title, image, schedule, status); the reminder editor saves with it and the manager toggles a reminder's status with it. | - | owner |
| [`/mini_power/v1/app/setting/get_charging_device_identity_new_status`](app/setting/get_charging_device_identity_new_status.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/setting/get_charging_device_identity_status_default_true`](app/setting/get_charging_device_identity_status_default_true.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/setting/get_device_setting`](app/setting/get_device_setting.md) | TODO | `charger_get_device_setting` | skeleton |
| [`/mini_power/v1/app/setting/get_port_protocol_status`](app/setting/get_port_protocol_status.md) | TODO | - | pool-only |
| [`/mini_power/v1/app/setting/get_port_remarks`](app/setting/get_port_remarks.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/setting/get_power_range_support_protocols`](app/setting/get_power_range_support_protocols.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/setting/get_protocol_status`](app/setting/get_protocol_status.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/setting/set_charging_device_identity_new_status`](app/setting/set_charging_device_identity_new_status.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/setting/set_charging_device_identity_status`](app/setting/set_charging_device_identity_status.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/setting/set_charging_device_identity_status_default_true`](app/setting/set_charging_device_identity_status_default_true.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/setting/set_charging_mode_status`](app/setting/set_charging_mode_status.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/setting/set_compatibility_status`](app/setting/set_compatibility_status.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/setting/set_mode_sub_status`](app/setting/set_mode_sub_status.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/setting/set_port_protocol_status`](app/setting/set_port_protocol_status.md) | TODO | - | pool-only |
| [`/mini_power/v1/app/setting/set_port_remark`](app/setting/set_port_remark.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/setting/set_protocol_status`](app/setting/set_protocol_status.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/style/add_manual_clock_screensavers`](app/style/add_manual_clock_screensavers.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/style/delete_manual_clock_screensavers`](app/style/delete_manual_clock_screensavers.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/style/get_clock_screensavers`](app/style/get_clock_screensavers.md) | TODO | `charger_get_screensavers` | skeleton |
| [`/mini_power/v1/app/style/get_manual_clock_screensavers`](app/style/get_manual_clock_screensavers.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/style/get_screensaver_img_url`](app/style/get_screensaver_img_url.md) | TODO | - | pool-only |
| [`/mini_power/v1/app/style/get_url`](app/style/get_url.md) | TODO | - | skeleton |
| [`/mini_power/v1/app/style/set_manual_clock_screensaver_name`](app/style/set_manual_clock_screensaver_name.md) | TODO | - | skeleton |

Not here: MQTT or BLE facts (see [../../mqtt/README.md](../../mqtt/README.md), [../../ble/README.md](../../ble/README.md)), step-by-step flows ([../../flows/README.md](../../flows/README.md)); ownership rules are in [../../docs/STRUCTURE.md](../../docs/STRUCTURE.md).

<!-- hand-written below: kept by tools/service_index.py -->

## 3.24.3 URL strings without an inventory row (string-only)

Eleven `mini_power` URL strings are in the 3.24.3 object pool (`pp.txt`) but are neither in `data/endpoints.json` nor loaded by any decoded asm instruction (a search for each string and for its `pp+` offset in `blutter_output/asm` finds no load). The Dart code that uses them is UNCONFIRMED to sit in mixin applications that the Blutter dump omits (for example `AntiLossMapHttpMixin` in `small_charging_platform/src/scp/anti_loss_map/anti_loss_map_http_mixin.dart` is an empty class in the dump, while `weather_clock_location_helper.dart` calls `getDeviceLastLocationAntiLossData` and `setDeviceLastLocationAntiLossData` on it). None of them is in the 3.18.0 pool, so all are new in 3.24.3. No request body was traced, so there is no page for them; this table is their only record (tag `string-only`).

| URL string | pool entry | what the surrounding code suggests |
|---|---|---|
| `/mini_power/v1/app/setting/get_user_last_location` | `pp+0x9f9d8` | the weather clock reads the device's last location (`_fetchLastLocationFromCloud`, `weather_clock_location_helper.dart @0x35b9b54`; it returns early when the device serial is empty, `@0x35b9b78`, and calls `getDeviceLastLocationAntiLossData` at `@0x35b9c48`, a function in the mixin gap). Request keys: UNCONFIRMED (the sender is in the gap). Response keys read by the helper: `location` (`@0x35b9f58`, a value whose string length is logged) holding `lat` (`@0x35ba2c8`) and `lng` (`@0x35ba2e8`) |
| `/mini_power/v1/app/setting/set_user_last_location` | `pp+0x86700` | the weather clock writes the current GPS position to the cloud (`fetchCurrentLocationAndSync`, `weather_clock_location_helper.dart @0x3907b24`; log prefix `[WeatherClock] set_user_last_location`). It calls `setDeviceLastLocationAntiLossData` (`@0x3907cfc`, mixin gap) with the device serial, the latitude and the longitude as two doubles (`d0`, `d1`, `@0x3907ce8`, `@0x3907cec`) and two closures; the body keys are UNCONFIRMED (the sender is in the gap) |
| `/mini_power/v1/app/setting/get_morning_greeting` | `pp+0x86cc8` | a morning greeting switch (pool strings `action_set_morning_greeting`, `morning_greeting_enabled` next to it) |
| `/mini_power/v1/pet_screensaver/default_animations/list` | `pp+0x9fce0` | AI pet screensaver (`ai_pet_screensaver` pages, models `ai_pet_screensaver_*_model.dart`) |
| `/mini_power/v1/pet_screensaver/tasks/create` | `pp+0xa0c88` | AI pet screensaver generation task |
| `/mini_power/v1/pet_screensaver/tasks/query` | `pp+0x9fd78` | AI pet screensaver generation task |
| `/mini_power/v1/pet_screensaver/tasks/list` | `pp+0xa0588` | AI pet screensaver task list (record page) |
| `/mini_power/v1/pet_screensaver/tasks/update` | `pp+0xa0a80` | AI pet screensaver generation task |
| `/mini_power/v1/pet_screensaver/tasks/delete` | `pp+0xa0ae0` | AI pet screensaver generation task |
| `/mini_power/v1/pet_screensaver/tasks/image_review` | `pp+0x12bb40` | AI pet screensaver image review |
| `/mini_power/v1/pet_screensaver/quota/query` | `pp+0xa07f0` | AI pet screensaver quota (`ai_pet_screensaver_quota_model.dart`) |

The three reminder endpoints (`reminder/get_reminder_list`, `reminder/set_reminder`, `reminder/del_reminder`) are traced and documented in the table above.
