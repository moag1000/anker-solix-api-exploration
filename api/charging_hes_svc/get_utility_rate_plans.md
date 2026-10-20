> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_utility_rate_plans

## Purpose

Reads the utility rate plans of a site (`ElectricityPlaceConfirmPageLogic::_getUtilityRatePlan`; the inventory lists five more senders: `ElectricityUsageHelper::getCurEmsModeType`, `getManualSetTOUDetailWithUrl`, `EmsAiModeConditionLogic::_getLargeUtilityRatePlan`, `GeneralPriceSettingLogic::getDevicePriceType`, `SmartModeLogic::_getUtilityRatePlan`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`Api::getHesUtilityRatePlans` (`base_service/api_url.dart @0x24a5d58`) returns `/charging_hes_installer_svc/get_utility_rate_plans` (`@0x24a5d64`) when the static flag `0xad8` is true and `/charging_hes_svc/get_utility_rate_plans` (`@0x24a5d70`) otherwise. The one sender read, `ElectricityPlaceConfirmPageLogic::_getUtilityRatePlan` (`electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29abe94`), loads the late static field `getHesUtilityRatePlans` (`@0x29abf08`), uses the method object `Method.post` (pool entry `pp+0xa7e0`, `@0x29abfac`) and sends through `encryptionRequestHttp` (`@0x29abfe0`). That the late static field holds the result of `Api::getHesUtilityRatePlans` was not read, and the five other senders were not read.

Run-time choice of the URL (app side, traced 2026-10-20): the flag `0xad8` (`Api::isProApp`, `base_service/api_url.dart @0x22b317c`) is stored once in `Api.init` (`base_service/api_url.dart @0x49ce9dc`) from a package-name test against `"anker.pros"`; the full rule is on [get_history_setting.md](get_history_setting.md#methodurl) and in [charging_hes_installer_svc/README.md](../charging_hes_installer_svc/README.md#variant-selector-installer-app-versus-consumer-app).

## Encrypted?

encrypted: `true` (app side) for the sender read. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app". `ElectricityPlaceConfirmPageLogic::_getUtilityRatePlan` calls `encryptionRequestHttp` (`electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29abfe0`).

## Request

`_getUtilityRatePlan` stores 3 keys in a `<String, Object>` literal (`electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29abf68`), which does not type the values. `not_include_nem` and `accuracy` are constants: the tagged immediates `r16 = 2` (`@0x29abf4c`, Smi 1) and `r16 = 10` (`@0x29abf60`, Smi 5). `station_id` is `field_7b` of the logic (`@0x29abf34`); `ElectricityPlaceConfirmPageLogic::onInit` (`electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x34f41d4`) stores that field with a cast to `String` (`r8 = String` `@0x34f4434`, cast `@0x34f4440`, store `@0x34f444c`), so the value is a String.

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | string | yes | `"<station_id>"` | `electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29abf24` |
| `not_include_nem` | int (Smi, w) | yes | `1` | `electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29abf40` |
| `accuracy` | int (Smi, w) | yes | `5` | `electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29abf54` |

Keys of the other senders (traced 2026-10-20; app side, values as the map literals build them, Smi decoded by the SMI rule): `SmartModeLogic::_getUtilityRatePlan` (`charging/ui/page/device/a5101/setting/smartMode/smart_mode_logic.dart @0x3eae388`) sends the same three keys as above in a `<String, Object>` literal (`station_id`, `not_include_nem` raw 2 = Smi 1, `accuracy` raw 10 = Smi 5, `@0x3eae3d8`..`@0x3eae3f8`). `EmsAiModeConditionLogic::_getLargeUtilityRatePlan` (`ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x2a30d54`) loads the same late static URL (`LoadStaticField(0xb04)` `@0x2a30d30`) but names the second key `notIncludeNem` (camel case, `@0x2a30d7c`, raw 2 = Smi 1, 32-bit store `@0x2a30d8c`), with `station_id` from `field_4b` and `accuracy` raw 10 = Smi 5 (`@0x2a30d9c`). `ElectricityUsageHelper::getCurEmsModeType` (`electricity_price/components/electricity_price_common/electricity_usage_helper.dart`) is a function shared by several URLs: when the URL equals the late static `getHesUtilityRatePlans` (`@0x292e490`, `==` `@0x292e4b8`) it adds `station_id`, `not_include_nem` (raw 2 = Smi 1) and `accuracy` (raw 10 = Smi 5) with `[]=` (`@0x292e4d4`..`@0x292e52c`). `GeneralPriceSettingLogic::getDevicePriceType` (`electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x29a4bdc`) builds a four-key `<String, Object?>` map for the URL `getHesUtilityRatePlans` (`@0x29a4ba0`): `station_id` (`field_7b`), `not_include_nem` (raw 2 = Smi 1), `currency` (raw 10 = Smi 5, `@0x29a4c1c`) and `accuracy` (raw 10 = Smi 5, `@0x29a4c30`). Response handling of the shared helper `ElectricityUsageHelper::getManualSetTOUDetailWithUrl` (`@0x2c4f910`): when the URL equals the late static (`@0x2c4ff98`, `==` `@0x2c4ffc0`) it calls `parserHesResponseTOUDataFromSite` (`@0x2c4fffc`, function `@0x2c50018`), which looks up `peak_sessions` (`@0x2c500f8`) and `price_unit` (`@0x2c50120`, cast to String with the fallback `""` `@0x2c501a4`) in the answer map; the answer handling of the other four senders was not read.

## `param_type`/`cmd`

n/a

## Response model (link)

no model: the success closure (`electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29abffc`) reads two integer keys directly (see Response).

## Response

(asm-traced) Keys read by the success closure: `electricity_strategy_mode` (int, default 0 `electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29ac0dc`, cast `@0x29ac124`) and, when that value equals 1 (`cmp x1, #1` `@0x29ac150`), `price_source_sub_type` (int, default 0 `@0x29ac180`, cast `@0x29ac1d0`); both are stored in fields of the logic (`@0x29ac13c`, `@0x29ac1e8`).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "station_id": "<station_id>",
  "not_include_nem": 1,
  "accuracy": 5
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`. The failure closure of this sender was not read.

## Callers in app

- `base_service/api_url.dart`: `getHesUtilityRatePlans` @0x24a5d58 (URL literal only, no `*Http*` call; sender `ElectricityPlaceConfirmPageLogic::_getUtilityRatePlan` (`electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29abe94`), reached through callers `ElectricityPlaceConfirmPageLogic::_getUtilityRatePlan` (`electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29abe94`); other senders: `ElectricityUsageHelper::getCurEmsModeType`, `ElectricityUsageHelper::getManualSetTOUDetailWithUrl`, `EmsAiModeConditionLogic::_getLargeUtilityRatePlan`, `GeneralPriceSettingLogic::getDevicePriceType`, `SmartModeLogic::_getUtilityRatePlan`; resolved from the URL literal at `base_service/api_url.dart @0x24a5d70` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. `tools/out/diff_3.18.0_3.24.3.md` lists `accuracy`, `currency`, `ems_data`, `not_include_nem`, `site_id` and `station_id` as removed for this URL (string-level), but the 3.24.3 sender read here still stores `station_id`, `not_include_nem` and `accuracy`, so that row only means the literals are not matched to the senders linked to this URL. The installer variant is new in 3.24.3.

## Known unknowns

- The URL link stays string-only: the sender loads the late static `getHesUtilityRatePlans` (`electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29abef4`; offset 0xb04, declared `static late String getHesUtilityRatePlans` in `base_service/api_url.dart`); its initializer was not found. — traced 2026-10-20: same finding as [get_history_setting.md](get_history_setting.md#known-unknowns): the late static `getHesUtilityRatePlans` (offset 0xb04) has no explicit store in `base_service/api_url.dart` (the only static store is the flag `@0x49ce9dc`) and the only function of that name is `Api::getHesUtilityRatePlans` (`@0x24a5d58`); the link is the Dart late-static mechanism, not visible in the asm
- The response handling of the four other senders (`SmartModeLogic`, `EmsAiModeConditionLogic::_getLargeUtilityRatePlan`, `ElectricityUsageHelper::getCurEmsModeType`, `GeneralPriceSettingLogic::getDevicePriceType`) was not read — traced 2026-10-20: not followed in this pass; the request keys of all five are listed under Request. The app sends `notIncludeNem` from one sender only; whether the server reads that spelling is server behaviour and not known from the app.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
