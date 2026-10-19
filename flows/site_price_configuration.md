> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# Site price configuration (fixed price)

How the app saves a fixed electricity price from the fixed price page of the electricity price module. The page builds one of three request bodies and a shared helper chooses the URL from the type of the device or site: a station of the HES family gets a `device_command`, a site gets `update_site_price`, a single device gets `set_device_attrs`. The old page described only the site case. The site body is owned by [update_site_price](../api/power_service/site/update_site_price.md), the device case by [set_device_attrs](../api/power_service/app/device/set_device_attrs.md) and the HES case by [device_command](../api/charging_hes_svc/device_command.md). "Audit row N" counts the data rows of [../docs/audit/FLOWS.md](../docs/audit/FLOWS.md), see the [README](README.md#audit-row-numbers).

## Trigger (UI action)

On the HES fixed price page (`hes_fixed_price_view.dart`) the user enters a buy price (and, if supported, a sell price) and taps save: the view calls `HesFixedPriceLogic::savePrice` (call at `hes_fixed_price_view.dart @0x43a04fc`, function `hes_fixed_price_logic.dart @0x43a0518`).

Other pages send `update_site_price` too, with their own bodies: `StationPriceSettingLogic::savePrice` (`station_price_setting_logic.dart @0x30dc59c`, call of `updateSitePriceRequest`), the electricity price page (`electricity_price_logic.dart @0x3fb0438`), the utility rate plan pages (`site_utility_rate_plan_logic.dart @0x279decc`, `site_utility_rate_logic.dart @0x3ff8624`) and the TOU components. They are not part of this flow.

## Preconditions

- The device or site type object (`field_8b` of the logic) answers three predicates that select the body and the URL (`GDT` calls at `hes_fixed_price_logic.dart @0x43a055c` for the HES case and `@0x43a0cc0` for the device case).
- Empty input: when the price text has length 0 the page closes with `GetNavigation.back()` and sends nothing (`hes_fixed_price_logic.dart @0x43a057c`, `@0x43a05a8`).
- Installer app variant: the static `isProApp` flag (`@0x43a05e4`) chooses `system_code` instead of `station_id` in the body (`@0x43a0604`).
- The number of decimals (`accuracy`) is set earlier by `getCurrency`: `PN::getDecimalPlacesForCode` when the product code is non-empty, else `getDecimalPlacesForPowerSiteType` (`hes_fixed_price_logic.dart @0x29af028`, `@0x29af050`).

## Steps

| # | actor | action | owner page link | asm citation |
|---|---|---|---|---|
| 1 | user | Taps save. | this page | `hes_fixed_price_view.dart @0x43a04fc` |
| 2 | app | HES case: changes the price unit in the cloud (`changeCurrencyUnit`, body with `station_id` or `system_code` and `price_unit` or `priceUnit`), then builds the `device_command` body with `station_id`, `main_sn`, `time`, `version`, `accuracy` and a `utility_rate_plan` that holds one all-day price session (`peak_sessions`, `peak_valley_prices` with `buy`, `sell`, `energy_unit` `/kWh`). | [device_command](../api/charging_hes_svc/device_command.md), [adjust_station_price_unit](../api/charging_hes_svc/adjust_station_price_unit.md) | `hes_fixed_price_logic.dart @0x43a06e0`, `@0x43a0718`, `@0x43a0748`, `@0x43a079c`, `@0x43a07ec`, `@0x43a0880`, `@0x43a09a8`, `@0x43a0c90`; `electricity_usage_helper.dart @0x29ae7c0` |
| 3 | app | Device case: builds `{"device_sn": ..., "attributes": {"price_type": "fixed", "fixed_price": ..., "currency": ...}}`. | [set_device_attrs](../api/power_service/app/device/set_device_attrs.md) | `hes_fixed_price_logic.dart @0x43a0ce4`, `@0x43a0d00`, `@0x43a0d18`, `@0x43a0d24`, `@0x43a0d30`, `@0x43a0d4c` |
| 4 | app | Site case: logs `decimal length:` and builds the body with `site_id`, `price`, `site_price_unit`, `site_co2`, `price_type`, `accuracy` and, when the page supports a sale price and the sell field is not empty, `sell_price`. `site_co2` is the pool double 0.997, `price_type` is the string `fixed`. | [update_site_price](../api/power_service/site/update_site_price.md) | `hes_fixed_price_logic.dart @0x43a0e10`, `@0x43a0e60`, `@0x43a0e7c`, `@0x43a0f04`, `@0x43a0f40`, `@0x43a0f4c`, `@0x43a0f58`, `@0x43a0f64`, `@0x43a0f70`, `@0x43a1044` |
| 5 | app | Hands the body to `ElectricityUsageHelper::setDeviceEMSPriceArgument` with a success and a failure callback. | this page | `hes_fixed_price_logic.dart @0x43a12ac` |
| 6 | app | `getSaveDeviceEMSPrice` picks the URL by the type predicates: HES gives the static device command URL (`Api.sendDeviceCommand`), a site gives `/power_service/v1/site/update_site_price`, a device gives `/power_service/v1/app/device/set_device_attrs`, anything else gives an empty string. The helper sends the body with `encryptionRequestHttp` (POST, loading overlay). | [update_site_price](../api/power_service/site/update_site_price.md) | `electricity_usage_helper.dart @0x249e448`, `@0x249e46c`, `@0x249e48c`, `@0x249e49c`, `@0x249e4a8`, `@0x249e4c4`, `@0x249e35c`, `@0x249e404` |
| 7 | cloud | Stores the price and answers. | [update_site_price](../api/power_service/site/update_site_price.md) untagged by design (no app-side fact) |
| 8 | app | Success callback: builds the result `{buyPrice, salePrice, currencySymbol}`, closes the page with it and fires an event bus message. Failure callback: logs `HesFixedPriceLogic============>` with the message and shows a toast. | this page | `hes_fixed_price_logic.dart @0x43a13c4` (success, keys `@0x43a1458`, `@0x43a1474`, `@0x43a148c`), `@0x43a1314` (failure), `@0x43a1370` |

## Side effects

- The page returns the saved prices and the currency symbol to the calling page (step 8).
- HES case: the price unit is changed first, in its own cloud request, before the plan is written.
- The site co2 factor sent is the fixed value 0.997; the old page's "CO2 calculation is server-side only" is consistent: the app sends the constant and does no calculation.

## Timing (delays/polling)

No delay, timer or polling in `savePrice` or the helper. The loading overlay stays until the request finishes (`showLoading` option at `electricity_usage_helper.dart @0x249e3fc`).

## Failure paths

- Empty price: the page closes without a request.
- Request failure: the failure callback logs and shows a toast; no retry. Error codes: [errors](../api/errors.md).
- Type not recognised: the URL is the empty string and the helper still calls `encryptionRequestHttp` with it (`electricity_usage_helper.dart @0x249e4d0`); what the HTTP layer does with an empty path was not read.

## Since/changed

Corrections of the old FLOWS.md (audit rows in brackets):

- Decimals: `accuracy` is chosen by the product number, not by market or currency: 5 for the product codes A5143 and A1903 and 2 for every other product; the old "2 specific markets use 4 (JPY/KRW?)" does not exist (rows 62, 63: `PN::getDecimalPlacesForCode`, `charging_pn.dart @0x29af0dc`, returns the Smi raw 10 for the two listed codes and raw 4 otherwise, so 5 and 2). No owner page records this rule yet (the `accuracy` row of [update_site_price](../api/power_service/site/update_site_price.md) is still unfilled), so it is recorded here.
- `price_type` is the literal `fixed` here (row 71, OK); the old payload example values (price 0.30, `site_co2` 0.5, unit `EUR/kWh`, `current_mode` null) were an example, not from asm. The old `price_type` `use_time` for TOU belongs to the TOU components, not to this page.
- New in this trace: the three-way URL choice and the HES body.

## Known unknowns

- The names of the three type predicates (`GDT` offsets `-0xa38`, `-0x667`, `-0xbd8`): from the URL each one selects they are the HES, site and device tests, but the method names are not in the asm.
- Whether the HES case writes both the `device_command` and the unit change in all cases, and the order of the two callbacks.
- What the empty-URL fallback does for an unknown type.
- The fixed-price flows of the other pages listed in Trigger (`station_price_setting_logic.dart`, TOU components) and the dynamic and TOU variants of `update_site_price` (`price_type` `use_time`).
