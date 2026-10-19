# Changelog

## Errata 2026-10 (Smi decoding)

One line per WRONG verdict of the Phase 2 Smi sweeps (full tables in `docs/audit/`). Doc line numbers refer to the file BEFORE the banner was added (commit 68bc345); in the current file add 2.

- FLOWS.md:29 — `"cmd": 246` (param_type 6 schedule) → cmd 123 (charging/http/http_request_repository_impl.dart set17C1SiteDeviceParam @0x238cca8 (3.24.3))
- FLOWS.md:35-36 — "`cmd` = 246 (0xF6) for cloud, NOT 17 ... thomluther uses 17, APK uses 246" → APK sends 123 (0x7B); 17 = setSiteDeviceParam path (charging/http/http_request_repository_impl.dart set17C1SiteDeviceParam @0x238cca8 (3.24.3))
- FLOWS.md:40 — "up to 30 TLV tags (a2-bb)" → 29 data tags a2-be (+ CRC tag 0xFD) (charging/ble/device/A17C1/a17c1_device_controller.dart setTacticsTime @0x288ac88 (AllocateArray), keys @0x288ac90..0x288ae50 (3.24.3))
- FLOWS.md:40 — "timestamp (fd)": tag fd is a timestamp → tag 0xFD = CRC32, not a timestamp (charging/ble/device/A17C1/a17c1_device_controller.dart setTacticsTime @0x288b224 (intToList4 of the parsed Crc32.convert), @0x288b238 (3.24.3))
- FLOWS.md:41 — "MTU = 400 (larger than default 200 ...)" → 200 (and only a non-zero flag) (charging/ble/device/A17C1/a17c1_device_controller.dart setTacticsTime @0x288b274 (3.24.3))
- FLOWS.md:42 — CRC32 checksum appended as tag `0x1FA (506)` → 0xFD (253) (charging/ble/device/A17C1/a17c1_device_controller.dart setTacticsTime @0x288b238 (3.24.3))
- FLOWS.md:56, 531 — "Maximum 14 time slots (from 14 buffer allocations)" → 7 slots (charging/ble/device/A17C1/a17c1_device_controller.dart setTacticsTime @0x288ac88 (3.24.3))
- FLOWS.md:129, 140, 533 — `running(6)`: idle(0) -> running(6); state table `6 Running` → running = 3 (charging/ui/page/device/a17x8/a17x8countdown/a17x8countdown_logic.dart changeStartOrPause @0x3dd03e4 (3.24.3))
- FLOWS.md:129, 139 — `paused(4)`: running(6) -> paused(4); state table `4 Paused` → paused = 2 (charging/ui/page/device/a17x8/a17x8countdown/a17x8countdown_logic.dart changeStartOrPause @0x3dd03ec (3.24.3))
- FLOWS.md:147, 151, 163, 173, 181 — "type: Start = 6"; `type: 6=start, 4=pause, 0=delete` → start/resume 3, pause 2, delete 0 (charging/ui/page/device/a17x8/a17x8countdown/a17x8countdown_logic.dart changeStartOrPause @0x3dd03e4..0x3dd04a8 (3.24.3) and charging/ble/device/A17X8/a17x8_device_controller.dart setCountdownCmd @0x3dcfdf0 (`intToList(type)`))
- FLOWS.md:149-154 — TLV Key column `0x0144 / 0x0146 / 0x0148 / 0x014A` (a2..a5) for 0x007E → 0xA2, 0xA3, 0xA4, 0xA5 (charging/ble/device/A17X8/a17x8_device_controller.dart setCountdownCmd @0x3dcfde4, @0x3dcfe20, @0x3dcfe54, @0x3dcfe90 (3.24.3))
- FLOWS.md:187 — "Bytes [0-5]: totalTime via listToInt" → bytes [0-2] (charging/ble/device/A17X8/a17x8_device_commands.dart parseCountDownInfo @0x3b63514..0x3b63534 (3.24.3))
- FLOWS.md:188 — "Byte [6]: switchState" → byte [3] (charging/ble/device/A17X8/a17x8_device_commands.dart parseCountDownInfo @0x3b6354c (3.24.3))
- FLOWS.md:189-190 — "Byte [8]: elapsed time marker"; `remaining = max(0, totalTime - elapsed)` → byte [4]; elapsed bytes [5-7] (charging/ble/device/A17X8/a17x8_device_commands.dart parseCountDownInfo @0x3b6358c, @0x3b635f0 (3.24.3))
- FLOWS.md:230-237 — TLV Key column `0x0144 / 0x0146 / 0x0148 / 0x014A / 0x014C / 0x014E` (a2..a7) for 0x007C → 0xA2..0xA7 (charging/ble/device/A17X8/a17x8_device_controller.dart setTimingCmd @0x3de1b54, @0x3de1c0c, @0x3de1d34, @0x3de1d58, @0x3de1dd0, @0x3de1e8c (3.24.3))
- FLOWS.md:314-317, 323-330 — TLV Key column `0x0144 .. 0x014E` and tag names `a2, a4, a6, a8, aa, ac` → a2, a3, a4, a5, a6, a7 (+a8) (charging/ble/device/A17C1/a17c1_device_controller.dart setDevicePowerLimit @0x2276ec0, @0x2276f08, @0x2276f44, @0x2276f90, @0x2276fcc, @0x227704c (3.24.3) (path 1))
- FLOWS.md:308 — guard 4: `0W grid-collapse? offset 0x28F == 2` (BR: `mode_type (offset 0x28F) == 2`) → == 1 (charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart anonymous closure @0x25c9328 (3.18.0))
- FLOWS.md:333-334 — After sending: `charge_priority == 4` sets `is_charge_priority`; `== 2` sets the secondary flag → charge_priority == 2 and == 1 (charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart anonymous closure @0x25c9884 and @0x25c98cc, @0x25c9ad8 and @0x25c9af0 (3.18.0))
- FLOWS.md:348 — `{tag a2=currentSOC, a4=minSOC, a6=newSOC}` → a2, a3, a4 (charging/ble/device/A17C1/a17c1_device_controller.dart setSoc @0x3d95494, @0x3d954d0, @0x3d95510 (3.24.3) (3-tag branch))
- FLOWS.md:349 — `EventBus fire(2214, 2)` → data = 1 (id 2214 correct) (charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart @0x3d94ec8 (id) and @0x3d94ed0 (data) (3.24.3))
- FLOWS.md:426 — parseSwitchData indices `[18]=AC state, [20]=DC state, [24]=smart mode` → [9], [10], [12] (charging/ble/device/A1770/a1770_commands.dart parseSwitchData @0x45eb1f8, @0x45eb27c, @0x45eb384 (3.24.3))
- FLOWS.md:505 — "Most currencies use 5 decimal places, 2 specific markets use 4 (JPY/KRW?)" → 5 for PN A5143/A1903, else 2 (charging_pn.dart PN::getDecimalPlacesForCode @0x29af0dc (3.24.3))
- FLOWS.md:531 — summary table: "cmd=246, CRC32, 14 max slots" → cmd 123, CRC tag 0xFD, 7 slots (see lines 29, 42, 56)
- FLOWS.md:533 — summary table: "States 0/4/6, delete=type 0" → states 0/2/3 (see line 129)
- BUSINESS_RULES.md:27-30 — path tags `a2(feeder) + a4(0) + a6(acPower) + a8(switch) + aa(pvLimit) + ac(extra)` → a2..a7 (charging/ble/device/A17C1/a17c1_device_controller.dart setDevicePowerLimit @0x2276ec0..0x227704c (3.24.3))
- BUSINESS_RULES.md:39 — guard 4: `mode_type (offset 0x28F) == 2` → == 1 (charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart @0x25c9328 (3.18.0))
- BUSINESS_RULES.md:45-46 — `charge_priority == 4` / `== 2` → == 2 and == 1 (charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart @0x25c9884, @0x25c98cc (3.18.0))
- BUSINESS_RULES.md:54 — "single command 0x5E with 30 TLV tags (a2-bb) + timestamp (fd)" → 29 data tags (a2-be) + CRC 0xFD (charging/ble/device/A17C1/a17c1_device_controller.dart setTacticsTime @0x288ac88, @0x288b238 (3.24.3))
- BUSINESS_RULES.md:102 — `power limit enable = device_online AND charge_priority_value == 4` → charge_priority_value == 2 (charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart checkDeviceEnableStatus @0x1e980b4 (3.18.0))
- BUSINESS_RULES.md:74-77 — setBackPower tags `a4 (326)`, `a6 (328)`, `aa (332)`, `ac (334)` → a3, a4, a6, a7 (charging/ble/device/A17C1/a17c1_device_controller.dart setBackPower @0x281a610, @0x281a658, @0x281a698, @0x281a6d8 (3.24.3))
- BUSINESS_RULES.md:174-175 — `setSoc(upper=10, lower=5, step=10)` and `MessageEvent(id=2214, data=2)` → data = 1 (charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart @0x3d94ec8, @0x3d94ed0 (3.24.3))
- BUSINESS_RULES.md:180-185 — `getPowerLimitList - 22 Attributes Fetched` → 11 (3.18.0) / 14 (3.24.3) (charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart @0x1b9f8bc (3.18.0))
- BUSINESS_RULES.md:207, 272, 345 — "A17X8 Central Connection Guard ... Default timeout: 30 seconds for command response" (also lines 272, 345) → 5 s command wait (30 s = connect timeout) (charging/ble/device/A17X8/a17x8_device_controller.dart sendCommandWithParam @0x24190c0 (3.24.3))
- BUSINESS_RULES.md:232 — weekday TLV tag `0x14E` → 0xA7 (charging/ble/device/A17X8/a17x8_device_controller.dart setTimingCmd @0x3de1e8c (3.24.3))
- BUSINESS_RULES.md:345 — `30s` called the "BLE command timeout" (and background disconnect) → 30 s is the connect timeout; command wait 5 s; background disconnect 30 min (charging/communication/command_controller/ble_command_controller.dart sendCommand @0x226fc88 (3.24.3))
- BUSINESS_RULES.md:469-475 — HES work modes `0 standBy`, `2 gridOff`, `6 working` → 0 standby, 1-8 working, 255 gridOff (charging/ui/page/device/a5101/setting/grid_dispatch/grid_dispatch_logic.dart WorkMode switch @0x27c7724-0x27c7810 (3.24.3))
- BUSINESS_RULES.md:566, 571, 768 — Transaction lock "Default timeout: 12 seconds (when no device-specific config)" → 6 s (config present) / 15 s (default) (base_service/ak_iot_kit/transaction/transactionlock_interceptor.dart @0x221b1f0 (3.24.3))
- BUSINESS_RULES.md:594-597 — Currency decimal places: most markets 5, 2 markets 4 → 5 (A5143, A1903) / 2 (others) (charging_pn.dart @0x29af0dc (3.24.3))
- BUSINESS_RULES.md:674-682 — A17C5 gate `if firmware_component_version >= 2: isSupportPvLimit = true` → data[11] == 1 (needs length >= 12) (charging/ble/device/A17C5/a17c5_device_commands.dart @0x4863624 (3.24.3))
- BUSINESS_RULES.md:693-699 — BLE lockout `Status 15` / `Status 16` → 10 and 11 (pp.txt BleCmdStatus map [pp+0xe480] (3.24.3))
- ENUMS.md:162-165 — Backup Mode `0 AUTO`, `1 MANUAL` → auto = 1, manual = 0 (charging disaster_preparedness_command.dart setBackup @0x3574770 (3.24.3, ak_soft_pps_ems))
- ENUMS.md:166 — Backup Mode `4 CLEAR` → 2 (ak_soft_pps_ems/src/disaster_preparedness/command/disaster_preparedness_command.dart clearBackup @0x2603c00 (3.24.3))
- ENUMS.md:331-337 — BLE Command Status `7 scanWifiFailed .. 13 fireWarmVeriryFailed` → 33, 34, 35, 36, 37, 113, 114 (name-to-code binding inferred from pool instance order; keys 7–13 absence is direct) (pp.txt BleCmdStatus map [pp+0xe480] (3.24.3))
- ENUMS.md:338-340 — BLE Command Status `14 needAuthentication, 15 passwordWrongAuthenticationFailed, 16 passwordRetryCountExceededAuthenticationFailed` → 9, 10, 11 (pp.txt BleCmdStatus [pp+0x50bb8], [pp+0x50be8], [pp+0x50bf8] and map [pp+0xe480] (3.24.3))
- ENUMS.md:341 — BLE Command Status `17 unknown` → no wire code (fallback) (pp.txt BleCmdStatus [pp+0xe488])
- BLE_COMMAND_MAP.md:40 — Frame offset 1: `0x02` "Protocol version (APK-observed)" → 0x01 (charging/communication/transformer/zx_command_transformer.dart _getSettingCommand @0x22735ac (3.24.3))
- BLE_COMMAND_MAP.md:41 — Frame offset 2: direction byte `0x42`/`0x44` → 0x21 / 0x22 (charging/communication/transformer/zx_command_transformer.dart _getSettingCommand @0x2273510 (3.24.3))
- BLE_COMMAND_MAP.md:60 — not Smi: Data Type Codes: `3 (var)` variable 1-4 bytes, raw bytes → 3 is returned only for 4-byte values (charging/communication/transformer/zx_command_transformer.dart _getDataType @0x2273f84 (3.24.3))
- BLE_COMMAND_MAP.md:80 — `fd`: milliseconds (used in CMD_COMMON_V2) → tag 0xFD = CRC32, not a timestamp (charging/ble/device/A17C1/a17c1_device_controller.dart setBackPower @0x281aa44..0x281aa94, setTacticsTime @0x288b224..0x288b238 (3.24.3))
- BLE_COMMAND_MAP.md:105 — Head example `"cmd": 34` → 17 (charging/communication/transformer/mqtt_command_transformer.dart `cmdMap` @0x226f2a4 (value for normalCommand; builder @0x226f274) (3.24.3); @0x19a27b8 (3.18.0))
- BLE_COMMAND_MAP.md:106 — Head example `"cmd_status": 4` → 2 (charging/communication/transformer/mqtt_command_transformer.dart generateCommand @0x226ef94 (3.24.3); @0x19a2548 (3.18.0))
- BLE_COMMAND_MAP.md:107 — Head example `"sign_code": 2` → 1 (charging/communication/transformer/mqtt_command_transformer.dart generateCommand @0x226efa8 (3.24.3); @0x19a255c (3.18.0))
- BLE_COMMAND_MAP.md:124 — Command type `normalCommand` `0x22 (34)` -> `cmd` 34 → 17 (0x11) (charging/communication/transformer/mqtt_command_transformer.dart `cmdMap` 0x226f2a4 (3.24.3, builder @0x226f274); @0x19a27b8 (3.18.0))
- BLE_COMMAND_MAP.md:125 — Command type `otaCommand` `0x0C (12)` -> `cmd` 12 → 6 (0x06) (charging/communication/transformer/mqtt_command_transformer.dart `cmdMap` 0x226f2b8 (3.24.3, builder @0x226f274); @0x19a27cc (3.18.0))
- BLE_COMMAND_MAP.md:126 — Command type `a17y0OtaCommand` `0x0C (12)` -> `cmd` 12 → 6 (0x06) (charging/communication/transformer/mqtt_command_transformer.dart `cmdMap` 0x226f2cc (3.24.3, builder @0x226f274); @0x19a27e0 (3.18.0))
- BLE_COMMAND_MAP.md:127 — Command type `uploadLogCommand` `0x0A (10)` -> `cmd` 10 → 5 (0x05) (charging/communication/transformer/mqtt_command_transformer.dart `cmdMap` 0x226f2e0 (3.24.3, builder @0x226f274); @0x19a27f4 (3.18.0))
- BLE_COMMAND_MAP.md:128 — Command type `remoteScanWifi` `0x32 (50)` -> `cmd` 50 → 25 (0x19) (charging/communication/transformer/mqtt_command_transformer.dart `cmdMap` 0x226f2f4 (3.24.3, builder @0x226f274); @0x19a2808 (3.18.0))
- BLE_COMMAND_MAP.md:129 — Command type `remoteSwitchWifi` `0x34 (52)` -> `cmd` 52 → 26 (0x1A) (charging/communication/transformer/mqtt_command_transformer.dart `cmdMap` 0x226f308 (3.24.3, builder @0x226f274); @0x19a281c (3.18.0))
- BLE_COMMAND_MAP.md:130 — Command type `unbindDevice` `0x18 (24)` -> `cmd` 24 → 12 (0x0C) (charging/communication/transformer/mqtt_command_transformer.dart `cmdMap` 0x226f31c (3.24.3, builder @0x226f274); @0x19a2830 (3.18.0))
- BLE_COMMAND_MAP.md:131 — Command type `getDeviceBssid` `0x38 (56)` -> `cmd` 56 → 28 (0x1C) (charging/communication/transformer/mqtt_command_transformer.dart `cmdMap` 0x226f330 (3.24.3, builder @0x226f274); @0x19a2844 (3.18.0))
- BLE_COMMAND_MAP.md:146 — not Smi: Fragments: `(MTU - 10)` bytes per packet → MTU - 11 (or exactly 200 when MTU is 0) (charging/ble_zx/base/assemble_command_util.dart splitPackageCmd @0x227226c..0x2272280 (3.24.3))
- BLE_COMMAND_MAP.md:238 — "`list[N] == 2` -> feature enabled (value 2 = true in this protocol)" → list[N] == 1 -> true (charging/ble/device/A17C1/a17c1_device_commands.dart parseDeviceAllInfo @0x48665dc, @0x4866790, @0x48667e0, @0x4866878 (3.24.3); @0x3679a3c, @0x3679a84, @0x3679b34 (3....)
- BLE_COMMAND_MAP.md:262 — `msg_seq`: "APK uses `2`, upstream uses `1`" → APK uses 1 (charging/communication/transformer/mqtt_command_transformer.dart generateCommand @0x226ef34 (3.24.3); @0x19a24e8 (3.18.0))
- BLE_COMMAND_MAP.md:297 — CountDownInfo `[0..3]` 4 bytes `totalTimeMinutes` `listToInt(bytes[0:3])` → bytes [0..2], 3 bytes (charging/ble/device/A17X8/a17x8_device_commands.dart parseCountDownInfo @0x3b63510..0x3b63534 (3.24.3))
- BLE_COMMAND_MAP.md:298 — CountDownInfo `[4]` 1 byte "(unused)" → byte [4] is read (field_f) (charging/ble/device/A17X8/a17x8_device_commands.dart parseCountDownInfo @0x3b63588..0x3b635b4 (3.24.3))
- BLE_COMMAND_MAP.md:300 — CountDownInfo `[6]` `switchState` 0=off, 1=on → byte [3] (charging/ble/device/A17X8/a17x8_device_commands.dart parseCountDownInfo @0x3b6354c (3.24.3))
- BLE_COMMAND_MAP.md:301 — CountDownInfo `[8]` `endHour` → byte [4] (charging/ble/device/A17X8/a17x8_device_commands.dart parseCountDownInfo @0x3b6358c (3.24.3))
- BLE_COMMAND_MAP.md:301 — TimingInfo `[8]` `endHour` end hour (0-23) → byte [4] (charging/ble/device/A17X8/a17x8_device_commands.dart parseTimingInfo @0x3b63b50 (3.24.3))
- BLE_COMMAND_MAP.md:311 — TimingInfo `[2]` `switchState` 0=off, 2=on (note: 2, not 1!) → byte [1] == 1 is "on" (charging/ble/device/A17X8/a17x8_device_commands.dart parseTimingInfo @0x3b63a98, @0x3b63ab4 (3.24.3))
- BLE_COMMAND_MAP.md:312 — TimingInfo `[4]` `hours` start hour (0-23) → byte [2] (charging/ble/device/A17X8/a17x8_device_commands.dart parseTimingInfo @0x3b63ad8 (3.24.3))
- BLE_COMMAND_MAP.md:313 — TimingInfo `[6]` `minutes` start minute (0-59) → byte [3] (charging/ble/device/A17X8/a17x8_device_commands.dart parseTimingInfo @0x3b63b14 (3.24.3))
- BLE_COMMAND_MAP.md:315 — TimingInfo `[9..]` weekdays, one byte per day (1=Mon..7=Sun) → weekdays start at [5] (charging/ble/device/A17X8/a17x8_device_commands.dart parseTimingInfo @0x3b63bb0..0x3b63c0c (3.24.3))
- BLE_COMMAND_MAP.md:320 — DischargeTimeModel (`setTacticsTime` 005e) "14 maximum time slots" → 7 slots (charging/ble/device/A17C1/a17c1_device_controller.dart setTacticsTime @0x288ac88 (3.24.3))
- BLE_COMMAND_MAP.md:330 — "Uses tags a2-bb (30 tags) + fd (timestamp)" → 29 data tags a2-be + CRC tag 0xFD (charging/ble/device/A17C1/a17c1_device_controller.dart setTacticsTime @0x288ac88, keys @0x288ac90..0x288ae50, @0x288b238 (3.24.3))
- BLE_COMMAND_MAP.md:361 — OutputPortInfo `[1..4]` 4 bytes voltage mV → bytes [1..2], 2 bytes (charging/ble/device/A2345/a2345_device_commands.dart parseChargePortInfo @0x3b2ecc8..0x3b2ecf4 (3.24.3))
- BLE_COMMAND_MAP.md:362 — OutputPortInfo `[5..8]` 4 bytes current mA → bytes [3..4], 2 bytes (charging/ble/device/A2345/a2345_device_commands.dart parseChargePortInfo @0x3b2ed0c..0x3b2ed38 (3.24.3))
- BLE_COMMAND_MAP.md:363 — OutputPortInfo `[9..12]` 4 bytes power mW → bytes [5..6], 2 bytes (charging/ble/device/A2345/a2345_device_commands.dart parseChargePortInfo @0x3b2ed50..0x3b2ed7c (3.24.3))
- BLE_COMMAND_MAP.md:364 — OutputPortInfo `[14]` status → byte [7] (charging/ble/device/A2345/a2345_device_commands.dart parseChargePortInfo @0x3b2edd0 (3.24.3))
- BLE_COMMAND_MAP.md:365 — OutputPortInfo `[16]` temperature (degrees) → byte [8] (charging/ble/device/A2345/a2345_device_commands.dart parseChargePortInfo @0x3b2ee0c (3.24.3))
- BLE_COMMAND_MAP.md:604 — `carChargerLockStatus` 2=off, 4=on ("bit-shifted") → 1=off, 2=on (ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart (map with key "carChargerLockStatus") @0x2cdf80c..0x2cdf81c (3.24.3))
- BLE_COMMAND_MAP.md:605 — `port_saving_mode` 1=normal, 2=smart, 4=custom (DeviceSavingModeEnum) → device byte 1 = close (1), 2 = open (2); no value 4 (charging/ble/device/A1753/a1753_device_commands.dart parseDeviceAllInfo @0x484f318..0x484f348 (3.24.3); pp.txt DeviceSavingModeEnum [pp+0x15a60] notSupport 0, [pp+0x55...)
- BLE_COMMAND_MAP.md:823 — not Smi: "131 total DataCodeType enum values" → 133 (pp.txt Obj!A5101DataCodeType (133 instances) (3.24.3, 3.18.0))
- BLE_COMMAND_MAP.md:828 — not Smi: SET-only `0x02BE-0x02D1` `diesel*` "(14 codes)" → 17 codes (0x02be-0x02cd and 0x02d1) (charging/ble/device/A5101/a5101_commands.dart setDataCodeMap @0x3b8a184 (dieselMode 0x02be) .. @0x3b8a670 (0x02cd), @0x3b8a6c4 (dieselNextMaintenanceTime 0x02d1) (3.24.3))
- BLE_COMMAND_MAP.md:829 — not Smi: SET-only `0x09C9` `gridSensitivity` → gridSensitivity = 0x09EE (0x09C9 is gridSensitivityEnable) (charging/ble/device/A5101/a5101_commands.dart setDataCodeMap @0x3b8a814 (0x09c9 = gridSensitivityEnable), @0x3b8a868 (0x09ee = gridSensitivity) (3.24.3))
- BLE_COMMAND_MAP.md:830 — not Smi: SET-only `0x09D4` `softwarePowerExportLimitInput` → softwarePowerExportLimitInput = 0x09D5 (charging/ble/device/A5101/a5101_commands.dart setDataCodeMap @0x3b8a8bc (0x09d4 = softwarePowerExportLimitEnable), @0x3b8a910 (0x09d5 = softwarePowerExportLimitInput) ...)
- BLE_COMMAND_MAP.md:831 — not Smi: SET-only `0x09D3` `x1AllowCharge` → x1AllowCharge = 0x0050, and it is in BOTH maps (charging/ble/device/A5101/a5101_commands.dart setDataCodeMap @0x3b8a9b8 (0x09d3 = hardwarePowerExportLimitInput), @0x3b8aa0c (0x0050 = x1AllowCharge); getDataCodeMap @...)
- BLE_COMMAND_MAP.md:837 — not Smi: GET-only `0x014C` `pvState` → pvState = 0x0004 (0x014C is outageFrequency) (charging/ble/device/A5101/a5101_commands.dart getDataCodeMap @0x3b8b814 (pvState 0x0004), @0x3b8bc04 (0x014c = outageFrequency) (3.24.3))
- BLE_COMMAND_MAP.md:838 — not Smi: GET-only `0x014D` `batRemain` → batRemain = 0x000D (0x014D is blackoutDuration) (charging/ble/device/A5101/a5101_commands.dart getDataCodeMap @0x3b8b7c0 (batRemain 0x000d), @0x3b8bc58 (0x014d = blackoutDuration) (3.24.3))
- BLE_COMMAND_MAP.md:839 — not Smi: GET-only `0x0155` `supportFunction` → supportFunction = 0x0156 (0x0155 is fastStopState) (charging/ble/device/A5101/a5101_commands.dart getDataCodeMap @0x3b8c144 (supportFunction 0x0156), @0x3b8c0f0 (0x0155 = fastStopState) (3.24.3))
- BLE_COMMAND_MAP.md:840 — not Smi: GET-only `0x0160` `minSoc` → minSoc = 0x0018 (0x0160 is clsState) (charging/ble/device/A5101/a5101_commands.dart getDataCodeMap @0x3b8c1ec (minSoc 0x0018), @0x3b8c3e4 (0x0160 = clsState) (3.24.3))
- BLE_COMMAND_MAP.md:841 — not Smi: GET-only `0xE004` `systemStatus` → systemStatus = 0x0000 (0xE004 is upgradeType) (charging/ble/device/A5101/a5101_commands.dart getDataCodeMap @0x3b8bfa0 (systemStatus 0x0000), @0x3b8c2e8 (0xe004 = upgradeType) (3.24.3))
- BLE_COMMAND_MAP.md:846 — not Smi: Both GET and SET `0xF009` `gridStandardCode` → gridStandardCode = 0x0212 (0xF009 is timeZoneSetting) (charging/ble/device/A5101/a5101_commands.dart setDataCodeMap @0x3b88db8 / getDataCodeMap @0x3b8ac28 (gridStandardCode 0x0212); @0x3b88dfc / @0x3b8ac6c (0xf009 = timeZo...)
- BLE_COMMAND_MAP.md:846 — not Smi: Both `0x0137` `backupMode` → backupMode = 0x0009 (0x0137 is selfCheckError) (charging/ble/device/A5101/a5101_commands.dart setDataCodeMap @0x3b8901c / getDataCodeMap @0x3b8ae8c (backupMode 0x0009); @0x3b892c4 / @0x3b8b178 (0x0137 = selfCheckErr...)
- BLE_COMMAND_MAP.md:847 — not Smi: Both `0x020E` `batteryLoadPower` → batteryLoadPower = 0x003C (0x020E is autoPowerOnOrOff) (charging/ble/device/A5101/a5101_commands.dart setDataCodeMap @0x3b89170 / getDataCodeMap @0x3b8b024 (batteryLoadPower 0x003c); @0x3b895b4 / @0x3b8b37c (0x020e = autoPo...)
- BLE_COMMAND_MAP.md:847 — not Smi: Both `0x0222` `pvLoadPower` → pvLoadPower = 0x0034 (0x0222 is screenLightTime) (charging/ble/device/A5101/a5101_commands.dart setDataCodeMap @0x3b890e8 / getDataCodeMap @0x3b8af9c (pvLoadPower 0x0034); @0x3b89390 / @0x3b8b244 (0x0222 = screenLight...)
- BLE_COMMAND_MAP.md:848 — not Smi: Both `0x0221` `gridLoadPower` → gridLoadPower = 0x0044 (0x0221 is screenSwitch) (charging/ble/device/A5101/a5101_commands.dart setDataCodeMap @0x3b8923c / getDataCodeMap @0x3b8b0f0 (gridLoadPower 0x0044); @0x3b899a4 / @0x3b8b6c4 (0x0221 = screenSwi...)
- BLE_COMMAND_MAP.md:848 — not Smi: Both `0xF00C` `gridBatteryPower` → gridBatteryPower = 0x0042 (0xF00C is manualBackupPower) (charging/ble/device/A5101/a5101_commands.dart setDataCodeMap @0x3b891f8 / getDataCodeMap @0x3b8b0ac (gridBatteryPower 0x0042); @0x3b8965c / @0x3b8b424 (0xf00c = manual...)
- BLE_COMMAND_MAP.md:850-852 — not Smi: "~60 codes in enum but NOT in either BLE map": `soc`(0x3a), `workMode`(0x46), `batteryReserve`(0x21), `peakShaving`(0x24), `heatPumpSGEnable`(0x57), `evChargerAllPower`(0x85), `autoDisaster`(0x44) → the listed members ARE in the maps (charging/ble/device/A5101/a5101_commands.dart setDataCodeMap / getDataCodeMap (3.24.3); pp.txt Obj!A5101DataCodeType off_8 (soc 0x3a, workMode 0x46, batteryReserve 0x2...)
- BLE_COMMAND_MAP.md:878 — 005e `setBackPower` `fd: timestamp` → tag 0xFD = CRC32, not a timestamp (charging/ble/device/A17C1/a17c1_device_controller.dart setBackPower @0x281aa44..0x281aa94 (3.24.3))
- BLE_COMMAND_MAP.md:879 — 005e `setTacticsTime` `a2-bb: 30 schedule slot tags, fd: timestamp` → 29 data tags a2-be + CRC tag 0xFD (charging/ble/device/A17C1/a17c1_device_controller.dart setTacticsTime @0x288ac88..0x288ae50, @0x288b238 (3.24.3))
- BLE_COMMAND_MAP.md:880 — 005e `setPeakValley` `a2: mode, a3: flag, fd: timestamp` → fd is CRC32 (tags a2, a3 OK) (charging/ble/device/A17C1/a17c1_device_controller.dart setPeakValley @0x428a888, @0x428a8c8 (tags a2, a3), @0x428b058..0x428b0a8 (CRC, tag 506) (3.24.3))
- BLE_COMMAND_MAP.md:890 — not Smi: 0069 `hourPerMinute` "(params unclear)" → not an opcode builder (charging/ble/device/A17C1/a17c1_device_controller.dart hourPerMinute @0x274e0b8 (3.24.3))
- BLE_COMMAND_MAP.md:907 — not Smi: A17X8 007b `setCountdownCmd` (alt) "shares tags with 007e" → 0x7b is setLocationLightSwitchCmd (charging/ble/device/A17X8/a17x8_device_controller.dart setLocationLightSwitchCmd @0x2763e7c (3.24.3))
- BLE_COMMAND_MAP.md:919 — not Smi: A17C0 0068 `setMicroInversionModel` `a2-a9: brand, model, min/max load` → a2-ad (12 tags) (charging/ble/device/A17C0/a17C0_device_controller.dart setMicroInversionModel @0x261cda0..0x261d378 (3.24.3))
- BLE_COMMAND_MAP.md:1026 — A1753 extra tags: tag `f8` -> 0x197+19b (DeviceSavingModeEnum) → byte 1 = close, byte 2 = open, else notSupport; [2], [3] == 1 (bools) (charging/ble/device/A1753/a1753_device_commands.dart parseDeviceAllInfo (3.24.3, 3.18.0))
- BLE_COMMAND_MAP.md:1100 — not Smi: A2345 "28 tags parsed in `parseDeviceAllInfo`" → 30 (charging/ble/device/A2345/a2345_device_commands.dart parseDeviceAllInfo @0x3b2ff2c, size 0x1990 (3.24.3); 30 `indexString` arguments in 3.18.0 as well)
- BLE_COMMAND_MAP.md:1393 — not Smi: A17X8 0405: tag `a3` -> field_187 (List\<int\>, len≥2 check, [4]==2→bool) → `listToInt == 1` bool, field 0x18f in 3.24.3 (charging/ble/device/A17X8/a17x8_device_commands.dart parseDeviceAllInfo (3.24.3, 3.18.0))
- BLE_COMMAND_MAP.md:1428 — A17C1 Battery & SOC: tag `e8` -> field_2bf (bitlist) → bit[0] == 1 means heating (charging/ble/device/A17C1/a17c1_device_commands.dart parseDeviceAllInfo (3.24.3, 3.18.0))
- BLE_COMMAND_MAP.md:1478 — fb/fc sub-field `[2]` `== 2` -> bool at 0x49b `ui_feature_flag` → element [1] == 1 (charging/ble/device/A17C1/a17c1_device_commands.dart parseDeviceAllInfo (fc branch) @0x48665bc..0x48665f0 (3.24.3); @0x3679a24..0x3679a58 (3.18.0))
- BLE_COMMAND_MAP.md:1479 — fb/fc sub-field `[10]` `== 2` -> bool at 0x457 `unknown_bool` → element [5] == 1 (charging/ble/device/A17C1/a17c1_device_commands.dart parseDeviceAllInfo (fc branch) @0x486660c..0x4866648 (3.24.3); @0x3679a6c..0x3679aa8 (3.18.0))
- BLE_COMMAND_MAP.md:1480 — fb/fc sub-field `[14]` `== 2` -> bool at 0x28b `capability_flag_14` ("isEnable0w") → element [7] == 1 (charging/ble/device/A17C1/a17c1_device_commands.dart parseDeviceAllInfo (fc branch) @0x4866770..0x48667a4 (3.24.3); @0x3679b1c..0x3679b4c (3.18.0))
- BLE_COMMAND_MAP.md:1481 — fb/fc sub-field `[18]` raw -> 0x28f `capability_flag_18` → element [9] (charging/ble/device/A17C1/a17c1_device_commands.dart parseDeviceAllInfo (fc branch) @0x486670c..0x4866730 (3.24.3); @0x3679ac0..0x3679adc (3.18.0))
- BLE_COMMAND_MAP.md:1658 — A1790 NEW: tag `f8` -> field_197+19b (List\<int\>, DeviceSavingModeEnum) → [0], [1]: byte 1 = close, 2 = open, else notSupport; [2], [3], [6], [7], [8] == 1 (charging/ble/device/A1790/a1790_device_commands.dart parseDeviceAllInfo / charging/ble/device/A1790/a1790_device_commands.dart parseWorkInfo (3.24.3, 3.18.0))
- BLE_COMMAND_MAP.md:1702 — Task-1 text: "`r16` holds the start offset ... `r2` holds the end offset (start + field_width) ... `r17` the object field offset"; "reads sequential 2-byte fields ... `sublist(offset, offset+2)`" → r2 = start (real), r16 = end (raw / 2); the first two fields are 4 bytes, then 2-byte fields up to start 63, then 1-byte fields (charging/ble/device/A1780/a1780_commands.dart parseOtherData @0x45ebffc..0x45ec028 (3.24.3); @0x2d022f0 (3.18.0))
- BLE_COMMAND_MAP.md:1704 — Task-1 table column "Pos (r16)" values 26, 34, 38, 42, ... 170 (as buffer read positions) → end offsets N / 2 (13, 17, 19, 21, ... 85) (charging/ble/device/A1780/a1780_commands.dart parseOtherData (46 blocks, @0x45ebffc..@0x45ed508) (3.24.3); @0x2d022f0..@0x2d037fc (3.18.0))
- BLE_COMMAND_MAP.md:1738 — not Smi: Pos 144 / End 71 / Obj offset 0x3D3 (979) `c3` (battery_soh, listToInt()) → offset 0x3D3 (979) belongs to the block r16 = 142 / r2 = 70 (3.18.0 @0x2d0324c); this block stores at 795 (0x31b) (charging/ble/device/A1780/a1780_commands.dart parseOtherData @0x2d032f4 (3.18.0), @0x45ed000 (3.24.3))
- BLE_COMMAND_MAP.md:1759 — Switch data table positions `18, 20, 22, 24` ("sequential 2-byte positions"; "Parses 4 switch/boolean fields") → byte indexes [9], [10], [11], [12] (single bytes) (charging/ble/device/A1780/a1780_commands.dart parseSwitchData @0x45ed658, @0x45ed6dc, @0x45ed760, @0x45ed7e4 (3.24.3); @0x2d03944, @0x2d039c0, @0x2d03a3c, @0x2d03ab8 (...)
- BLE_COMMAND_MAP.md:1768 — parseCountdownData: "reads 4 elements from positions 18, 20, 22, 24 ... `listToInt()` ... stored at 0x1AB (427)" → byte indexes [9], [10], [11], [12] (4 bytes); offset 0x1AB changed to 439 = 0x1b7 (charging/ble/device/A1770/a1770_commands.dart parseCountdownData @0x45e9c10, @0x45e9c40, @0x45e9c70, @0x45e9ca0 (3.24.3); @0x2cfff58..0x2d00058 (3.18.0))
- BLE_COMMAND_MAP.md:1774 — parseCountdownData position table `18-24`, `26-28`, `30` → [9..12] and [13..16] (charging/ble/device/A1770/a1770_commands.dart parseCountdownData (3.24.3))
- BLE_COMMAND_MAP.md:1775 — parseCountdownData second group: "positions 26, 28 and 30" -> countdown_hours, countdown_minutes? → a second 4-byte value from byte indexes [13..16], stored at 443 (431 in 3.18.0) (charging/ble/device/A1770/a1770_commands.dart parseCountdownData @0x45e9d60, @0x45e9d90, @0x45e9dc0, @0x45e9df0 (3.24.3); @0x2d00088..0x2d00100 (3.18.0))
- BLE_COMMAND_MAP.md:2345-2349 — not Smi: "Present in BOTH" decimals 189, 190, 191, 192, 193 (0xBD-0xC1: bd, be, bf, c0, c1) → read by A17C5 only (charging/ble/device/A17C1/a17c1_device_commands.dart and A17C5/a17c5_device_commands.dart parseDeviceAllInfo (3.24.3, 3.18.0 identical))
- BLE_COMMAND_MAP.md:2361-2363 — not Smi: "ONLY in A17C5" decimals 170, 171, 172 (aa temperature, ab photovoltaic_power, ac battery_power_signed) → read by A17C1 as well (charging/ble/device/A17C1/a17c1_device_commands.dart and A17C5/a17c5_device_commands.dart parseDeviceAllInfo (3.24.3, 3.18.0 identical))
- BLE_COMMAND_MAP.md:2367-2368 — not Smi: "ONLY in A17C5" decimals 210 (d2 light_mode), 211 (d3 output_power) → d2 and d3 are read by A17C1 (d2 not by A17C5) (charging/ble/device/A17C1/a17c1_device_commands.dart and A17C5/a17c5_device_commands.dart parseDeviceAllInfo (3.24.3, 3.18.0 identical))
- BLE_COMMAND_MAP.md:2372-2375 — not Smi: "ONLY in A17C5" decimals 224 (e0), 225 (e1), 232 (e8), 233 (e9) → read by A17C1; not read by the A17C5 function itself (charging/ble/device/A17C1/a17c1_device_commands.dart and A17C5/a17c5_device_commands.dart parseDeviceAllInfo (3.24.3, 3.18.0 identical))
- BLE_COMMAND_MAP.md:2402 — not Smi: SB3 summary: "Extra data tags: 0xD4 (timeout), 0xD5 (pv_limit), 0xD6 (ac_input_limit), 0xE9 (unknown SB3-only)" → 0xE9 is also an A17C1 tag (charging/ble/device/A17C5/a17c5_device_commands.dart parseDeviceAllInfo (d4 @0x4861f60, d5 @0x48641e8, d6 @0x4862e80); A17C1 parseDeviceAllInfo e9 @0x4866bb4 (3.24.3))

*Batch C1 (VALIDATION_MODEL.md, PARAM_DATA_STRUCTURES.md, JSON_EXAMPLES.md, RESPONSE_EXAMPLES.md, endpoints/charging_disaster_prepared.md, patches/README.md): line numbers refer to the files at commit f105769 (before the banner); in the current file add 2.*

- VALIDATION_MODEL.md:27 — not Smi: `get_power_limit` `(param_type=16)` → get_power_limit takes no param_type (data/param_types.json row 16 (3.24.3): param_type 16 = SOLARBANK_POWERDOCK, getCombineBoxListData; getSitePowerLimit @0x2378fb4 (api/power_service/site/get_power_limit.md))
- VALIDATION_MODEL.md:608, 620 — not Smi: Summary table `get_power_limit`(16) → no param_type (same as line 27)
- VALIDATION_MODEL.md:298 — not Smi: `a4-be` = 7 weekday slots (005e) → 7 slots is right but the tag range is a3-be (28 slot tags = 7 x 4), a2 = mode tag (charging/ble/device/A17C1/a17c1_device_controller.dart setTacticsTime @0x288ac88 (3.24.3))
- PARAM_DATA_STRUCTURES.md:129, 134 — not Smi: Key Pattern `"cmd": 17`; "`cmd: 17` appears to be a constant for SET operations" → not a constant for the APK: 17 for param types 1-5 and 23, 123 for 6, 13, 16, 18, 19, 20, 26, 32 (data/param_types.json rows (3.24.3): cmd_raw 34 -> 17 for param types 1-5, 23; cmd_raw 246 -> 123 for 6, 13, 16, 18, 19, 20, 26, 32)
- PARAM_DATA_STRUCTURES.md:286 — not Smi: `setDisaster: ... "manual_disaster_switch": 1` → true (bool) (ak_soft_ems/manual_power_backup/manual_power_backup_logic.dart @0x25ecd50 (3.24.3))
- endpoints/charging_disaster_prepared.md:137 — `disaster_type` `Type code (4 = manual)` → manual_disaster_detail.disaster_type = 2 (ak_soft_ems/manual_power_backup/manual_power_backup_logic.dart @0x25ecd80 (3.24.3); charging/ui/page/station/mixin/auto_disaster.dart @0x346eb78 (3.18.0))
- endpoints/charging_disaster_prepared.md:166 — Manual-disaster request body `"disaster_type": 4` → 2 (ak_soft_ems/manual_power_backup/manual_power_backup_logic.dart @0x25ecd80 (3.24.3); charging/ui/page/station/mixin/auto_disaster.dart @0x346eb78 (3.18.0))
- endpoints/charging_disaster_prepared.md:173 — "`disaster_type = 4` is hardcoded for manual mode" → 2 (ak_soft_ems/manual_power_backup/manual_power_backup_logic.dart @0x25ecd80 (3.24.3))
- endpoints/charging_disaster_prepared.md:204 — `"is_ble": 4` in the quit request → 2 (ak_soft_ems/ems_service_impl.dart showSevereWeatherModeDialog @0x3324ed0 (context field_13), map key `is_ble` @0x3325100 (3.24.3); charging/ui/page/station/mixin/auto_disaster.dart @0x34568c4 (3.18.0))
- endpoints/charging_disaster_prepared.md:209 — "`is_ble = 4` is hardcoded" → 2 (ak_soft_ems/ems_service_impl.dart @0x3324ed0, @0x33251ec (context field_13) (3.24.3); charging/ui/page/station/mixin/auto_disaster.dart @0x34568c4 (3.18.0))
- endpoints/charging_disaster_prepared.md:219 — `backupMode = 4` (CLEAR) via `clearBackup()` → 2 (ak_soft_pps_ems/src/disaster_preparedness/command/disaster_preparedness_command.dart clearBackup @0x2603c00 (3.24.3); charging/ak_iot_kit/business/disaster_preparedness/command/disaster_preparedness_command.dart @0x1f4a424 (3.18.0))
- endpoints/charging_disaster_prepared.md:241-242 — setBackup example `"backupMode": 1` with `manualBackupSwitch: true` → backupMode 1 means AUTO; a manual backup sends 0 (ak_soft_pps_ems/src/disaster_preparedness/command/disaster_preparedness_command.dart setBackup @0x3574770 (3.24.3); @0x1dc71a4 (3.18.0))
- endpoints/charging_disaster_prepared.md:251 — `backupMode (0=AUTO, 1=MANUAL)` → AUTO = 1, MANUAL = 0 (ak_soft_pps_ems/src/disaster_preparedness/command/disaster_preparedness_command.dart setBackup @0x3574770 (3.24.3))
- endpoints/charging_disaster_prepared.md:263 — `"backupMode": 4` in clearBackup() → 2 (ak_soft_pps_ems/src/disaster_preparedness/command/disaster_preparedness_command.dart clearBackup @0x2603c00 (3.24.3); @0x1f4a424 (3.18.0))
- endpoints/charging_disaster_prepared.md:280 — `backupMode (0=AUTO, 1=MANUAL, 4=DISABLED)` → AUTO = 1, MANUAL = 0, CLEAR (not DISABLED) = 2 (ak_soft_pps_ems/src/disaster_preparedness/command/disaster_preparedness_command.dart setBackup @0x3574770, clearBackup @0x2603c00 (3.24.3))
- endpoints/charging_disaster_prepared.md:294 — subPackageInfo `any()` with a `== 4` predicate → subPackageStatus == 2 (ak_soft_pps_ems/src/disaster_preparedness/model/disaster_preparedness_info.dart anonymous closure @0x4585950, constant @0x45859b4 (3.24.3))
- endpoints/charging_disaster_prepared.md:302 — "38+ warning types" → 19 warning types (ak_soft_ems/ems_list/constants/disaster_constants.dart nine inner arrays @0x4200354..@0x4200904 (3.24.3))
- endpoints/charging_disaster_prepared.md:306 — Winter Weather warning count `6` → 3 (ak_soft_ems/ems_list/constants/disaster_constants.dart @0x4200354 (3.24.3); flutter_ems/ems_list/constants/disaster_constants.dart @0x332cae4 (3.18.0))
- endpoints/charging_disaster_prepared.md:307 — Freeze warning count `2` → 1 (ak_soft_ems/ems_list/constants/disaster_constants.dart @0x42003fc (3.24.3); flutter_ems/ems_list/constants/disaster_constants.dart @0x332cb8c (3.18.0))
- endpoints/charging_disaster_prepared.md:308 — Snow Storm warning count `4` → 2 (ak_soft_ems/ems_list/constants/disaster_constants.dart @0x42004ac (3.24.3); flutter_ems/ems_list/constants/disaster_constants.dart @0x332cc3c (3.18.0))
- endpoints/charging_disaster_prepared.md:309 — Fire Weather warning count `2` → 1 (ak_soft_ems/ems_list/constants/disaster_constants.dart @0x4200554 (3.24.3); flutter_ems/ems_list/constants/disaster_constants.dart @0x332cce4 (3.18.0))
- endpoints/charging_disaster_prepared.md:310 — Wind warning count `2` → 1 (ak_soft_ems/ems_list/constants/disaster_constants.dart @0x42005f4 (3.24.3); flutter_ems/ems_list/constants/disaster_constants.dart @0x332cd84 (3.18.0))
- endpoints/charging_disaster_prepared.md:311 — Thunderstorm warning count `2` → 1 (ak_soft_ems/ems_list/constants/disaster_constants.dart @0x4200694 (3.24.3); flutter_ems/ems_list/constants/disaster_constants.dart @0x332ce24 (3.18.0))
- endpoints/charging_disaster_prepared.md:312 — Tornado warning count `2` → 1 (ak_soft_ems/ems_list/constants/disaster_constants.dart @0x4200734 (3.24.3); flutter_ems/ems_list/constants/disaster_constants.dart @0x332cec4 (3.18.0))
- endpoints/charging_disaster_prepared.md:313 — Flood warning count `10` → 5 (ak_soft_ems/ems_list/constants/disaster_constants.dart @0x4200814 (3.24.3); flutter_ems/ems_list/constants/disaster_constants.dart @0x332cfa4 (3.18.0))
- endpoints/charging_disaster_prepared.md:314 — Tropical/Hurricane warning count `8` → 4 (ak_soft_ems/ems_list/constants/disaster_constants.dart @0x4200904 (3.24.3); flutter_ems/ems_list/constants/disaster_constants.dart @0x332d094 (3.18.0))
- patches/README.md:33 — fc sub-field `[2] ui_flag (==2 -> enabled)`; patch byte key `"02"`, `MASK: 0x02` → element [1] == 1 (heuristic: index-basis equivalence BLE list <-> MQTT bytes assumed, not traced) (charging/ble/device/A17C1/a17c1_device_commands.dart parseDeviceAllInfo fc branch index @0x48665bc, compare @0x48665dc (3.24.3); index @0x3679a24, compare @0x3679a3c (3.18.0))
- patches/README.md:34 — fc sub-field `[14] is_enable_0w (==2 -> zero-export enabled, debug "-isEnable0w-")`; patch comment `fc[14]==2 means 0W enabled`; byte key `"14"`, `MASK: 0x02` → element [7] == 1 (heuristic: index-basis equivalence BLE list <-> MQTT bytes assumed, not traced) (charging/ble/device/A17C1/a17c1_device_commands.dart parseDeviceAllInfo fc branch index @0x4866770, compare @0x4866790 (3.24.3); index @0x3679b1c, compare @0x3679b34 (3.18.0))
- patches/README.md:35 — fc sub-field `[18] feeder0w_config (used in setDevicePowerLimit)`; byte key `"18"` → element [9] (heuristic: index-basis equivalence BLE list <-> MQTT bytes assumed, not traced) (charging/ble/device/A17C1/a17c1_device_commands.dart parseDeviceAllInfo fc branch @0x486670c..@0x4866730 (3.24.3); @0x3679ac0..@0x3679adc (3.18.0))
- patches/README.md:42 — "Value 2 = enabled in this protocol (NOT 1)" → value 1 = enabled (charging/ble/device/A17C1/a17c1_device_commands.dart parseDeviceAllInfo fc branch compares @0x48665dc, @0x486662c, @0x4866790 (3.24.3); @0x3679a3c, @0x3679a84, @0x3679b34 (3.18.0))
- patches/README.md:53, 56 — "Note fc[14] value ... Check if fc[14] changed from 0<->2" → fc[7], 0<->1 (charging/ble/device/A17C1/a17c1_device_commands.dart parseDeviceAllInfo fc branch index @0x4866770, compare @0x4866790 (3.24.3))

## 2026-04-04 — Home Power Panel (A17B1) complete device documentation + flow analysis

> Triggered by [ha-anker-solix #480](https://github.com/thomluther/ha-anker-solix/issues/480)
> (manual backup mode for HPP). Deep dive into all HPP-related APK code.
> Code-traced through 12 decompiled Dart files (40,000+ lines of ARM64 ASM).

### New documents

- **`devices/home_power_panel.md`** — Complete A17B1 device reference (10 KB):
  MQTT status fields (_PP_JSON), Mode State enum, EmsModeType, BLE commands,
  Cloud API methods, Dart UI page inventory, Python API implementation map,
  implementation gaps for HA integration

- **`endpoints/charging_disaster_prepared.md`** — Previously undocumented API service
  layer (6 endpoints) for backup/disaster mode control:
  `set_site_device_disaster`, `get_site_device_disaster`, `get_site_device_disaster_status`,
  `get_support_func`, `quit_disaster_prepare`, `clear`

### Key findings for thomluther/ha-anker-solix

**Complete flow analysis** — code-traced through the actual decompiled Dart to determine
how backup mode really works:

1. **Two abstraction layers exist** (Cloud API vs IoT Kit) — they use **different field names**
   for the same concepts. The Cloud API layer is what should be implemented:
   - Cloud API: `auto_disaster_switch` / `manual_disaster_switch` / `manual_disaster_detail`
   - IoT Kit: `backupMode` / `autoBackupSwitch` / `manualBackupSwitch` (native bridge, skip this)

2. **`charging_disaster_prepared/`** — 6 endpoints, code-traced request/response structures:
   - `set_site_device_disaster`: Enable manual backup = `{manual_disaster_switch: true, manual_disaster_detail: {disaster_type: 4, start_time: <unix>, end_time: <unix>}}`
   - `get_site_device_disaster` → `DisasterSetting` (3 fields: auto_switch, manual_switch, details[])
   - `get_support_func` → `SupportFunc` (support_auto_disaster + country codes)
   - `get_site_device_disaster_status` → `DisasterStatus` (auto/manual status + current detail)
   - `quit_disaster_prepare`: `{type, identifier_id, is_ble: 4, disaster_type: <from status>}`
   - `clear`: via IoT Kit only (`backupMode: 4`)

3. **5 data models fully traced** from `device_disaster_model.dart` (1136 lines):
   - DisasterSetting (ChangeNotifier, 3 fields)
   - DisasterStatus (3 fields incl. nullable DisasterPrepareDetail)
   - DisasterPrepareDetail (7 fields incl. disaster_type, uuid, event)
   - DisasterEvent (5 fields, start/end as unix timestamps)
   - SupportCountryCode (code + google_code)

4. **Initialization flow traced**: onInit → resolve siteId → 3 parallel GETs
   (setting + support + status) via RefreshManager

5. **Manual disaster `disaster_type = 4`** hardcoded in APK

6. **`charging_hes_svc/device_command`** — Station-level EMS strategy (separate system):
   - `electricity_strategy` nested object with `conserve_percent` and `mode`
   - `off_grid_switching` with `off_grid_enable` and `off_grid_sensitivity`
   - Full `A5101DeviceCommandModel` with 4 nested sub-models documented

**HPP communication architecture**:
- MQTT: Read-only JSON status via `{SN}/0505/a2` — no MQTT commands exist
- BLE: "Minimal-Command Device" — only Realtime Trigger + EV Charger commands
- Cloud API: Exclusive control channel (3 service prefixes)

### Expanded existing documents

- **`endpoints/charging_hes_svc.md`** — +22 new endpoints from pp.txt string pool
  (sync_back_up_history, enable_aiems_mode, get_history_setting, get_device_self_check,
  get_electric_utility_and_electric_plan_list, get_external_device_config, etc.)

- **`endpoints/charging_energy_service.md`** — +8 endpoints with parameter details
  (get_system_running_info with full response fields, energy_statistics with all params,
  get_sns, restart_peak_session, etc.)

- **`endpoints/device_specific.md`** — New `[A17B1]` section with all disaster_prepared
  and device_command endpoints tagged

- **`models/hes.md`** — A5101DeviceCommandModel expanded from 1 line to full structure:
  ElectricityStrategy, OffGridSwitching, HeatPumpModel (8 fields),
  AdvancedSetting (4 fields). Plus expanded CheckFunctionModel (7 fields),
  AutoDisasterDetailModel (5 fields), DisasterPrepareDetailsModel, A5101StationGridConfigModel.

- **`ENUMS.md`** — Added Backup Mode enum (AUTO=0, MANUAL=1, CLEAR=4)

- **`README.md`** — Updated charging_disaster_prepared description

### pp.txt string pool analysis

Extracted and cross-referenced 100+ HPP-related string constants:
- 7 `charging_disaster_prepared/` endpoint paths with pp offsets
- 19 `akiot.device.*` action strings (IoT Kit command layer)
- All backup/disaster field names: `backupMode`, `backupSwitch`, `backupStartTime`,
  `backupEndTime`, `backupPowerStartTime`, `backupPowerEndTime`, `chargeDischargeStatus`,
  `manualBackupStartTime`, `manualBackupEndTime`
- EMS strategy fields: `electricity_strategy`, `electricity_strategy_mode`,
  `conserve_percent`, `off_grid_switching`, `off_grid_enable`, `off_grid_sensitivity`
- Debug strings: `"sendA17B1Command--->cmdId: "`, `"====A17B1 StationMqttMixin AutoDisaster cmd: "`

### Files changed

- 2 new files (`devices/home_power_panel.md`, `endpoints/charging_disaster_prepared.md`)
- 6 files expanded (`charging_hes_svc.md`, `charging_energy_service.md`, `device_specific.md`,
  `models/hes.md`, `ENUMS.md`, `README.md`)
- 1 file updated (`CHANGELOG.md`)

---

## 2026-03-28 — Protocol reference, business rules, flows, device-tested corrections

### Device-tested corrections (on own SB2 Pro + Smart Plug, mqtt_monitor)

- **0W mode = c7 (home_load_preset) set to 0** — no special flag, just preset=0W
  (136 MQTT messages, automation off, c7 changed from 130W→0W at 17:22:43)
- **fc = static capability array** — 136 messages over 5 minutes, zero bytes changed
- **isEffective inversion DISPROVED** — APK assembly showed inverted logic but device
  test shows a4=1=enabled (normal). Assembly inversion was UI-layer, not protocol.
- **Schedule CRUD confirmed** — 3 mqtt_monitor runs: CREATE(a2=1), MODIFY(a2=2), DELETE(a2=0)
  Weekdays [01,02,05] = Mon+Tue+Fri. thomluther's naming independently identical.
- **A17X8 a3/ae are STATIC** in 0405 status — not schedule/countdown flags as APK suggested

### New documents

- **BUSINESS_RULES.md** (781 lines) — SET command guards, error codes, state machine, safety rules
- **FLOWS.md** (529 lines) — 14 step-by-step traces from UI button to wire bytes
- **BLE_COMMAND_MAP.md** (~2400 lines) — Wire protocol, 200+ tags, enums, data structures

### Concrete NEW API/Protocol Findings (not previously known)

**Wire protocol details** (from ZXCommandTransformer/ZXCmdUtil assembly):
- Two protocol layers: MQTT binary (`FF 09` header) wraps BLE TLV (`0xA1` tag marker)
- Data type codes: 0x01=ui(1B), 0x02=**signed** int LE(2B), 0x03=variable, 0x04=**bitmap**, 0x05=signed float LE
- Checksum: XOR of all bytes (upstream-confirmed)
- Timestamps: Unix seconds (not ms) — upstream-confirmed
- Byte order: little-endian everywhere — upstream-confirmed

**MQTT envelope** (from MqttCommandTransformer):
- `sess_id`/`msg_seq` hardcoded in APK ("1"/2) — upstream uses different values ("1234-5678"/1)
- Topic pattern: `cmd/anker_power/{product_key}/{device_sn}/req` — upstream-confirmed
- 8 MqttCommandType values with cmd codes (0x22=normal, 0x0C=OTA, 0x18=unbind, etc.)
- Payloads are base64-encoded, optional GZip (0x1F8B magic), then JSON

**A17X7 Smart Meter** (upstream has mapping, our initial names were partially wrong):
- Tags a8/a9/aa/ab confirmed by upstream as grid_to_home/pv_to_grid/import_energy/export_energy
- Tags ac/ad are APK firmware-compatibility aliases (not in upstream)
- Debug strings confirm: "fromGrid", "toGrid", "fromGridSum", "toGridSum"

**A17C1 Solarbank 2 — 11 new status tags** (not in upstream 0405 mapping):
- `ae`=ac_output_power_signed (upstream-corrected), `af`=schedule_enabled?, `b8`=ac_input_power?
- `ba`=percentage_value (÷100.0, NOT bitmask), `bb`=heating_power (upstream comment confirmed)
- `fc`=static capability array (device-tested: 136 msgs, zero change on 0W toggle)
- Divisors from assembly: `ab`÷10, `ac`÷10, `b0`÷100, `b7`÷100, `c8`÷10, `d3`÷10

**A17C2 Hybrid Inverter — 8 tags with Chinese debug labels**:
- `ac`="电池充放电功率" (bat charge/discharge power)
- `ae`="并网口功率" (grid-connected port power), `af`="离网口功率" (off-grid port power)
- `d3`="标识当前是否0溃网" (grid collapse flag)

**A17C5 Solarbank 3 — 15+ extra tags vs A17C1**:
- Extra commands: AC socket (0x73), device timeout (0x9A), PV limit, usage mode (0x5E)
- Multi-system messages: 0420/0421/0428

**EV Charger field→TLV tag mapping** (cross-referenced APK field names with upstream tags):
- 12 confirmed tag assignments (controlType→a2, carChargerLockStatus→a3, etc.)
- 3 NEW commands: `ioDetection*`, `disconnectFunction`, `initSettings`
- Only start/stop/boost use encoding_type=2

**A1790 F3800**:
- `b3` uses `bytesToHexString` (NOT listToInt) = battery_serial_hex
- `f8` uses DeviceSavingModeEnum (1=normal, 2=smart, 4=custom)

**A1771/A1753 PPS** — 5 new tags from Chinese debug strings:
- `df`="绿电模式" (green energy mode), `e0`="绿电充电功率上限" (green charge limit)
- `e2`="是否启用波峰波谷" (peak/valley enabled), `e4`="波峰波谷数据"

**Data structures with byte-level layouts**:
- CountDownInfo: 8-byte min payload, remaining = max(0, total - elapsed)
- TimingInfo: 5 fixed bytes + variable weekdays (NOT bitmask, sequential 1-7)
- OutputPortInfo (A2345): portIndex, voltage(mV), current(mA), power(mW)
- SubBatteryInfo (A1790): 17 fields including SOC, health, heating, error

**10 complete enum tables** with API integer values:
- EmsModeType: 1/4/5/8/9/10
- EvChargerDeviceStatus: 0-8 (OCPP-aligned)
- GeneratorMode: 0-6 (silentDc through dcExercise)
- StartWayEnum: 1-8 (wifi/ble/touch/rfid/plug/timed/autoResume/modbus)

**22 FeatureSwitch flags** from SceneInfo:
- New: `enable_aiems_v2`, `grid_to_ev`, `meter_self_testing`, `power_saving_mode`

**Device→Command Matrix**: Which of thomluther's 53 CMD_* each device supports.

**A17D0** identified in A17B1 parser — initially thought unreleased, but is the
[Generator Input Adapter](https://support.ankersolix.com/s/article/Anker-SOLIX-Generator-Input-Adapter-User-Guide-A17D0)
(A17D0111, $399, shipping product).

### Upstream validation (10 findings cross-referenced)

6 confirmed, 4 corrected:
- CONFIRMED: All 6 A17C1 divisors, EV Charger tags, MQTT topic format, timestamps, XOR checksum
- CORRECTED: Data type 0x02 = signed (not unsigned), 0x04 = bitmap (not int)
- CORRECTED: sess_id/msg_seq differ between APK and upstream (both hardcoded)
- CORRECTED: A17C1 tag ae = ac_output_power_signed (not ac_socket_switch)
- CORRECTED: A17X7 tag naming (a8=grid_to_home, a9=pv_to_grid per upstream)

### READ path analysis (methodology breakthrough)

Traced UI/controller consumption of parser-stored values:
- **fc[14]** — APK debug says "isEnable0w" but **device-tested: STATIC** (capability flag, not live setting)
- **fc[18]** — APK uses in setDevicePowerLimit context but **device-tested: STATIC**
- **Tag ba** is percentage (÷100.0) in APK, NOT bitmask as upstream suggests
- **isEffective (a4)** — APK assembly suggested inversion (true→0) but **device-tested: a4=1=enabled (normal)**
- Dart AOT does NOT compile ARM `and` bitmask instructions — uses indexed byte arrays

### Root cause analysis of methodology errors

5 systematic failures identified and documented:
1. Only traced WRITE (parser), missed READ (UI) → Fix: trace both paths
2. Documented storage format, not wire format → Fix: report wire format
3. Inferred semantics from serialization helpers → Fix: helpers only measure size
4. Missed tag aliasing (same offset = same field) → Fix: check offsets
5. Error propagation across devices → Fix: validate semantics first

### BLE_COMMAND_MAP.md growth
From 0 to ~2400 lines covering:
- Wire protocol + MQTT envelope + compression + encryption
- TLV parsing internals + value encoding (scaling, signed, sub-byte)
- ~80 SET commands + ~200 STATUS tags across 13 device families
- 10 enum tables + 5 GET→SET flows + 30 value range definitions
- 6 complete API response model structures
- Device→Command matrix for all upstream devices
- 10 byte-level data structure layouts
- 37 missing upstream CMD_* cross-referenced

---

## 2026-03-28 — BLE/MQTT command map, device pages, protocol cross-reference (Part 2 original)

### BLE/MQTT Command Map (new methodology)

Cross-referenced decompiled APK command builder functions with thomluther's device-tested
TLV tag assignments. Validated on 5 confirmed commands (Smart Plug 007a/007c/007e,
Solarbank 005e/0080) — 100% match rate on field order and types.

Key insight: Dart Smi encoding means assembly constant >> 1 = actual hex tag value.

Coverage:
- **A17C1/C5 (Solarbank 2/3)**: 17 commands, 6 NEW (electricity price, self-test,
  micro power limit)
- **A17X8 (Smart Plug)**: 7 commands, 3 NEW (momentary switch, countdown variant)
- **PPS family**: 17 commands, 3 NEW (light wait time, locale, port memory)
- **A1790 (F3800)**: 3 NEW (generator ATS params, sub-battery switches)
- **A5190 (EV Charger)**: Full field→tag mapping (12 confirmed, 3 NEW: ioDetection,
  disconnect, initSettings)
- **A5101 (X1 HES)**: Different protocol (att_id + JSON, not TLV) — entirely unmapped
- **EverFrost**: 12 commands, ALL NEW (entirely unmapped in upstream)
- **Prime Charger / A91B2**: 9 commands, ALL NEW

### Device pages

Added `devices/` directory with per-device reference pages:
- `solarbank.md` — param_types, usage modes, MQTT commands, abbreviated fields
- `smart_plug.md` — verified MQTT commands, timer fields
- `ev_charger.md` — 35 API endpoints, BLE actions, field→TLV tag mapping
- `x1_hes_e10.md` — 65 A5101DataCodeType MQTT field names with hex codes

Each page links to upstream community issues and all relevant files in this repo.

### Community demand priority

Added P1-P4 priority tags based on thomluther/ha-anker-solix issue analysis.
Tagged non-relevant endpoints (AIOT popups, AI chat, screen savers, easter eggs).

### Confidence language audit

Replaced "verified" with device-tested / upstream-confirmed / structurally inferred
throughout all documentation.

---

## 2026-03-27 — Accuracy overhaul: upstream verification, breadth+depth APK scan (Part 1)

### Critical fixes

- **`set_device_attrs` nesting resolved**: Upstream confirms `switch_0w`, `pv_power_limit`,
  `power_limit`, `ac_power_limit`, `tag`, `init_status` etc. go **inside** `attributes` dict,
  not alongside it. Pattern: `{"device_sn": "...", "attributes": {"switch_0w": 0}}`
- **`setSiteDevicePowerLimit` nesting fixed**: `power_limit`, `limit`, `limit_real` are
  **inside** the JSON-encoded `param_data` string, not top-level request fields
- **`updatePeakAndValley` completely wrong → fixed**: Was documented as `set_site_device_param`
  wrapper with `power_limit, limit, limit_real`. Actually a HES-specific endpoint
  (`/charging_hes_svc/update_hes_utility_rate_plan`) with camelCase fields
  `siteId, peakValleyPriceSeason`
- **`disturb_scenes` nesting fixed**: Boolean fields (`start_charging`, `stop_charging`, etc.)
  go **inside** the `disturb_scenes` object, not at the same level
- **`setDeviceHomeLoadRes` missing `site_id`**: Upstream confirms `site_id` is sent in request
- **`dealUtilityRatePlanData` wrong params**: Had shifted params from `setDeviceFeedGridSwitch`,
  corrected to `peak_sessions`

### endpoints/*.md parameter-shifting bug (150+ functions affected)

All 16 endpoint files had a systematic bug where parameters from one function were
incorrectly assigned to an adjacent function (off-by-one in extraction). All files
regenerated from the authoritative `ENDPOINT_FIELDS.md`.

### Breadth scan: 95 new endpoints from device-specific logic

Scanned device logic files outside `http_request_repository_impl.dart`:
- **6 new API service prefixes**: `/smart_service/v1/`, `/charging_imsg_svc/`,
  `/charging_hes_dynamic_price_svc/`, `/charging_disaster_prepared/`,
  `/charging_common_svc/location/`, `/power_service/v2/`
- **A5190 (EV Charger)**: 35 endpoints — RFID, OCPP, Vehicle, Orders, Sharing
- **A7320 (Generator)**: 32 endpoints — Extender System CRUD, Oil Maintenance, Exercise
- **A5101 (HES/X1)**: 25+ endpoints — AI-EMS, Self-Check, Energy Stats, OTA, Backup
- **Dynamic Pricing**: 6 endpoints
- **Storm Guard / Disaster**: 5 endpoints
- **Anka AI Agent**: 3 endpoints
- All documented in new `endpoints/device_specific.md` with device tags

### Depth scan: 460 toJson() classes analyzed

- **`feed-in_power_limit`** uses a HYPHEN (not underscore!) — discovered in param_data
- **`home_load_data`** has deep nesting: `appliance_loads: [{name, power, number, id}]`
  and `device_power_loads: [{device_sn, power}]`
- **Attributes** contains 6 additional fields: `feeder0w`, `pv_power_limit_option`,
  `user_power_limit`, `legal_power_limit`, `region_power_limit`, `ip_region`
- **Feature flags**: `enable_aiems_v2`, `grid_to_ev`, `meter_self_testing`,
  `power_limit_status`, `power_saving_mode`
- **`reserved_soc`** and **`exceed_alarm`** in SiteConsumptionStrategy

### Upstream cross-reference

- **`cmd=17`** confirmed as SET constant
- **`param_data`** confirmed as JSON string (not nested object)
- **2 missing endpoints added**: `set_power_cutoff` (`device_sn, cutoff_data_id`),
  `set_aps_power` (`sn, power`)
- **`switch_0w` semantics**: 0=allow grid export, 1=block (inverted!)
- **`updateSitePriceRequest`** missing `dynamic_price` nested structure — added

### Minor fixes

- Typo: `counrty` → `country` in getCurrencyGetList
- Response model count: 90 → 91
- `power_limit_option_real` type conflict: null → int (from toJson evidence)
- Function count: "32 functions" → 31 (actual count)
- `bindUnX1Charger` camelCase fields added to REQUIRED_FIELDS

### Confidence language audit

Systematic review of all "verified", "confirmed" claims across 12 files:
- Replaced "verified" with "device-tested" (for mqtt_monitor results)
- Replaced "verified" with "upstream-confirmed" (for thomluther/community-tested code)
- Replaced "confirmed" with "structurally inferred" (for toJson() decompilation evidence)
- Split confidence table: Device-tested / Upstream-confirmed / Structurally inferred / Heuristic
- Credit "upstream community" (not just thomluther) for device testing — except
  Issue #423 which thomluther specifically tested

### HA relevance tagging

- Added community demand priority table (P1-P4) to `device_specific.md`
  based on thomluther/ha-anker-solix issue analysis
- Tagged sections not relevant for HA integration: AIOT popups, Anka AI,
  passport (except login), screen savers, easter eggs, app help/FAQ
- All Anker Solix devices are consumer products (no commercial-only line);
  X1 HES requires installer but is user-owned

### Files changed

- 25 files modified, 2 new files (`endpoints/device_specific.md`, `CHANGELOG.md`)
- Total repo: ~7500 lines across 41 files
