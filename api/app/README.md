> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# app

Service index for the URL prefix `/app/`. Each endpoint page is the single owner of its request, response and tags; a skeleton page (status "skeleton", purpose TODO) carries only what `data/endpoints.json` knows and has `Confidence: string-only` until a human reads the asm. Upstream keys are `API_ENDPOINTS` keys of `api/apitypes.py`.

| endpoint | purpose | upstream key | status |
|---|---|---|---|
| [`/app/ai/anka`](ai/anka.md) | TODO | - | skeleton |
| [`/app/cloudstor/get_app_up_token_general`](cloudstor/get_app_up_token_general.md) | TODO | - | skeleton |
| [`/app/cloudstor/get_app_up_token_without_login`](cloudstor/get_app_up_token_without_login.md) | TODO | - | skeleton |
| [`/app/cloudstor/get_down_load_urls`](cloudstor/get_down_load_urls.md) | TODO | - | skeleton |
| [`/app/devicemanage/update_relate_device_info`](devicemanage/update_relate_device_info.md) | TODO | - | skeleton |
| [`/app/devicerelation/clear_share`](devicerelation/clear_share.md) | TODO | - | skeleton |
| [`/app/devicerelation/confirm_invite`](devicerelation/confirm_invite.md) | TODO | - | skeleton |
| [`/app/devicerelation/device_invite`](devicerelation/device_invite.md) | TODO | - | skeleton |
| [`/app/devicerelation/get_shared_device`](devicerelation/get_shared_device.md) | TODO | `get_shared_device` | skeleton |
| [`/app/devicerelation/ignore_invite`](devicerelation/ignore_invite.md) | TODO | - | skeleton |
| [`/app/devicerelation/relate_device`](devicerelation/relate_device.md) | TODO | - | skeleton |
| [`/app/devicerelation/un_relate_and_unbind_device`](devicerelation/un_relate_and_unbind_device.md) | TODO | - | skeleton |
| [`/app/devicerelation/up_alias_name`](devicerelation/up_alias_name.md) | TODO | - | skeleton |
| [`/app/devicerelation/update_share`](devicerelation/update_share.md) | TODO | - | skeleton |
| [`/app/help/add_feedback`](help/add_feedback.md) | TODO | - | skeleton |
| [`/app/help/app_versions/check`](help/app_versions/check.md) | TODO | - | skeleton |
| [`/app/help/banner/nps`](help/banner/nps.md) | TODO | - | skeleton |
| [`/app/help/banners`](help/banners.md) | TODO | - | skeleton |
| [`/app/help/dst`](help/dst.md) | TODO | - | skeleton |
| [`/app/help/dynamic/config/list`](help/dynamic/config/list.md) | TODO | - | skeleton |
| [`/app/help/faqs`](help/faqs.md) | TODO | - | skeleton |
| [`/app/help/handle_survey_popup`](help/handle_survey_popup.md) | TODO | - | skeleton |
| [`/app/help/manual_list`](help/manual_list.md) | TODO | - | skeleton |
| [`/app/help/product_tutorial_search`](help/product_tutorial_search.md) | TODO | - | skeleton |
| [`/app/help/scan_code_white_list`](help/scan_code_white_list.md) | TODO | - | skeleton |
| [`/app/help/xtest/data`](help/xtest/data.md) | TODO | - | skeleton |
| [`/app/logging/get_device_logging`](logging/get_device_logging.md) | TODO | - | skeleton |
| [`/app/logging/upload`](logging/upload.md) | TODO | - | skeleton |
| [`/app/logging/upload_pb_events`](logging/upload_pb_events.md) | TODO | - | skeleton |
| [`/app/news/get_popups`](news/get_popups.md) | TODO | - | skeleton |
| [`/app/news/popup_record`](news/popup_record.md) | TODO | - | skeleton |
| [`/app/ota/batch/check_update`](ota/batch/check_update.md) | TODO | `get_ota_batch` | skeleton |
| [`/app/push/clear_count`](push/clear_count.md) | TODO | - | skeleton |
| [`/app/push/register_push_token`](push/register_push_token.md) | TODO | - | skeleton |

Not here: MQTT or BLE facts (see [../../mqtt/README.md](../../mqtt/README.md), [../../ble/README.md](../../ble/README.md)), step-by-step flows ([../../flows/README.md](../../flows/README.md)); ownership rules are in [../../docs/STRUCTURE.md](../../docs/STRUCTURE.md).
