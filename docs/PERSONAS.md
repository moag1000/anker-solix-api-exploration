> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# Personas and reading paths

This page defines who this repository is written for. A page counts as "usable" when a person from one of the five groups below can reach the answer to their first question within the reading path listed for them. The status tags and rules behind every fact are defined in [METHODOLOGY.md](../METHODOLOGY.md) and are not repeated here.

The repository is being rebuilt on App 3.24.3 (branch `rework/3.24.3`). Each step names the **Now** page (an owner page that exists on this branch, re-verified against 3.24.3) and, where the owner is not written yet, the **Planned** path as plain text. The old root pages (`FLOWS.md`, `ENUMS.md`, `VALIDATION_MODEL.md`, ...) are 3.18.0 references that are being superseded; they are named only where no owner page exists yet and are marked as such.

## 1. Library maintainer

- **Who:** Maintains or contributes to an open-source client library such as [thomluther/anker-solix-api](https://github.com/thomluther/anker-solix-api).
- **First question:** "What exactly does the app send for this endpoint?"
- **First page needed:** the endpoint page for the service, plus the machine-readable endpoint table.

| Step | Now | Planned |
|---|---|---|
| 1 | [api/README.md](../api/README.md) (service index), then the endpoint page `api/<service>/<endpoint>.md` | |
| 2 | [data/endpoints.json](../data/endpoints.json) (machine-readable, diffable against the library) | |
| 3 | [api/param_types.md](../api/param_types.md), [api/sdk_senders.md](../api/sdk_senders.md) | |
| 4 | [ENUMS.md](../ENUMS.md) (3.18.0 reference, audit in [audit/ENUMS.md](audit/ENUMS.md)) | `reference/enums.md` |
| 5 | [METHODOLOGY.md](../METHODOLOGY.md) (how to judge a claim) | unchanged |

## 2. Home Assistant integration developer

- **Who:** Builds or extends a Home Assistant integration and wants to expose a device setting.
- **First question:** "Which setting controls X, what is the GET to SET flow, and what are the validation ranges?"
- **First page needed:** the flow page for the feature and the param_type table.

| Step | Now | Planned |
|---|---|---|
| 1 | [flows/README.md](../flows/README.md) (flow pages: system output limit, encrypted request, Modbus setup) | more flow pages |
| 2 | [api/param_types.md](../api/param_types.md) | |
| 3 | [VALIDATION_MODEL.md](../VALIDATION_MODEL.md) (3.18.0 reference, numbers under review) | `reference/validation_model.md` |
| 4 | the parameter table of the endpoint page in [api/README.md](../api/README.md) | |
| 5 | [devices/a17c5.md](../devices/a17c5.md) and [devices/modbus.md](../devices/modbus.md) (device pages on 3.24.3) | `devices/<pn>.md` for the other products |

## 3. mqtt_monitor user

- **Who:** Watches live MQTT traffic of a device and needs to decode what it sees.
- **First question:** "What is field a8, or command 0x7c?"
- **First page needed:** the MQTT decoder page for the device's product number (PN).
- **Status: per-PN decoder pages exist** for the products listed in [mqtt/README.md](../mqtt/README.md); products without a page are not decoded yet.

| Step | Now | Planned |
|---|---|---|
| 1 | [mqtt/README.md](../mqtt/README.md), then the page for your PN (`mqtt/<pn>.md`) | |
| 2 | [mqtt/envelope.md](../mqtt/envelope.md) (envelope, command types, TLV frame, data type codes) | |
| 3 | [mqtt/upstream_commands.md](../mqtt/upstream_commands.md) (every upstream command constant with its PN pages) | |
| 4 | [VALIDATION_MODEL.md](../VALIDATION_MODEL.md) ("MQTT-Only Settings"; 3.18.0 reference, numbers under review) | `reference/validation_model.md` |
| 5 | [ENUMS.md](../ENUMS.md) (meaning of enum values seen in fields; 3.18.0 reference) | `reference/enums.md` |

## 4. BLE project developer

- **Who:** Writes or maintains a Bluetooth LE client for Anker Solix devices.
- **First question:** "Which opcode, which TLV layout, and how does the handshake work?"
- **First page needed:** the BLE page for the device's PN (planned; see below).

BLE is a local channel. It is not a live fallback for the cloud: the app disables BLE while WiFi is active, so do not plan a design around switching between the two.

The [ble/](../ble/README.md) pages exist: [protocol](../ble/protocol.md), [handshake](../ble/handshake.md) and one page per product number. The shared TLV frame and the per-product command tags stay on the MQTT pages, because the same frame carries them; the BLE pages link them.

| Step | Now | Planned |
|---|---|---|
| 1 | [mqtt/envelope.md](../mqtt/envelope.md) (TLV frame) and [mqtt/README.md](../mqtt/README.md) (command tags per PN) | `ble/protocol.md`, `ble/<pn>.md` |
| 2 | [ble/README.md](../ble/README.md) | [ble/handshake.md](../ble/handshake.md) |
| 3 | [ENUMS.md](../ENUMS.md) (3.18.0 reference) | `reference/enums.md` |
| 4 | [METHODOLOGY.md](../METHODOLOGY.md) (Smi rule for reading numbers) | unchanged |

## 5. Curious user / newcomer

- **Who:** Owns Anker Solix hardware or is evaluating it, with no API background.
- **First question:** "What can be controlled at all, and what is a site or a station?"
- **First page needed:** the README use-case index; the glossary (`GLOSSARY.md`) is planned.
- **Glossary planned (target `GLOSSARY.md`); no equivalent today. Start with the README use-case index.**

| Step | Now | Planned |
|---|---|---|
| 1 | [README.md](../README.md#how-to-use-this-reference) (use-case index) | unchanged |
| 2 | [METHODOLOGY.md](../METHODOLOGY.md) (what the confidence tags mean) | |
| 3 | [devices/a17c5.md](../devices/a17c5.md) (a worked device page; not a glossary) | `GLOSSARY.md` (site, station, device, PN) |
| 4 | [flows/README.md](../flows/README.md) (what the app can do, step by step) | more flow pages |
