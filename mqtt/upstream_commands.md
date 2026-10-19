> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: upstream-confirmed · Owner page: this page

# Upstream command index (mqttcmdmap.py)

One table that maps every command constant of upstream `api/mqttcmdmap.py` to the products it is bound to in `api/mqttmap.py` and to the PN pages of this repository. The payload of each command is not copied here: upstream is the owner of the value tables, the PN pages own the app evidence. The envelope, topics and frame layout are owned by [envelope.md](envelope.md).

Evidence rows are written `audit row N` and refer to [../docs/audit/BLE_COMMAND_MAP.md](../docs/audit/BLE_COMMAND_MAP.md). The audit marked rows 583-636 NOT-FROM-ASM (the old doc copied them from upstream); the header tag of this page is therefore `upstream-confirmed`.

## Contents

1. [Commands](#commands): [constant index](#upstream-command-constants-mqttcmdmappy)

## Commands

### Upstream command constants (mqttcmdmap.py)

#### Purpose
Maps each command constant of upstream `mqttcmdmap.py` to the products it is bound to and to the pages of this repository.

#### Upstream name
All names are upstream's: constants `CMD_*` in `mqttcmdmap.py` (line numbers in the table) and their bindings in `SOLIXMQTTMAP` of `mqttmap.py`. Every row is upstream-confirmed; the app evidence for a command (opcode, tags, widths) is owned by the PN pages and is not repeated here.

#### Command code
No command code on this page: the opcodes are the keys of the bindings in `mqttmap.py` (hex strings, never halved); the app builders for them are documented on the PN pages. The audit rows 583-636 are the old doc's per-command tables and were marked NOT-FROM-ASM (upstream constants, no asm source); the notes in the last column are the audit's cross-checks against asm.

#### Direction
app→device for the command constants; the status messages are `mqttmap.py` message maps, not listed here. Tag: upstream-confirmed.

#### Topic pattern
[envelope.md](envelope.md#topics): `cmd/anker_power/<pn>/<sn>/req`.

#### Payload fields
Index only, no payload copies. The bindings column counts every occurrence of the constant in `SOLIXMQTTMAP` (including command groups); "pages" lists the PN pages of this repository for the products the constant is bound to (a page existing does not mean the page documents a builder for that opcode). Constants marked "none (not in the old doc)" were added upstream after the old doc was written or were not in its tables; `CMD_HEADER`, `CMD_COMMON` and `CMD_COMMON_V2` are building blocks, not commands.

| command constant | definition line (`mqttcmdmap.py`) | audit row | bound in `mqttmap.py` (first three) | pages for the bound products | app cross-check and conflicts (audit note) |
|---|---|---|---|---|---|
| `CMD_HEADER` | upstream-confirmed (line 209) | audit row 584 | not bound in `SOLIXMQTTMAP` | not bound, no page | The APK writes `A1 01 22` (or `A1 01 21`) at the start of every command, so the "22" of pattern_22 is a real 0x22 value (audit row 584). |
| `CMD_COMMON` | upstream-confirmed (line 216) | none (not in the old doc) | not bound in `SOLIXMQTTMAP` | not bound, no page | - |
| `CMD_COMMON_V2` | upstream-confirmed (line 219) | none (not in the old doc) | A1763 `0101` line 4286, A1763 `0102` line 4334, A1763 `0103` line 4374 (10 bindings, 4 products) | no page for the bound products (outside 3.6a/3.6b) | - |
| `CMD_STATUS_REQUEST` | upstream-confirmed (line 222) | audit row 636 | A17C0 `0040` line 4921, A17X8 `0040` line 5372, A2345 `0200` line 5447 (5 bindings, 5 products) | [a17c0.md](a17c0.md), [a17x8.md](a17x8.md), [a2345.md](a2345.md), [a91b2.md](a91b2.md) | - |
| `CMD_REALTIME_TRIGGER` | upstream-confirmed (line 227) | audit row 636 | A1722 `0057` line 4129, A1723 `0057` line 4154, A1725 `0057` line 4167 (37 bindings, 37 products) | [a172x.md](a172x.md), [a1780.md](a1780.md), [a1790.md](a1790.md), [a17b1.md](a17b1.md), [a17c0.md](a17c0.md), [a17c1.md](a17c1.md), [a17c2.md](a17c2.md), [a17c5.md](a17c5.md), [a17x7.md](a17x7.md), [a17x8.md](a17x8.md), [a2345.md](a2345.md), [a5101.md](a5101.md), [a91b2.md](a91b2.md) | APK 0x57 builder confirms a2 (1 byte) and a3 (4 bytes), not the 60 to 600 range; pool list `[0, 0x40]` exists (audit rows 636, 230). |
| `CMD_TIMER_REQUEST` | upstream-confirmed (line 245) | audit row 636 | A17X8 `007f` line 5377 (1 binding, 1 product) | [a17x8.md](a17x8.md) | - |
| `CMD_TEMP_UNIT` | upstream-confirmed (line 250) | audit row 636 | A1725 `0050` line 4165, A1726 `0050` line 4188, A1727 `0050` line 4201 (16 bindings, 16 products) | [a172x.md](a172x.md), [a1780.md](a1780.md), [a1790.md](a1790.md), [a17c0.md](a17c0.md), [a17c1.md](a17c1.md), [a17c2.md](a17c2.md), [a17c5.md](a17c5.md) | - |
| `CMD_TEMP_UNIT_V2` | upstream-confirmed (line 261) | none (not in the old doc) | AS200 `0103` line 5786 (1 binding, 1 product) | no page for the bound products (outside 3.6a/3.6b) | - |
| `CMD_DEVICE_MAX_LOAD` | upstream-confirmed (line 272) | audit row 636 | not bound in `SOLIXMQTTMAP` | not bound, no page | - |
| `CMD_DEVICE_TIMEOUT_MIN` | upstream-confirmed (line 282) | audit row 636 | A1725 `0045` line 4162, A1727 `0045` line 4198, A1729 `0045` line 4234 (8 bindings, 8 products) | [a172x.md](a172x.md), [a1780.md](a1780.md), [a1790.md](a1790.md) | - |
| `CMD_AC_CHARGE_SWITCH` | upstream-confirmed (line 293) | audit row 583 | not bound in `SOLIXMQTTMAP` | not bound, no page | - |
| `CMD_AC_CHARGE_LIMIT` | upstream-confirmed (line 304) | none (not in the old doc) | A1722 `0044` line 4112, A1723 `0044` line 4137, A1761 `0044` line 4246 (9 bindings, 8 products) | [a172x.md](a172x.md), [a1780.md](a1780.md), [a1790.md](a1790.md) | - |
| `CMD_AC_OUTPUT_SWITCH` | upstream-confirmed (line 314) | audit row 586 | A1722 `004a` line 4119, A1723 `004a` line 4144, A1761 `004a` line 4257 (9 bindings, 9 products) | [a172x.md](a172x.md), [a1780.md](a1780.md), [a1790.md](a1790.md), [a17x8.md](a17x8.md) | - |
| `CMD_AC_FAST_CHARGE_SWITCH` | upstream-confirmed (line 325) | audit row 585 | A1761 `005e` line 4265 (1 binding, 1 product) | no page for the bound products (outside 3.6a/3.6b) | - |
| `CMD_AC_OUTPUT_MODE` | upstream-confirmed (line 336) | audit row 587 | A1761 `0077` line 4267, A1790 `0077` line 4696, A1790P `0077` line 4735 (3 bindings, 3 products) | [a1790.md](a1790.md) | - |
| `CMD_AC_OUTPUT_TIMEOUT_SEC` | upstream-confirmed (line 352) | audit row 588 | A1781 `0042` line 4643 (1 binding, 1 product) | [a1780.md](a1780.md) | - |
| `CMD_DC_OUTPUT_SWITCH` | upstream-confirmed (line 368) | audit row 589 | A1722 `004b` line 4120, A1723 `004b` line 4145, A1726 `004b` line 4180 (10 bindings, 10 products) | [a172x.md](a172x.md), [a1780.md](a1780.md), [a1790.md](a1790.md) | - |
| `CMD_DC_12V_OUTPUT_MODE` | upstream-confirmed (line 379) | audit row 590 | A1761 `0076` line 4266, A1790 `0076` line 4695, A1790P `0076` line 4734 (3 bindings, 3 products) | [a1790.md](a1790.md) | - |
| `CMD_DC_OUTPUT_TIMEOUT_SEC` | upstream-confirmed (line 395) | audit row 591 | A1726 `0043` line 4173, A1728 `0043` line 4209, A1781 `0043` line 4644 (3 bindings, 3 products) | [a172x.md](a172x.md), [a1780.md](a1780.md) | - |
| `CMD_ENERGY_SAVING_SWITCH` | upstream-confirmed (line 411) | none (not in the old doc) | A1781 `004e` line 4660 (1 binding, 1 product) | [a1780.md](a1780.md) | - |
| `CMD_LIGHT_SWITCH` | upstream-confirmed (line 422) | audit row 592 | not bound in `SOLIXMQTTMAP` | not bound, no page | - |
| `CMD_LIGHT_MODE` | upstream-confirmed (line 433) | audit row 593 | A1722 `004f` line 4121, A1723 `004f` line 4146, A1726 `004f` line 4181 (10 bindings, 10 products) | [a172x.md](a172x.md), [a1780.md](a1780.md), [a1790.md](a1790.md) | Cross-check: blinking = 4 matches the A1780 `cmp x2,#4` blink test (unboxed, A1780 positional-parser rows); 0-3 equal ScreenBrightType. |
| `CMD_DISPLAY_SWITCH` | upstream-confirmed (line 444) | audit row 594 | A1722 `0052` line 4128, A1723 `0052` line 4153, A1725 `0052` line 4166 (13 bindings, 13 products) | [a172x.md](a172x.md), [a1780.md](a1780.md), [a1790.md](a1790.md) | - |
| `CMD_DISPLAY_MODE` | upstream-confirmed (line 455) | audit row 595 | A1725 `004c` line 4164, A1727 `004c` line 4200, A1729 `004c` line 4236 (9 bindings, 9 products) | [a172x.md](a172x.md), [a1780.md](a1780.md), [a1790.md](a1790.md) | Cross-check: off=0, low=1, medium=2, high=3 equal the ScreenBrightType pool enum. |
| `CMD_DISPLAY_TIMEOUT_SEC` | upstream-confirmed (line 466) | audit row 596 | A1725 `0046` line 4163, A1727 `0046` line 4199, A1729 `0046` line 4235 (9 bindings, 9 products) | [a172x.md](a172x.md), [a1780.md](a1780.md), [a1790.md](a1790.md) | - |
| `CMD_PORT_MEMORY_SWITCH` | upstream-confirmed (line 477) | audit row 597 | A1790 `0079` line 4697, A1790P `0079` line 4736 (2 bindings, 2 products) | [a1790.md](a1790.md) | - |
| `CMD_USB_PORT_SWITCH` | upstream-confirmed (line 488) | audit row 598 | A2345 `0207` line 5457 (1 binding, 1 product) | [a2345.md](a2345.md) | - |
| `CMD_AC_PORT_SWITCH` | upstream-confirmed (line 509) | none (not in the old doc) | A91B2 `0207` line 5538 (1 binding, 1 product) | [a91b2.md](a91b2.md) | - |
| `CMD_SOC_LIMITS_V2` | upstream-confirmed (line 527) | audit row 599 | A1763 `0103` line 4419, A1783 `0103` line 4571, A1782 `0103` line 4907 (3 bindings, 3 products) | no page for the bound products (outside 3.6a/3.6b) | The `fd` timestamp claim conflicts with the APK (tag 0xFD = CRC32 in the A17C1 builders; TLV rows). |
| `CMD_DEVICE_SWITCH` | upstream-confirmed (line 546) | none (not in the old doc) | AS200 `0103` line 5742 (1 binding, 1 product) | no page for the bound products (outside 3.6a/3.6b) | - |
| `CMD_SB_STATUS_CHECK` | upstream-confirmed (line 557) | audit row 600 | A17C0 `0056` line 4923 (1 binding, 1 product) | [a17c0.md](a17c0.md) | - |
| `CMD_SB_POWER_CUTOFF` | upstream-confirmed (line 603) | audit row 601 | A17C0 `0067` line 4925, A17C1 `0067` line 5007, A17C2 `0067` line 5059 (4 bindings, 4 products) | [a17c0.md](a17c0.md), [a17c1.md](a17c1.md), [a17c2.md](a17c2.md) | Cross-check: the APK SOC call falls back to 10 / 5 / 10 (FLOWS audit); the maps {5:4, 10:5} and {5:5, 10:10} are upstream only. |
| `CMD_SB_MIN_SOC` | upstream-confirmed (line 628) | audit row 602 | A17C5 `0067` line 5168, AE100 `0067` line 5415 (2 bindings, 2 products) | [a17c5.md](a17c5.md) | - |
| `CMD_SB_INVERTER_TYPE` | upstream-confirmed (line 639) | audit row 603 | A17C0 `0068` line 4926 (1 binding, 1 product) | [a17c0.md](a17c0.md) | - |
| `CMD_SB_AC_SOCKET_SWITCH` | upstream-confirmed (line 681) | audit row 604 | A17C5 `0073` line 5178 (1 binding, 1 product) | [a17c5.md](a17c5.md) | - |
| `CMD_SB_3RD_PARTY_PV_SWITCH` | upstream-confirmed (line 692) | audit row 605 | A17C5 `0085` line 5205, AE100 `0085` line 5418 (2 bindings, 2 products) | [a17c5.md](a17c5.md) | - |
| `CMD_SB_EV_CHARGER_SWITCH` | upstream-confirmed (line 703) | audit row 606 | AE100 `0084` line 5417 (1 binding, 1 product) | no page for the bound products (outside 3.6a/3.6b) | - |
| `CMD_SB_MAX_LOAD` | upstream-confirmed (line 715) | audit rows 607, 608 | A17C1 `005a` line 4993, A17C1 `0080` line 5023, A17C2 `005a` line 5046 (9 bindings, 5 products) | [a17c1.md](a17c1.md), [a17c2.md](a17c2.md), [a17c5.md](a17c5.md) | No APK counterpart: there is no 0x5a builder in either version (audit row 222). |
| `CMD_SB_DISABLE_GRID_EXPORT_SWITCH` | upstream-confirmed (line 734) | audit row 609 | A17C1 `0080` line 5031, A17C2 `0080` line 5084, A17C3 `0080` line 5138 (5 bindings, 5 products) | [a17c1.md](a17c1.md), [a17c2.md](a17c2.md), [a17c5.md](a17c5.md) | - |
| `CMD_SB_PV_LIMIT` | upstream-confirmed (line 760) | audit row 610 | A17C5 `0080` line 5202 (1 binding, 1 product) | [a17c5.md](a17c5.md) | - |
| `CMD_SB_AC_INPUT_LIMIT` | upstream-confirmed (line 771) | audit row 611 | A17C2 `0080` line 5085, A17C5 `0080` line 5203 (2 bindings, 2 products) | [a17c2.md](a17c2.md), [a17c5.md](a17c5.md) | - |
| `CMD_SB_LIGHT_SWITCH` | upstream-confirmed (line 784) | audit row 612 | A17C1 `0068` line 5015, A17C2 `0068` line 5067, A17C3 `0068` line 5122 (4 bindings, 4 products) | [a17c1.md](a17c1.md), [a17c2.md](a17c2.md), [a17c5.md](a17c5.md) | - |
| `CMD_SB_LIGHT_MODE` | upstream-confirmed (line 802) | audit row 613 | A17C1 `0068` line 5014, A17C2 `0068` line 5066, A17C3 `0068` line 5121 (4 bindings, 4 products) | [a17c1.md](a17c1.md), [a17c2.md](a17c2.md), [a17c5.md](a17c5.md) | - |
| `CMD_SB_DEVICE_TIMEOUT` | upstream-confirmed (line 820) | audit row 614 | A17C5 `009a` line 5206 (1 binding, 1 product) | [a17c5.md](a17c5.md) | Cross-check: no /30 divider exists in the APK setter or in getSleepTimeInt (audit row 222). |
| `CMD_SB_USAGE_MODE` | upstream-confirmed (line 838) | audit row 615 | A17C5 `005e` line 5167 (1 binding, 1 product) | [a17c5.md](a17c5.md) | Cross-check: modes 1-5, 7, 8 equal the AiModeEnum wire values (ENUMS audit). "48 x 1-byte slots: discharge=1, charge=4, default=6" was not asm-checked. |
| `CMD_PLUG_SCHEDULE` | upstream-confirmed (line 947) | audit row 616 | A17X8 `007c` line 5375 (1 binding, 1 product) | [a17x8.md](a17x8.md) | Arithmetic: 0-5947 = 23 * 256 + 59 (hour * 256 + minute). |
| `CMD_PLUG_DELAYED_TOGGLE` | upstream-confirmed (line 993) | audit row 617 | A17X8 `007e` line 5376 (1 binding, 1 product) | [a17x8.md](a17x8.md) | Arithmetic: 0-1522491 = 23 * 65536 + 59 * 256 + 59 (sec:min:hour). The APK writes the delay with `intToList3`, i.e. up to 16,777,215. |
| `CMD_EV_CHARGER_MODE` | upstream-confirmed (line 1030) | audit row 618 | A5191 `0105` line 5884 (1 binding, 1 product) | no page for the bound products (outside 3.6a/3.6b) | Cross-check: 1-4 equal the ChargeControlType wire values (start 1, cancel 2, startNow 3, boost 4). |
| `CMD_DEVICE_POWER_MODE` | upstream-confirmed (line 1047) | audit row 619 | A5191 `0108` line 5898 (1 binding, 1 product) | no page for the bound products (outside 3.6a/3.6b) | - |
| `CMD_PLUG_LOCK_SWITCH` | upstream-confirmed (line 1059) | audit row 620 | A5191 `0100` line 5868 (1 binding, 1 product) | no page for the bound products (outside 3.6a/3.6b) | Cross-check: off=1, on=2 is confirmed by the APK lock-status value (carChargerLockStatus real 1 / 2). |
| `CMD_EV_AUTO_START_SWITCH` | upstream-confirmed (line 1070) | audit row 621 | A5191 `0100` line 5869 (1 binding, 1 product) | no page for the bound products (outside 3.6a/3.6b) | - |
| `CMD_EV_MAX_CHARGE_CURRENT` | upstream-confirmed (line 1081) | audit row 622 | A5191 `0100` line 5870 (1 binding, 1 product) | no page for the bound products (outside 3.6a/3.6b) | - |
| `CMD_EV_LIGHT_BRIGHTNESS` | upstream-confirmed (line 1097) | audit row 623 | A5191 `0100` line 5873 (1 binding, 1 product) | no page for the bound products (outside 3.6a/3.6b) | - |
| `CMD_EV_LIGHT_OFF_SCHEDULE` | upstream-confirmed (line 1110) | audit row 624 | A5191 `0100` line 5877 (1 binding, 1 product) | no page for the bound products (outside 3.6a/3.6b) | Arithmetic: 0-5947 = 23 * 256 + 59. |
| `CMD_EV_AUTO_CHARGE_RESTART_SWITCH` | upstream-confirmed (line 1136) | audit row 625 | A5191 `0100` line 5871 (1 binding, 1 product) | no page for the bound products (outside 3.6a/3.6b) | - |
| `CMD_EV_CHARGE_RANDOM_DELAY_SWITCH` | upstream-confirmed (line 1147) | audit row 626 | A5191 `0100` line 5872 (1 binding, 1 product) | no page for the bound products (outside 3.6a/3.6b) | - |
| `CMD_SWIPE_UP_MODE` | upstream-confirmed (line 1158) | audit row 627 | A5191 `0100` line 5874 (1 binding, 1 product) | no page for the bound products (outside 3.6a/3.6b) | Cross-check: 0-3 equal EvChargerGestureFunction 0-3 (pool). |
| `CMD_SWIPE_DOWN_MODE` | upstream-confirmed (line 1176) | audit row 628 | A5191 `0100` line 5875 (1 binding, 1 product) | no page for the bound products (outside 3.6a/3.6b) | Cross-check: 0-3 equal EvChargerGestureFunction 0-3 (pool). |
| `CMD_SMART_TOUCH_MODE` | upstream-confirmed (line 1194) | audit row 629 | A5191 `0100` line 5876 (1 binding, 1 product) | no page for the bound products (outside 3.6a/3.6b) | - |
| `CMD_MODBUS_SWITCH` | upstream-confirmed (line 1204) | audit row 630 | A5191 `0100` line 5878 (1 binding, 1 product) | no page for the bound products (outside 3.6a/3.6b) | - |
| `CMD_MAIN_BREAKER_LIMIT` | upstream-confirmed (line 1215) | audit row 631 | A5191 `010c` line 5905 (1 binding, 1 product) | no page for the bound products (outside 3.6a/3.6b) | - |
| `CMD_EV_LOAD_BALANCING` | upstream-confirmed (line 1228) | audit row 632 | A5191 `010c` line 5906 (1 binding, 1 product) | no page for the bound products (outside 3.6a/3.6b) | - |
| `CMD_EV_SOLAR_CHARGING` | upstream-confirmed (line 1261) | audit row 633 | A5191 `010e` line 5912 (1 binding, 1 product) | no page for the bound products (outside 3.6a/3.6b) | - |
| `CMD_EV_CHARGER_SCHEDULE_SETTINGS` | upstream-confirmed (line 1322) | audit row 634 | A5191 `0106` line 5891 (1 binding, 1 product) | no page for the bound products (outside 3.6a/3.6b) | - |
| `CMD_EV_CHARGER_SCHEDULE_TIMES` | upstream-confirmed (line 1340) | audit row 635 | A5191 `0106` line 5892 (1 binding, 1 product) | no page for the bound products (outside 3.6a/3.6b) | Arithmetic: 0-5947 = 23 * 256 + 59. |
| `CMD_AC_DC_MODE` | upstream-confirmed (line 1378) | none (not in the old doc) | A7320 `0073` line 5939 (1 binding, 1 product) | no page for the bound products (outside 3.6a/3.6b) | - |
| `CMD_BATTERY_CHARGE_LIMITS` | upstream-confirmed (line 1389) | none (not in the old doc) | AS200 `0103` line 5741 (1 binding, 1 product) | no page for the bound products (outside 3.6a/3.6b) | - |

#### Example
synthesized. Not applicable: the index has no payload.

```text
(none)
```

#### Related API endpoint
none (MQTT only).

#### Since/changed
No 3.18.0 comparison: the page indexes upstream, not the app. The audit confirms the TLV header tag `a1` of every upstream command table against the app builders (audit row 584).

#### Known unknowns
- Constants without an app builder: `CMD_SB_MAX_LOAD` has no 0x5a builder in either app version (audit rows 607, 608, 222); `CMD_SB_DEVICE_TIMEOUT` (`009a`) has no divisor 30 in the app setter (audit rows 614, 228).
- Conflict: upstream `CMD_SOC_LIMITS_V2` describes `fd` as a timestamp, the app writes a CRC32 in tag `fd` (audit rows 599, 219); recorded in [README.md](README.md).
- The EV charger and plug constants (`CMD_EV_*`, `CMD_PLUG_*`, `CMD_MODBUS_SWITCH` and others) have no asm audit; the PN pages for their products are not written.

#### Device-tested by
none.

