> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# save_dynamic_price

## Purpose

Saves the dynamic-price (or time-slot) configuration of a site for one provider: the app sends the provider name, the set/unset switch, the site or device id and the provider-specific parameter objects chosen on the setup pages.

## Upstream name

`none` for the installer URL (no upstream name). The consumer twin `/charging_hes_dynamic_price_svc/save_dynamic_price` is listed without a key in `api/apitypes.py` (line 480, comment "needs owner").

## Method+URL

`POST /charging_hes_installer_svc/save_dynamic_price` (asm-traced). The URL comes from the static getter `Api.saveDynamicPrice` (`base_service/api_url.dart @0x2e82b34`): installer string `pp+0x8aa20` (`@0x2e82b40`) when `isProApp` is true, otherwise `/charging_hes_dynamic_price_svc/save_dynamic_price` (`@0x2e82b4c`); see [the variant selector](README.md#variant-selector-installer-app-versus-consumer-app). Twelve sender functions load the field (table under "Callers in app"); all use `Method.post` (pool entry `pp+0xa7e0`). The Tibber sender goes through `HttpHelper.getDataFromServiceV2` (`http_helper.dart @0x4393090`, `encryptionRequestHttp` `@0x4393190`, `showLoading: true`).

## Encrypted?

Yes by wrapper (asm-traced): every sender ends in `encryptionRequestHttp`, directly or inside `HttpHelper.getDataFromService` / `getDataFromServiceV2` (`http_helper.dart @0x27bdbc8`, `@0x4393190`), without `needEncryption`, so the default `true` applies (`api/encryption.md`, [which calls are encrypted](../encryption.md#which-calls-are-encrypted)). Whether the call goes through the SDK is decided at run time; asm alone does not decide it.

## Request

One body per setup flow. Every sender builds a small map first (provider name, switch, id) and then adds provider-specific members. The id member is chosen the same way everywhere: `sn` when a device serial exists and is non-empty, otherwise `siteId` (both set with `[]=`).

| field | type | required | example | source |
|---|---|---|---|---|
| `companyName` | String | yes | `"Tibber"`, `"Flatpeak"` | map literal key in every sender except the two helpers: `electricity_price/components/dynamic_price/general_kit/http_server/dynamic_price_http_server.dart @0x4392eb0` (Tibber), `electricty_place_confirm_logic.dart @0x4397bc4`, `@0x4397f74`, `electricty_company_select_logic.dart @0x41e04f8`, `@0x4396be8`, `electricity_price_provider_logic.dart @0x41dfb48`, `tou_and_timeslot_settings_poly_logic.dart @0x43a2c50`, `charge_discharge_setting_logic.dart @0x41b4700` (C5 `@0x41b5758`), `custom_time_period_controller.dart @0x41c6ed0`. The literal values `"Tibber"` (`@0x4392ebc`) and `"Flatpeak"` (`@0x4397bd0`, `@0x4397f80`, `@0x41e0504`, `@0x4396bf4`) are fixed in those senders; the others send the selected provider's name from a field |
| `setMode` | bool | yes | `true` | map literal key in every sender: `dynamic_price_http_server.dart @0x4392ec8` (value `false`, `@0x4392ed4`), `electricty_place_confirm_logic.dart @0x4397bdc`, `@0x4397f8c`, `electricty_company_select_logic.dart @0x41e0510`, `@0x4396c00`, `electricity_price_provider_logic.dart @0x41dfb90`, `tou_and_timeslot_settings_poly_logic.dart @0x43a2c6c`, `charge_discharge_setting_logic.dart @0x41b4720` (C5 `@0x41b5778`), `custom_time_period_controller.dart @0x41c6eec`, `electricity_price_model_api_helper.dart @0x2e82a14`, `electricity_price_plan_api_helper.dart @0x41a64e8`; the other values are not listed here |
| `sn` | String | one of `sn` / `siteId` | `"<device sn>"` | set in every sender, for example `dynamic_price_http_server.dart @0x4392f28` |
| `siteId` | String | one of `sn` / `siteId` | `"<site id>"` | set in every sender, for example `dynamic_price_http_server.dart @0x4392f48` |
| entries of `providerParams` | map entries | no | not decoded | read from the page arguments, cast to `Map` and merged into the body entry by entry: `electricity_price_provider_logic.dart @0x41dfc64` with the `forEach` closure `@0x41e1358` (key cast to `String`, then `[]=`); the same read at `electricty_company_select_logic.dart @0x41e063c`, `@0x4396d2c`, `electricty_place_confirm_logic.dart @0x43981ec`, `tou_and_timeslot_settings_poly_logic.dart @0x43a328c`, `charge_discharge_setting_logic.dart @0x41b5374`, C5 `@0x41b5e00`. The page `ElectricityPriceProviderLogic.next` fills `providerParams` with `company`, `area`, `country`, `sellProduct`, `currentSellType`, `userNordpoolParam`, `userOctopusParam` and `periodInterval` (`@0x41df734` to `@0x41df978`) |
| `userTibberParam` | map | Tibber only | not decoded | `dynamic_price_http_server.dart @0x4392f74`; the value is `toJson` of the provider object (`@0x4392f68`), fields `code` and `hasError` on [the model page](../../models/dynamic_price_company_model.md) (class `UserTibberParam`) |
| `userInfo` | map | Flatpeak confirm | not decoded | `electricty_place_confirm_logic.dart @0x4397d44` (`save`), `@0x4398184` (`saveDynamicPrice`); fields (`longitude`, `latitude`, `city`, `street`, `zipCode`, `onlySaveUserInfo`) on the model page (class `UserInfo`) |
| `userFlatpeakParam` | map | Flatpeak confirm | not decoded | `electricty_place_confirm_logic.dart @0x43981cc` |
| `aggregationFrequency` | int | no | not decoded | `electricty_place_confirm_logic.dart @0x43981ac` (value not decoded) |
| `dynamicPriceParam` | map | time-slot flows | not decoded | `tou_and_timeslot_settings_poly_logic.dart @0x43a326c`, `charge_discharge_setting_logic.dart @0x41b5030`, C5 `@0x41b5de0` |
| `chargeTimeList`, `chargeDisTimeList` | list | charge/discharge settings | not decoded | `charge_discharge_setting_logic.dart @0x41b5230`, `@0x41b525c` |
| `chargeNum`, `dischargeNum` | int | charge/discharge settings | not decoded | `@0x41b528c`, `@0x41b52bc` |
| `export2Grid`, `cutoffPower` | not decoded | charge/discharge settings | not decoded | `@0x41b5300`, `@0x41b534c` |

The `custom_time_period_controller.dart` sender (`saveChargeTimes`) sets `sn`/`siteId` and also uses the strings `today` and `tomorrow` (`@0x41c7010`, `@0x41c701c`); how they enter the body (as keys or as values) was not decoded. The two helpers `ElectricityPriceModelApiHelper.changeToTimeSlotMode` and `ElectricityPricePlanApiHelper.changeToDynamicPlan` send only `setMode`, `sn` / `siteId` (no provider name). No integer literal was identified as a body value in these senders; integers inside the function bodies (for example the raw `120` at `charge_discharge_setting_logic.dart @0x41b4d70`) were not traced to a body key and are not reported here, so no Smi table applies to this page.

## `param_type`/`cmd`

n/a

## Response model (link)

`SaveDynamicPriceResponse` ([../../models/dynamic_price_server_model.md](../../models/dynamic_price_server_model.md)), parsed with `SaveDynamicPriceResponse.fromJson` (`dynamic_price_server_model.dart @0x4393690`) at `dynamic_price_http_server.dart @0x4393624`, the Tibber sender only.

## Response

Wrapper keys `code`, `msg`, `data` as in [../encryption.md](../encryption.md#response-handling-and-error-codes). Tibber sender: the payload goes to `SaveDynamicPriceResponse.fromJson` (`messageId`, `flatpeakSetting`). The Flatpeak confirm sender (`electricty_place_confirm_logic.dart`, success closure `@0x4398348`) reads the raw map:

| field | type | required | example | source |
|---|---|---|---|---|
| `flatpeakSetting` | map | no | `{ ... }` | `@0x4398424`; the closure checks `Map<String, dynamic>` (`@0x4398458`) |
| `flatpeakSetting.buyCompany`, `.sellCompany`, `.buyType`, `.sellType` | String | no | not decoded | `@0x4398490`, `@0x4398514`, `@0x4398640`, `@0x43986d0`; the app then fires an event bus message `codePriceTypeChanged` (log text `@0x4398874`) |

The other senders ignore the answer apart from success or failure (failure closures show a `saveFailedToast`, for example `electricty_place_confirm_logic.dart @0x4397ee4`).

## Example request/response

Request, synthesized (Tibber sender)

```json
{ "companyName": "Tibber", "setMode": false, "siteId": "<site id>", "userTibberParam": { "code": "<code>", "hasError": false } }
```

Response: no captured response; the key list is on the model page.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or shows a toast; the shared transport codes are in [../encryption.md](../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

| sender (function `@0xADDR`) | UI page | call `@0xADDR` |
|---|---|---|
| `_DynamicPriceHttpServer.saveDynamicPrice` (`electricity_price/components/dynamic_price/general_kit/http_server/dynamic_price_http_server.dart @0x4392e74`; field load `@0x4392ff8`) | Tibber setup | `getDataFromServiceV2` `@0x4393064` |
| `ElectricityPlaceConfirmPageLogic.save` (`electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x4397b74`) and `.saveDynamicPrice` (`@0x4397f20`) | Flatpeak place confirmation page | `@0x4397dfc`, `@0x439832c` |
| `ElectricityCompanySelectLogic.saveDynamicPrice` (`electricity_price/components/dynamic_price/setting/electricty_company_select_logic.dart @0x41e04b0`) and `._switchToFlatpeakThenConfirm` (`@0x4396ba0`) | provider selection page | `@0x41e078c`, `@0x4396eac` |
| `ElectricityPriceProviderLogic.next` (`electricity_price/components/dynamic_price/setting/electricity_price_provider_logic.dart @0x41df5fc`) | provider setup page | `@0x41dfda4` |
| `savedata` (`electricity_price/components/electricity_module/page/tou_and_timeslot_settings_poly_logic.dart @0x43a2c10`) | TOU and time-slot settings (poly) | `@0x43a350c` |
| `save` (`electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x41b469c`; C5 `electricity_price/components/timeslot/page/charge_discharge_setting_C5/charge_discharge_setting_logic_c5.dart @0x41b5708`) | charge/discharge time-slot settings | `@0x41b55f0`; `@0x41b607c` |
| `saveChargeTimes` (`electricity_price/components/timeslot/page/custom_time_period/custom_time_period_controller.dart @0x41c6e90`) | custom charge time period | `@0x41c7108` |
| `ElectricityPriceModelApiHelper.changeToTimeSlotMode` (`electricity_price/components/electricity_price_common/electricity_price_model_api_helper.dart @0x2e829b8`) | switching the station to time-slot mode | `getDataFromService` `@0x2e82b18` |
| `ElectricityPricePlanApiHelper.changeToDynamicPlan` (`electricity_price/components/electricity_price_common/electricity_price_plan_api_helper.dart @0x41a648c`) | switching the station to a dynamic plan | `@0x41a6630` |

## Since/changed

3.18.0: absent as an installer URL (the 3.18.0 pool holds no `installer_svc` string); the consumer twin `/charging_hes_dynamic_price_svc/save_dynamic_price` is in the 3.18.0 pool. 3.24.3: present (new). since: 3.24.3. `SaveDynamicPriceResponse` exists in 3.18.0; `ThirdJumpModel.aggregationFrequency` and `UserFlatpeakParam.aggregationFrequency` are new in 3.24.3 (model pages), so the Flatpeak confirm sender sends `aggregationFrequency` (`@0x43981ac`) only in 3.24.3 (not compared with the 3.18.0 sender).

## Known unknowns

- Value types and contents of the provider parameter objects (`userNordpoolParam`, `userOctopusParam`, `userFlatpeakParam`, `dynamicPriceParam`, `providerParams` members) are not decoded; the key sets of the provider objects are on [the company model page](../../models/dynamic_price_company_model.md).
- Server behaviour is not known (what `setMode: false` does, which provider names exist besides Tibber and Flatpeak).
- Whether the installer variant accepts the consumer-style bodies is not tested.

## Device-tested by

none
