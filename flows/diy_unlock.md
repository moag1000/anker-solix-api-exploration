> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# DIY legal power limit unlock

How the app asks the user to unlock an output limit above the legal limit with the `DiyLegalPowerLimitSheet`, and what the verification call does in each of the three places that open the sheet. The sheet is new in 3.24.3. The request and the response of the verification are owned by [verify_unlock_default_power_code](../api/devicecontrol/device/verify_unlock_default_power_code.md); the three response keys that choose and fill the sheet (`unlock_default_power_type`, `unlock_pop_image`, `unlock_pop_content`) by [StationPowerLimitModel](../models/station_power_limit.md). The station power limit page is traced step by step in [system_output_limit.md](system_output_limit.md#steps) (steps 9 to 12); this page covers the sheet itself and the two other entry points.

## Trigger (UI action)

The sheet opens when the user confirms a power value that is above the legal limit of the device or station. Three entry points exist in 3.24.3 (all allocate `DiyLegalPowerLimitSheet` and call `show`, `diy_legal_power_limit_sheet.dart @0x2af0208`):

- Station power limit page: `_setOutputPowerLimit` prompt, allocation at `station_power_limit_logic.dart @0x43554c4`, `show` at `@0x4355524`; it sets the site id slot (offset 0x1f) and no serial.
- A17C1 settings, output power picker: the callback `a17c1setting_logic.dart @0x3d91bd4` allocates the sheet at `@0x3d91fa8` and shows it at `@0x3d92008`; it sets the image, the content and the device serial slot (offset 0x23, `@0x3d91ff4`, `@0x3d91ffc`, `@0x3d92004`) and no site id. The type comes from the device model through `DiyLegalPowerLimitType.fromInt` (call at `@0x3d91f30`).
- Grid-connected settings: `_checkLegalLimitForDevice` (`grid_connected_settings_controller.dart @0x2aefef4`) calls `showBottomLegal` (call at `@0x2aeffb8`, function `@0x2aefffc`) when the value is above the legal limit read from a per-device map (compare at `@0x2aeffa4`); the device serial slot is set unless a flag says the page is in a site context (`tbnz` at `@0x2af00d0`, store at `@0x2af0164`).

## Preconditions

- The type value `unlock_default_power_type` selects the variant. The mapping is the same in `showBottomLegal` and in the station page: the Smi compares `cmp w0, #2` and `cmp w0, #4` (tagged 1 and 2) give `image` (pool object `pp+0xa5748`) and `imagePassword` (`pp+0xa5750`); anything else gives `h5` (`pp+0xa5758`) (`grid_connected_settings_controller.dart @0x2af005c`, `@0x2af0084`, `@0x2af0064`, `@0x2af008c`, `@0x2af0098`). The enum indexes are h5 0, image 1 and imagePassword 2. The sheet state picks the content widget by that index (`diy_legal_power_limit_sheet.dart @0x30b9334`, `@0x30b933c`; widgets at `@0x30b9370`, `@0x30b93f0`, `@0x30b946c`).
- `initState` of the sheet state reads the current region abbreviation (`getCurrentRegionAbbr`, `diy_legal_power_limit_sheet.dart @0x2c1f344`); the H5 variant puts it into the page URL.
- The sheet is a bottom sheet (`ExtensionBottomSheet.bottomSheet`, `diy_legal_power_limit_sheet.dart @0x2af02d0`).

## Steps

| # | actor | action | owner page link | asm citation |
|---|---|---|---|---|
| 1 | user | Confirms a value above the legal limit in one of the three places. | this page | entry points in Trigger |
| 2 | app | Opens the sheet with the variant, `unlock_pop_image`, `unlock_pop_content` and the site id or device serial, and two callbacks. | [StationPowerLimitModel](../models/station_power_limit.md) | `diy_legal_power_limit_sheet.dart @0x2af0214` |
| 3 | app | Variant `image`: shows the image and the text; confirm calls the callback of the sheet. Variant `h5`: shows a web page (`InAppWebView`) loaded from `https://anker-webview-us-qa.anker.com/over-power.html?country=` plus the region, a consent toggle and a confirm button. | this page | `diy_legal_power_limit_sheet.dart @0x43583b0` (URL), `@0x4358f94` (toggle), `@0x30b9f6c` (confirm button) |
| 4 | user | Variant `imagePassword`: types the unlock code and confirms. The handler returns without a request when the code is empty. | [verify_unlock_default_power_code](../api/devicecontrol/device/verify_unlock_default_power_code.md) | `diy_legal_power_limit_sheet.dart @0x30bbef4` |
| 5 | app | Sends `verify_unlock_default_power_code` with `unlock_code` and exactly one of `device_sn` (when a serial slot is set) or `site_id`. | [verify_unlock_default_power_code](../api/devicecontrol/device/verify_unlock_default_power_code.md#request) | `diy_legal_power_limit_sheet.dart @0x30bc02c` |
| 6 | cloud | Answers with `verify_result`. | [verify_unlock_default_power_code](../api/devicecontrol/device/verify_unlock_default_power_code.md#response) untagged by design (no app-side fact) |
| 7 | app | `verify_result` true: calls the sheet's success callback. `verify_result` false or missing: shows `passwordError`. Transport or server error: logs `verifyUnlockDefaultPowerCode fail` and shows `netWorkError`. | [verify_unlock_default_power_code](../api/devicecontrol/device/verify_unlock_default_power_code.md#errors-seen) | `diy_legal_power_limit_sheet.dart @0x30bc0ac` (callback), `@0x30bc490` (`passwordError`), `@0x30bc328`, `@0x30bc374` (error) |
| 8 | app | What the callbacks do depends on the entry point: station page, both callbacks close the sheet and set the system output limit ([system_output_limit.md](system_output_limit.md#steps)); A17C1 picker, both callbacks call `setPowerLimit` with the chosen index; grid-connected settings, both callbacks are one shared empty closure (`pp+0xa5760`, `pp+0xa5768`), so the sheet only reports its closing result to `_checkLegalLimitForDevice`, which compares it with `true`. | [solarbank_power_limit_change.md](solarbank_power_limit_change.md) | `station_power_limit_logic.dart @0x4355aec`, `@0x4355b94`; `a17c1setting_logic.dart @0x3d93024`, `@0x3d93108`; `grid_connected_settings_controller.dart @0x2af0114`, `@0x2af0130`, `@0x2aeffec` |

## Side effects

- Whether a successful verification changes server state (for example allowing later requests above the legal limit) is not known; the grid-connected entry point has no follow-up call in the app, which makes server-side state the only consequence there (owner page, Known unknowns).
- The H5 page is loaded from a host whose name contains `qa` (`anker-webview-us-qa`) in this build (`diy_legal_power_limit_sheet.dart @0x43583b0`).

## Timing (delays/polling)

No delay or polling in the sheet code read here. A load error of the web view only logs `[Power WebView] Load ERROR` (`diy_legal_power_limit_sheet.dart @0x43592ec`).

## Failure paths

- Empty code: no request (step 4). Wrong code: `passwordError`, the sheet stays open.
- Network or server error: `netWorkError`; no limit is changed by the sheet. Error codes: [errors](../api/errors.md).
- Web view load error (H5): logged only; whether the confirm button stays usable is not read.

## Since/changed

The sheet, the endpoint and the three model keys are new in 3.24.3 (3.18.0 has neither the URL string nor the key `unlock_default_power_type`). Their descriptions in the old FLOWS.md do not exist; this flow has no audit rows.

## Known unknowns

- The confirm path of the `h5` variant (the toggle and `_confirmButton` are identified; the callback they call was not followed).
- What the server does with a successful verification and whether `legal_limit` is enforced server-side (see [verify_unlock_default_power_code](../api/devicecontrol/device/verify_unlock_default_power_code.md#known-unknowns)).
- The owner page of the endpoint states that the station page is the only caller; the A17C1 picker and the grid-connected settings are two more callers that pass a device serial, so the request there carries `device_sn` instead of `site_id`.
- Where the user gets the unlock code (printed, shown in the image, or from support).
