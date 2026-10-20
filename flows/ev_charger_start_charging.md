> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# EV charger start charging (A5190 / A5191)

How the app starts, stops, force-starts or boosts a charging session of the EV charger from its home page. The command goes to the AK IoT kit as a property write; the Dart layer sends no cloud request and no MQTT or BLE frame of its own. The control values are owned by [ev_charger_device_models.md](../models/ev_charger_device_models.md#chargecontroltype-ev-charger-command-value); the identifier `akiot.device.write_property` is owned by [../reference/iot_kit_channels.md](../reference/iot_kit_channels.md). "Audit row N" counts the data rows of [../docs/audit/FLOWS.md](../docs/audit/FLOWS.md), see the [README](README.md#audit-row-numbers).

## Trigger (UI action)

On the EV charger home page (`a5190_home_page.dart`) four buttons call `A5190HomeLogic::onTapControl` (`a5190_home_logic.dart @0x3943d7c`) with one `ChargeControlType` pool object each: boost at `a5190_home_page.dart @0x43b1a54`, start now at `@0x43b1af4`, start at `@0x43b1b94`, stop (enum member `cancel`) at `@0x43b1c34`. A second set of closures with the same four objects sits at `a5190_home_page.dart @0x3943d60`, `@0x39449a0`, `@0x39449fc`, `@0x3944a58`. The button labels are not read from the asm; the toast keys of the old page are used below only where they appear as strings in the handler.

## Preconditions

- A paired A5190 or A5191 device on the home page.
- Connection gate in `onTapControl`: the getter `showBleConnectBottomSheet` (call at `a5190_home_logic.dart @0x3943dd0`, getter `@0x39447ec`) asks `_isOcppOrBleEnable` (`@0x3944820`, function `@0x3944854`). That function returns true when the page state `field_c3` is true (`@0x3944874`) and otherwise `_isBleConnected` (`@0x3944890`). When it returns false the getter returns the page flag `field_bf` (`@0x3944834`); if that flag is true the page opens `AkBleConnectBottomSheet` (`@0x3943e08`) and returns without sending. The field names are not in the dump, but the log texts name them: `field_bf` is the third-party OCPP flag (log text `isThirdPartyOcpp.value:` at `@0x350592c`; the logic sets it from `isThirdParty()` at `@0x35064d0` and from the OCPP source value 2, compare `cmp w0, #2` at `@0x3505cb0`, tagged so 1), `field_c3` is the internal OCPP online flag (log text `内部OCPP在线状态`, `@0x35063a8`; set from the device field at offset 359 equal to 2, `cmp w3, #4` at `@0x3506384`, and forced false while `field_bf` is true, `@0x3505b24` to `@0x3505b44`). Both are `RxBool` fields; `field_bf` starts false (`@0x36f9408`).

## Steps

| # | actor | action | owner page link | asm citation |
|---|---|---|---|---|
| 1 | user | Taps one of the four buttons. | this page | `a5190_home_page.dart @0x43b1a54`, `@0x43b1af4`, `@0x43b1b94`, `@0x43b1c34` |
| 2 | app | `onTapControl` runs the gate of Preconditions, records the start time (`DateTime`) and calls `AKIotEVChargeCommand::setControlType` with the control value. | this page | `a5190_home_logic.dart @0x3943e2c`, call at `@0x3943e94` |
| 3 | app | `setControlType` builds the parameter map with the single key `controlType` (the control value as an unboxed int, `BoxInt64Instr`) and calls `AKIotBasicCommand::writeProperty` with the property name `action_control_charging`. | [iot_kit_channels](../reference/iot_kit_channels.md) | `ev_charge_command.dart @0x394478c` (key), `@0x39447cc` (property name), `@0x39447d4` (call) |
| 4 | app | `writeProperty` calls `AKIoTKitManagerImpl.writeProperty`, which sends the identifier `akiot.device.write_property` with `handle`. | [iot_kit_channels](../reference/iot_kit_channels.md) | `basic_command.dart @0x228feb0`; `ak_iot_kit_manager_impl.dart @0x228ff28` (identifier), `@0x228ff48` (`handle`) |
| 5 | SDK | The native kit sends the property write. Whether it goes over MQTT or BLE is decided inside the kit, not in Dart. | [iot_kit_channels](../reference/iot_kit_channels.md#transport-one-method-channel-three-event-channels) untagged by design (no app-side fact) |
| 6 | app | Awaits the result, takes the end time and measures the elapsed time in milliseconds for telemetry (`difference`, then `d0 = 1000`); `_actionEventTrack` reports it. | this page | `a5190_home_logic.dart @0x3943ea0`, `@0x3943ed8`, `@0x3943ee0`, `@0x39440c0` |
| 7 | app | Result type `success` (`cmp` with the pool object `pp+0xa5b0` at `@0x3943f10`): waits 20 s and then clears a page flag (closure `@0x3944914`); if the control value is boost it shows the boost success toast (`BoostTipsToastUtil::showSuccessToast`). | this page | `a5190_home_logic.dart @0x3943f2c` (`Future.delayed`), `@0x3943f60` (boost compare), `@0x3943f70` (toast) |
| 8 | app | Any other result: `parseControllerCommandResult` maps the code to a toast. | this page | `a5190_home_logic.dart @0x3943f98`, toasts at `@0x3943fdc`, `@0x3944000` (start failed), `@0x3944040` (stop failed), `@0x394405c` (generic) |

The four control values (`start`, `cancel`, `startNow`, `boost`) and their wire values are owned by [ev_charger_device_models.md](../models/ev_charger_device_models.md#chargecontroltype-ev-charger-command-value); the page call sites are the ones named in Trigger.

## Side effects

- The 20 s delay of step 7 clears a page flag afterwards (`a5190_home_logic.dart @0x3944914`, closure of `onTap`); what the flag controls in the UI is not read.
- The elapsed time is reported to analytics (step 6).
- The flow does not re-read the charger state; later status arrives through the normal receive path.

## Timing (delays/polling)

20 s: `Future.delayed` at `a5190_home_logic.dart @0x3943f2c` uses the pool `Duration` `pp+0x29cf0` with `off_8` = 0x1312d00 = 20,000,000 microseconds (a pool object value, not a register immediate, so the Smi rule does not apply). No polling.

## Failure paths

- BLE gate: the connect sheet is shown instead of sending (Preconditions).
- Result not `success`: toast from step 8; the key `evChargeStartFailedHint` for the start values and `evChargeStopFailedHint` for stop. Error codes: [errors](../api/errors.md).
- No retry in Dart.
- Toast choice for step 8 (`a5190_home_logic.dart @0x3943f98` to `@0x394406c`): `parseControllerCommandResult` (`ev_charge_command_error_code_parser.dart @0x3944478`) reads the error object of the result (`field_1b`; null gives no text, `@0x39444a8`) and its `code` (a Smi, untagged with `LoadInt32Instr`, so the compares are real values): codes 33 to 40 (0x21 to 0x28) and 48 to 51 (0x30 to 0x33) map to the localization keys `evChargeErrorCode0x21` to `evChargeErrorCode0x28` and `evChargeErrorCode0x30` to `evChargeErrorCode0x33` (compares `@0x3944514` to `@0x3944658`; the compares at `@0x3944534` and `@0x3944658` use the tagged values 0x42 and 0x66); every other code, 41 to 47 and above 51, gives null. A non-null text is shown as is. When the parser returns null the page falls back on the control value (raw enum index in `ChargeControlType.off_8`, pool objects `pp+0xe0040` and following): start now (1) and start (2) show `evChargeStartFailedHint` (`@0x3943fdc`, `@0x3944000`), cancel (3) shows `evChargeStopFailedHint` (`@0x3944040`, compare `cmp w0, #6` on the tagged index at `@0x3944030`), and boost (4) shows the generic `failed` (`@0x394405c`). An empty text is not shown (`cbz` on the string length at `@0x3944074`). The English texts of the twelve keys (pool localization map, `pp.txt` lines 53376 to 53387): 0x21 "EV charger is preparing to charge.", 0x22 "EV charger is charging.", 0x23 "Charging paused by charger.", 0x24 "Charging paused by EV.", 0x25 "EV charger has stopped.", 0x26 "EV charger is currently reserved.", 0x27 "EV charger unavailable.", 0x28 "EV charger faulty.", 0x30 "Unstable network connection. Please try again later.", 0x31 "EV charger timeout. Please try again later.", 0x32 "Something's wrong. Please try again later.", 0x33 "EV charger offline. Please check network connection." Fact belongs on the future `devices/a5190.md` and on [../api/errors.md](../api/errors.md) (Task 10).

## Since/changed

- `encoding_type` (the old page's open question, issue 322): the string `encoding_type` is absent from the 3.24.3 object pool, the asm and the `libapp.so` binary (grep count 0 in each). The Dart layer sends only `controlType`; the old statement that the encoding happens below the Flutter layer is consistent with this, but nothing in the app shows where it would happen.
- The old page called the path "MQTT only". The Dart code shows only the property write; the transport is not visible (step 5). Rows consumed: 16 (enum values, OK).

## Known unknowns

- Which transport the native kit uses for the property write, and what bytes it puts on the wire (needs a capture, see the upstream constants on [../mqtt/upstream_commands.md](../mqtt/upstream_commands.md)).
