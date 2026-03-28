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
- `fc`: 22-byte indexed array with 5 sub-fields:
  - [0] power_limit_ref
  - [2] ui_flag (==2 → enabled)
  - [14] is_enable_0w (==2 → zero-export enabled, debug: "-isEnable0w-")
  - [18] feeder0w_config (used in setDevicePowerLimit)

All tag names prefixed with `apk_` to distinguish from upstream-confirmed names.
Value 2 = enabled in this protocol (NOT 1).

### Verification needed
To confirm a tag name, change the corresponding setting in the Anker app
while mqtt_monitor is running, and check if the tag value changes as expected.
Best candidates for quick verification:
- Toggle 0W mode → fc[14] should change from 0 to 2
- Change power limit → fc[0] and ba should change
- Enable schedule → af should change from 0 to 1
- Start heating → bb should show power value > 0
