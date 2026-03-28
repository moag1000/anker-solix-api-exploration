# Business Rules — A17C1 Solarbank 2 Pro

> Extracted from APK UI controller and device controller assembly.
> These rules determine WHEN a SET command is allowed and WHAT values are valid.
> **This information is NOT available from mqtt_monitor or API documentation.**

## Pre-flight Check: isCurDeviceConnected

Called before **every** SET operation. All 4 conditions must pass:

```
1. device variable must be initialized (not null/sentinel)
   → Fail: "device变量还未初始化" (device variable not yet initialized)
2. Rx observable field_43.value must be TRUE
3. Rx observable field_47.value must be TRUE
4. Connected BLE MAC must match device MAC (getUnifiedMac comparison)
```

If ANY fails → command is **silently skipped**. Found at 5 call sites in home_logic.

## setDevicePowerLimit (command 0080)

### 4 Code Paths (depending on which parameters are provided)

| Path | Condition | TLV Tags Sent | Notes |
|------|-----------|--------------|-------|
| 1 | acPowerLimit != null | a2(feeder) + a4(0) + a6(acPower) + a8(switch) + aa(pvLimit) + ac(extra) | Full command |
| 2 | param2 != null, acPower == null | a2(feeder) + a4(0) + a6(acPower via different key) | AC power path |
| 3 | param2 == null, pvLimit != null | a8(switch) + aa(pvLimit) only | PV limit only |
| 4 | ALL null | a8(switch) + aa(pvLimit) only, BUT checks fc_enabled first | Default path |

### Guards (checked in order)

| # | Check | Consequence | What it means |
|---|-------|-------------|---------------|
| 1 | `device_online` (offset 0x4CF) == false | Skip entirely | Device not reachable |
| 2 | `feeder_power` (offset 0x297) == cached value | Skip (no change) | Value hasn't changed, don't resend |
| 3 | `fc_enabled` (offset 0x28B) == true AND no explicit params | Return null (skip) | Capability flag blocks generic power limit changes |
| 4 | `mode_type` (offset 0x28F) == 2 | Triggers 0W-state dialog | "已是0W溃网状态" (Already in 0W grid-collapse state) |

### After sending

| Check | Value | Action |
|-------|-------|--------|
| `charge_priority` == 4 | Sets is_charge_priority flag | Enters charge priority mode |
| `charge_priority` == 2 | Sets field_2C7 flag | Secondary charge priority |

## setTacticsTime (command 005e — Schedule)

### Constraints

- **Maximum 7 time slots** (determined from 7 anonymous closures + 14 buffer allocations)
- Each slot uses `DischargeTimeModel` with 4 fields: `startTime`, `endTime`, `power`, `chargingPercentage`
- Schedule is sent as single command 0x5E with 30 TLV tags (a2-bb) + timestamp (fd)

### Enable Condition

Schedule UI is enabled ONLY when:

```
NOT (is_charge_priority(0x2C3) AND secondary_charge_priority(0x2C7))
```

**Rule: If BOTH charge priority flags are true → scheduling is DISABLED.**

This is implemented in `checkDeviceEnableStatus` and controls the UI Rx observable.

## setBackPower (command 005e — Backup mode)

### TLV Structure
| Tag (key) | Value | Description |
|-----------|-------|-------------|
| a2 (324) | always `4` | Mode = backup (hardcoded) |
| a4 (326) | always `0` | Reserved |
| a6 (328) | 0 or 1 | Enabled boolean (from param boolean test) |
| aa (332) | 4-byte int | Start time (intToList4) |
| ac (334) | 4-byte int | End time (intToList4) |

## setSoc (command 0067 — Power Cutoff)

### Default Values (when parameter is null)

| Parameter | Default | Source |
|-----------|---------|--------|
| SOC value 1 (output cutoff) | **10%** | a17c1setting_logic:17304 |
| SOC value 2 (lowpower input) | **5%** | a17c1setting_logic:17318 |
| SOC value 3 (input cutoff) | **10%** | a17c1setting_logic:17332 |

### Also calls Cloud API
`/power_service/v1/app/compatible/set_power_cutoff` — server-side validation applies.

## setDeviceLightMode (command 0068 — LED)

**No pre-conditions.** Simplest SET command — sends 2 TLV tags (mode + brightness) directly.

## checkDeviceEnableStatus (called on every data refresh)

Three separate enable flags, each controlling different UI elements:

| Flag | Offset | Condition | Controls |
|------|--------|-----------|----------|
| **Power limit enable** | 0x4CF + 0x2CB | `device_online AND charge_priority_value == 4` | Power limit slider/buttons |
| **Schedule enable** | 0x2C3 + 0x2C7 + 0x28B | `NOT (is_charge_priority AND field_2C7)` | Schedule/tactics UI |
| **Online status** | 0x4CF | Direct boolean read | General device availability |

## Error Handling

```
After data refresh:
  Read error_code from offset 0x3DB
  Log: "检查主包错误码" (Check main package error code)
  If error AND device connected:
    Show error dialog to user with error code
```

## What This Means for HA Integration

1. **Always check device connectivity** before sending commands — 4-step check, not just "is online"
2. **Don't resend unchanged values** — the app caches and compares before sending
3. **Charge priority blocks scheduling** — if charge_priority mode is active, don't offer schedule controls
4. **7 schedule slots max** — don't try to send more
5. **SOC has safe defaults** (10/5/10) — use these if user doesn't specify
6. **0W state = just set home_load_preset to 0** — no special flag needed (device-tested)
7. **No OTA guard** — the app does NOT check firmware update status before SET commands
8. **4 different setDevicePowerLimit paths** — the parameters determine which TLV tags are sent

---

# Business Rules — A17C1 Cloud API Operations

> These complement the BLE rules above. The app uses BOTH API + BLE for most operations.

## Master Guard: isSettingsEnable

```
isSettingsEnable():
  1. device.isUpdating != 0  →  return FALSE (OTA in progress)
  2. device.isOnline == false →  return FALSE
  → ALL settings blocked during OTA or when offline
```

**Every** settings page checks this first.

## canEditEquipmentFeedNetwork (Grid Feed-In)

```
ALL 4 must be true:
  1. isSettingsEnable()
  2. grid_connected == true
  3. meter_present == true
  4. read_only == false
```

**Rule: Grid feed-in editing requires meter AND grid connection.**

## canEditSafetySoC (SOC Reserve)

```
ALL 3 must be true:
  1. isSettingsEnable()
  2. grid_connected == false (!)
  3. device NOT in station
```

**Rule: SOC editing only when NOT grid-connected and NOT in a station.** This is counter-intuitive.

## Dual API + Device Pattern

After a **Cloud API** call succeeds, the app often sends the **same command locally** via BLE/MQTT:

```
1. Cloud API: set_power_cutoff(device_sn, cutoff_data_id)
   → On success:
2. BLE/MQTT: setSoc(upper=10, lower=5, step=10)  ← defaults if null
3. EventBus: broadcast MessageEvent(id=2214, data=2)  ← notify other UI
```

**Rule: Cloud API is the primary channel. BLE/MQTT is the backup/confirmation. Both are sent.**

## getPowerLimitList — 22 Attributes Fetched

The app fetches these in a single `get_device_attrs` call:
`region_power_limit`, `legal_power_limit`, `ip_region`, `region_microinverter_limit`,
`switch_0w`, `enable_0w`, `power_limit_option_real`, `pv_power_limit_option`,
`pv_power_limit` + ~13 more.

**Rule: All power limit constraints come from the server in one batch. Don't hardcode ranges.**

## Mode Transitions

Modes are managed at **site level** (A1782 station), NOT by A17C1 directly:
- Uses `set_site_device_param` with appropriate `param_type`
- Mode_type is embedded in JSON payload
- **No client-side mode transition restrictions found** — enforcement is server-side

---

# Business Rules — A17X8 Smart Plug

> Extracted from a17x8_device_controller.dart + a17x8 UI logic assembly.

## Central Connection Guard (ALL commands)

Every SET command passes through `sendCommandWithParam`:
```
1. _getCurrentStatus() must == DeviceConnectionStatus.connected
2. Default timeout: 30 seconds for command response
→ If not connected: command silently dropped
```

## Relay Switch (007a)

- **No additional guards** beyond connection check
- **Debounce**: After sending, a delayed Future sets a cooldown flag (offset 0x49f)
- Prevents rapid toggle-toggle-toggle

## Schedule/Timing (007c)

### Maximum schedules
- Device attribute `timing_limit` queried via `getDeviceAttrsInfo`
- **Default: 24** if attribute is null (`mov x4, #0x18`)

### Delete = same command
- Delete uses `setTimingCmd` with action type for deletion
- **No separate delete opcode** — same 0x7c command

### Parameter validation
- `id`: defaults to 0 if null
- `switchState`: defaults to 0 if null
- `hours`: defaults to 0 if null
- `minutes`: defaults to 0 if null
- `weekdays`: only added to TLV if list is **non-empty** (checked before adding tag 0x14E)

### isEffective (enabled) — inverted logic!
```
if isEffective == true:  send 0  (enabled = 0 in protocol!)
if isEffective == false: send 1  (disabled = 1 in protocol!)
```
**Rule: Schedule enabled/disabled flag is INVERTED in the TLV protocol.**

### Response also carries relay state
```
"获取定时-----更新继电器开关状态" (get timer → update relay switch state)
```
**Rule: Timing query response includes current relay on/off. Schedule and switch state are coupled.**

## Countdown/Timer (007e)

### Duration encoding
- 3-byte int (intToList3) → max ~16,777,215 seconds (~194 days)
- Negative remainTime **clamped to 0** (sign bit check + set to zero)

### Cancel = send with switchState=0
- **No separate cancel opcode** — same 0x7e with switchState=0

### Connectivity fallback
```
if BLE disconnected AND WiFi online:
    show "deviceIsOffline" toast
if BLE disconnected AND WiFi offline:
    show "deviceOfflineAndBluetoothDisconnected" toast
→ Command NOT sent in either case
```

## Timer + Schedule Coexistence

**No mutual exclusion.** Timer and schedule can be active simultaneously.
They are independent UI pages with independent commands.

## What This Means for HA Integration

1. **Connection check before every command** — 30s timeout, silently drops if disconnected
2. **Max 24 schedules** (from server attribute, default 24)
3. ~~Schedule enabled flag is INVERTED~~ **CORRECTION: a4=1=enabled is NORMAL** (device-tested 2026-03-28)
4. **Timer cancel = same command with switchState=0** — no separate cancel
5. **Debounce relay toggle** — prevent rapid switching
6. **Timing responses carry relay state** — use them to refresh switch status
7. **Timer and schedule coexist** — no need to disable one for the other

---

# Error Code → Message Mapping

> These are the actual error descriptions from the APK. mqtt_monitor only shows
> the numeric code — these translations come from the app's string pool.

## A17C1 Solarbank 2 Pro — 12 Error Codes

| Code | Meaning | Impact |
|------|---------|--------|
| 1 | System failure | Wait or contact service |
| 2 | System failure | Power cycle (hold 3s) |
| 3 | **Off-grid overload** | Load exceeds spec |
| 4 | **Grid connection lost** | — |
| 5 | Power grid exception | Fluctuation/outage |
| 6 | **PV input overvoltage** | Each panel max 60V |
| 7 | Device overheating | — |
| 8 | **Meter communication lost** | **Exits self-consumption mode!** |
| 9 | Software version outdated | — |
| 10 | **Meter CT connection error** | System re-checks every **5 minutes** |
| 11 | Device sleep mode | Data temporarily unavailable |
| 12 | Low device temperature | — |

**Bug risk**: Error 8 exits self-consumption mode entirely. Not handling this leaves system in wrong mode.

## EV Charger A5190 — 23 Fault Codes

| Hex | Fault | Stops Charging? |
|-----|-------|----------------|
| 0x01 | CP voltage / connector issue | Yes |
| 0x02 | Overvoltage | Yes |
| 0x04 | Undervoltage | Yes |
| 0x06 | Abnormal current | Yes |
| 0x07 | Overheat | Yes |
| 0x0C | **Temp high — power REDUCED** | **No — reduces power only** |
| 0x12 | Ground fault | Yes |
| 0x13 | Leakage trip | Yes |
| 0x16 | **Lost signal with smart meter** | **No — continues at limited power** |
| 0x17 | **Lost signal with system** | **No — continues at limited power** |
| 0x18 | **Card reader fault** | **No — does NOT affect charging** |
| 0x19 | **Wiring error** | Yes — **DO NOT self-fix** |
| 0x1D | **Time sync needed** | Affects scheduling + statistics |
| 0x21 | **Internal fault** | **No — does NOT affect charging** |

**Bug risk**: Not all faults stop charging. 0x0C, 0x16, 0x17, 0x18, 0x21 are non-stopping.
Treating all faults as "stop" would incorrectly interrupt charging sessions.

## A17X8 Smart Plug — 2 Error Codes

| Code | Meaning |
|------|---------|
| 1 | Over-power protection — check if appliance overloaded |
| 2 | Device disconnected — reconnect via Shelly app |

---

# Timing Constants (from APK Duration pool)

| Duration | Used For |
|----------|---------|
| 300ms | Default debounce (AnkerDebounceThrottle) |
| 900ms | Safety SOC status update delay |
| 2000ms | MQTT message listener delay |
| 5000ms | API polling interval |
| **30s** | **BLE command timeout** + background disconnect |
| **60s** | MQTT listener cycle |
| **5 min** | Meter CT re-check interval (error code 10) |
| **30 min** | **Background disconnect threshold** — BLE considered dead after 30min backgrounded |

**Bug risk**: 30-minute background threshold means BLE connections break if app is backgrounded.

---

# Business Rules — A5190 EV Charger V1

> These rules are critical for anyone building EV charger integration.

## 6A Fallback Rule

In **5 scenarios**, the charger falls back to **6A minimum current**:
1. Load balancing loses connection to energy monitor
2. Solar charging loses communication with energy devices
3. Modbus TCP communication lost
4. Electric meter disconnected (standalone or system)
5. Main device AND meter both disconnected

**This is a safety feature, not a bug.**

## 80% Main Breaker Rule

Load balancing keeps total consumption below **80% of main breaker limit**.
Not 100% — there's a 20% safety margin hardcoded.

## Phase Auto-Switching

```
If any phase current drops below 6A during three-phase solar charging:
  → Switch to single-phase to maximize solar use
  → Grid power only used if minimum 6A cannot be reached
```

## Solar Charging Modes

| Mode | Behavior |
|------|----------|
| Pure Solar | Pauses when solar < 6A. **Brief grid micro-usage** to assess solar availability |
| Solar + Grid | Solar-only when surplus meets minimum. Grid supplements when insufficient |
| Boost | User can tap Boost during any session → switches to fast/full power |

**Hidden detail**: "Brief grid micro-usage" prevents frequent relay switching. This is NOT a bug.

## Schedule Conflicts

**"Don't schedule both car and charger."** If both car's built-in schedule and charger schedule are set, behavior is undefined. The app warns but does not prevent this.

**Charger schedule works offline** — no cloud/app connection needed once set.

## What This Means for HA Integration

1. **Handle 6A fallback** — when communication lost, charger drops to 6A. Show this state.
2. **80% breaker rule** — don't set limits above 80% of breaker capacity
3. **Non-stopping faults exist** — codes 0x0C, 0x16-0x18, 0x21 don't stop charging
4. **Solar micro-grid-usage is normal** — small grid draws during solar mode are expected
5. **Phase switching is automatic** — don't try to control it manually
6. **Offline schedule capability** — schedules persist without cloud

---

# Business Rules — A5101 HES / X1

> Extracted from a5101 UI logic and system policy controller assembly.

## 4 Universal Guard Conditions (block ALL setting changes)

Every A5101 SET command checks these 4 conditions. If ANY is true → command blocked:

| # | Condition | Chinese Log | Meaning |
|---|-----------|------------|---------|
| 1 | EMS policy disabled | "禁用ems策略" | Device's energy management strategy is off |
| 2 | Off-grid state | "离网状态" | Device is currently off-grid |
| 3 | BLE not connected | "蓝牙未连接" | Near-field BLE required but not present |
| 4 | Manual off-grid | "近场手动离网状态" | User manually switched to off-grid locally |

**Rule: ALL HES settings require EMS enabled + grid connected + BLE connected + not manual off-grid.**

## Peak Shaving — Maximum Power by Product

| Product | Max Peak Shaving | Notes |
|---------|-----------------|-------|
| A5101 (X1 single-phase US) | **60,000W** (60kW) | |
| A5102 (X1 single-phase EU) | **60,000W** (60kW) | |
| A5103 (X1 three-phase) | **180,000W** (180kW) | 3× single-phase |
| A5341 (Backup Controller) | **38,400W** (38.4kW) | |
| Unknown/default | **0W** | Feature disabled |

**Rule: Peak shaving limits are hardcoded per product number. Don't allow values above these.**

## Battery Reserve

- **Default**: 20%
- **Maximum**: 100%
- Set via `sendDeviceCommandOfConservepercent()`

## Disaster Preparedness / Storm Guard

Two modes: **Manual** and **Auto**

Parameters:
- `disaster_preparedness_enable`: on/off
- `disaster_preparedness_soc`: SOC reserve threshold
- `disaster_preparedness_start` / `_end`: time window
- `auto_disaster_preparedness_enable`: auto mode toggle

**Auto-disaster data synced via BLE in packets** — enable/disable sent only after ALL packets complete.

## Off-Grid Switching

Parameters: `off_grid_enable`, `off_grid_sensitivity`

Seamless off-grid switch available (zero-transfer-time). Same 4 guard conditions apply.

## Heat Pump SG-Ready

- Separate weekday and weekend time plans
- Has enable/disable toggle
- Timer settings managed separately
- Transmitted via `heatPumpSetting` in device command payload

## HES Work Modes

| Value | Mode | Description |
|-------|------|-------------|
| 0 | `standBy` | Standby |
| 2 | `gridOff` | Grid disconnected |
| 6 | `working` | Normal operation |

---

# Business Rules — A1790 F3800 / Expansion Batteries

## Expansion Battery Guards

Before any operation on expansion batteries, the app checks:
- `isSubBatteryEqualing()` — **6+ call sites**. If battery equalization is in progress → block operations
- `isSubBatteryOverError()` — shows error dialog + uploads error report
- `isBatteryError()` — general battery error check

**Rule: Never send commands to expansion batteries during equalization.**

## Generator Auto-Start (A7320 / AX170)

| Parameter | Description |
|-----------|-------------|
| `oilEngineStartCondition` | Flag that triggers auto-start |
| `oilEngineStartSoc` | SOC threshold for startup |
| `standbyOilMachineNormalStartSoc` | Normal hours start SOC |
| `standbyOilMachineQuietStartSoc` | Quiet hours start SOC (typically higher) |
| `oilEngineStartTime` | Scheduled start time |
| `isStartCloseSoc` | Validates start/close SOC consistency |

**Rule: Generator has DUAL SOC thresholds — normal vs quiet hours. Quiet hours threshold is typically higher to avoid unnecessary starts at night.**

---

# Cross-Cutting Rules (all devices)

## WiFi: 2.4GHz Only

**ALL Anker Solix devices** only support 2.4GHz WiFi. The app shows `selectWifi5GTips` warning across every device type (A5101, A5140, A5143, A5150, A1781, and all device bind flows).

**Rule: Never attempt 5GHz WiFi connection. It will fail silently.**

## OTA Blocks Device Control

- `isOtaInProgress()` checked before rendering home page UI (A1790, A1782)
- **ALL user operations blocked during OTA** — not just settings, but the entire home page
- **OTA requires MinSoc** — battery must be above threshold before BLE firmware update
- **Rollback available** — component-level rollback supported with dedicated UI

## Battery Temperature Protection (4 zones)

| Zone | Effect |
|------|--------|
| `outHighTemperatureProtection` | **Discharge blocked** |
| `outLowTemperatureProtection` | **Discharge blocked** |
| `inHighTemperatureProtection` | **Charging blocked** |
| `inLowTemperatureProtection` | **Charging blocked** |

**Rule: Temperature protection is per-direction. High temp blocks the current direction (charge OR discharge), not both.**

## Slider Debounce

`sendDeviceCommandWithDebounce()` wraps all slider-based SET operations. Prevents rapid-fire commands when user drags a slider. The debounce fires only the LAST value after the user stops moving.

## Input Validation

`RangeTextInputFormatter`: Rejects values < 1 or > max (loaded dynamically from server). Invalid input reverts to previous value — no error shown.

---

# HES State Machine (11 device states)

> From `mode_state_definition.dart`. States 6-9 and 20 are hardware-initiated overrides.

| Value | State | Type | Description |
|-------|-------|------|-------------|
| 0 | `NA` | — | Unknown |
| 1 | `selfUse` | User-set | Self-consumption |
| 2 | `timeOfUse` | User-set | Time-of-use pricing |
| 3 | `manualBackupPower` | User-set | Manual backup |
| 4 | `severeWeatherMode` | User-set | Storm Guard / auto disaster |
| 5 | `onlyBackup` | User-set | Backup only |
| 6 | `atsEmsOffGridMode` | **Hardware override** | ATS forced off-grid |
| 7 | `socCalibration` | **Hardware override** | SOC calibration in progress |
| 8 | `gridOutage` | **Hardware override** | Physical grid outage detected |
| 9 | `lowSolarInput` | **Hardware override** | Low solar input status |
| 20 | `forcedRecharge` | **Hardware override** | Forced battery recharge |

**Rule: States 6-9 and 20 CANNOT be set by user/API — they are triggered by hardware conditions. An integration must show these as read-only states.**

## Transaction Lock System

Commands are guarded by a per-device, per-property transaction lock:
- Keyed by `deviceSn`
- Tracks: `transactionId`, `properties`, `timestamp`, `timeOutTimer`
- **Default timeout: 12 seconds** (when no device-specific config)
- Different device models can have different timeouts
- If property count matches locked count → lock not needed (skip)
- Older firmware: `"sdk 能力协商不支持事务锁"` — transaction lock not supported, commands pass unguarded

**Rule: Don't send overlapping commands to the same device within 12s.**

---

# Site Creation Rules

## 10 Device Categories for Sites

| # | Category | Description |
|---|----------|-------------|
| 1 | `solar_list` | Solar panels / inverters |
| 2 | `grid_list` | Grid-connected devices |
| 3 | `smartplug_list` | Smart plugs |
| 4 | `pps_list` | Portable Power Stations |
| 5 | `solarbank_list` | SolarBank devices |
| 6 | `powerpanel_list` | Power Panels |
| 7 | `combiner_box_list` | Combiner Boxes |
| 8 | `solarbank_pps_list` | Combined SolarBank+PPS |
| 9 | `charging_pile_list` | EV Charging Piles |
| 10 | `home_backup_system_list` | Home Backup Systems |

**18 Product Numbers** in the PN enum, each mapped to a `powerSiteType` integer.

## Currency Decimal Places (by market)

- **Most markets**: 5 decimal places (€, $, £, etc.)
- **2 specific markets**: 4 decimal places (likely JPY, KRW — currencies without cents)

---

# Dynamic Pricing / TOU Rules

## Three Price Types

| Type | Field | Description |
|------|-------|-------------|
| `"fixed"` | `price` | Fixed rate per kWh |
| `"use_time"` | `use_time` → PeakValleyParamData | Time-of-use with peak/valley/off-peak |
| `"dynamic"` | `dynamic_price` → DynamicPriceParamData | Live pricing (Nordpool, Tibber, etc.) |

## Provider Support (by Product Number)

| Provider | Supported PNs | Description |
|----------|--------------|-------------|
| Flatpeak | 5 product numbers | Generic TOU |
| Tibber | 5 product numbers | Nordic dynamic pricing |
| AI EMS | **only 2 product numbers** | AI-optimized energy management |

**Rule: AI EMS is only available on 2 specific products. Don't offer it on unsupported devices.**

## Seasonal TOU

TOU supports `PeakValleySeasonModel` — **seasonal pricing** with different rates per season.
Default `mode_type` = 5.

## Charge/Discharge Windows

`chargeTimePeriod` and `dischargeTimePeriod` are **independently configurable** lists with `start`/`end` time strings. They don't need to be complementary.

## Dynamic Price Save Payload

When saving dynamic price config, the app sends:
- `price: 0.0` (zero — actual prices fetched live from provider)
- `site_price_unit: ""` (empty — provider determines unit)
- `site_co2: 0.0` (zero)
- `price_type: "dynamic"`
- `dynamic_price: {provider config object}`

---

# Energy Calculations

## CO2 Savings — Server-Computed

- `site_co2` field sent with price config
- Savings calculation happens **server-side**
- App only displays pre-computed values from `savingsUnit`, `saveCarbonsUnit`, `powerGenerationsUnit`
- Formula shown to users via `co2SavingsComputationRule` localization key

**Rule: Don't try to calculate CO2 locally — use the server-provided values.**

## Chart Granularity

4 periods: `day`, `week`, `month`, `year` with `YYYY-MM-DD` date format.

---

# Parallel System Rules (Solarbank Multi-System)

## Power Options Scale with Parallel

| Config | Max Load Options |
|--------|-----------------|
| Single device | 350, 600, 800, 1000W |
| Multi-device parallel | 1200, 2400, 3600, 4800W |

Fields: `enable_parallel`, `parallel_home_load`, `parallel_display`, `parallel_type`

## PV Surplus Handling

- `pvSurplusPower` tracked per site
- When PV > load + battery full → surplus goes to grid export (if enabled) or curtailed by PV limit

## A17C5 Firmware Feature Gate

```
if firmware_component_version >= 2:
    isSupportPvLimit = true   → PV power limit setting available
else:
    isSupportPvLimit = false  → PV limit UI hidden
```
Debug: "固件是否支持pv设置光伏上限 isSupportPvLimit:"

---

# Auth / Account Rules

## Token Auto-Refresh

HTTP 401 → `_handler401()` → automatic re-authentication via `_reLogInIoTSDK()`.
**Transparent** — happens during API calls without user interaction.

## BLE Password Lockout

After too many wrong BLE passwords (firmware-enforced limit):
- Status 15: `passwordWrongAuthenticationFailed` — "鉴权失败，密码错误"
- Status 16: `passwordRetryCountExceededAuthenticationFailed` — "密码次数超过，已锁定" (LOCKED)

**Rule: BLE lockout is device-side. No unlock from app — device must be power-cycled.**

## Account Freeze

`freeze_status` field + `/passport/freeze_account` endpoint exist.
`accountExpiredReminderOK` string suggests expired account warnings.

## IP Ban

**No client-side ban detection.** The 10x ban rule (thomluther) is server-side only.

---

# BLE Constraints

| Constraint | Value | Source |
|-----------|-------|--------|
| Connection timeout | **30 seconds** | simple_ble_connector.dart |
| Background disconnect | **30 minutes** | Duration pool |
| Default MTU | **200 bytes** | AssembleCmdUtil |
| MTU overhead | **10 bytes** | AssembleCmdUtil |
| Max concurrent | **OS-limited** (~6-7 Android) | flutter_reactive_ble |
| OTA reconnect | **Suppressed** during firmware update | ota_reconnect_suppress_helper |

## MTU Negotiation

MTU is explicitly negotiated and logged: `"Transmission parameters: MTU="`
Packet fragmentation controlled by `isMTU` parameter.

---

# EV Charger Firmware Compatibility

Two explicit firmware version checks:
- `"X1固件版本过低"` — X1 firmware version too low (for EV+X1 integration)
- `"充电桩固件版本过低"` — Charger firmware version too low

**Rule: EV Charger features may be unavailable if X1 HES or charger firmware is too old.**

## Forced Firmware Updates

`force_upgrade` and `is_forced` fields in FirmwareUpdateModel.
**Mandatory updates cannot be deferred.**

---

# Complete Safety Summary

## Conditions That Block ALL Commands

| Condition | Applies To | Check |
|-----------|-----------|-------|
| OTA in progress | All devices | `isOtaInProgress()` / `isSettingsEnable()` |
| Device offline | All devices | `isCurDeviceConnected()` |
| BLE disconnected | BLE devices | `_getCurrentStatus() != connected` |
| Battery equalizing | A1790 expansion | `isSubBatteryEqualing()` |
| EMS disabled | A5101 HES | "禁用ems策略" guard |
| Off-grid state | A5101 HES | "离网状态" guard |
| Manual off-grid | A5101 HES | "近场手动离网状态" guard |

## Conditions That Silently Limit Functionality

| Condition | Effect |
|-----------|--------|
| Charge priority active | Schedule editing disabled |
| Not grid-connected | SOC editing disabled (A17C1) |
| No meter present | Grid feed-in editing disabled |
| Firmware too old | PV limit, EV features unavailable |
| BLE password locked | Device unreachable until power-cycle |
| Transaction lock active | Commands within 12s dropped |
| Value unchanged | setDevicePowerLimit skipped |

## Non-Obvious Protocol Behaviors

| Behavior | Detail |
|----------|--------|
| ~~Schedule enabled = 0 in TLV~~ | **DISPROVED**: device test shows a4=1=enabled (normal) |
| 5 EV faults don't stop charging | 0x0C, 0x16, 0x17, 0x18, 0x21 |
| Timer cancel = SET with state=0 | No separate cancel command |
| Timing response carries relay state | Switch and schedule coupled |
| Power above grid limit = silent clamp | No error, just clamped |
| Error 8 = exits self-consumption | Mode changes without user action |
| 0W mode = c7 preset set to 0 | No special flag, just preset=0W |
