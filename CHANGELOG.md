# Changelog

## Errata 2026-10 (Smi decoding)

One line per WRONG verdict of the Phase 2 Smi sweeps (full tables in `docs/audit/`).

- FLOWS.md:29 — `"cmd": 246` (param_type 6 schedule) → cmd 123 (charging/http/http_request_repository_impl.dart set17C1SiteDeviceParam @0x238cca8 (3.24.3))
- FLOWS.md:35-36 — "`cmd` = 246 (0xF6) for cloud, NOT 17 ... thomluther uses 17, APK uses 246" → APK sends 123 (0x7B); 17 = setSiteDeviceParam path (charging/http/http_request_repository_impl.dart set17C1SiteDeviceParam @0x238cca8 (3.24.3))
- FLOWS.md:40 — "up to 30 TLV tags (a2-bb)" → 29 data tags a2-be (+ CRC tag 0xFD) (charging/ble/device/A17C1/a17c1_device_controller.dart setTacticsTime @0x288ac88 (AllocateArray), keys @0x288ac90..0x288ae50 (3.24.3))
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
- BUSINESS_RULES.md:469-475 — HES work modes `0 standBy`, `2 gridOff`, `6 working` → 0 standby, 1-8 working, 255 gridOff (charging/ui/page/device/a5101/setting/grid_dispatch/grid_dispatch_logic.dart WorkMode switch @0x27c7724-0x27c7810 (3.24.3))
- BUSINESS_RULES.md:566, 571, 768 — Transaction lock "Default timeout: 12 seconds (when no device-specific config)" → 6 s (config present) / 15 s (default) (base_service/ak_iot_kit/transaction/transactionlock_interceptor.dart @0x221b1f0 (3.24.3))
- BUSINESS_RULES.md:594-597 — Currency decimal places: most markets 5, 2 markets 4 → 5 (A5143, A1903) / 2 (others) (charging_pn.dart @0x29af0dc (3.24.3))
- BUSINESS_RULES.md:674-682 — A17C5 gate `if firmware_component_version >= 2: isSupportPvLimit = true` → data[11] == 1 (needs length >= 12) (charging/ble/device/A17C5/a17c5_device_commands.dart @0x4863624 (3.24.3))
- BUSINESS_RULES.md:693-699 — BLE lockout `Status 15` / `Status 16` → 10 and 11 (pp.txt BleCmdStatus map [pp+0xe480] (3.24.3))
- ENUMS.md:162-165 — Backup Mode `0 AUTO`, `1 MANUAL` → auto = 1, manual = 0 (charging disaster_preparedness_command.dart setBackup @0x3574770 (3.24.3, ak_soft_pps_ems))
- ENUMS.md:166 — Backup Mode `4 CLEAR` → 2 (ak_soft_pps_ems/src/disaster_preparedness/command/disaster_preparedness_command.dart clearBackup @0x2603c00 (3.24.3))
- ENUMS.md:331-337 — BLE Command Status `7 scanWifiFailed .. 13 fireWarmVeriryFailed` → 33, 34, 35, 36, 37, 113, 114 (pp.txt BleCmdStatus map [pp+0xe480] (3.24.3))
- ENUMS.md:338-340 — BLE Command Status `14 needAuthentication, 15 passwordWrongAuthenticationFailed, 16 passwordRetryCountExceededAuthenticationFailed` → 9, 10, 11 (pp.txt BleCmdStatus [pp+0x50bb8], [pp+0x50be8], [pp+0x50bf8] and map [pp+0xe480] (3.24.3))
- ENUMS.md:341 — BLE Command Status `17 unknown` → no wire code (fallback) (pp.txt BleCmdStatus [pp+0xe488])

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
