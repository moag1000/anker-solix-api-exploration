> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# ThirdJumpModel and SaveDynamicPriceResponse

## Purpose

Carries the two answers of the Tibber/Flatpeak dynamic-price setup: the URL the user is sent to for authorizing a third-party provider (`ThirdJumpModel`) and the confirmation of a saved provider setting (`SaveDynamicPriceResponse`).

## Dart class + file

`ThirdJumpModel` (`fromJson @0x4391aa0`), `SaveDynamicPriceResponse` (`fromJson @0x4393690`) and `FlatpeakSetting` (`fromJson @0x4393880`), file `electricity_price/components/dynamic_price/general_kit/http_server/model/dynamic_price_server_model.dart` (package `electricity_price`).

## Fields

Column `since`: `≤3.18.0` means the key is present in 3.18.0 (earlier versions not checked). Every `source` address is the string load of the JSON key inside the class `fromJson` and was re-read in the asm.

### ThirdJumpModel

`fromJson` `dynamic_price_server_model.dart @0x4391aa0`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `jumpUrl` | `String` | no | ≤3.18.0 | `dynamic_price_server_model.dart @0x4391ba4` |
| `flatpeakWaitTime` | `int` | no | ≤3.18.0 | `dynamic_price_server_model.dart @0x4391c04` |
| `aggregationFrequency` | `int` | no | 3.24.3 | `dynamic_price_server_model.dart @0x4391c5c` |

### SaveDynamicPriceResponse

`fromJson` `dynamic_price_server_model.dart @0x4393690`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `messageId` | `String` | no | ≤3.18.0 | `dynamic_price_server_model.dart @0x4393794` |
| `flatpeakSetting` | `FlatpeakSetting?` | yes | ≤3.18.0 | `dynamic_price_server_model.dart @0x43937f0` |

### FlatpeakSetting

`fromJson` `dynamic_price_server_model.dart @0x4393880`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `buyCompany` | `String` | no | ≤3.18.0 | `dynamic_price_server_model.dart @0x4393984` |
| `buyType` | `String` | no | ≤3.18.0 | `dynamic_price_server_model.dart @0x43939e4` |
| `sellCompany` | `String` | no | ≤3.18.0 | `dynamic_price_server_model.dart @0x4393a44` |
| `sellType` | `String` | no | ≤3.18.0 | `dynamic_price_server_model.dart @0x4393aa0` |

## Produced by

- `ThirdJumpModel`: [`get_third_jump_url`](../api/charging_hes_installer_svc/get_third_jump_url.md), `_DynamicPriceHttpServer.getThirdJumpUrl`, `ThirdJumpModel.fromJson` at `dynamic_price_http_server.dart @0x4391a64`.
- `SaveDynamicPriceResponse`: [`save_dynamic_price`](../api/charging_hes_installer_svc/save_dynamic_price.md), `_DynamicPriceHttpServer.saveDynamicPrice`, success closure `@0x43935a4`, `SaveDynamicPriceResponse.fromJson` at `dynamic_price_http_server.dart @0x4393624`.

## Consumed by

`ElectricityCompanySelectLogic`, `ElectricityPlaceConfirmPageLogic` and `ElectricityPriceProviderLogic` (`electricity_price/components/dynamic_price/setting/`) call the two `_DynamicPriceHttpServer` methods (`electricty_company_select_logic.dart @0x43925b8`, `@0x4391770`). Field-level use is not traced.

## Changed since 3.18.0

`ThirdJumpModel.aggregationFrequency` (`@0x4391c5c`, non-null `int`) is new in 3.24.3; because the field is declared non-null, a server that omits the key would make the parse fail (how the Dart code handles that is not traced). `jumpUrl`, `flatpeakWaitTime`, `messageId`, `flatpeakSetting` and the four `FlatpeakSetting` keys exist in 3.18.0.

## Known unknowns

- The unit of `flatpeakWaitTime` and `aggregationFrequency` is not documented (no captured response; the UI strings were not read).
- Whether the Tibber path returns `flatpeakSetting` (the class name suggests Flatpeak only) is not known.
