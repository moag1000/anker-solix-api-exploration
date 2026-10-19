> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Page type: device · Owner page: this page

# Smart Plug — A17X8

Row numbers ("audit row N") count the table rows of [../docs/audit/devices.md](../docs/audit/devices.md) from the top; this page consumes rows 36 to 50. Method, tags and the Smi rule: [../METHODOLOGY.md](../METHODOLOGY.md).

## PN, marketing name, generation/family

- `A17X8`, SOLIX Smart Plug (2500 W, energy monitoring). Consumer accessory for the Solarbank ecosystem, used in the smart-plug driven "blend mode" (usage mode `smartplugs`, see [../reference/enums.md](../reference/enums.md#solarbank-usage-mode-upstream)). Marketing name, wattage and role: upstream-confirmed (upstream issues [ha-anker-solix #150](https://github.com/thomluther/ha-anker-solix/issues/150) and [anker-solix-api #124](https://github.com/thomluther/anker-solix-api/issues/124); audit row 49 NOT-FROM-ASM). Switch support is implemented in the upstream library; timer and schedule support were still open when the old page was written.
- The `mini_power` endpoints belong to the Prime Chargers (A2345, A2687), not to the Smart Plug.

## Features matrix

Opcodes are the pool lists `[0, 0x7a]` and so on, which are real bytes and never halved (audit rows 36 to 39); the field tags are halved Smi immediates (raw 324 is tag `a2`, audit rows 40, 41, 48). All fields of a command: [../mqtt/a17x8.md](../mqtt/a17x8.md).

| feature | API (link) | MQTT (link) | BLE (link) | device-tested? |
|---|---|---|---|---|
| relay switch on/off (`007a`) | [set_device_feature](../api/power_service/site/set_device_feature.md) (`setRemainPluginStatus`, `site_id` and a `smart_plug` list); flow: [smart_plug_relay_toggle](../flows/smart_plug_relay_toggle.md) | [007a](../mqtt/a17x8.md#007a-setrelayswitchcmd), `setRelaySwitchCmd` (a17x8_device_controller.dart @0x3073938) | [ble/a17x8.md](../ble/a17x8.md) | yes: FW 0.0.2.7, mqtt_monitor, see "Device-tested by" |
| schedule (`007c`) | none | [007c](../mqtt/a17x8.md#007c-settimingcmd), `setTimingCmd` (a17x8_device_controller.dart @0x3de1eb8); flow: [smart_plug_schedule](../flows/smart_plug_schedule.md) | [ble/a17x8.md](../ble/a17x8.md) | yes: FW 0.0.2.7, mqtt_monitor |
| delayed toggle / countdown timer (`007e`) | none | [007e](../mqtt/a17x8.md#007e-setcountdowncmd), `setCountdownCmd` (a17x8_device_controller.dart @0x3dcfee0); flow: [smart_plug_countdown_timer](../flows/smart_plug_countdown_timer.md) | [ble/a17x8.md](../ble/a17x8.md) | yes: start, pause, resume (upstream PR 283) |
| timer state request (`007f`) | none | [007f](../mqtt/a17x8.md#007f-getcountdowncmd), `getCountdownCmd` (a17x8_device_controller.dart @0x2764034) | [ble/a17x8.md](../ble/a17x8.md) | no |
| status (`0405`, upstream-confirmed message id) | none | [0405](../mqtt/a17x8.md#0405-status-message-param_info) | unknown | no |
| plug data in the site scene info | [scene info](../models/energy.md) (upstream-confirmed; per-plug keys such as `current_power`, `auto_switch`, `running_time`) | none | none | no |

## Command facts consumed from the audit

Tag: asm-traced unless stated. Each fact cites the 3.24.3 site; the field-level table is owned by [../mqtt/a17x8.md](../mqtt/a17x8.md).

- `007a`: one field, `a2` = switch, 0 off and 1 on (audit row 40; `a17x8_device_controller.dart` `setRelaySwitchCmd` key @0x307390c, opcode @0x3073938).
- `007c`: tags `a2` to `a7` are action, slot, enabled, time, switch and weekdays (audit row 41; `a17x8_device_controller.dart` `setTimingCmd` @0x3de1b54, @0x3de1c0c, @0x3de1d34, @0x3de1d58, @0x3de1dd0, @0x3de1e8c). `a2` action: 0 delete, 1 create, 2 modify (audit row 42).
- `007e`: `a2` = 0 is cancel (`a17x8countdown_logic.dart` `deleteCountdown` @0x3dcf9c4, audit row 44); 2 and 3 are pause and resume (`a17x8countdown_logic.dart` `changeStartOrPause` @0x3dd03e4 to @0x3dd04a8, audit row 46, discovered in an mqtt_monitor session and contributed upstream as PR 283). `a4` and `a5` carry the toggle-back switch (keys 328 and 330 halved, `a17x8_device_controller.dart` `setCountdownCmd` @0x3dcfe54, @0x3dcfe90, audit row 48).
- `007e` `a3` (delay) and `a5` (toggle-back delay): the 3-byte encoding has two readings (asm versus upstream); the rows and the conflict are owned by [../mqtt/a17x8.md](../mqtt/a17x8.md#007e-setcountdowncmd) and [../mqtt/README.md](../mqtt/README.md).
- `007e` `a2` = 1 (start) is an upstream value (`CMD_PLUG_DELAYED_TOGGLE`: off 0, start 1, pause 2, resume 3; upstream-confirmed). The app's own start and resume path sends 3 (`changeStartOrPause`, same site as above; audit row 45 NOT-FROM-ASM).
- `007c` `a7` weekdays: the old page said day numbers 1 (Monday) to 7 (Sunday), variable length, "0x07 = Sunday", not a bitmask. That is an upstream and device statement, not an asm fact (audit row 43 NOT-FROM-ASM); the 3.24.3 wire rules are in [../mqtt/a17x8.md](../mqtt/a17x8.md#007c-settimingcmd).
- `007f`: the app polls the timer state with this request (`a17x8_device_controller.dart` opcode @0x2764034, audit row 39).

## Since/changed

| item | old page (3.18.0 reading) | 3.24.3 | audit row |
|---|---|---|---|
| `007e` `a3` and `a5` encoding | "3 bytes (seconds:minutes:hours)" | two readings, see [../mqtt/a17x8.md](../mqtt/a17x8.md); asm-traced `intToList3` @0x3dcfbe4 | 47 (WRONG) |

## Known firmware notes

- A17X8 FW 0.0.2.7 is the firmware on which the commands were tested; no other firmware is recorded. Behavior per firmware is otherwise unknown. Opcodes and tags are owned by [../mqtt/a17x8.md](../mqtt/a17x8.md).

## Known unknowns

Tag: untagged by design (no API fact).

- Confirm the byte order and unit of the `007e` delay values on a device (asm and upstream disagree; the rows are owned by [../mqtt/a17x8.md](../mqtt/a17x8.md)).
- How saved schedules appear in the `0405` status message (TimingInfo readback) and the full schedule create, modify, delete cycle.
- A system export ZIP with MQTT data recorded while the plug is toggled and while a timer runs (requested upstream).
- Whether day numbers or a bitmask are used for `007c` weekdays on current firmware (audit row 43).
- Open test requests for this product: [../docs/DEVICE_TEST_BACKLOG.md](../docs/DEVICE_TEST_BACKLOG.md).

## Device-tested by

mqtt_monitor session on A17X8 FW 0.0.2.7 (pause and resume, contributed as upstream PR 283); tester name, client version and date are not recorded in the old page.
