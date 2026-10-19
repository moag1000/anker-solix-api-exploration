> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# Personas and reading paths

This page defines who this repository is written for. A page counts as "usable" when a person from one of the five groups below can reach the answer to their first question within the reading path listed for them. The status tags and rules behind every fact are defined in [METHODOLOGY.md](../METHODOLOGY.md) and are not repeated here.

The repository is being rebuilt on App 3.24.3, so each step has two columns. **Today** links to the file that exists now (the older layout). **Target** names the planned path in the new layout as plain text; those files are created by later tasks of the rework and are deliberately not linked, so nothing dangles. Once a target page exists, this page switches to it.

## 1. Library maintainer

- **Who:** Maintains or contributes to an open-source client library such as [thomluther/anker-solix-api](https://github.com/thomluther/anker-solix-api).
- **First question:** "What exactly does the app send for this endpoint?"
- **First page needed:** the endpoint page for the service, plus the machine-readable endpoint table.

| Step | Today | Target |
|---|---|---|
| 1 | [README Endpoints section](../README.md#endpoints) (index), then one service page such as [endpoints/power_service_site.md](../endpoints/power_service_site.md) | `api/<service>/<endpoint>.md` |
| 2 | [ENDPOINT_FIELDS.md](../ENDPOINT_FIELDS.md) | `data/endpoints.json` (machine-readable, diffable against the library) |
| 3 | [PARAM_DATA_STRUCTURES.md](../PARAM_DATA_STRUCTURES.md) | `api/param_types.md` |
| 4 | [ENUMS.md](../ENUMS.md) | `reference/` |
| 5 | [METHODOLOGY.md](../METHODOLOGY.md) (how to judge a claim) | `METHODOLOGY.md` (unchanged) |

## 2. Home Assistant integration developer

- **Who:** Builds or extends a Home Assistant integration and wants to expose a device setting.
- **First question:** "Which setting controls X, what is the GET to SET flow, and what are the validation ranges?"
- **First page needed:** the flow page for the feature and the param_type table.

| Step | Today | Target |
|---|---|---|
| 1 | [FLOWS.md](../FLOWS.md) | `flows/<name>.md` |
| 2 | [PARAM_DATA_STRUCTURES.md](../PARAM_DATA_STRUCTURES.md) | `api/param_types.md` |
| 3 | [VALIDATION_MODEL.md](../VALIDATION_MODEL.md) | `flows/<name>.md` (ranges live on the flow page) |
| 4 | [REQUIRED_FIELDS.md](../REQUIRED_FIELDS.md) | `api/<service>/<endpoint>.md` |
| 5 | [devices/solarbank.md](../devices/solarbank.md) (example device) | `devices/<pn>.md` |

## 3. mqtt_monitor user

- **Who:** Watches live MQTT traffic of a device and needs to decode what it sees.
- **First question:** "What is field a8, or command 0x7c?"
- **First page needed:** the MQTT decoder page for the device's product number (PN).
- **Status today: partial.** No existing page is a per-PN field decoder; those pages (`mqtt/<pn>.md`) are a target. The nearest answers are spread over four files, listed below.

| Step | Today | Target |
|---|---|---|
| 1 | [devices/solarbank.md](../devices/solarbank.md) (MQTT sections: "MQTT Commands", "MQTT Abbreviated Fields"; A17C1 `0050`/`0067`/`005a`/`005e` a2..a4 fields) | `mqtt/<pn>.md` |
| 2 | [BLE_COMMAND_MAP.md](../BLE_COMMAND_MAP.md) (MQTT sections: "A17B1 — Solarbank 2 System JSON Keys (MQTT status)", "A5101 — X1 HES MQTT Status Fields", device to command matrix) | `mqtt/<pn>.md` |
| 3 | [devices/smart_plug.md](../devices/smart_plug.md) (MQTT section: "MQTT Commands", A17X8 timer and pause/resume) | `devices/<pn>.md` |
| 4 | [VALIDATION_MODEL.md](../VALIDATION_MODEL.md) ("MQTT-Only Settings" for A17C0-C5; ranges per command) | `flows/<name>.md` |
| 5 | [ENUMS.md](../ENUMS.md) (meaning of enum values seen in fields) | `reference/` |

## 4. BLE project developer

- **Who:** Writes or maintains a Bluetooth LE client for Anker Solix devices.
- **First question:** "Which opcode, which TLV layout, and how does the handshake work?"
- **First page needed:** the BLE page for the device's PN.

BLE is a local channel. It is not a live fallback for the cloud: the app disables BLE while WiFi is active, so do not plan a design around switching between the two.

| Step | Today | Target |
|---|---|---|
| 1 | [BLE_COMMAND_MAP.md](../BLE_COMMAND_MAP.md) (BLE part) | `ble/<pn>.md` |
| 2 | [ENUMS.md](../ENUMS.md) | `reference/` |
| 3 | [devices/solarbank.md](../devices/solarbank.md) (example device) | `devices/<pn>.md` |
| 4 | [METHODOLOGY.md](../METHODOLOGY.md) (Smi rule for reading numbers) | `METHODOLOGY.md` (unchanged) |

## 5. Curious user / newcomer

- **Who:** Owns Anker Solix hardware or is evaluating it, with no API background.
- **First question:** "What can be controlled at all, and what is a site or a station?"
- **First page needed:** today the README use-case index; target is the glossary (`GLOSSARY.md`), then that index.
- **Glossary planned (target `GLOSSARY.md`); no equivalent today. Start with the README use-case index.**

| Step | Today | Target |
|---|---|---|
| 1 | [README.md](../README.md#how-to-use-this-reference) (use-case index) | `README.md` (use-case index) |
| 2 | [devices/solarbank.md](../devices/solarbank.md) (closest thing to an overview; not a glossary) | `GLOSSARY.md` (site, station, device, PN) |
| 3 | [models/device.md](../models/device.md) | `models/` |
| 4 | [FLOWS.md](../FLOWS.md) (what the app can do, step by step) | `flows/<name>.md` |
