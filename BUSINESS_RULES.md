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
3. **Schedule enabled flag is INVERTED** (enabled=0 in TLV, not 1!)
4. **Timer cancel = same command with switchState=0** — no separate cancel
5. **Debounce relay toggle** — prevent rapid switching
6. **Timing responses carry relay state** — use them to refresh switch status
7. **Timer and schedule coexist** — no need to disable one for the other
