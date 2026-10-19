> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# EV charger start charging (A5190 / A5191)

How the app starts, stops, force-starts or boosts a charging session of the EV charger from its home page. The command goes to the AK IoT kit as a property write; the Dart layer sends no cloud request and no MQTT or BLE frame of its own. The four control values have no other owner page yet (the legacy [../devices/ev_charger.md](../devices/ev_charger.md) is not reworked), so the table in the Steps section is their record; the identifier `akiot.device.write_property` is owned by [../reference/iot_kit_channels.md](../reference/iot_kit_channels.md). "Audit row N" counts the data rows of [../docs/audit/FLOWS.md](../docs/audit/FLOWS.md), see the [README](README.md#audit-row-numbers).

## Trigger (UI action)

On the EV charger home page (`a5190_home_page.dart`) four buttons call `A5190HomeLogic::onTapControl` (`a5190_home_logic.dart @0x3943d7c`) with one `ChargeControlType` pool object each: boost at `a5190_home_page.dart @0x43b1a54`, start now at `@0x43b1af4`, start at `@0x43b1b94`, stop (enum member `cancel`) at `@0x43b1c34`. A second set of closures with the same four objects sits at `a5190_home_page.dart @0x3943d60`, `@0x39449a0`, `@0x39449fc`, `@0x3944a58`. The button labels are not read from the asm; the toast keys of the old page are used below only where they appear as strings in the handler.

## Preconditions

- A paired A5190 or A5191 device on the home page.
- Connection gate in `onTapControl`: the getter `showBleConnectBottomSheet` (call at `a5190_home_logic.dart @0x3943dd0`, getter `@0x39447ec`) asks `_isOcppOrBleEnable` (`@0x3944820`, function `@0x3944854`). That function returns true when the page state `field_c3` is true (`@0x3944874`) and otherwise `_isBleConnected` (`@0x3944890`). When it returns false the getter returns the page flag `field_bf` (`@0x3944834`); if that flag is true the page opens `AkBleConnectBottomSheet` (`@0x3943e08`) and returns without sending. The names of `field_c3` and `field_bf` are not in the asm.

## Steps

| # | actor | action | owner page link | asm citation |
|---|---|---|---|---|
| 1 | user | Taps one of the four buttons. | this page | `a5190_home_page.dart @0x43b1a54`, `@0x43b1af4`, `@0x43b1b94`, `@0x43b1c34` |
| 2 | app | `onTapControl` runs the gate of Preconditions, records the start time (`DateTime`) and calls `AKIotEVChargeCommand::setControlType` with the control value. | this page | `a5190_home_logic.dart @0x3943e2c`, call at `@0x3943e94` |
| 3 | app | `setControlType` builds the parameter map with the single key `controlType` (the control value as an unboxed int, `BoxInt64Instr`) and calls `AKIotBasicCommand::writeProperty` with the property name `action_control_charging`. | [iot_kit_channels](../reference/iot_kit_channels.md) | `ev_charge_command.dart @0x394478c` (key), `@0x39447cc` (property name), `@0x39447d4` (call) |
| 4 | app | `writeProperty` calls `AKIoTKitManagerImpl.writeProperty`, which sends the identifier `akiot.device.write_property` with `handle`. | [iot_kit_channels](../reference/iot_kit_channels.md) | `basic_command.dart @0x228feb0`; `ak_iot_kit_manager_impl.dart @0x228ff28` (identifier), `@0x228ff48` (`handle`) |
| 5 | SDK | The native kit sends the property write. Whether it goes over MQTT or BLE is decided inside the kit, not in Dart. | [iot_kit_channels](../reference/iot_kit_channels.md#transport-one-method-channel-three-event-channels) | `string-only` |
| 6 | app | Awaits the result, takes the end time and measures the elapsed time in milliseconds for telemetry (`difference`, then `d0 = 1000`); `_actionEventTrack` reports it. | this page | `a5190_home_logic.dart @0x3943ea0`, `@0x3943ed8`, `@0x3943ee0`, `@0x39440c0` |
| 7 | app | Result type `success` (`cmp` with the pool object `pp+0xa5b0` at `@0x3943f10`): waits 20 s and then clears a page flag (closure `@0x3944914`); if the control value is boost it shows the boost success toast (`BoostTipsToastUtil::showSuccessToast`). | this page | `a5190_home_logic.dart @0x3943f2c` (`Future.delayed`), `@0x3943f60` (boost compare), `@0x3943f70` (toast) |
| 8 | app | Any other result: `parseControllerCommandResult` maps the code to a toast. | this page | `a5190_home_logic.dart @0x3943f98`, toasts at `@0x3943fdc`, `@0x3944000` (start failed), `@0x3944040` (stop failed), `@0x394405c` (generic) |

Control values (the wire value is the field `off_14` of the enum object, not `off_8`, which is the enum index and differs; row tag: asm-traced, audit row 16). The four objects are pool entries and are not Smi-tagged immediates.

| member | pool object and page call site | wire value `controlType` | UI string of the old page |
|---|---|---|---|
| `start` | `pp+0xe0048`, `a5190_home_page.dart @0x43b1b94` | `off_14` is 1 | `evChargeStart` |
| `cancel` (stop) | `pp+0xe0050`, `a5190_home_page.dart @0x43b1c34` | `off_14` is 2 | `evChargeStop` |
| `startNow` | `pp+0xe0040`, `a5190_home_page.dart @0x43b1af4` | `off_14` is 3 | `evChargeStartNow` |
| `boost` | `pp+0xdfed8`, `a5190_home_page.dart @0x43b1a54` | `off_14` is 4 | `evChargeBoost` |

## Side effects

- The 20 s delay of step 7 clears a page flag afterwards (`a5190_home_logic.dart @0x3944914`, closure of `onTap`); what the flag controls in the UI is not read.
- The elapsed time is reported to analytics (step 6).
- The flow does not re-read the charger state; later status arrives through the normal receive path.

## Timing (delays/polling)

20 s: `Future.delayed` at `a5190_home_logic.dart @0x3943f2c` uses the pool `Duration` `pp+0x29cf0` with `off_8` = 0x1312d00 = 20,000,000 microseconds (a pool object value, not a register immediate, so the Smi rule does not apply). No polling.

## Failure paths

- BLE gate: the connect sheet is shown instead of sending (Preconditions).
- Result not `success`: toast from step 8; the key `evChargeStartFailedHint` for the start values and `evChargeStopFailedHint` for stop. Error codes: `api/errors.md`.
- No retry in Dart.

## Since/changed

- `encoding_type` (the old page's open question, issue 322): the string `encoding_type` is absent from the 3.24.3 object pool, the asm and the `libapp.so` binary (grep count 0 in each). The Dart layer sends only `controlType`; the old statement that the encoding happens below the Flutter layer is consistent with this, but nothing in the app shows where it would happen.
- The old page called the path "MQTT only". The Dart code shows only the property write; the transport is not visible (step 5). Rows consumed: 16 (enum values, OK).

## Known unknowns

- Which transport the native kit uses for the property write, and what bytes it puts on the wire (needs a capture, see the upstream constants on [../mqtt/upstream_commands.md](../mqtt/upstream_commands.md)).
- The names and meaning of `field_c3` and `field_bf` in the gate.
- The mapping of result codes to the toasts in step 8 (the compares at `@0x3943fa8` to `@0x3944034` were not decoded).
