> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# save_dynamic_price

## Purpose

Saves the dynamic-price (provider) settings of a site: provider, charge and discharge slots and cut-off power (callers `ChargeDischargeSettingLogic::save`, `ChargeDischargeSettingLogic_C5::save`, `CustomTimePeriodController::saveChargeTimes`, `ElectricityCompanySelectLogic::saveDynamicPrice`, `ElectricityPlaceConfirmPageLogic::save`) (string-only: inferred from the function names; one sender is read).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_dynamic_price_svc/save_dynamic_price` (asm-traced for the sender read): `ChargeDischargeSettingLogic::save` (`electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x41b469c`) loads the URL from the static field `saveDynamicPrice` (`LoadStaticField(0xadc)` `@0x41b5564`, initializer `Api.saveDynamicPrice`), loads the method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x41b55c4` and sends through `encryptionRequestHttp` (`@0x41b55f0`; options `fail`, `showLoading`, `success`, descriptor `@0x41b55e8`).

The URL is chosen at run time by `Api.saveDynamicPrice` (`base_service/api_url.dart @0x2e82b34`): it loads the static flag at field offset `0xad8` (`@0x2e82b34`, `tbnz` on the Dart false bit) and returns `/charging_hes_dynamic_price_svc/save_dynamic_price` when the flag is false (`@0x2e82b4c`) and `/charging_hes_installer_svc/save_dynamic_price` when it is true (`@0x2e82b40`). The result is cached in the late static field at offset `0xadc`, which the senders read.

Twelve further places load the static field `saveDynamicPrice` (for example `electricity_price/components/electricity_price_common/electricity_price_model_api_helper.dart @0x2e82ab4`, `electricity_price/components/dynamic_price/general_kit/http_server/dynamic_price_http_server.dart @0x4392ff8`, `electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x4397d7c`); those senders were not read.

## Encrypted?

encrypted: `true` (asm-traced: the sender read reaches `encryptionRequestHttp`, `electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x41b55f0`). Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(string-only: most field types are not read) One sender read. Its map literal has the type arguments `<String, dynamic>` (`electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x41b4734`), which name no value type; `setMode` is typed from its constant.

| field | type | required | example | source |
|---|---|---|---|---|
| `companyName` | string | yes | `"<company>"` | `electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x41b4700` (value from a field `ldr w2` `@0x41b4714`, store `@0x41b471c`) |
| `setMode` | bool | yes | `true` | `electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x41b4720` (constant `r16 = true` `@0x41b472c`, store `@0x41b4730`) |
| `sn` | string | optional | `"<sn>"` | `electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x41b47b4` (guard: a call result tested `tbnz` `@0x41b478c`, length test `cbz` `@0x41b47a4`; store call `@0x41b47bc`) |
| `siteId` | string | optional | `"<site_id>"` | `electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x41b47e0` (same guard; store call `@0x41b47e8`) |
| `dynamicPriceParam` | object | yes | the map built by `DynamicPriceParam.toJson` | `electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x41b5030` (result of `toJson` `@0x41b5024`, store call `@0x41b5038`) |

Later in the same function the keys `chargeTimeList` (`@0x41b5230`), `chargeDisTimeList` (`@0x41b525c`), `chargeNum` (`@0x41b528c`), `dischargeNum` (`@0x41b52bc`), `export2Grid` (`@0x41b5300`), `cutoffPower` (`@0x41b534c`, an int boxed by `BoxInt64Instr` `@0x41b5324`) and `providerParams` (`@0x41b5374`) are stored into maps; the asm does not show that these are the request map, so they are not listed as request fields.

Types read in the second pass (traced 2026-10-20, app side): `companyName` (field at offset 287, load `electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x41b4714`), `sn` (283, `@0x41b4798`) and `siteId` (279) are the String fields of `ChargeDischargeSettingLogic` that its init code fills with `String` casts (`@0x34f78b4`, `@0x34f7814`, `@0x34f7774`) and its constructor sets to `""` (`@0x4149eb4`..`@0x4149ec4`); see [get_price](get_price.md#request). `dynamicPriceParam` has the keys listed there. The call is sent with `encryptionRequestHttp` (`@0x41b55f0`, named arguments `fail`, `showLoading` (constant true), `success`, descriptor `@0x41b55e8`).

## `param_type`/`cmd`

n/a

## Response model (link)

(string-only) not parsed in the sender read: the success closure was not read.

## Response

(string-only) The answer shape was not read.

Callbacks (traced 2026-10-20, app side): the success closure of `ChargeDischargeSettingLogic::save` (`electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x41b691c`, argument `Object?`) stores the key `isReset` in a map (`@0x41b6964`), casts the answer to `Map<String, dynamic>` (`@0x41b6984`) and goes on to call `ElectricityPriceService` (`getService` `@0x41b69ac`); the model of the answer that the installer-service variant parses is `SaveDynamicPriceResponse` on [dynamic_price_server_model](../../models/dynamic_price_server_model.md). Which keys the consumer closure reads from the map was not followed.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "companyName": "<company>",
  "setMode": true,
  "sn": "<sn>",
  "siteId": "<site_id>",
  "dynamicPriceParam": {}
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender read. Code meanings are owned by `api/errors.md`.

## Callers in app

- `base_service/api_url.dart`: `saveDynamicPrice` @0x2e82b34 (URL literal only, no `*Http*` call; sender `ChargeDischargeSettingLogic::save` (`electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x41b469c`), reached through callers `ChargeDischargeSettingLogic::save` (`electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x41b469c`); other senders: `ChargeDischargeSettingLogic_C5::save`, `CustomTimePeriodController::saveChargeTimes`, `ElectricityCompanySelectLogic::_switchToFlatpeakThenConfirm`, `ElectricityCompanySelectLogic::saveDynamicPrice`, `ElectricityPlaceConfirmPageLogic::save`; resolved from the URL literal at `base_service/api_url.dart @0x2e82b4c` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. Params changed: removed `companyName`, `setMode` (`tools/out/diff_3.18.0_3.24.3.md`, string-level diff on the URL builder `Api.saveDynamicPrice`). In 3.24.3 the sender read builds both keys itself (`electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x41b4700`, `@0x41b4720`), so neither key is absent.

## Known unknowns

- Whether `chargeTimeList`, `chargeDisTimeList`, `chargeNum`, `dischargeNum`, `export2Grid`, `cutoffPower`, `providerParams` belong to the request body (`electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x41b5230`..`@0x41b5374`): the target map of those stores was not traced. — attempted 2026-10-20: the stores at `@0x41b5230`..`@0x41b5374` use `[]=` on `field_4f` of the logic (`@0x41b521c`), a field that no store in this file assigns, while the request map is the literal at `@0x41b4734` kept in a frame slot; whether `field_4f` is the same map is not shown (two-hop not readable), so the keys stay unlisted
- Which of the twelve other senders send other keys. — traced 2026-10-20: the other senders are copies of the same logic under other class names or helper classes (`CustomTimePeriodController`, `ElectricityCompanySelectLogic`, listed under Callers in app); their key stores were not compared one by one
- The response keys. — traced 2026-10-20: the success closure casts the answer to `Map<String, dynamic>` and the key reads were not followed (see Response)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
