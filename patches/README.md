# Patches for Local Testing

These patches apply APK-extracted tag names to thomluther's mqtt_monitor
for local verification. They are NOT upstream PRs.

## Usage

```bash
cd /path/to/anker-solix-api
git apply /path/to/anker-solix-api-exploration/patches/a17c1_apk_tags.patch
```

To revert:
```bash
git checkout api/mqttmap.py
```

## Available Patches

### a17c1_apk_tags.patch
Adds 12 APK-extracted tags to `_A17C1_0405` in `mqttmap.py`:
- `a4`: status_code (value=2 in test dump)
- `ae`: ac_output_power_signed (wire=int, APK stores as bool)
- `af`: schedule_enabled (bool, cross-device match with A17X8)
- `b8`: ac_input_power (value=1 in test dump — bool or 1W?)
- `b9`: self_test_enabled (bool, defaults false)
- `ba`: percentage_value (×0.01, value=0.29 in test dump)
- `bb`: heating_power (upstream comment confirms)
- `e9`: battery_capacity (defaults 0)
- `ea`: unknown flag (value=1 in test dump)
- `fc`: 22-byte indexed array — likely CAPABILITY flags (static), NOT live settings
  - [0], [2], [14], [18] mapped as capability flags
  - **Device test (2026-03-28): fc did NOT change when 0W mode was toggled**
  - The 0W setting goes via Cloud API, not MQTT 0405 status

All tag names prefixed with `apk_` to distinguish from upstream-confirmed names.

### Device test results (2026-03-28)
- fc bytes: **STATIC** — did not change on 0W toggle. Likely capability array.
- All other apk_ tags showed plausible, stable values consistent with device state.

### Methodology lesson learned
APK UI debug strings (like "-isEnable0w-") reference the app's internal state,
which combines MQTT status AND Cloud API data at the same offset. Static analysis
cannot distinguish which data source populates a field.

### Verification still needed
To confirm remaining tag names, change settings while mqtt_monitor runs:
- Toggle 0W mode → check fb (grid_export_disabled), NOT fc[14]
- Change power limit → fc[0] and ba should change
- Enable schedule → af should change from 0 to 1
- Start heating → bb should show power value > 0
