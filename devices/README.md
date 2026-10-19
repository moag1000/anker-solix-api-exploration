> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# Devices

This directory holds one product page per product number (`<pn>.md`): a short summary, links to the API, MQTT and BLE owner pages, and the device-tested status. All pages are on App 3.24.3. [a17c5.md](a17c5.md) (Solarbank 3) and [modbus.md](modbus.md) (third-party control, a feature page rather than a PN page) were written for 3.24.3. The five legacy pages (`ev_charger.md`, `home_power_panel.md`, `smart_plug.md`, `solarbank.md`, `x1_hes_e10.md`) were brought onto 3.24.3 by consuming their Smi audit table ([../docs/audit/devices.md](../docs/audit/devices.md)); they stay until the migration map marks them done.

| page | product | page type | confidence tag (lowest on the page) |
|---|---|---|---|
| [a17c5.md](a17c5.md) | Solarbank 3 E2700 Pro | PN page | asm-traced |
| [modbus.md](modbus.md) | third-party control (Modbus, Home Assistant, Homey) | feature page | asm-traced (see the page header) |
| [solarbank.md](solarbank.md) | Solarbank family A17C0, A17C1, A17C2, A17C3, A17C5 | device page | asm-traced |
| [smart_plug.md](smart_plug.md) | Smart Plug A17X8 | device page | asm-traced |
| [ev_charger.md](ev_charger.md) | EV Charger V1 A5190 and A5191 | device page | asm-traced |
| [home_power_panel.md](home_power_panel.md) | Home Power Panel A17B1 | device page | asm-traced |
| [x1_hes_e10.md](x1_hes_e10.md) | X1 HES, E10, AX170 (A5101 and relatives) | device page | asm-traced |

The tag of a page is the lowest tag among its facts ([../METHODOLOGY.md](../METHODOLOGY.md)); stronger claims carry their own tag inline. On the legacy pages, statements that the audit could not tie to the asm (upstream values, counts, examples) are tagged inline or listed under Known unknowns.

Not here: payloads, field maps or opcodes; owners are listed in [../docs/STRUCTURE.md](../docs/STRUCTURE.md).
