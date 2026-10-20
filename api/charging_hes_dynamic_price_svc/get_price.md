> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_price

## Purpose

Loads the electricity price curve (today and tomorrow) of a dynamic-price provider for a site (callers `ChargeDischargeSettingLogic::getElectricityPrice`, `ChargeDischargeSettingLogic_C5::getElectricityPrice`, `DynamicPriceDetailInfoViewState::getTodayAndTomorrowPrice`, `TOUAutoPricePkgResultLogic::getData`, `TimeSlotPreviewLogic::getPriceDetail`, `TimeslotPreviewPolyLogic::getPriceDetail`, `PowerUsageScenarioController::getPriceDetail`, `SystemPolicyLogic::getPriceDetail`) (string-only: inferred from the function names; one sender is read).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_dynamic_price_svc/get_price` (asm-traced for the sender read): `ChargeDischargeSettingLogic::getElectricityPrice` (`electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x29b2c00`) loads the URL from the static field `getPrice` (`LoadStaticField(0xaec)` `@0x29b359c`, initializer `Api.getPrice`) and calls `HttpHelper::getDataFromService` (`@0x29b360c`). `HttpHelper::getDataFromService` (`electricity_price/components/electricity_price_common/http/http_helper.dart @0x27bda38`) takes the URL, the body map and a success closure and sends them with `Method.post` (pool entry `pp+0xa7e0`, `electricity_price/components/electricity_price_common/http/http_helper.dart @0x27bdb94`) through `encryptionRequestHttp` (`electricity_price/components/electricity_price_common/http/http_helper.dart @0x27bdbc8`).

The URL is chosen at run time by `Api.getPrice` (`base_service/api_url.dart @0x2554b74`): it loads the static flag at field offset `0xad8` (`@0x2554b74`, `tbnz` on the Dart false bit) and returns `/charging_hes_dynamic_price_svc/get_price` when the flag is false (`@0x2554b8c`) and `/charging_hes_installer_svc/get_price` when it is true (`@0x2554b80`). The result is cached in the late static field at offset `0xaec`, which the senders read.

Other places that load the static field `getPrice` (`LoadStaticField(0xaec)`): `electricity_price/components/timeslot/page/charge_discharge_setting_C5/charge_discharge_setting_logic_c5.dart @0x29b4104`, `electricity_price/components/timeslot/view/timeslot_preview_logic.dart @0x2c56180`, `electricity_price/components/timeslot/view/timeslot_preview_poly_logic.dart @0x2c526f0`, `electricity_price/components/electricity_price_common/tou_auto_preview/tou_auto_price_pkg_result_logic.dart @0x2c48bcc`, `electricity_price/components/fixed_price/general_electricity_price_settting/dynamic_price_detail_info_view.dart @0x27d1cf0`, `ak_soft_ems/ems_list/power_usage_scenario_controller.dart @0x2554a2c`; these senders were not read.

## Encrypted?

encrypted: `true` (asm-traced: the sender read reaches `encryptionRequestHttp`, `electricity_price/components/electricity_price_common/http/http_helper.dart @0x27bdbc8`). Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(string-only: no field type is read) One sender read. Its map literal has the type arguments `<String, dynamic>` (`electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x29b2ca0`), which name no value type.

| field | type | required | example | source |
|---|---|---|---|---|
| `type` | ? | yes | `"<type>"` | `electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x29b2c84` (value from a field of the logic object, `ldr w2` `@0x29b2c94`, stored in the literal `@0x29b2c9c`) |
| `sn` | ? | optional | `"<sn>"` | `electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x29b2d20` (guard: a call result tested `tbnz` `@0x29b2cf8`, length test `cbz` `@0x29b2d10`; store call `@0x29b2d28`) |
| `siteId` | ? | optional | `"<site_id>"` | `electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x29b2d4c` (same guard; store call `@0x29b2d54`) |
| `companyName` | ? | optional | `"<company>"` | `electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x29b2d7c` (guard: length test `cbz` `@0x29b2d6c`; store call `@0x29b2d84`) |
| `dynamicPriceParam` | object | optional | the map built by `DynamicPriceParam.toJson` | `electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x29b2ed4` (the result of `toJson` `@0x29b2ec8`, store call `@0x29b2edc`); two more branches store the same key at `@0x29b33c0` and `@0x29b34f0` |
| `providerParams` | ? | optional | `{...}` | `electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x29b3510` (a map read from the sender's local data `@0x29b3518`, tested as `Map` `@0x29b3564`, copied `@0x29b3590`) |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed in the sender read: `getElectricityPrice` passes closures to `getDataFromService` (`electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x29b35d0`, `@0x29b35dc`) without a model class; the closures were not read.

## Response

(string-only) The answer shape was not read.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "type": "<type>",
  "sn": "<sn>",
  "siteId": "<site_id>",
  "companyName": "<company>",
  "dynamicPriceParam": {}
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender read. Code meanings are owned by `api/errors.md`.

## Callers in app

- `base_service/api_url.dart`: `getPrice` @0x2554b74 (URL literal only, no `*Http*` call; sender `HttpHelper::getDataFromService` (`electricity_price/components/electricity_price_common/http/http_helper.dart @0x27bda38`) (HTTP helper wrapper), called from `ChargeDischargeSettingLogic::getElectricityPrice` (`electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x29b2c00`); also through `ChargeDischargeSettingLogic_C5::getElectricityPrice`, `DynamicPriceDetailInfoViewState::getTodayAndTomorrowPrice`, `TOUAutoPricePkgResultLogic::getData`, `TimeSlotPreviewLogic::getPriceDetail`, `TimeslotPreviewPolyLogic::getPriceDetail`; other senders: `PowerUsageScenarioController::getPriceDetail`, `PowerUsageScenarioLogic::_requestDynamicPriceInfo`, `SystemPolicyLogic::getPriceDetail`; resolved from the URL literal at `base_service/api_url.dart @0x2554b8c` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. Params changed: removed `companyName`, `pn`, `siteId`, `type`, `userNordpoolParam`, `userOctopusParam` (`tools/out/diff_3.18.0_3.24.3.md`, string-level diff on the URL builder `Api.getPrice`). In 3.24.3 the sender read builds `type`, `siteId`, `companyName`, `sn`, `dynamicPriceParam` and `providerParams` itself, so the keys moved from the URL builder's neighbourhood into the senders; `pn`, `userNordpoolParam` and `userOctopusParam` were not found in the sender read.

## Known unknowns

- Types of every key: the literal names no value type; `type` comes from a field (`electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x29b2c94`).
- Which of the other eight senders send other keys: only `ChargeDischargeSettingLogic::getElectricityPrice` was read.
- The structure of `DynamicPriceParam` and `providerParams` and the provider-specific parameters (the 3.18.0 names `userNordpoolParam`, `userOctopusParam` suggest provider options; not shown by the 3.24.3 asm).
- The response keys and the closures' parsing.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
