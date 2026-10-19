> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# DynamicPriceCompanyModel

## Contents

1. [Purpose](#purpose)
1. [Dart class + file](#dart-class--file)
1. [Fields](#fields)
1. [Produced by](#produced-by)
1. [Consumed by](#consumed-by)
1. [Changed since 3.18.0](#changed-since-3180)
1. [Known unknowns](#known-unknowns)

## Purpose

Carries the list of dynamic-price and time-slot providers (companies) that a site may choose from, the provider the user already selected, the site battery limits and the user location, as returned by `get_price_company`.

## Dart class + file

`DynamicPriceCompanyModel` and its element classes, file `ak_soft_contract/src/energy/model/dynamic_price_company_model.dart` (package `ak_soft_contract`). `DynamicPriceCompanyModel.fromJson` is at `@0x27b94ac`; the other `fromJson` addresses are listed per class below.

## Fields

Column `since`: `≤3.18.0` means the key is present in 3.18.0 (earlier versions not checked). Every `source` address is the string load of the JSON key inside the class `fromJson`; each address was re-read in the asm and shows the quoted key. Nullability and Dart types come from `tools/model_fields.py` (`data/models.json`).

### DynamicPriceCompanyModel

`fromJson` `dynamic_price_company_model.dart @0x27b94ac`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `touCompanyInfos` | `List` | no | ≤3.18.0 | `dynamic_price_company_model.dart @0x27b94cc` |
| `timeSlotCompanyInfos` | `List` | no | ≤3.18.0 | `dynamic_price_company_model.dart @0x27b9600` |
| `touUserSelect` | `UserSelect?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27b9734` |
| `timeSlotUserSelect` | `UserSelect?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27b97d0` |
| `siteCapacity` | `int?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27b986c` |
| `siteMaxCharge` | `int?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27b98f4` |
| `supportSell` | `bool?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27b997c` |
| `userInfo` | `UserInfo?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27b99e8` |
| `hideTimeslot` | `bool?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27b9a7c` |

### CompanyInfos

`fromJson` `dynamic_price_company_model.dart @0x27bbc5c`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `name` | `String?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bbc7c` |
| `currency` | `String?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bbd00` |
| `timeslotInterval` | `int?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bbd88` |
| `companySupportSell` | `bool?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bbe10` |
| `nordpoolParam` | `NordpoolParam?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bbe68` |
| `octopusParam` | `OctopusParam?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bbf04` |
| `userFlatpeakParam` | `UserFlatpeakParam?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bbfa0` |
| `userTibberParam` | `UserTibberParam?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bc00c` |
| `timeSlotRecommendParams` | `TimeSlotRecommendParams?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bc078` |

### UserSelect

`fromJson` `dynamic_price_company_model.dart @0x27b9fe8`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `name` | `String?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27ba008` |
| `currency` | `String?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27ba088` |
| `userNordpoolParam` | `UserNordpoolParam?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27ba10c` |
| `userOctopusParam` | `UserOctopusParam?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27ba1a0` |
| `dynamicPriceParam` | `DynamicPriceParam?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27ba23c` |
| `userFlatpeakParam` | `UserFlatpeakParam?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27ba2d8` |
| `userTibberParam` | `UserTibberParam?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27ba374` |

### UserInfo

`fromJson` `dynamic_price_company_model.dart @0x27b9afc`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `longitude` | `String?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27b9b1c` |
| `latitude` | `String?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27b9ba0` |
| `city` | `String?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27b9c24` |
| `street` | `String?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27b9ca8` |
| `zipCode` | `String?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27b9d2c` |
| `onlySaveUserInfo` | `bool?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27b9db0` |

### NordpoolParam

`fromJson` `dynamic_price_company_model.dart @0x27bd100`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `area` | `List<NordpoolArea>` | no | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bd120` |
| `recommendParams` | `RecommendParams?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bd260` |
| `enableSellType` | `unknown` | not determined | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bd2fc` |

### NordpoolArea

`fromJson` `dynamic_price_company_model.dart @0x27bd708`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `area` | `String?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bd728` |
| `interval` | `int?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bd7b0` |

### OctopusParam

`fromJson` `dynamic_price_company_model.dart @0x27bcb04`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `buyProducts` | `List<BuySellProducts>` | no | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bcb24` |
| `sellProducts` | `List<BuySellProducts>` | no | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bcc64` |
| `area` | `List<OctopusArea>` | no | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bcda4` |

### OctopusArea

`fromJson` `dynamic_price_company_model.dart @0x27bcf3c`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `regionName` | `String?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bcf5c` |
| `groupId` | `String?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bcfe4` |

### BuySellProducts

`fromJson` `dynamic_price_company_model.dart @0x27bb31c`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `name` | `String?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bb33c` |
| `code` | `String?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bb3c0` |
| `interval` | `int?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bb444` |

### RecommendParams

`fromJson` `dynamic_price_company_model.dart @0x27bd378`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `buyRate` | `int?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bd398` |
| `buyFixFee` | `unknown` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bd41c` |
| `sellFixRate` | `unknown` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bd4c8` |
| `exportTariff` | `unknown` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bd574` |
| `sellType` | `int?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bd620` |

### TimeSlotRecommendParams

`fromJson` `dynamic_price_company_model.dart @0x27bc144`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `chargeTimePeriod` | `unknown` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bc194` |
| `dischargeTimePeriod` | `unknown` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bc250` |
| `dischargeTime` | `num?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bc310` |
| `chargeTime` | `num?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bc398` |
| `chargeTotalTime` | `num?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bc420` |
| `disChargeTotalTime` | `num?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bc4a4` |

### UserNordpoolParam

`fromJson` `dynamic_price_company_model.dart @0x27bb4f8`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `buyRate` | `int?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bb518` |
| `buyFixFee` | `unknown` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bb5a0` |
| `sellRate` | `unknown` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bb654` |
| `sellType` | `int?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bb708` |
| `area` | `String?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bb790` |
| `currency` | `String?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bb818` |
| `enableSellType` | `int?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bb8a0` |
| `sellVat` | `unknown` | yes | 3.24.3 | `dynamic_price_company_model.dart @0x27bb928` |

### UserOctopusParam

`fromJson` `dynamic_price_company_model.dart @0x27bad1c`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `groupId` | `String?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bad3c` |
| `buy` | `BuySellProducts?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27badc4` |
| `sell` | `BuySellProducts?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bae60` |
| `currency` | `String?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27baefc` |
| `export` | `bool?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27baf84` |

### UserFlatpeakParam

`fromJson` `dynamic_price_company_model.dart @0x27ba640`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `direction` | `String?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27ba660` |
| `connectToken` | `String?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27ba6e8` |
| `buyCompany` | `BuySellCompany?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27ba770` |
| `sellCompany` | `BuySellCompany?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27ba80c` |
| `aggregationFrequency` | `int?` | yes | 3.24.3 | `dynamic_price_company_model.dart @0x27ba8a8` |

### UserTibberParam

`fromJson` `dynamic_price_company_model.dart @0x27ba424`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `code` | `String?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27ba444` |
| `hasError` | `bool?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27ba4c8` |

### BuySellCompany

`fromJson` `dynamic_price_company_model.dart @0x27babe0`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `name` | `String?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bac00` |
| `hasError` | `bool?` | yes | ≤3.18.0 | `dynamic_price_company_model.dart @0x27bac84` |

`ChargeTimePeriod` (`start`, `end`, `fromJson @0x27bc8b4`, keys `@0x27bc8e8`, `@0x27bc964`) is the element type of the two `unknown`-typed lists of `TimeSlotRecommendParams`; that element mapping is an inference from the class name, the list parse was not traced.

The `UserSelect` members mirror the provider parameter objects the app sends back with [save_dynamic_price](../api/charging_hes_installer_svc/save_dynamic_price.md) (`userNordpoolParam`, `userOctopusParam`, `userFlatpeakParam`, `userTibberParam`, `dynamicPriceParam`); the request side is owned by that page.

## Produced by

[`get_price_company`](../api/charging_hes_installer_svc/get_price_company.md): `DynamicPriceCompanyModel.fromJson` is called in the success closure of every sender listed on that page, for example `electricity_price_provider_logic.dart @0x29a79dc`, `electricty_company_select_logic.dart @0x29aacc8`, `dynamic_price_detail_info_view.dart @0x27d07b8`, `ak_soft_ems/ems_list/power_usage_scenario_controller.dart @0x2a2f16c` and `@0x37b1c8c`, `charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart @0x28eb650`, `power_usage_scenario_logic.dart @0x28a1bec`. The consumer-app twin URL `/charging_hes_dynamic_price_svc/get_price_company` is sent by the same functions (see [the variant selector](../api/charging_hes_installer_svc/README.md#variant-selector-installer-app-versus-consumer-app)).

## Consumed by

The Dart files that read the parsed object are the sender files listed above plus `electricity_price_serviceImpl.dart` (`@0x2891e78`, `@0x2892498`), `tou_and_timeslot_settings_detail_logic.dart` (`@0x27b90cc`), `tou_and_timeslot_settings_poly_logic.dart` (`@0x29b1ea0`), `general_price_setting.dart` (`@0x27d25a4`) and the two charge/discharge setting logics (`@0x29b65a4`, `@0x29b7a3c`), each at the `fromJson` call. Field-level use is not traced.

## Changed since 3.18.0

Keys with `since` 3.24.3 are new in this version: `UserFlatpeakParam.aggregationFrequency` (`@0x27ba8a8`) and `UserNordpoolParam.sellVat` (`@0x27bb928`). The other keys exist in 3.18.0 (the data in `data/models.json` compares both versions; no key was removed).

## Known unknowns

- Types marked `unknown` (`buyFixFee`, `sellFixRate`, `exportTariff`, `sellRate`, `sellVat`, `enableSellType` of `NordpoolParam`, the time-period lists) were not resolved by the extractor.
- The meaning of `type` values and of the `name` strings (provider names such as the ones the app sends as `companyName`) is not documented; no captured response exists.
