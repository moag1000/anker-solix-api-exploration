> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# Personas and reading paths

This page defines who this repository is written for. A page counts as "usable" when a person from one of the five groups below can reach the answer to their first question within the reading path listed for them. The status tags and rules behind every fact are defined in [METHODOLOGY.md](../METHODOLOGY.md) and are not repeated here. The front door that links each path is the [README](../README.md); the layout and the owner of each kind of fact are in [STRUCTURE.md](STRUCTURE.md).

Every page named below is an owner page re-verified against App 3.24.3. The superseded 3.18.0 root pages (listed in [README section 9](../README.md#9-3180-reference-superseded)) are not part of any reading path.

## 1. Library maintainer

- **Who:** Maintains or contributes to an open-source client library such as [thomluther/anker-solix-api](https://github.com/thomluther/anker-solix-api).
- **First question:** "What exactly does the app send for this endpoint?"
- **First page needed:** the endpoint page for the service, plus the machine-readable endpoint table.

| Step | Page |
|---|---|
| 1 | [api/README.md](../api/README.md) (service index), then the endpoint page `api/<service>/<endpoint>.md` |
| 2 | [data/endpoints.json](../data/endpoints.json) (machine-readable, diffable against the library; schema in [data/README.md](../data/README.md)) |
| 3 | [api/param_types.md](../api/param_types.md), [api/sdk_senders.md](../api/sdk_senders.md) |
| 4 | [api/auth.md](../api/auth.md), [api/encryption.md](../api/encryption.md), [api/errors.md](../api/errors.md) |
| 5 | [reference/enums.md](../reference/enums.md) and [models/README.md](../models/README.md) (enum values, response fields) |
| 6 | [SAFE_USAGE.md](SAFE_USAGE.md) (what to poll, how often, what not to do) |
| 7 | [METHODOLOGY.md](../METHODOLOGY.md) (how to judge a claim) |

## 2. Home Assistant integration developer

- **Who:** Builds or extends a Home Assistant integration and wants to expose a device setting.
- **First question:** "Which setting controls X, what is the GET to SET flow, and what are the validation ranges?"
- **First page needed:** the flow page for the feature and the param_type table.

| Step | Page |
|---|---|
| 1 | [flows/README.md](../flows/README.md) (one page per user-visible action) |
| 2 | [api/param_types.md](../api/param_types.md) |
| 3 | [reference/validation_model.md](../reference/validation_model.md) (client-side ranges and checks) |
| 4 | the parameter table of the endpoint page, reached from [api/README.md](../api/README.md) |
| 5 | [devices/README.md](../devices/README.md) (product pages such as [a17c5.md](../devices/a17c5.md) and [modbus.md](../devices/modbus.md)) |
| 6 | [SAFE_USAGE.md](SAFE_USAGE.md) and [reference/business_rules.md](../reference/business_rules.md) (polling, retry, token behaviour) |

## 3. mqtt_monitor user

- **Who:** Watches live MQTT traffic of a device and needs to decode what it sees.
- **First question:** "What is field a8, or command 0x7c?"
- **First page needed:** the MQTT decoder page for the device's product number (PN).
- **Status:** per-PN decoder pages exist for the products listed in [mqtt/README.md](../mqtt/README.md); a product without a page is not decoded yet. Device owners can also pick a verification task from [DEVICE_TEST_BACKLOG.md](DEVICE_TEST_BACKLOG.md).

| Step | Page |
|---|---|
| 1 | [mqtt/README.md](../mqtt/README.md), then the page for your PN (`mqtt/<pn>.md`) |
| 2 | [mqtt/envelope.md](../mqtt/envelope.md) (envelope, command types, TLV frame, data type codes) |
| 3 | [mqtt/upstream_commands.md](../mqtt/upstream_commands.md) (every upstream command constant with its PN pages) |
| 4 | [reference/validation_model.md](../reference/validation_model.md) (MQTT-only settings) |
| 5 | [reference/enums.md](../reference/enums.md) (meaning of enum values seen in fields) |
| 6 | [DEVICE_TEST_BACKLOG.md](DEVICE_TEST_BACKLOG.md) and [CONTRIBUTING.md](../CONTRIBUTING.md) (pick a test, report the result) |

## 4. BLE project developer

- **Who:** Writes or maintains a Bluetooth LE client for Anker Solix devices.
- **First question:** "Which opcode, which TLV layout, and how does the handshake work?"
- **First page needed:** the BLE page for the device's PN, after the protocol and handshake pages.

BLE is a local channel. It is not a live fallback for the cloud: the app disables BLE while WiFi is active, so do not plan a design around switching between the two.

The shared TLV frame and the per-product command tags are owned by the MQTT pages, because the same frame carries them; the BLE pages link them instead of copying.

| Step | Page |
|---|---|
| 1 | [ble/protocol.md](../ble/protocol.md) (GATT UUIDs, MTU, fragmentation, timeouts) |
| 2 | [ble/handshake.md](../ble/handshake.md) (native ECDH plugin, session keys) |
| 3 | [ble/README.md](../ble/README.md), then the page for your PN (`ble/<pn>.md`) |
| 4 | [mqtt/envelope.md](../mqtt/envelope.md) and `mqtt/<pn>.md` (TLV frame and command tags) |
| 5 | [reference/enums.md](../reference/enums.md) (enum values) |
| 6 | [METHODOLOGY.md](../METHODOLOGY.md) (Smi rule for reading numbers) |

## 5. Curious user / newcomer

- **Who:** Owns Anker Solix hardware or is evaluating it, with no API background.
- **First question:** "What can be controlled at all, and what is a site or a station?"
- **First page needed:** the README use-case index and the [glossary](../GLOSSARY.md).

| Step | Page |
|---|---|
| 1 | [README.md](../README.md#3-use-case-index) (use-case index) |
| 2 | [GLOSSARY.md](../GLOSSARY.md) (site, station, device, PN) |
| 3 | [METHODOLOGY.md](../METHODOLOGY.md) (what the confidence tags mean) |
| 4 | [flows/README.md](../flows/README.md) (what the app can do, step by step) |
| 5 | [SAFE_USAGE.md](SAFE_USAGE.md) (before trying anything against your own account) |
