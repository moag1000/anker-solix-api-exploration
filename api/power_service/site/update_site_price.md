> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# update_site_price

## Purpose

<!-- TODO -->

## Upstream name

`update_site_price` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/site/update_site_price`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x279e384`
(literal also at 8 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify" / `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x279e0cc` |
| `price` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x279e0cc` |
| `site_co2` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x279e0cc` |
| `site_price_unit` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x279e0cc` |
| `price_type` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x279e0cc` |
| `current_mode` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x279e0cc` |
| `accuracy` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x279e0cc` |
| `device_sn` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x41a7afc` |
| `attributes.price_type` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x41a7afc` |
| `attributes.fixed_price` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x41a7afc` |
| `attributes.currency` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x41a7afc` |
| `id` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x41a7afc` |
| `buy` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x41a7afc` |
| `sell` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x41a7afc` |
| `energy_unit` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x41a7afc` |
| `start_time_period` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x41a7afc` |
| `end_time_period` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x41a7afc` |
| `peak_type` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x41a7afc` |
| `day_type` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x41a7afc` |

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

- `charging/http/http_request_repository_impl.dart`: `postCloudSitePrice` @0x31e4050 (encryptionRequestHttp; encrypted: true); `updateSitePriceRequest` @0x279e0cc (encryptionRequestHttp; encrypted: true)
- `electricity_price/components/electricity_price_common/electricity_price_plan_api_helper.dart`: `saveMediumChargingPlan` @0x41a73e0 (encryptionRequestHttp; encrypted: true)
- `electricity_price/components/electricity_price_common/electricity_usage_helper.dart`: `getSaveDeviceEMSPrice` @0x249e420 (URL literal only, no `*Http*` call; sender found through callers: `ElectricityUsageHelper::setDeviceEMSPriceArgument` (`electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x249e2cc`) via `ElectricityUsageHelper::setDeviceEMSPriceArgument` (`electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x249e2cc`))
- `electricity_price/components/electricity_price_common/view/tou_plan_logic.dart`: `savePlan` @0x31b88b4 (encryptionRequestHttp; encrypted: true)
- `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart`: `setFixedPrice` @0x41a7afc (encryptionRequestHttp; encrypted: true)
- `electricity_price/components/tou/impl_v2/service/tou_http_service.dart`: `updateSitePrice` @0x4883d48 (request; encrypted: default-true (requestHttp) — verify)
- `electricity_price/components/tou/page/tou_detail/view/tou_edit_preview_logic.dart`: `<anonymous closure> in TOUEditPreviewLogic::savePlan` @0x31df304 (URL literal only, no `*Http*` call; no sender within 3 caller levels); `savePlan` @0x31de7dc (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/feature/peak_valley/confirm/confirm_peak_valley_logic.dart::setSitePrice`
- `charging/feature/utilitiy_rate_plan/dynamic_price/confirm/dynamic_price_confirm_logic.dart::save`
- `charging/feature/utilitiy_rate_plan/fixed_rate/fixed_rate_v2_logic.dart::save`
- `charging/feature/utilitiy_rate_plan/station_price_mode/station_price_mode_logic.dart::setSitePrice`
- `charging/http/http_request_repository.dart::postCloudSitePrice`
- `charging/http/http_request_repository.dart::updateSitePriceRequest`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/electricity_price/electricity_price_logic.dart::savePrice`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/utility_rate_plan/site_utility_rate_logic.dart::save`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/utility_rate_plan/site_utility_rate_plan_logic.dart::setTOUPrice`
- `charging/ui/page/device/main/station_device_home/station_price_setting/station_price_setting_logic.dart::savePrice`
- `electricity_price/components/electricity_price_common/electricity_usage_helper.dart::setDeviceEMSPriceArgument`
- `electricity_price/components/electricity_price_common/view/tou_plan_logic.dart::clickSeasonItem`
- `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart::setFixedPriceV2`
- `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart::setTOU`
- `electricity_price/components/tou/impl_v2/repository/medium_tou_repository.dart::saveTouPlan`
- `electricity_price/components/tou/impl_v2/repository/platform_tou_repository.dart::saveTouPlan`
- `electricity_price/components/tou/page/tou_detail/view/tou_edit_preview_logic.dart::onDoneClick`
- `electricity_price/components/tou_pct/page/electricity_price_pad_preview/electricity_price_pad_preview_logic.dart::setSitePrice`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
