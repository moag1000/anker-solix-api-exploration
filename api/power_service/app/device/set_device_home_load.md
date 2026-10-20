> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# set_device_home_load

## Purpose

Writes the home-load (backup/priority load) configuration of a device or site from the back-power, peak-valley and A1782 system-policy pages (callers `BackPowerLogic::onDoneClick`, `ConfirmPeakValleyLogic::onDoneClick`, `A1782SystemPolicyLogic::setMode`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`set_device_load` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/device/set_device_home_load` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x2631510`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2631508`, in `HttpRequestControllerImpl::set17C1DeviceHomeLoadRes` (`charging/http/http_request_repository_impl.dart @0x26313ac`), sent through `encryptionRequestHttp` (`@0x2631538`).

Same URL and method object in the other sender(s) read:

- `POST /power_service/v1/app/device/set_device_home_load` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x274a518`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x274a510`, in `HttpRequestControllerImpl::setDeviceHomeLoadRes` (`charging/http/http_request_repository_impl.dart @0x274a458`), sent through `encryptionRequestHttp` (`@0x274a540`).

## Encrypted?

encrypted: "default-true (requestHttp) — verify" / `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) Six senders were found; two `HttpRequestControllerImpl` senders were read. `setDeviceHomeLoadRes` (`charging/http/http_request_repository_impl.dart @0x274a458`) sends `{device_sn, home_load_data}` in a `<String, String>` literal (`@0x274a4cc`, raw `r2 = 8` at `@0x274a49c`), so both values are Strings. `set17C1DeviceHomeLoadRes` (`@0x26313ac`) sends 4 pairs in a `<String, Object>` literal (`@0x26314c4`, raw `r2 = 16` at `@0x2631400`): `device_sn`, `mode_type`, `custom_rate_plan` (a list of `CustomRatePlanModel`; a null value is replaced by an empty list, null check `@0x2631464`, length `r2 = 0` `@0x2631474`) and `home_load_data` = `""` (`@0x26314bc`). `TouHttpService::setDeviceHomeLoad` sends `home_load_data` as `jsonEncode` output; `postCloudSiteOrDeviceEms` and `ElectricityUsageHelper` build their bodies elsewhere.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | `charging/http/http_request_repository_impl.dart @0x274a4a4` |
| `home_load_data` | string | yes | `"<home_load_data>"` | `charging/http/http_request_repository_impl.dart @0x274a4b8` |
| `mode_type` | ? | yes (`set17C1DeviceHomeLoadRes` only) | ? | `charging/http/http_request_repository_impl.dart @0x2631424` |
| `custom_rate_plan` | ? | yes (`set17C1DeviceHomeLoadRes` only) | ? | `charging/http/http_request_repository_impl.dart @0x263144c` |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed in the builders read (asm-traced): both pass forwarding closures that hand the response object to the caller; no `fromJson` or response key is read in them.

## Response

Not read in the builders read.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<device_sn>",
  "home_load_data": "<home_load_data>"
}
```

Response: not synthesized (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `postCloudSiteOrDeviceEms` @0x3d8864c (encryptionRequestHttp; encrypted: true); `set17C1DeviceHomeLoadRes` @0x26313ac (encryptionRequestHttp; encrypted: true); `setDeviceHomeLoadRes` @0x274a458 (encryptionRequestHttp; encrypted: true)
- `electricity_price/components/electricity_price_common/electricity_usage_helper.dart`: `getSetElectricityUsagePolicyUrl` @0x31b9e50 (URL literal only, no `*Http*` call; sender `ElectricityUsageHelper::setSiteTOUDetail` (`electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x31b90a0`), a callee called after the URL load in `ElectricityUsageHelper::setManualSetTOUDetail` (`electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x31b8da8`); resolved from the URL literal at `electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x31b9e88` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md)); `setManualSetTOUDetail` @0x31b8da8 (URL literal only, no `*Http*` call; sender `ElectricityUsageHelper::setSiteTOUDetail` (`electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x31b90a0`), a callee called after the URL load in the same function; resolved from the URL literal at `electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x31b8fb8` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))
- `electricity_price/components/tou/impl_v2/service/tou_http_service.dart`: `setDeviceHomeLoad` @0x4882f10 (request; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/feature/backup_power/back_power_logic.dart::onDoneClick`
- `charging/feature/peak_valley/confirm/confirm_peak_valley_logic.dart::onDoneClick`
- `charging/http/http_request_repository.dart::postCloudSiteOrDeviceEms`
- `charging/http/http_request_repository.dart::set17C1DeviceHomeLoadRes`
- `charging/http/http_request_repository.dart::setDeviceHomeLoadRes`
- `charging/ui/page/device/a1782/station/system_policy/a1782_system_policy_logic.dart::setMode`
- `charging/ui/page/device/a17c0/a17c0energyPlan/a17c0energy_plan_logic.dart::setDeviceHomeLoadData`
- `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart::_dealWithBleResponse`
- `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart::closeBackPower`
- `charging/ui/page/device/a17c1/energy_deploy/energy_deploy_logic.dart::saveHomeLoadData`
- `charging/ui/page/device/a17c1/energy_plan/energy_plan_logic.dart::deleteHomeLoadData`
- `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart::closeBackPower`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/merge_system_energy/merge_system_energy_plan_logic.dart::deleteHomeLoadData`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/power_usage_scenario/ae100/custom_mode_usage_scenario_logic.dart::showModeUpgradeDialog`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/power_usage_scenario/ae100/detail/custom_mode_usage_scenario_detail_logic.dart::_saveToDeviceAndCloud`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/power_usage_scenario/power_usage_scenario_logic.dart::closeBackPower`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/power_usage_scenario/power_usage_scenario_logic.dart::setHomeLoadSiteParam`
- `electricity_price/components/electricity_price_common/electricity_usage_helper.dart::setManualSetTOUDetail`
- `electricity_price/components/electricity_price_common/view/tou_plan_logic.dart::savePlan`
- `electricity_price/components/tou/impl_v2/repository/charging_pile_tou_repository.dart::saveTouPlan`
- `electricity_price/components/tou/page/tou_detail/view/tou_edit_preview_logic.dart::saveMode`
- `electricity_price/components/tou/page/tou_detail/view/tou_edit_preview_logic.dart::savePlan`
- `electricity_price/components/tou/page/tou_result_view/tou_result/tou_result_logic.dart::_cyclePowerResultCallback`
- `electricity_price/components/tou/page/tou_result_view/tou_result/tou_result_logic.dart::saveMode`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What `home_load_data` contains (a String in `setDeviceHomeLoadRes`, empty in `set17C1DeviceHomeLoadRes`, `jsonEncode` output in `TouHttpService`): the structure is decided by the callers.
- Types of `mode_type` and `custom_rate_plan`, and the body of `postCloudSiteOrDeviceEms` (no keys found by the extractor).
- The response: forwarded; the callers were not decoded.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
