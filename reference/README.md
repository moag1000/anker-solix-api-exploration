> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# Reference

| Page | Tag | What it owns |
|---|---|---|
| [business_rules.md](business_rules.md) | string-only | Business rules re-verified on 3.24.3 incl. the polling facts for library authors (timers, heartbeats, retry, 401/461/463) |
| [enums.md](enums.md) | string-only | Enums referenced by the BLE/MQTT pages (consumed from docs/audit/ENUMS.md) |
| [iot_kit_channels.md](iot_kit_channels.md) | asm-traced | The 90 `akiot.*` IoT-Kit identifiers (3.18.0: 68; 22 new in 3.24.3), transport (`ak_iot_kit_flutter` MethodChannel + 3 EventChannels), call sites |
| [validation_model.md](validation_model.md) | asm-traced | Client-side validation before sending (ranges, pairs, checks) + pointer table to the mqtt/ owners |

The 3.18.0 root pages are superseded by the pages above; their old content was in the 3.18.0 root pages `ENUMS.md`, `BUSINESS_RULES.md` and `VALIDATION_MODEL.md` (deleted; their numbers were under review, audit tables in [../docs/audit/](../docs/audit/)).

Not here: per-endpoint payloads ([../api/README.md](../api/README.md)); owner map in [../docs/STRUCTURE.md](../docs/STRUCTURE.md).
