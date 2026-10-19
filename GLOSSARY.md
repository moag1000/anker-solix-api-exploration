> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# Glossary

One line per term. Each line says what the word means in this repository and links to the owner page that holds the evidence; the glossary states no numbers, addresses or payloads of its own. Where the upstream library ([thomluther/anker-solix-api](https://github.com/thomluther/anker-solix-api)) names a thing, the upstream spelling wins and is given as "upstream name"; a name of ours is marked `(no upstream name)`. Where no owner page exists yet, the entry says so. Reading rules and tags are in [METHODOLOGY.md](METHODOLOGY.md); the owner of each kind of fact is in [docs/STRUCTURE.md](docs/STRUCTURE.md).

## Contents

1. [Sites, devices and identifiers](#sites-devices-and-identifiers)
1. [Product families](#product-families)
1. [Requests, parameters and commands](#requests-parameters-and-commands)
1. [Power limits](#power-limits)
1. [Transport and tools](#transport-and-tools)
1. [Evidence vocabulary](#evidence-vocabulary)

## Sites, devices and identifiers

- **site**: the cloud object that groups the devices of one installation and is addressed by `site_id`; upstream name: `site` (`site_list`, `site_detail` in `API_ENDPOINTS`). Owners: [get_site_list](api/power_service/site/get_site_list.md), [get_site_detail](api/power_service/site/get_site_detail.md).
- **station**: the app's word for the system as a whole in settings pages (for example "station power limit"); not a separate cloud object from the site and not an upstream term, except in the upstream parameter name `SOLARBANK_STATION` (param_type 18). Evidence: [param_types](api/param_types.md), [StationPowerLimitModel](models/station_power_limit.md).
- **scene / scene_info**: the energy-flow document of a site (power values, feature switches, hardware list) that the app shows on its home screen; upstream name: `scene_info` (endpoint `get_scen_info`). Owners: [get_scen_info](api/power_service/site/get_scen_info.md), [platform_get_site_scene](api/power_service/v2/site/platform_get_site_scene.md), [SceneInfoModel](models/scene_info_model.md).
- **device**: one physical product registered to an account, identified by its serial number (`device_sn`) and product number (`device_pn`). Evidence: [models/device.md](models/device.md), [reference/enums.md](reference/enums.md) (product code table).
- **sub-device**: a device that the app lists beneath another device (for example the units grouped with an EV charger); upstream has no such term. Evidence: [SubDeviceModel](models/ev_charger_device_models.md#subdevicemodel); other uses of `sub_device_list` are in [models/firmware.md](models/firmware.md) (no dedicated owner page yet; see the legacy group pages in [models/README.md](models/README.md)).
- **PN (product number)**: the code that names a product type, such as `A17C5`; it is shared by every unit of that product and selects the decoder and the device page. Also called `device_pn` or `product_code` in payloads. Owner: [reference/enums.md](reference/enums.md); per-product pages: [devices/](devices/README.md), [mqtt/](mqtt/README.md), [ble/](ble/README.md).
- **SN (serial number)**: the identifier of one physical unit (`device_sn`), unique per unit, in contrast to the PN. Evidence: [models/device.md](models/device.md), [mqtt/iot.md](mqtt/iot.md) (how the PN picks the controller).

## Product families

- **Solarbank gen 1 / gen 2 / gen 3 / gen 4**: the balcony-battery generations; upstream groups them as `SolixDeviceCategory` values `solarbank_1` to `solarbank_4`; the product number of each generation is in the product table of [reference/enums.md](reference/enums.md) (gen 4 has no page here yet). Owners: [devices/solarbank.md](devices/solarbank.md) (legacy page), [devices/a17c5.md](devices/a17c5.md), [reference/enums.md](reference/enums.md).
- **PPS (portable power station)**: upstream device type `pps`, the portable battery-station family; product codes in [reference/enums.md](reference/enums.md), models in [models/pps.md](models/pps.md).
- **HES (home energy system)**: upstream device type `hes`, the whole-home systems such as X1 (A5101) and E10; see [devices/x1_hes_e10.md](devices/x1_hes_e10.md) (legacy page) and [models/hes.md](models/hes.md).
- **Solarbank PPS**: upstream device type `solarbank_pps`, a portable power station that acts as a solarbank in a site; no owner page yet, see the product table in [reference/enums.md](reference/enums.md).
- **Power Dock / combiner box**: upstream device type `combiner_box`, the unit that joins several solarbanks (`param_type` 16 reads its serial). Owners: [param_types](api/param_types.md), [CombineBoxEntity](models/combine_box_entity.md).

## Requests, parameters and commands

- **param_type**: the string that selects which settings document `set_site_device_param` and `get_site_device_param` read or write; upstream name: `SolixParmType`. Owner: [param_types](api/param_types.md).
- **cmd**: the integer sent next to `param_type` in the same request body; it follows the sender code path, not the `param_type`. Not to be confused with the MQTT `cmd` of the envelope or a BLE opcode. Owner: [param_types](api/param_types.md); MQTT side: [mqtt/envelope.md](mqtt/envelope.md); BLE side: [ble/protocol.md](ble/protocol.md).
- **param_data**: the JSON text carried as a string inside the request, whose keys depend on the `param_type`. Owners: [param_types](api/param_types.md), [set_site_device_param](api/power_service/site/set_site_device_param.md).
- **EMS mode**: the operating or usage mode of the energy management system (for example self-consumption, time of use, smart mode); the app enum is `EmsModeType`, and upstream names the solarbank variants `SolarbankUsageMode`. Owner: [reference/enums.md](reference/enums.md) (wire values are there, not here).
- **encrypted request**: an app call whose body and headers go through the ECDH session of the app; which calls use it and how the headers are built is owned by [api/encryption.md](api/encryption.md); step order from UI to answer: [flows/encrypted_request.md](flows/encrypted_request.md).
- **Smi**: the Dart small-integer tagging that makes Blutter immediates look doubled in tagged slots; the decoding table is owned by [METHODOLOGY.md](METHODOLOGY.md#smi-rule-reading-numbers-from-blutter-output).

## Power limits

- **legal limit vs user power limit**: `legal_limit` is the threshold above which the app asks for the DIY unlock; the user power limit is the output limit the user picks and sends with `param_type` 19. The server-side definitions are not known. Owners: [StationPowerLimitModel](models/station_power_limit.md), [flows/system_output_limit.md](flows/system_output_limit.md), [set_site_device_param](api/power_service/site/set_site_device_param.md#usage-param_type-19-system-output-power-limit).
- **display_type**: a constant key that 3.24.3 adds to the `param_type` 19 payload; its server meaning is open and has a device-test record. Owner: [set_site_device_param](api/power_service/site/set_site_device_param.md#device-tested-by).
- **DIY unlock**: the app prompt (image, password or web page variant) shown before an output limit above the legal limit is set; the password variant calls [verify_unlock_default_power_code](api/devicecontrol/device/verify_unlock_default_power_code.md). Trace: [flows/system_output_limit.md](flows/system_output_limit.md).

## Transport and tools

- **akiot / IoT-Kit**: the native IoT-Kit SDK of the app and its `akiot.*` channel identifiers, the link between the Dart code and device communication. Owner: [reference/iot_kit_channels.md](reference/iot_kit_channels.md).
- **MQTT envelope**: the JSON layer around the binary frame of a device message, with its head fields and topics. Owner: [mqtt/envelope.md](mqtt/envelope.md); generic decode pipeline: [mqtt/iot.md](mqtt/iot.md).
- **TLV frame**: the type-length-value binary frame used on MQTT and BLE. Owners: [mqtt/envelope.md](mqtt/envelope.md), [ble/protocol.md](ble/protocol.md).
- **BLE**: the local Bluetooth channel to a device; a local channel only, never a live fallback for the cloud. Owner: [ble/protocol.md](ble/protocol.md).
- **mqtt_monitor**: the upstream tool that shows live MQTT traffic of a device and is the means of device-testing field maps (upstream name; see the project at [thomluther/anker-solix-api](https://github.com/thomluther/anker-solix-api)). In this repository: [README.md](README.md#for-mqtt_monitor-decoding-sessions), [docs/PERSONAS.md](docs/PERSONAS.md#3-mqtt_monitor-user), decoder pages in [mqtt/README.md](mqtt/README.md).

## Evidence vocabulary

- **asm-traced**, **string-only**, **upstream-confirmed**: confidence tags defined in [METHODOLOGY.md](METHODOLOGY.md#confidence-tags).
- **device-tested**: the strongest tag; a real device accepted or rejected the exact payload, with client, device, date and tester recorded. Defined in [METHODOLOGY.md](METHODOLOGY.md#confidence-tags); an example record is [set_site_device_param](api/power_service/site/set_site_device_param.md#device-tested-by).
- **owner page**: the single page where a fact lives; every other page links to it. Rule: [docs/STRUCTURE.md](docs/STRUCTURE.md#ownership-rule).
