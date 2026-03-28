# Command Flows — Step-by-Step Traces

> Complete traces from UI button press to wire bytes.
> Each flow shows: what the user does → what the app validates →
> what bytes are sent → what response is expected.

---

## Flow 1: Solarbank 2 Schedule (param_type 6)

### User Action
Create custom schedule: Mon-Fri 00:00-08:00 at 200W, 08:00-24:00 at 600W

### Call Chain
```
Energy Plan UI → A17C1AnkerDevice::setTacticsTime()
  → A17C1DeviceController::setTacticsTime() [14020 bytes, largest function!]
  AND
  → ElectricityUsageHelper → HTTP set_site_device_param
```

### Dual Path: BLE + API (both sent)

**API Path:**
```json
POST /power_service/v1/site/set_site_device_param
{
  "site_id": "<site_id>",
  "cmd": 246,
  "param_type": "6",
  "param_data": "{\"mode_type\":3,\"custom_rate_plan\":[{\"index\":0,\"week\":[0,1,2,3,4],\"ranges\":[{\"start_time\":\"00:00\",\"end_time\":\"08:00\",\"power\":200},{\"start_time\":\"08:00\",\"end_time\":\"24:00\",\"power\":600}]}]}"
}
```

Note: `cmd` = 246 (0xF6) for cloud, NOT 17 as in thomluther's API. Both values work —
thomluther uses 17, APK uses 246.

**BLE Path:**
```
Command 0x005E with up to 30 TLV tags (a2-bb) + timestamp (fd)
MTU = 400 (larger than default 200 for schedule data)
CRC32 checksum appended as tag 0x1FA (506)
```

### DischargeTimeModel (per time slot)

```
Bytes [0-1]: startTime (minutes from midnight, LE) — e.g., 0 = 00:00
Bytes [2-3]: endTime (minutes from midnight, LE) — e.g., 480 = 08:00
Bytes [4-5]: power (watts, LE) — e.g., 200
Bytes [6-7]: chargingPercentage (SOC target %)
Bytes [8-9]: weekday_mask (optional, 0 if absent)
```

### Constraints
- **Maximum 14 time slots** (from 14 buffer allocations)
- **Maximum 7 weekday groups** (from 7 anonymous closures)
- CRC32 checksum required on BLE path
- Schedule enable condition: `NOT (is_charge_priority AND secondary_flag)`

---

## Flow 2: EV Charger Start Charging

### User Action
Tap "Start Charging" / "Start Now" / "Boost" button

### ChargeControlType Values
| Action | controlType value | UI Label |
|--------|------------------|----------|
| Start (scheduled) | **1** | "evChargeStart" |
| Stop / Cancel | **2** | "evChargeStop" |
| Start Now (immediate) | **3** | "evChargeStartNow" |
| Boost | **4** | "evChargeBoost" |

### Call Chain
```
A5190 Home Page → onTapControl(ChargeControlType)
  → AKIotEVChargeCommand::setControlType(controlType)
    → AKIotBasicCommand::writeProperty("action_control_charging", {"controlType": <int>})
      → IotManagerExtension → akiot.device.write_property (MQTT)
```

### The Payload (simple!)
```json
{
  "action": "action_control_charging",
  "params": {
    "controlType": 3
  }
}
```

### encoding_type 2 — What We Found

**Critical finding**: `encoding_type` does NOT exist in the Flutter layer.
The APK sends a standard `action_control_charging` via `akiot.device.write_property`.

The `encoding_type: 2` differentiation (from thomluther's mqttcmdmap.py) happens
**below the Flutter layer** — either in:
- The AK IoT Kit native SDK (Android/iOS, not Dart)
- The cloud MQTT broker
- The device firmware

**The Flutter app does NOT generate a random seed, does NOT handle special encoding.**
It simply sends `{"controlType": 1/2/3/4}` and the infrastructure handles the rest.

### Error Handling
- On failure: shows "evChargeStartFailedHint" toast
- On boost success: shows `BoostTipsToastUtil::showSuccessToast()` + delayed callback
- Duration tracked: start_time to end_time measured for telemetry

### What This Means for Issue #322
The actual MQTT wire format with encoding_type 2 must be reverse-engineered
from mqtt_monitor captures on a real EV Charger — the APK cannot reveal it.
The controlType values (1-4) are confirmed and directly usable.

---

## Flow 3: Smart Plug Countdown Timer (007e)

### User Action
Set 30-minute timer to switch plug OFF when done

### Call Chain
```
A17X8 Countdown Page → changeStartOrPause()
  → _isCurDeviceConnected() check (4 steps)
  → State toggle: idle(0) → running(6), running(6) → paused(4)
  → _setCountdownCmd()
    → A17X8DeviceController::setCountdownCmd()
      → sendCommandWithParam([0, 0x7E], valueMap)
```

### Countdown States
| Value | State |
|-------|-------|
| 0 | Idle / no countdown |
| 4 | Paused |
| 6 | Running |

### TLV Command (0x007E)

For "30 min, switch OFF":
- Total time: 1800 seconds = `0x000708`
- switchState: OFF = 0
- type: Start = 6

| Tag (thomluther) | TLV Key | Bytes | Value | Encoding |
|---------|---------|-------|-------|----------|
| a2 | 0x0144 | 1 | `06` | type: 6=start, 4=pause, 0=delete |
| a3 | 0x0146 | 3 | `08 07 00` | totalTime: 1800s (LE) |
| a4 | 0x0148 | 1 | `00` | switchState: 0=OFF, 1=ON |
| a5 | 0x014A | 3 | `08 07 00` | remainTime: 1800s (LE, same as total on start) |

### intToList3 Encoding (little-endian)
```
1800 decimal = 0x000708
→ [0x08, 0x07, 0x00]  (low byte first)
```

### Delete Timer
Same command 0x007E with type = **0** (no separate delete opcode):
```
a2: 00  (type=delete)
a3: 08 07 00  (original total time)
a4: 00  (switch state)
a5: 00 00 00  (remain=0)
```

### Pause Timer
Same command with type = **4**:
```
a2: 04  (type=pause)
a3: 08 07 00  (original total time)
a4: 00  (switch state)
a5: DC 05 00  (remain=1500s = 25 min remaining, LE)
```

### Resume Timer
Same command with type = **6** and updated remainTime.

### Timer Status in 0405 (tag 0xAD)

Minimum 8 bytes:
```
Bytes [0-5]: totalTime via listToInt (e.g., 1800)
Byte  [6]:   switchState (0=OFF, 1=ON target)
Byte  [8]:   elapsed time marker
Computed:    remaining = max(0, totalTime - elapsed)
```

Stored at device offset **0x477** as CountDownInfo object.
EventBus message **1356** fired on update.

### Debounce
After relay toggle (007a), a delayed Future prevents re-toggling.
No debounce on timer commands themselves.

---

## Flow 4: Smart Plug Schedule (007c)

### User Action
Create schedule: "Turn ON at 08:00, Turn OFF at 22:00, repeat Mon+Wed+Fri"

### Call Chain
```
A17X8 Timing List Page → _setTimingCmd()
  → _isCurDeviceConnected() check
  → A17X8DeviceController::setTimingCmd(timingInfo)
    → sendCommandWithParam([0, 0x7C], valueMap)
```

### TimingInfo Fields
| Field | Source | Description |
|-------|--------|-------------|
| actionType | UI action | 0=delete, 1=create, 2=update |
| id | slot index | Schedule entry number |
| switchState | target | 0=OFF, 1=ON (but see inversion below!) |
| hours | time picker | Hour (0-23) |
| minutes | time picker | Minute (0-59) |
| isEffective | toggle | **INVERTED: true→sends 0, false→sends 1** |
| repeatCycleList | weekday picker | Day numbers: [1,3,5] = Mon,Wed,Fri |

### TLV Command (0x007C)

For "Create: ON at 08:00, Mon+Wed+Fri":

| Tag (thomluther) | TLV Key | Bytes | Value | Encoding |
|---------|---------|-------|-------|----------|
| a2 | 0x0144 | 1 | `01` | actionType: 1=create |
| a3 | 0x0146 | 1 | `00` | id: 0 (first slot) |
| a4 | 0x0148 | 1 | `01` | switchState: 1=ON |
| a5 | 0x014A | 1 | `00` | minutes: 0 |
| a6 | 0x014C | 1 | `08` | hours: 8 |
| a7 | 0x014E | var | `01 03 05` | weekdays: Mon(1), Wed(3), Fri(5) |

### isEffective Inversion!

```
if isEffective == true:   send 0  (enabled in protocol = 0!)
if isEffective == false:  send 1  (disabled in protocol = 1!)
```

**This is the #1 bug risk for schedule implementation.**

### Weekday Encoding
- Variable length list of day numbers
- 1=Monday, 2=Tuesday, ... 7=Sunday
- **NOT a bitmask** — sequential bytes, one per day
- Only added to TLV if list is non-empty

### Max Schedules
- Default: **24** (from `timing_limit` device attribute)
- Configurable per device via `getDeviceAttrsInfo("timing_limit")`

### Delete Schedule
Same command 0x007C with actionType = **0**:
```
a2: 00  (delete)
a3: 03  (id of schedule to delete)
```

### Response Coupling
Timing query response also carries **relay switch state**:
```
"获取定时-----更新继电器开关状态" (get timer → update relay switch state)
```
**Schedule and switch state are coupled in the protocol.**

---

## Flow 5: Solarbank Power Limit Change

### User Action
Change power output from 400W to 800W

### Call Chain (4 distinct paths!)
```
A17C1 Home Logic → guards check → A17C1AnkerDevice::setDevicePowerLimit()
  → A17C1DeviceController::setDevicePowerLimit()
    → sendCommandWithParam([0, 0x80], valueMap)
```

### Guards (checked in order, any fail → skip)

| # | Check | Field | Consequence |
|---|-------|-------|-------------|
| 1 | Device online? | offset 0x4CF | Skip entirely |
| 2 | Value changed? | offset 0x297 vs cached | Skip if unchanged |
| 3 | fc_enabled? | offset 0x28B | Return null if true + no params |
| 4 | 0W grid-collapse? | offset 0x28F == 2 | Show dialog |

### 4 Code Paths

| Path | Condition | Tags Sent |
|------|-----------|-----------|
| 1 | acPowerLimit provided | a2+a4+a6+a8+aa+ac (full) |
| 2 | param2 provided, no acPower | a2+a4+a6 (AC path) |
| 3 | pvPowerLimit provided | a8+aa only (PV path) |
| 4 | ALL null (default) | a8+aa only (checks fc_enabled first) |

### TLV Command (0x0080)

For "set output to 800W":

| Tag (thomluther) | TLV Key | Bytes | Value | Encoding |
|---------|---------|-------|-------|----------|
| a2 | 0x0144 | 2 | feeder0w value | intToList2 (LE) |
| a4 | 0x0146 | 2 | `00 00` (always 0) | intToList2 |
| a6 | 0x0148 | 2 | acPowerLimit | intToList2 |
| a8 | 0x014A | 2 | switch0w value | intToList2 |
| aa | 0x014C | 2 | pvPowerLimit | intToList2 |
| ac | 0x014E | 2 | additional | intToList2 |

### After Sending
- If `charge_priority == 4` → sets is_charge_priority flag
- If `charge_priority == 2` → sets secondary charge priority flag
- Both flags affect schedule enable status

---

## Flow Summary: What Thomluther Needs

| Flow | Command | Key Insight |
|------|---------|-------------|
| Schedule | API param_type=6 + BLE 005e | **Both paths sent**. cmd=246 in APK (not 17). CRC32 on BLE. |
| EV Start | action_control_charging | **encoding_type 2 is below Flutter layer** — 4 simple controlType values |
| Plug Timer | BLE 007e | States: 0=idle, 4=paused, 6=running. Delete=same cmd with type=0 |
| Plug Schedule | BLE 007c | **isEffective is INVERTED** (true→0, false→1). Max 24 slots. |
| Power Limit | BLE 0080 | **4 distinct code paths** depending on which params provided |
