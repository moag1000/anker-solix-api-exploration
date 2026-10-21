> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_price

## Purpose

Reads the price table of a site for one provider: the time-of-use price seasons or the dynamic hourly prices of today and tomorrow; the price preview and time-slot pages use it to draw the prices.

## Upstream name

`none` for the installer URL (no upstream name). The consumer twin `/charging_hes_dynamic_price_svc/get_price` is listed without a key in `api/apitypes.py` (line 478, comment "needs owner").

## Method+URL

`POST /charging_hes_installer_svc/get_price` (asm-traced). The URL comes from the static getter `Api.getPrice` (`base_service/api_url.dart @0x2554b74`): installer string `pp+0x81730` (`@0x2554b80`) when `isProApp` is true, otherwise `/charging_hes_dynamic_price_svc/get_price` (`pp+0x81738`, `@0x2554b8c`); see [the variant selector](README.md#variant-selector-installer-app-versus-consumer-app). Ten sender functions load the field (table under "Callers in app"); the `electricity_price` senders use `HttpHelper.getDataFromService` (`Method.post`, `electricity_price/components/electricity_price_common/http/http_helper.dart @0x27bdb94`), the others call `encryptionRequestHttp` with `Method.post` themselves.

## Encrypted?

Yes by wrapper (asm-traced): every sender ends in `encryptionRequestHttp` (`HttpHelper::getDataFromService`, `http_helper.dart @0x27bdbc8`, or a direct call) without `needEncryption`, so the default `true` applies (`api/encryption.md`, [which calls are encrypted](../encryption.md#which-calls-are-encrypted)). Whether the call goes through the SDK is decided at run time; asm alone does not decide it.

## Request

Map literals built per sender. The common core is `companyName` (the provider name), `type` and `sn` or `siteId`; the time-slot senders add the user parameters of the chosen provider.

| field | type | required | example | source |
|---|---|---|---|---|
| `companyName` | String | yes | `"<provider name>"` | every sender, for example `dynamic_price_detail_info_view.dart @0x27d1928`; the value comes from the selected provider of the page |
| `type` | int | yes | `2` | `dynamic_price_detail_info_view.dart @0x27d1970`, raw `4` (`@0x27d1978`) stored with `stur w16`, Smi, so 2; the same raw 4 at `dynameic_price_detail_info_view_c5.dart @0x27d0094`, `timeslot_preview_poly_logic.dart @0x2c52060`, `timeslot_preview_logic.dart @0x2c560c4`, `power_usage_scenario_controller.dart @0x2554a84`, `system_policy_logic.dart @0x28ec238`, `power_usage_scenario_logic.dart @0x28a2008` (each `tools/smi.py`: 4, `stur w`, 2). `tou_auto_price_pkg_result_logic.dart @0x2c48a70` sends raw `2`, Smi, so 1 |
| `sn` | String | one of `sn` / `siteId` | `"<device sn>"` | `dynamic_price_detail_info_view.dart @0x27d1b3c`, `tou_auto_price_pkg_result_logic.dart @0x2c48aec`, `charge_discharge_setting_logic.dart @0x29b2d20`, `timeslot_preview_poly_logic.dart @0x2c520cc`, `timeslot_preview_logic.dart @0x2c56138` |
| `siteId` | String | one of `sn` / `siteId` | `"<site id>"` | `dynamic_price_detail_info_view.dart @0x27d1b68`, and as the only id key in `power_usage_scenario_controller.dart @0x2554a60`, `system_policy_logic.dart @0x28ec1f0`, `power_usage_scenario_logic.dart @0x28a1fec` |
| `pn` | String | no | `"A5101"` | only the three non-package senders: `power_usage_scenario_controller.dart @0x2554aa0`, `system_policy_logic.dart @0x28ec278` (literal `"A5101"` `@0x28ec2b8`), `power_usage_scenario_logic.dart @0x28a2024` |
| `userNordpoolParam`, `userOctopusParam` | map | no | not decoded | `dynamic_price_detail_info_view.dart @0x27d1b98`, `@0x27d1c10`: the provider parameter objects of the user selection, see [../../models/dynamic_price_company_model.md](../../models/dynamic_price_company_model.md) |
| `dynamicPriceParam` | map | no | not decoded | `charge_discharge_setting_logic.dart @0x29b2ed4` (set three times, `@0x29b33c0`, `@0x29b34f0`, one per branch), `timeslot_preview_poly_logic.dart @0x2c526dc`; the value is built from the time-slot form |
| entries of `providerParams` | map entries | no | not decoded | `tou_auto_price_pkg_result_logic.dart @0x2c48b40`, `charge_discharge_setting_logic.dart @0x29b3510`: `providerParams` is read from the page arguments and merged into the body (same pattern as in [save_dynamic_price](save_dynamic_price.md#request)) |

`chargeNum` and `dischargeNum` are read (not set) by `timeslot_preview_poly_logic.dart` (`@0x2c524d0`, `@0x2c5257c`); they are request keys only of [save_dynamic_price](save_dynamic_price.md#request). `userNordpoolParam` and `userOctopusParam` are keys of map literals built in the same function; that map is the body is inferred from the call that follows.

## `param_type`/`cmd`

n/a

## Response model (link)

`ElectricityPriceModel` ([../../models/electricity_price_model.md](../../models/electricity_price_model.md)), parsed with `ElectricityPriceModel.fromJson` (`electricity_price_model.dart @0x255111c`) in the success closure of every sender (addresses on the model page).

## Response

All fields live in the model (wrapper `code`, `msg`, `data` as in [../encryption.md](../encryption.md#response-handling-and-error-codes)). The success closures pass the payload to `fromJson`.

## Example request/response

Request, synthesized

```json
{ "companyName": "<provider name>", "type": 2, "siteId": "<site id>", "pn": "A5101" }
```

Response: no captured response; the key list is on the model page.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or shows a toast; the shared transport codes are in [../encryption.md](../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../errors.md).

## Callers in app

| sender (file `@0xADDR` of the function) | UI page |
|---|---|
| `getTodayAndTomorrowPrice` (`electricity_price/components/fixed_price/general_electricity_price_settting/dynamic_price_detail_info_view.dart @0x27d184c`; field load `@0x27d1d04`) and the C5 variant (`dynameic_price_detail_info_view_c5.dart @0x27cff68`; `@0x27d03a8`) | dynamic price detail page |
| `TOUAutoPricePkgResultLogic.getData` (`electricity_price/components/electricity_price_common/tou_auto_preview/tou_auto_price_pkg_result_logic.dart @0x2c489dc`; `@0x2c48be0`) | auto TOU result preview |
| `getElectricityPrice` (`electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x29b2c00`; `@0x29b35b0`) and the C5 variant (`charge_discharge_setting_logic_c5.dart @0x29b3774`; `@0x29b4118`) | charge/discharge time-slot settings |
| `getPriceDetail` (`electricity_price/components/timeslot/view/timeslot_preview_poly_logic.dart @0x2c51e8c`; `@0x2c52704`) and `timeslot_preview_logic.dart @0x2c56060` (`@0x2c56194`) | time-slot price preview |
| `PowerUsageScenarioController.getPriceDetail` (`ak_soft_ems/ems_list/power_usage_scenario_controller.dart @0x25549d0`; `@0x2554a40`; call `@0x2554b54`) | power usage scenario (EMS) screen |
| `SystemPolicyLogic.getPriceDetail` (`charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart @0x28ec184`; `@0x28ec1d0`; call `@0x28ec360`) | A5101 system policy page |
| `PowerUsageScenarioLogic._requestDynamicPriceInfo` (`charging/ui/page/device/main/sitation_energy_system/station_home_settings/power_usage_scenario/power_usage_scenario_logic.dart @0x28a1f44`; `@0x28a2060`; call `@0x28a20d4`) | power usage scenario page of the station settings |

## Since/changed

3.18.0: absent as an installer URL (the 3.18.0 pool holds no `installer_svc` string); the consumer twin `/charging_hes_dynamic_price_svc/get_price` is in the 3.18.0 pool. 3.24.3: present (new). since: 3.24.3. The model classes `DynamicPrice`, `Prices` and `PeakValleyPrices` are new in 3.24.3 (model page).

## Known unknowns

- The meaning of `type` (values 1 and 2 after the Smi rule) is not documented.
- The values of the provider parameter maps are not decoded here; their shape follows the provider objects of [get_price_company](get_price_company.md). — traced 2026-10-20: the provider objects are listed with their keys on [the company model page](../../models/dynamic_price_company_model.md); the value types of the entries stay as documented there
- Server behaviour is not known.

## Device-tested by

none
