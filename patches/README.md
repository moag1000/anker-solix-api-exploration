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
- `fc`: 22-byte indexed byte array with 5 sub-fields:
  - [0] power_limit_ref
  - [2] ui_flag (==2 → enabled)
  - [14] **is_enable_0w** (==2 → zero-export enabled, debug: "-isEnable0w-")
  - [18] feeder0w_config (used in setDevicePowerLimit)

**Code trace (2026-03-28)**: offset 0x287 (fc) and 0x28b (is_enable_0w) are written
EXCLUSIVELY by the MQTT 0405 parser. API stores enable_0w in a separate model.
This IS an MQTT-sourced field.

All tag names prefixed with `apk_` to distinguish from upstream-confirmed names.
Value 2 = enabled in this protocol (NOT 1).

### Device test results (2026-03-28)
- fc bytes did not change during test — likely timing issue (0405 status is
  periodic, ~3 min interval). Test was too short.
- All other apk_ tags showed plausible, stable values consistent with device state.
- 0W toggle sends MQTT command 0080 (feeder0w+switch0w) AND API call.

### Verification still needed
**Improved test procedure** (wait for status update cycle):
1. Start mqtt_monitor with `--realtime-trigger` for continuous updates
2. Note fc[14] value
3. Toggle 0W mode in Anker App
4. Wait **at least 3-5 minutes** for next 0405 status cycle
5. Check if fc[14] changed from 0↔2
- Change power limit → fc[0] and ba should change
- Enable schedule → af should change from 0 to 1
- Start heating → bb should show power value > 0
