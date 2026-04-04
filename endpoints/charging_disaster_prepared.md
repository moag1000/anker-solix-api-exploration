# Charging Disaster Prepared

> Controls backup/disaster modes for Home Power Panel (A17B1) and HES (A5101).
> Separate from `charging_energy_service/` and `charging_hes_svc/`.
>
> **Source**: Blutter decompilation — code-traced through 5 files (see bottom)
>
> **Relevant Issues**: [ha-anker-solix #480](https://github.com/thomluther/ha-anker-solix/issues/480)

## How It Actually Works

There are **two abstraction layers** that both control backup/disaster mode.
They use **different field names** for the same concepts:

| Layer | Used by | Field style | Entry point |
|-------|---------|-------------|-------------|
| **Cloud API** | `system_policy_logic.dart` (DisasterMixin) | `auto_disaster_switch`, `manual_disaster_switch`, `manual_disaster_detail` | Direct HTTP POST |
| **IoT Kit** | `disaster_preparedness_command.dart` | `backupMode`, `autoBackupSwitch`, `manualBackupSwitch`, `backupStartTime`, `backupEndTime` | `akiot.device.invoke_action` → native bridge |

Both hit the same server endpoint. The Cloud API layer is what thomluther should implement.

### Two Independent Modes

| Mode | Trigger | API field | UI page |
|------|---------|-----------|---------|
| **Auto Disaster** | Server-side weather alerts (location-based) | `auto_disaster_switch` | `AutoDisasterSetting` (WebView with weather map) |
| **Manual Disaster** | User-defined time window | `manual_disaster_switch` + `manual_disaster_detail` | `ManualDisasterSetting` → `A17B1ManualBackupPowerPage` |

Both modes can be active simultaneously. Each has its own switch.

---

## Initialization Flow (what happens on page load)

```
A17B1SystemPolicyLogic.onInit()
  → A17B1AutoDisasterMixin.initDisaster()
    → resolve siteId (if missing: getDeviceInfos() first)
    → DisasterMixin.initDisaster()
      → refreshAutoDisaster()   // triggers 3 parallel fetches:
        → GET /charging_disaster_prepared/get_site_device_disaster     → DisasterSetting
        → GET /charging_disaster_prepared/get_support_func             → SupportFunc
        → GET /charging_disaster_prepared/get_site_device_disaster_status → DisasterStatus
      → initLocation()          // GPS for weather alerts
        → GET /charging_common_svc/location/get
```

All 3 disaster fetches use `RefreshManager` with `FetchedData<T>` wrappers.
Common request params: `{"type": <device_type_int>, "identifier_id": "<site_id>"}`.

---

## Endpoints

### `GET /charging_disaster_prepared/get_support_func`

**Dart**: `_fetchSupportFunc()` in DisasterMixin

Checks if the device supports disaster/backup features.

**Request**:
```json
{"type": "<device_type>", "identifier_id": "<site_id>"}
```

**Response → SupportFunc** (class 9033, size 0x10):
```
support_auto_disaster    bool     Auto disaster feature available
support_country_code     list?    Supported countries → List<SupportCountryCode>
```

**SupportCountryCode**:
```
code                     string   Country code (e.g. "US")
google_code              string   Google Maps country code
```

If `support_auto_disaster` is false, the entire disaster UI is hidden.

---

### `GET /charging_disaster_prepared/get_site_device_disaster`

**Dart**: `_fetchDisasterSetting()` in DisasterMixin

Returns current disaster configuration.

**Request**:
```json
{"type": "<device_type>", "identifier_id": "<site_id>"}
```

**Response → DisasterSetting** (class 10860, size 0x30, extends ChangeNotifier):
```
auto_disaster_switch     bool     Auto disaster mode enabled
manual_disaster_switch   bool     Manual disaster mode enabled
disaster_details         list     Active disaster events → List<DisasterEvent>
```

**DisasterEvent**:
```
uuid                     string   Event unique ID
event                    string   Event name/description (e.g. hurricane name)
start_time               int      Unix timestamp — start
end_time                 int      Unix timestamp — end
charging_time            int?     Charging duration (nullable)
```

---

### `GET /charging_disaster_prepared/get_site_device_disaster_status`

**Dart**: `_fetchAutoDisasterStatus()` in DisasterMixin

Returns runtime status of active disaster mode.

**Request**:
```json
{"type": "<device_type>", "identifier_id": "<site_id>"}
```

**Response → DisasterStatus** (class 9035, size 0x1c):
```
auto_disaster_status     int      Auto disaster status code (0 = inactive)
manual_disaster_status   int      Manual disaster status code (0 = inactive)
current_disaster_detail  object?  Active disaster → DisasterPrepareDetail (nullable)
```

**DisasterPrepareDetail**:
```
uuid                     string   Event unique ID
event                    string   Event name
event_key                string?  Event key (nullable)
start_time               int      Unix timestamp
end_time                 int      Unix timestamp
charging_time            int?     Charging time (nullable)
disaster_type            int      Type code (4 = manual)
```

---

### `POST /charging_disaster_prepared/set_site_device_disaster` [SET]

**Dart**: `setDisasterSwitch()` and `setManualDisasterSwitch()` in DisasterMixin

Central control endpoint. Two different request shapes depending on mode:

#### Enable/Disable Auto Disaster

```json
{
  "type": "<device_type>",
  "identifier_id": "<site_id>",
  "auto_disaster_switch": true
}
```

#### Enable Manual Disaster (with time window)

```json
{
  "type": "<device_type>",
  "identifier_id": "<site_id>",
  "manual_disaster_switch": true,
  "manual_disaster_detail": {
    "disaster_type": 4,
    "start_time": 1712160000,
    "end_time": 1712246400
  }
}
```

`disaster_type = 4` is hardcoded for manual mode.

#### Disable Manual Disaster

```json
{
  "type": "<device_type>",
  "identifier_id": "<site_id>",
  "manual_disaster_switch": false,
  "manual_disaster_detail": null
}
```

**State update**: Before sending, the code creates a new `DisasterSetting` object
preserving the OTHER switch's value. E.g. toggling manual preserves the current
auto_disaster_switch value, and vice versa.

---

### `POST /charging_disaster_prepared/quit_disaster_prepare` [SET]

**Dart**: `quitCurrentDisaster()` in DisasterMixin

Exits the currently active disaster preparation. Called when user taps "Quit" on
the active disaster card.

**Request**:
```json
{
  "type": "<device_type>",
  "identifier_id": "<site_id>",
  "is_ble": 4,
  "disaster_type": "<from current_disaster_detail.disaster_type>"
}
```

`is_ble = 4` is hardcoded. `disaster_type` comes from the active `DisasterStatus.current_disaster_detail`.

After success, calls `refreshAutoDisaster()` to reload all 3 state objects.

---

### `POST /charging_disaster_prepared/clear` [SET]

**Dart**: `AKIotDisasterPreparednessCommand.clearBackup()`

Alternative clear path via IoT Kit layer. Sends `backupMode = 4` (CLEAR).

This goes through `akiot.device.invoke_action` (native bridge), NOT direct HTTP.
Likely produces the same server-side effect as setting both switches to false.

---

## IoT Kit Layer (alternative path)

`AKIotDisasterPreparednessCommand` in `ak_iot_kit/business/disaster_preparedness/command/`

This wraps the same operation in the IoT Kit action format, dispatched via
`KitExtension.handle()` → `AkIotKitFlutter::handle()` (native SDK bridge).

### setBackup()

```json
{
  "deviceSn": "<device_sn>",
  "bleMac": "<ble_mac>",
  "id": "action_set_backup_mode",
  "param": {
    "backupMode": 1,
    "manualBackupSwitch": true,
    "backupStartTime": "<time>",
    "backupEndTime": "<time>",
    "quitCurrentBackup": false
  }
}
```

Key differences from Cloud API layer:
- Uses `backupMode` (0=AUTO, 1=MANUAL) instead of separate switch fields
- Uses `autoBackupSwitch` or `manualBackupSwitch` (selected by PreparednessMode enum)
- Sends `deviceSn` + `bleMac` instead of `type` + `identifier_id`
- Config: `[0x1, 0x4, 0x4, 0x3, "openTransaction", 0x3, null]`

### clearBackup()

```json
{
  "deviceSn": "<device_sn>",
  "bleMac": "<ble_mac>",
  "id": "action_set_backup_mode",
  "param": {
    "backupMode": 4
  }
}
```

Config: `[0x1, 0x3, 0x3, 0x3, null]`

### DisasterPreparednessInfo (IoT Kit response model)

Source: `ak_iot_kit/business/disaster_preparedness/model/disaster_preparedness_info.dart` (753 lines)

This model is used by the IoT Kit layer, NOT by the direct Cloud API calls.
Different field names from `DisasterSetting`:

```
supportBackupDisaster    int?    Device supports backup (0/1)
backupMode               int?    Current mode (0=AUTO, 1=MANUAL, 4=DISABLED)
manualBackupSwitch       int?    Manual backup enabled (0/1)
autoBackupSwitch         int?    Auto backup enabled (0/1)
backupStartTime          int?    Start time
backupEndTime            int?    End time
manualBackupStartTime    int?    Manual-specific start time
manualBackupEndTime      int?    Manual-specific end time
remainingTime            int?    Seconds remaining in active backup
chargeDischargeStatus    int?    Current charge/discharge state
subPackageInfo           list    Battery units → List<SubPackageInfo>
```

`subPackageInfo` items are checked with two predicates:
- `any()` with heating predicate
- `any()` with `== 4` predicate

---

## Weather Categories (Auto Disaster)

Source: `flutter_ems/ems_list/constants/disaster_constants.dart`

9 categories, 38+ warning types:

| Category | Warning count | Examples |
|----------|--------------|---------|
| Winter Weather | 6 | winterWeatherWarning, winterStormWarning, windChillWarning |
| Freeze | 2 | windChillWarning |
| Snow Storm | 4 | blizzardWarning, snowSquallWarning |
| Fire Weather | 2 | redFlagWarning |
| Wind | 2 | highWindWarning |
| Thunderstorm | 2 | severeThunderstormWarning |
| Tornado | 2 | tornadoWarning |
| Flood | 10 | coastalFlood, flashFlood, riverFlood, lakeshoreFlood |
| Tropical/Hurricane | 8 | tropicalStormWatch/Warning, hurricaneWatch/Warning |

Location set via `/charging_common_svc/location/set` (Google Maps place picker).
Weather detail page: `/h5/charging_disaster_prepared/disaster_detail/ankerWeather.html?lang=`

---

## Manual Backup Power (BLE + HTTP hybrid)

Separate from the disaster system. Accessed from `ManualDisasterSetting` which
navigates to `/a17b1ManualBackupPowerPage`.

`A17B1ManualBackupPowerLogic`:
- Receives `DisasterMixin` via navigation arguments
- Time picker: half-hour slots (00:00, 00:30, ... 23:30)
- Date range: 90 days ago to 365 days ahead
- 2000ms debounce on date changes
- BLE battery reserve: `sendA17B1Command("scp", <percent>)` — sets cycle percent
- HTTP persist: `syncSiteConfig()` after BLE write

`BackPowerLogic` (shared feature):
- BLE opcodes: 0x233 (response handler), 0x45a (dismiss)
- Date formats: `"MM/dd/yyyy"`, `"HH:mm"`, `"MM/dd/yyyy HH:mm"`
- Writes to device fields at offsets 0x4af and 0x4b3

---

## Implementation for thomluther (what to build)

### Minimum for Issue #480 (manual backup control)

1. **`GET /charging_disaster_prepared/get_support_func`**
   - Check `support_auto_disaster` → show/hide backup UI
   - Request: `{"type": <int>, "identifier_id": "<site_id>"}`

2. **`GET /charging_disaster_prepared/get_site_device_disaster`**
   - Read current `manual_disaster_switch` and `disaster_details`
   - Response: `DisasterSetting` with 3 fields

3. **`POST /charging_disaster_prepared/set_site_device_disaster`**
   - Enable manual: `{"type": ..., "identifier_id": ..., "manual_disaster_switch": true, "manual_disaster_detail": {"disaster_type": 4, "start_time": <unix>, "end_time": <unix>}}`
   - Disable manual: `{"type": ..., "identifier_id": ..., "manual_disaster_switch": false}`

4. **`POST /charging_disaster_prepared/quit_disaster_prepare`**
   - Exit active: `{"type": ..., "identifier_id": ..., "is_ble": 4, "disaster_type": <from status>}`

### Optional (auto disaster / status monitoring)

5. `GET /charging_disaster_prepared/get_site_device_disaster_status` → DisasterStatus
6. `GET /charging_common_svc/location/get` and `/set` for weather alert location

### What NOT to implement

- The IoT Kit layer (`akiot.device.invoke_action`) — this is a native SDK bridge,
  not a standard HTTP endpoint. The Cloud API path does the same thing.
- `DisasterPreparednessInfo` model — that's the IoT Kit model, not the HTTP response.
  Use `DisasterSetting` + `DisasterStatus` instead.

---

## Dart Source Files

| File | Lines | Purpose |
|------|-------|---------|
| `base_service/ak_iot_kit/business/basic/model/device_disaster_model.dart` | 1136 | **DisasterSetting**, DisasterStatus, DisasterEvent, DisasterPrepareDetail, SupportCountryCode models |
| `base_service/ak_iot_kit/ext/kit_ext.dart` | 1090 | KitExtension.handle() — IoT SDK dispatch |
| `ak_iot_kit/business/disaster_preparedness/command/disaster_preparedness_command.dart` | 451 | setBackup() / clearBackup() via IoT Kit |
| `ak_iot_kit/business/disaster_preparedness/model/disaster_preparedness_info.dart` | 753 | DisasterPreparednessInfo (IoT Kit model) |
| `ui/page/station/mixin/auto_disaster.dart` | 6296 | **Core mixin**: initDisaster, refreshAutoDisaster, all API calls |
| `ui/page/device/a17b1/system_policy/system_policy_logic.dart` | 5789 | A17B1-specific: setDisasterSwitch, setManualDisasterSwitch, quitCurrentDisaster |
| `ui/page/device/a17b1/device_setting/manual_backup_power/a71b1_manual_backup_power_logic.dart` | 5366 | Manual backup power UI logic (BLE path) |
| `ui/page/station/view/auto_disaster/auto_disaster_setting.dart` | 3101 | Auto disaster UI (WebView weather map) |
| `ui/page/station/view/auto_disaster/manual_disaster_setting.dart` | 2047 | Manual disaster UI (time pickers) |
| `ui/page/station/view/auto_disaster/manual_disaster_card.dart` | 2680 | Active manual disaster card (quit button) |
| `flutter_ems/ems_list/constants/disaster_constants.dart` | 674 | 9 weather categories, 38+ warning types |
| `charging/feature/backup_power/back_power_logic.dart` | 3957 | BLE backup power (opcodes 0x233, 0x45a) |
