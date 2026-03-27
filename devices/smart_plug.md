# Smart Plug — A17X8

> **Priority**: P1 (Core)
> [ha-anker-solix #150](https://github.com/thomluther/ha-anker-solix/issues/150) (61 comments) |
> [anker-solix-api #124](https://github.com/thomluther/anker-solix-api/issues/124) |
> Switch implemented in v3.5.0, timer/schedule still open

## Product Info

- **A17X8** — SOLIX Smart Plug (2500W, energy monitoring)
- Consumer accessory for Solarbank ecosystem
- Part of "blend mode" for smart plug-driven solar optimization

## MQTT Commands (device-tested on A17X8 FW 0.0.2.7)

### 007a — Plug Switch
| Field | Name | Values |
|-------|------|--------|
| a2 | `switch` | 0=OFF, 1=ON |

Implemented in upstream v3.5.0.

### 007c — Plug Schedule
| Field | Name | Values |
|-------|------|--------|
| a2 | `action` | 0=delete, 1=create, 2=modify |
| a3 | `slot` | Schedule slot number (1-x) |
| a4 | `enabled` | 0=disabled, 1=enabled |
| a5 | `time` | min:hour (2 bytes) |
| a6 | `switch` | 0=OFF at time, 1=ON at time |
| a7 | `weekdays` | Day numbers: 1=Mon..7=Sun, **variable length** |

Important: a7 is **day numbers**, not a bitmask. 0x07 = Sunday (day 7), not 3 bits.

### 007e — Plug Timer / Delayed Toggle
| Field | Name | Values |
|-------|------|--------|
| a2 | `toggle_to_switch` | 0=cancel, 1=start, **2=pause, 3=resume** |
| a3 | `toggle_to_delay_time` | 3 bytes (seconds:minutes:hours) |
| a4 | `toggle_back_switch` | 0=no toggle back, 1=toggle back after delay |
| a5 | `toggle_back_delay_time` | 3 bytes (seconds:minutes:hours) |

Pause (a2=2) and resume (a2=3) were discovered in our mqtt_monitor session
and contributed via [PR #283](https://github.com/thomluther/anker-solix-api/pull/283) (merged).

### 007f — Timer Status Request
Query command to get current timer state. Sent by app to poll active timers.

## Related Files in This Repo

- [VALIDATION_MODEL.md](../VALIDATION_MODEL.md#smart-plug-switch) — Verified MQTT command details
- [ENDPOINT_FIELDS.md](../ENDPOINT_FIELDS.md) — setRemainPluginStatus
- [ENUMS.md](../ENUMS.md) — A17X8 product code
- [DART_PYTHON_MAPPING.md](../DART_PYTHON_MAPPING.md) — Field name mappings
- [endpoints/power_service_site.md](../endpoints/power_service_site.md#power_servicev1siteset_device_feature) — set_device_feature endpoint

## API Endpoints

| Endpoint | Function | Notes |
|----------|----------|-------|
| `/power_service/v1/site/set_device_feature` | setRemainPluginStatus | `site_id, smart_plug` list |

The `mini_power` endpoints are for Prime Chargers (A2345/A2687), **not** for Smart Plugs
despite the naming similarity.

## Smart Plug in Scene Info

From upstream community testing, the scene_info response includes per-plug data:
```json
{"device_pn": "A17X8", "device_sn": "...", "device_name": "Smart Plug",
 "current_power": "0", "tag": "Living Room",
 "priority": 0, "auto_switch": false, "running_time": null}
```

## What's still needed

Per thomluther (Issue #150, latest comments):
1. **Timer field validation** — confirm seconds:minutes:hours byte order
2. **Schedule state in 0405** — how saved schedules appear in status messages
3. **System export ZIP** with MQTT data while toggling plug / running timer
4. Schedule create → modify → delete full cycle documentation
