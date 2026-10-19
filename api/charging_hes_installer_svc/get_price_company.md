> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_price_company

## Purpose

Reads the list of dynamic-price and time-slot providers (companies) available for a product or site, with the provider the user has already selected; it is the first call of the dynamic-price and time-of-use setup pages.

## Upstream name

`none` for the installer URL (no upstream name). The consumer twin `/charging_hes_dynamic_price_svc/get_price_company` is listed without a key in `api/apitypes.py` (line 477, comment "needs owner").

## Method+URL

`POST /charging_hes_installer_svc/get_price_company` (asm-traced). The URL comes from the static getter `Api.getPriceCompany` (`base_service/api_url.dart @0x27bde38`): installer string `pp+0x675d0` (`@0x27bde44`) when `isProApp` is true, otherwise `/charging_hes_dynamic_price_svc/get_price_company` (`pp+0x675d8`, `@0x27bde50`); see [the variant selector](README.md#variant-selector-installer-app-versus-consumer-app). Fourteen sender functions load the field (table under "Callers in app"). The ones in the `electricity_price` package go through `HttpHelper.getDataFromService`, which calls `encryptionRequestHttp` with `Method.post` (pool entry `pp+0xa7e0`, `electricity_price/components/electricity_price_common/http/http_helper.dart @0x27bdb94`); the ones in `ak_soft_ems` and `charging` call `encryptionRequestHttp` themselves with `Method.post`.

## Encrypted?

Yes by wrapper (asm-traced): every sender ends in `encryptionRequestHttp` (`HttpHelper::getDataFromService`, `http_helper.dart @0x27bdbc8`, or a direct call, addresses in the table under "Callers in app") without `needEncryption`, so the default `true` applies (`api/encryption.md`, [which calls are encrypted](../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time; asm alone does not decide it.

## Request

Every sender builds a small map literal. The common shape is `pn` plus either `sn` (a device) or `siteId` (a site), optionally `type`; the three senders in `ak_soft_ems` and `charging` send only `siteId` and `pn`. Key literals are cited per sender in the table under "Callers in app".

| field | type | required | example | source |
|---|---|---|---|---|
| `pn` | String | yes | `"A17C5"` | first pair of every sender; value is the product code of the object (`electricity_price_provider_logic.dart @0x29a77ec`, value field read at `@0x29a7804`) or a literal: `"A5101"` (`system_policy_logic.dart @0x28eb554`), `"A17C5"` (`power_usage_scenario_logic.dart @0x28a19d8`) |
| `sn` | String | one of `sn` / `siteId` | `"<device sn>"` | `electricity_price_provider_logic.dart @0x29a7874`, set when a mode flag is true and the device serial is non-empty (`@0x29a7850` to `@0x29a785c`) |
| `siteId` | String | one of `sn` / `siteId` | `"<site id>"` | `electricity_price_provider_logic.dart @0x29a78a8`, set otherwise; the `ak_soft_ems` and `charging` senders set only this key (`@0x2a2f044`, `@0x37b1b8c`, `@0x28eb4d4`, `@0x28a1a9c`) |
| `type` | int | no | `1` | `electricity_price_provider_logic.dart @0x29a78f4`; raw `2` (`@0x29a78fc`) stored with `stur w16`, Smi, so 1 (`tools/smi.py`); added with `addAll` only when a condition holds (`@0x29a78e4`, `@0x29a7918`) |
| `isSetDynamicPrice` | unknown | no | not decoded | `tou_and_timeslot_settings_poly_logic.dart @0x29b1d2c` (`queryHasSetTimeSlot`); the value was not decoded |

`device_sn` is read (not set) from the page arguments in `dynamic_price_detail_info_view.dart @0x27cf244` and the C5 variant; the same function sets a key `site_id` (`@0x27cf340`, C5 `@0x27cf6e4`) before `siteId`, and which map receives it, and whether it reaches the request body, was not resolved. `electricityPriceUseTypeInterface` (`@0x27cf0f0`) is a page argument read, not a request key.

## `param_type`/`cmd`

n/a

## Response model (link)

`DynamicPriceCompanyModel` ([../../models/dynamic_price_company_model.md](../../models/dynamic_price_company_model.md)), parsed with `DynamicPriceCompanyModel.fromJson` (`dynamic_price_company_model.dart @0x27b94ac`) in the success closure of ten of the senders (list on the model page). The other senders (`getDynamicPriceShowOrNot`, `queryHasSetTimeSlot`, `_supportAutoTou`, `_supportTimeslot`) also call `fromJson` (`general_price_setting.dart @0x27d25a4`, `tou_and_timeslot_settings_detail_logic.dart @0x27b90cc`, `electricity_price_serviceImpl.dart @0x2891e78`, `@0x2892498`) but only to test whether a provider list or a user selection exists.

## Response

All fields live in the model (wrapper `code`, `msg`, `data` as in [../encryption.md](../encryption.md#response-handling-and-error-codes)). The success closures receive the payload and pass it to `fromJson` without reading further keys.

## Example request/response

Request, synthesized

```json
{ "pn": "A17C5", "siteId": "<site id>" }
```

Response: no captured response; the key list is on the model page.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or shows a toast; the shared transport codes are in [../encryption.md](../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../errors.md).

## Callers in app

| sender (file `@0xADDR` of the function) | UI page | key literals (`@0xADDR`) |
|---|---|---|
| `ElectricityPriceProviderLogic.getDynamicPriceCompany` (`electricity_price/components/dynamic_price/setting/electricity_price_provider_logic.dart @0x29a77ac`; field load `@0x29a7930`) | provider selection page of the dynamic price setup | `pn @0x29a77ec`, `sn @0x29a7874`, `siteId @0x29a78a8`, `type @0x29a78f4` |
| `ElectricityCompanySelectLogic.getDynamicPriceCompany` (`electricity_price/components/dynamic_price/setting/electricty_company_select_logic.dart @0x29aaab4`; `@0x29aabe0`) | company selection page | `pn @0x29aaaf4`, `sn @0x29aab84`, `siteId @0x29aabb8` |
| `getDynamicPriceCompany` (`electricity_price/components/fixed_price/general_electricity_price_settting/dynamic_price_detail_info_view.dart @0x27cf088`; `@0x27cf394`) and the C5 variant (`dynameic_price_detail_info_view_c5.dart @0x27cf46c`; `@0x27cf738`) | dynamic price detail page | `pn @0x27cf180`, `sn @0x27cf2f4`, `siteId @0x27cf36c` (C5: `@0x27cf52c`, `@0x27cf698`, `@0x27cf710`) |
| `getDynamicPriceShowOrNot` (`electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x27d2300`; `@0x27d245c`) | general price setting page | `pn @0x27d2340`, `sn @0x27d2410`, `siteId @0x27d2438` |
| `queryHasSetTimeSlot` (`electricity_price/components/electricity_module/page/tou_and_timeslot_settings_detail_logic.dart @0x27bd8a0`; `@0x27bd9cc`) and the poly variant (`tou_and_timeslot_settings_poly_logic.dart @0x29b1c04`; `@0x29b1d58`) | TOU and time-slot settings pages | `pn @0x27bd8e0`, `sn @0x27bd970`, `siteId @0x27bd9a4` (poly: `@0x29b1c44`, `@0x29b1cd4`, `@0x29b1d08`, `isSetDynamicPrice @0x29b1d2c`) |
| `_supportAutoTou` (`electricity_price/components/electricity_module/electricity_price_serviceImpl.dart @0x2891a84`; `@0x2891d2c`), `_supportTimeslot` (`@0x2892148`; `@0x28923e8`) | capability checks of the price module | `pn @0x2891c58`, `sn @0x2891cd0`, `siteId @0x2891d04`; `@0x289231c`, `@0x289238c`, `@0x28923c0` |
| `getDynamicPriceCompany` (`electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x29b6424`; `@0x29b64cc`) and the C5 variant (`charge_discharge_setting_logic_c5.dart @0x29b78bc`; `@0x29b7964`) | charge/discharge time-slot settings | `siteId @0x29b6464`, `pn @0x29b6484` (C5: `@0x29b78fc`, `@0x29b791c`) |
| `PowerUsageScenarioController.getDynamicPriceCompany` (`ak_soft_ems/ems_list/power_usage_scenario_controller.dart @0x2a2efb8`; call `@0x2a2f114`) and `_requestDynamicPriceCompany` (`@0x37b1a70`; call `@0x37b1c2c`) | power usage scenario (EMS) screen | `siteId @0x2a2f044`, `pn @0x2a2f060`; `siteId @0x37b1b8c`, `pn @0x37b1ba0` |
| `SystemPolicyLogic._getDynamicPriceCompany` (`charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart @0x28eb470`; call `@0x28eb5fc`) | A5101 system policy page | `siteId @0x28eb4d4`, `pn @0x28eb514` (literal `"A5101"` `@0x28eb554`) |
| `PowerUsageScenarioLogic._requestDynamicPriceCompany` (`charging/ui/page/device/main/sitation_energy_system/station_home_settings/power_usage_scenario/power_usage_scenario_logic.dart @0x28a1960`; call `@0x28a1b3c`) | power usage scenario page of the station settings | `siteId @0x28a1a9c`, `pn @0x28a1ab0` (literal `"A17C5"` `@0x28a19d8`) |

Field-load addresses are given after each function as the second address; where a sender calls `HttpHelper.getDataFromService` the call is at `getDataFromService()` in the same function (for example `@0x29a797c`).

## Since/changed

3.18.0: absent as an installer URL (the 3.18.0 pool holds no `installer_svc` string); the consumer twin `/charging_hes_dynamic_price_svc/get_price_company` is in the 3.18.0 pool. 3.24.3: present (new). since: 3.24.3. `DynamicPriceCompanyModel` exists in 3.18.0; its key changes are on the model page.

## Known unknowns

- Server behaviour and the meaning of `type` and `isSetDynamicPrice` are not known.
- The sources of the `pn` and `sn`/`siteId` values are named only for the three literal cases; the object fields behind the others are not named in the asm.
- Whether the installer server answers the consumer-style keys (`pn`, `siteId`) the same way is not tested; this body has no `isProApp` branch.

## Device-tested by

none
