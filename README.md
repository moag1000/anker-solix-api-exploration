> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# Anker Solix API Exploration

> **⚠️ IMPORTANT DISCLAIMER**
>
> This reference was created through reverse engineering of the Anker App 3.24.3
> APK (rework in progress on branch `rework/3.24.3`, 2026-10-19; the previous
> 3.18.0 reference is tagged `v2026.04-app3.18.0`) using Blutter (Dart AOT decompiler).
> **The analysis was heavily AI-assisted.** Before polling the cloud with a library, read [docs/SAFE_USAGE.md](docs/SAFE_USAGE.md).
> This means the content may be:
>
> - **Inaccurate** — field names extracted from compiled binary code may be
>   misattributed to the wrong endpoint or context
> - **Incomplete** — many values, types and constraints are compiled into native
>   ARM64 machine code and could not be recovered
> - **Fundamentally wrong in parts** — AI interpretation of decompiled assembly
>   can produce plausible-looking but incorrect conclusions
>
> **Do not rely on this as authoritative documentation.** Every claim should be
> verified against the live API or the mqtt_monitor tool before use in production
> code. Anker can change any endpoint, field name or behavior between app versions
> without notice.
>
> **No server-side impact analysis has been performed.** This exploration documents
> what the app *sends*, not what the server *expects* or *tolerates*. Sending
> malformed, unexpected, or excessive requests to Anker's API or MQTT infrastructure
> could have unintended consequences including but not limited to account restrictions,
> device malfunction, or infrastructure impact. **Anyone using this data does so
> entirely at their own risk and responsibility.** The authors accept no liability
> for any consequences arising from the use of this information.

## 1. What this is

A reverse-engineering reference for the Anker Solix cloud API, the MQTT status channel and the Bluetooth LE protocol, written from the decompiled Anker app 3.24.3. It is for people who write or maintain client code (for example [thomluther/anker-solix-api](https://github.com/thomluther/anker-solix-api)), who build Home Assistant integrations, who decode MQTT traffic, or who just want to know what the app can do. It documents what the app **sends and handles**; it does not document what the server accepts.

This page is only the front door. It states no protocol facts of its own: every claim is a link to the page that owns it ([docs/STRUCTURE.md](docs/STRUCTURE.md) defines the owner of each kind of fact). Read the disclaimer above before relying on anything here.

## 2. Start here by role

Each role has a persona section (who it is for, the full reading path) in [docs/PERSONAS.md](docs/PERSONAS.md). Three links to start:

- **Library maintainer** ("what exactly does the app send?"): [api/README.md](api/README.md) (service index, one page per endpoint), [api/param_types.md](api/param_types.md), [api/sdk_senders.md](api/sdk_senders.md). Persona: [library maintainer](docs/PERSONAS.md#1-library-maintainer).
- **Home Assistant integration developer** ("which setting, which flow, which ranges?"): [flows/README.md](flows/README.md), [docs/SAFE_USAGE.md](docs/SAFE_USAGE.md), [reference/validation_model.md](reference/validation_model.md). Persona: [HA integration developer](docs/PERSONAS.md#2-home-assistant-integration-developer).
- **Device tester / mqtt_monitor user** ("what is this field, and what can I verify on my device?"): [mqtt/README.md](mqtt/README.md) (one decoder page per product number), [docs/DEVICE_TEST_BACKLOG.md](docs/DEVICE_TEST_BACKLOG.md) (pick a test for your hardware), [CONTRIBUTING.md](CONTRIBUTING.md) (how to report a result). Persona: [mqtt_monitor user](docs/PERSONAS.md#3-mqtt_monitor-user).
- **BLE project developer** ("opcode, TLV, handshake?"): [ble/protocol.md](ble/protocol.md), [ble/handshake.md](ble/handshake.md), [ble/README.md](ble/README.md). BLE is a local channel only and is not a live fallback for the cloud. Persona: [BLE developer](docs/PERSONAS.md#4-ble-project-developer).
- **Newcomer** ("what can be controlled, what is a site?"): [GLOSSARY.md](GLOSSARY.md), [METHODOLOGY.md](METHODOLOGY.md), [flows/README.md](flows/README.md). Persona: [newcomer](docs/PERSONAS.md#5-curious-user--newcomer).

## 3. Use-case index

| I want to ... | Go to |
|---|---|
| set the output limit of a Solarbank site | [api/power_service/site/set_site_device_param.md](api/power_service/site/set_site_device_param.md), flow [flows/system_output_limit.md](flows/system_output_limit.md) |
| understand what a `param_type` value does | [api/param_types.md](api/param_types.md) |
| change a Solarbank schedule or reserve | [flows/solarbank2_schedule.md](flows/solarbank2_schedule.md), [flows/solarbank_soc_reserve_change.md](flows/solarbank_soc_reserve_change.md) |
| control a smart plug (timer, schedule, relay) | [flows/smart_plug_countdown_timer.md](flows/smart_plug_countdown_timer.md), [flows/smart_plug_schedule.md](flows/smart_plug_schedule.md), [flows/smart_plug_relay_toggle.md](flows/smart_plug_relay_toggle.md) |
| start a charging session on an EV charger | [flows/ev_charger_start_charging.md](flows/ev_charger_start_charging.md), [devices/ev_charger.md](devices/ev_charger.md) |
| find the endpoint for a URL I saw | [api/README.md](api/README.md#service-index), machine-readable [data/endpoints.json](data/endpoints.json) |
| look up a response model's fields | [models/README.md](models/README.md), machine-readable [data/models.json](data/models.json) |
| log in, build headers, handle tokens | [api/auth.md](api/auth.md) |
| send an encrypted request | [api/encryption.md](api/encryption.md), [flows/encrypted_request.md](flows/encrypted_request.md) |
| decode an error code | [api/errors.md](api/errors.md) |
| read a device's MQTT status | [mqtt/README.md](mqtt/README.md), then `mqtt/<pn>.md` for the product number |
| understand the MQTT envelope and TLV frame | [mqtt/envelope.md](mqtt/envelope.md) |
| map an upstream command constant to its pages | [mqtt/upstream_commands.md](mqtt/upstream_commands.md) |
| pair or talk to a device over BLE | [ble/handshake.md](ble/handshake.md), [ble/protocol.md](ble/protocol.md), [ble/README.md](ble/README.md) |
| use Modbus / third-party control | [devices/modbus.md](devices/modbus.md), [flows/modbus_setup.md](flows/modbus_setup.md) |
| see what the `akiot.*` IoT-Kit channels are | [reference/iot_kit_channels.md](reference/iot_kit_channels.md) |
| check client-side validation ranges before sending | [reference/validation_model.md](reference/validation_model.md) |
| look up enum values and product codes | [reference/enums.md](reference/enums.md) |
| learn the app's polling, retry and error behaviour | [reference/business_rules.md](reference/business_rules.md), recommendations in [docs/SAFE_USAGE.md](docs/SAFE_USAGE.md) |
| poll the cloud without getting an account flagged | [docs/SAFE_USAGE.md](docs/SAFE_USAGE.md) |
| know which native libraries, hosts and channels the app has | [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) |
| test something on my own device | [docs/DEVICE_TEST_BACKLOG.md](docs/DEVICE_TEST_BACKLOG.md), then [CONTRIBUTING.md](CONTRIBUTING.md) |
| look up a term | [GLOSSARY.md](GLOSSARY.md) |

### For mqtt_monitor decoding sessions

Start at [mqtt/README.md](mqtt/README.md) and [mqtt/envelope.md](mqtt/envelope.md); the full path is [persona 3](docs/PERSONAS.md#3-mqtt_monitor-user).

## 4. Version matrix

The reference was rebuilt from App 3.24.3. The previous state, built from App 3.18.0, is preserved at the git tag `v2026.04-app3.18.0`. This table is the owner of the app identity strings; everything else about the two versions is on the linked pages.

| | 3.18.0 | 3.24.3 |
|---|---|---|
| Status in this repository | tag `v2026.04-app3.18.0`; the superseded root pages ([section 9](#9-3180-reference-superseded)) | current (all pages outside section 9) |
| Build | build 160 | versionCode 237, package `com.anker.charging` |
| Dart SDK | 3.4.4 | 3.11.0 (stable) |
| Tool | [Blutter](https://github.com/worawit/blutter) AOT decompilation | [Blutter](https://github.com/worawit/blutter) AOT decompilation |

Build identifiers:

- 3.18.0, Dart snapshot `d20a1be77c3d3c41b2a5accaee1ce549`
- 3.24.3, Dart snapshot `78da37fed6bf1489361a312568249f3f`
- 3.24.3, XAPK sha256 `7d6d0deab4834515c41aa5e8bafff03f9735e883f15c4f8d5b7194e871ff6ba5`

What changed in 3.24.3 (new and removed services, native libraries, SDKs and hosts) is in [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md#changed-since-3180). Endpoints present in only one of the two versions are marked on their pages and counted in the coverage block below. The corrections that the 3.24.3 audit made to earlier 3.18.0 statements (wrong command values, slot counts, state codes) are the Errata in [CHANGELOG.md](CHANGELOG.md#errata-2026-10-smi-decoding); the per-claim audit tables are in [docs/audit/](docs/audit/).

## 5. Coverage and confidence tags

Coverage and statistics are generated from the data files and the pages on disk. Nothing in this block is typed by hand; regenerate it with `python3 -I tools/readme_stats.py` (see [tools/README.md](tools/README.md)).

<!-- readme_stats:begin -->
This block is the data snapshot 2026-10-19, generated by `tools/readme_stats.py` from `data/*.json` and the files on disk; do not edit by hand (run the tool again).

**Coverage**

- Endpoint pages: 450 of 450 distinct URLs in `data/endpoints.json` have a page (439 with a code reference in 3.24.3, 9 only in the 3.24.3 object pool with no code reference, 2 only in 3.18.0), plus 3 hand-written pages with no inventory row; 453 endpoint pages in total.
- Of these pages, 124 are hand-written and 329 are skeletons (`Confidence: string-only` with unfilled `<!-- TODO -->` purpose); the skeletons carry only what `data/endpoints.json` knows.

**Statistics**

- 24 API services (directories under [api/](api/README.md))
- 1017 model classes in `data/models.json` (1012 with fields), 53 pages in [models/](models/README.md)
- 24 distinct param_type values sent by 3.24.3 (`data/param_types.json`, owner page [api/param_types.md](api/param_types.md))
- 21 MQTT pages in [mqtt/](mqtt/README.md), 20 flow pages in [flows/](flows/README.md)
- Smi audit of the old root pages ([docs/audit/](docs/audit/)): 1460 audited claims in 15 tables, of which 182 are WRONG (the real value is in each table)
<!-- readme_stats:end -->

Every fact page carries one of four confidence tags in its status header; the full definitions, the ranking and the Smi rule for reading integers from the decompiled code are in [METHODOLOGY.md](METHODOLOGY.md#confidence-tags).

| Tag | Meaning in one line |
|---|---|
| `asm-traced` | backed by a cited site in the 3.24.3 asm |
| `string-only` | the string is in the 3.24.3 binary, but no call site is traced |
| `upstream-confirmed` | matches code in thomluther/anker-solix-api that the community runs |
| `device-tested` | a real device accepted or rejected the exact payload; the record names client, version, PN, firmware, date and tester |

A page header reads `> Verified against: App 3.24.3 · Date · Confidence: <tag> · Owner page: <path>`. Guidance pages such as this one carry `Page type: guidance` instead of a tag.

## 6. Repository map

| Path | What it holds |
|---|---|
| [api/](api/README.md) | one page per cloud endpoint grouped by service, plus [param_types.md](api/param_types.md), [errors.md](api/errors.md), [auth.md](api/auth.md), [encryption.md](api/encryption.md), [sdk_senders.md](api/sdk_senders.md) |
| [mqtt/](mqtt/README.md) | one MQTT decoder page per product number, the shared [envelope](mqtt/envelope.md) |
| [ble/](ble/README.md) | BLE [protocol](ble/protocol.md), [handshake](ble/handshake.md) and one page per product number |
| [flows/](flows/README.md) | step traces of user-visible actions; links only, no payload copies |
| [devices/](devices/README.md) | product pages with device-tested status, plus [Modbus](devices/modbus.md) |
| [models/](models/README.md) | response and request model pages that own the field lists |
| [reference/](reference/README.md) | enums, business rules, validation model, IoT-Kit channels |
| [data/](data/README.md) | machine-readable exports (generated, never hand-edited) |
| [docs/](docs/STRUCTURE.md) | [STRUCTURE.md](docs/STRUCTURE.md) (fact ownership and migration map), [PERSONAS.md](docs/PERSONAS.md), [ARCHITECTURE.md](docs/ARCHITECTURE.md), [SAFE_USAGE.md](docs/SAFE_USAGE.md), [DEVICE_TEST_BACKLOG.md](docs/DEVICE_TEST_BACKLOG.md), [audit/](docs/audit/) (Smi audit tables), templates |
| [tools/](tools/README.md) | the generators, the linter and the tests behind the data and the statistics |
| [patches/](patches/README.md) | patches against the mqtt_monitor tool from the 3.18.0 era; stale, see its README before use |
| root | [METHODOLOGY.md](METHODOLOGY.md), [GLOSSARY.md](GLOSSARY.md), [CONTRIBUTING.md](CONTRIBUTING.md), [CHANGELOG.md](CHANGELOG.md), and the superseded pages of section 9 |

## 7. Data exports

[data/README.md](data/README.md) describes the four JSON exports (endpoints, models, param types, error codes), their schema and how stable they are. They are the inputs for diffing this reference against a client library; the prose pages cite them.

## 8. Contributing, safe usage, glossary

See [CONTRIBUTING.md](CONTRIBUTING.md) for the device-tested record template, how to report a contradiction, and the checks a change must pass (issue templates: `device-tested`, `correction`).

- Device owners: pick a test from [docs/DEVICE_TEST_BACKLOG.md](docs/DEVICE_TEST_BACKLOG.md) and report the result as described in CONTRIBUTING.
- Before polling the cloud with any library: [docs/SAFE_USAGE.md](docs/SAFE_USAGE.md).
- Terms: [GLOSSARY.md](GLOSSARY.md). The measurement method is [Discussion #222](https://github.com/thomluther/anker-solix-api/discussions/222) of the upstream library.

## 9. 3.18.0 reference, superseded

These root files still carry 3.18.0 content and are kept only until their deletion in Task 4.9. Each starts with a banner naming its owner pages on 3.24.3; do not use them as a source. The old `endpoints/` pages and the legacy group pages in [models/](models/README.md) and [devices/](devices/README.md) are covered by the migration map in [docs/STRUCTURE.md](docs/STRUCTURE.md#migration-map).

| Superseded file | Owner on 3.24.3 |
|---|---|
| [BLE_COMMAND_MAP.md](BLE_COMMAND_MAP.md) | [ble/](ble/README.md), [mqtt/](mqtt/README.md) |
| [BUSINESS_RULES.md](BUSINESS_RULES.md) | [reference/business_rules.md](reference/business_rules.md) |
| [DART_PYTHON_MAPPING.md](DART_PYTHON_MAPPING.md) | [data/models.json](data/models.json), [models/](models/README.md) |
| [ENDPOINT_FIELDS.md](ENDPOINT_FIELDS.md) | [api/](api/README.md) |
| [ENUMS.md](ENUMS.md) | [reference/enums.md](reference/enums.md) |
| [FIELD_TYPES.md](FIELD_TYPES.md) | [models/](models/README.md), [data/models.json](data/models.json) |
| [FLOWS.md](FLOWS.md) | [flows/](flows/README.md) |
| [JSON_EXAMPLES.md](JSON_EXAMPLES.md) | [api/](api/README.md) |
| [PARAM_DATA_STRUCTURES.md](PARAM_DATA_STRUCTURES.md) | [api/param_types.md](api/param_types.md) |
| [REQUIRED_FIELDS.md](REQUIRED_FIELDS.md) | [api/](api/README.md) |
| [RESPONSE_EXAMPLES.md](RESPONSE_EXAMPLES.md) | [api/](api/README.md) |
| [VALIDATION_MODEL.md](VALIDATION_MODEL.md) | [reference/validation_model.md](reference/validation_model.md) |

---

## Trademarks

Anker, Solix, Solarbank, EverFrost, and related product names are trademarks of
Anker Innovations Limited. Shelly is a trademark of Allterco Robotics. Nordpool,
Tibber, Octopus Energy, Amazon, Alexa, and Google are trademarks of their
respective owners. OCPP is a standard by the Open Charge Alliance.

This project is not affiliated with, endorsed by, or connected to any of these
companies. All trademarks are used here solely for identification and
interoperability documentation purposes under fair use.
