> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# BLE

Single source for BLE-specific facts: the wire protocol ([protocol.md](protocol.md): GATT UUIDs per product family, MTU/fragmentation, timeouts), the handshake ([handshake.md](handshake.md): native ECDH plugin, AES-GCM/CBC session keys) and one page per product number (BLE-only commands and opcodes; the TLV payload tables are owned by the [../mqtt/](../mqtt/README.md) pages and are linked, not copied). Rule (community finding, see protocol.md; not asm-traced): BLE is a local channel and is not a live fallback for the cloud; the app's connection logic tests WiFi first.

| Page | Tag | Title |
|---|---|---|
| [handshake.md](handshake.md) | asm-traced | BLE handshake |
| [protocol.md](protocol.md) | asm-traced | BLE protocol |
| [a1340.md](a1340.md) | asm-traced | A1340 BLE |
| [a172x.md](a172x.md) | asm-traced | A1722, A1723, A1725, A1726, A1727, A1728, A1729 (SOLIX C200 and C300 family) BLE |
| [a1753.md](a1753.md) | asm-traced | A1753, A1754, A1755, A1761, A1762 (SOLIX C800 and C1000 family) BLE |
| [a1770.md](a1770.md) | asm-traced | A1770 (F1200 Bluetooth-only) BLE |
| [a1771.md](a1771.md) | asm-traced | A1771 (F1200 Bluetooth and WLAN) BLE |
| [a1772.md](a1772.md) | asm-traced | A1772 (F1500) BLE |
| [a1780.md](a1780.md) | asm-traced | A1780 (F2000, Bluetooth-only) BLE |
| [a1780p.md](a1780p.md) | asm-traced | A1780P (F2000 with WLAN) BLE |
| [a1781.md](a1781.md) | asm-traced | A1781 (F2600) BLE |
| [a1790.md](a1790.md) | asm-traced | A1790, A1790P (F3800 and F3800 Plus) BLE |
| [a17a0.md](a17a0.md) | asm-traced | A17A0, A17A1, A17A2 (Powered Cooler 30, 40, 50) BLE |
| [a17a3.md](a17a3.md) | asm-traced | A17A3, A17A4, A17A5 (SOLIX Everfrost 2) BLE |
| [a17b1.md](a17b1.md) | asm-traced | A17B1 (SOLIX Home Power Panel) BLE |
| [a17b2.md](a17b2.md) | asm-traced | A17B2 (connected-device model) BLE |
| [a17c0.md](a17c0.md) | asm-traced | A17C0 (Solarbank E1600) BLE |
| [a17c1.md](a17c1.md) | asm-traced | A17C1 (Solarbank 2 E1600 Pro) BLE |
| [a17c2.md](a17c2.md) | asm-traced | A17C2 (Solarbank 2 E1600 AC) BLE |
| [a17c3.md](a17c3.md) | asm-traced | A17C3 (Solarbank 2 E1600 Plus) BLE |
| [a17c5.md](a17c5.md) | asm-traced | A17C5 (Solarbank 3 E2700 Pro) BLE |
| [a17e2.md](a17e2.md) | asm-traced | A17E2, AE103, AE111, AE113, A17E1 (Solarbank E2 series and E10) BLE |
| [a17x7.md](a17x7.md) | asm-traced | A17X7 and A17X7US (Smart Meter) BLE |
| [a17x8.md](a17x8.md) | asm-traced | A17X8 (Smart Plug) BLE |
| [a17y0.md](a17y0.md) | asm-traced | A17Y0 (E1600 0W Output Switch) BLE |
| [a2345.md](a2345.md) | asm-traced | A2345 (250 W Prime Charger) BLE |
| [a5101.md](a5101.md) | asm-traced | A5101, A5102, A5103, A5341 (X1 HES power module) BLE |
| [a5140.md](a5140.md) | asm-traced | A5140, A5141, A5143 (MI60 and MI80 microinverters) BLE |
| [a5150.md](a5150.md) | asm-traced | A5150 (A5150 Module) BLE |
| [a91b2.md](a91b2.md) | asm-traced | A91B2 (240 W Charging Station) BLE |
| [ae1x0.md](ae1x0.md) | asm-traced | AE1X0 and AE1R0 (meters) BLE |
| [shelly.md](shelly.md) | asm-traced | SHEM3, SHEMP3, SHPPS (Shelly 3EM, 3EM Pro, Plus Plug S) BLE |

Not here: MQTT field maps ([../mqtt/README.md](../mqtt/README.md)), cloud endpoints ([../api/README.md](../api/README.md)), enums ([../reference/enums.md](../reference/enums.md)); owner map in [../docs/STRUCTURE.md](../docs/STRUCTURE.md).
