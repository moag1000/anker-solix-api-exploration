> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# EV charger device models (RFID, tamper log, site info, group devices, OCPP)

## Contents

1. [A5190RfidCardModel](#a5190rfidcardmodel)
2. [RfidCardModel](#rfidcardmodel)
3. [A5190SecurityLogsModel](#a5190securitylogsmodel)
4. [Records](#records)
5. [EvChargerSiteInfoModel](#evchargersiteinfomodel)
6. [SiteInfo](#siteinfo)
7. [SiteDevice](#sitedevice)
8. [DeviceFeature](#devicefeature)
9. [GroupDeviceModel](#groupdevicemodel)
10. [SubDeviceModel](#subdevicemodel)
11. [OcppListModel](#ocpplistmodel)
12. [OcppItemModel](#ocppitemmodel)
13. [OCPPServerLinkInfoModel](#ocppserverlinkinfomodel)

## Purpose

Carries the answers of the EV charger device endpoints: RFID cards, the tamper-proof log, the site that holds a charger, the sub-devices grouped with a charger, and the OCPP endpoint list and link info.

## Dart class + file

`A5190RfidCardModel` (`ev_charger/src/ev_charger/model/a5190_rfid_card_model.dart`); `RfidCardModel` (`ev_charger/src/ev_charger/model/a5190_rfid_card_model.dart`); `A5190SecurityLogsModel` (`ev_charger/src/ev_charger/model/a5190_security_logs_model.dart`); `Records` (`ev_charger/src/ev_charger/model/a5190_security_logs_model.dart`); `EvChargerSiteInfoModel` (`ev_charger/src/ev_charger/model/ev_charger_site_info_model.dart`); `SiteInfo` (`ev_charger/src/ev_charger/model/ev_charger_site_info_model.dart`); `SiteDevice` (`ev_charger/src/ev_charger/model/ev_charger_site_info_model.dart`); `DeviceFeature` (`ev_charger/src/ev_charger/model/ev_charger_site_info_model.dart`); `GroupDeviceModel` (`ev_charger/src/ev_charger/model/group_device_model.dart`); `SubDeviceModel` (`ev_charger/src/ev_charger/model/group_device_model.dart`); `OcppListModel` (`ev_charger/src/ev_charger/page/home/setting/ocpp/models/ocpp_list_model.dart`); `OcppItemModel` (`ev_charger/src/ev_charger/page/home/setting/ocpp/models/ocpp_list_model.dart`); `OCPPServerLinkInfoModel` (`ev_charger/src/ev_charger/page/home/charge_sessions/model/ocpp_server_link_info_model.dart`). `fromJson` addresses are under each class below.

## Fields

Every `source` address is the string load of the JSON key inside the class `fromJson` and was re-read in the asm. Dart types and nullability come from `tools/model_fields.py` (`data/models.json`); an "of `X`" note is the list element class read from the `<X>` type argument next to the key. The top-level answer classes are registered in `AnkerJsonUtils.initAnkerModelSerializable` (`ev_charger_json_factory.internal.dart @0x45ab020`, see [../api/sdk_senders.md](../api/sdk_senders.md#response-typing-and-the-model-registry)); where a top-level class lists `data` as its first field, that field is the wrapper: if `json["data"]` is a String, `fromJson` decodes it with `jsonDecode`, otherwise the map itself is read.

### A5190RfidCardModel

Answer of `get_device_cards`.

`fromJson` `a5190_rfid_card_model.dart @0x45b2128`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `data` | `String` (wrapper, decoded as described above) | yes | ≤3.18.0 | `a5190_rfid_card_model.dart @0x45b2164` |
| `list` | `unknown` of `RfidCardModel` | yes | ≤3.18.0 | `a5190_rfid_card_model.dart @0x45b2248` |

### RfidCardModel

One RFID card in `A5190RfidCardModel.list`.

`fromJson` `a5190_rfid_card_model.dart @0x45b2400`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `card_number` | `String?` | yes | ≤3.18.0 | `a5190_rfid_card_model.dart @0x45b2420` |
| `alias_name` | `String?` | yes | ≤3.18.0 | `a5190_rfid_card_model.dart @0x45b24a8` |

### A5190SecurityLogsModel

Answer of `get_tamper_records`.

`fromJson` `a5190_security_logs_model.dart @0x45b3680`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `data` | `String` (wrapper, decoded as described above) | yes | ≤3.18.0 | `a5190_security_logs_model.dart @0x45b36bc` |
| `page_size` | `int?` | yes | ≤3.18.0 | `a5190_security_logs_model.dart @0x45b37a8` |
| `total` | `int?` | yes | ≤3.18.0 | `a5190_security_logs_model.dart @0x45b3830` |
| `page_num` | `int?` | yes | ≤3.18.0 | `a5190_security_logs_model.dart @0x45b38b8` |
| `records` | `unknown` of `Records` | yes | ≤3.18.0 | `a5190_security_logs_model.dart @0x45b3940` |

### Records

One tamper record in `A5190SecurityLogsModel.records`.

`fromJson` `a5190_security_logs_model.dart @0x45b3af8`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `content` | `String?` | yes | ≤3.18.0 | `a5190_security_logs_model.dart @0x45b3b18` |
| `create_time` | `int?` | yes | ≤3.18.0 | `a5190_security_logs_model.dart @0x45b3ba0` |

### EvChargerSiteInfoModel

Answer of `get_site_detail_by_sn` as parsed by the EV charger load-balancing screens.

`fromJson` `ev_charger_site_info_model.dart @0x45b0374`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `data` | `String` (wrapper, decoded as described above) | yes | ≤3.18.0 | `ev_charger_site_info_model.dart @0x45b03a0` |
| `site_info` | `SiteInfo?` | yes | ≤3.18.0 | `ev_charger_site_info_model.dart @0x45b0498` |

### SiteInfo

The site in `EvChargerSiteInfoModel.site_info`.

`fromJson` `ev_charger_site_info_model.dart @0x45b052c`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `site_id` | `String` | yes | ≤3.18.0 | `ev_charger_site_info_model.dart @0x45b0558` |
| `site_name` | `String` | yes | ≤3.18.0 | `ev_charger_site_info_model.dart @0x45b05d0` |
| `site_img` | `String` | yes | ≤3.18.0 | `ev_charger_site_info_model.dart @0x45b0648` |
| `device_type_list` | `List<int>` | no | ≤3.18.0 | `ev_charger_site_info_model.dart @0x45b06c0` |
| `ms_type` | `int` | yes | ≤3.18.0 | `ev_charger_site_info_model.dart @0x45b07d0` |
| `power_site_type` | `int` | yes | ≤3.18.0 | `ev_charger_site_info_model.dart @0x45b0844` |
| `is_allow_delete` | `bool` | yes | ≤3.18.0 | `ev_charger_site_info_model.dart @0x45b08b8` |
| `support_device_models` | `List<String>` | no | ≤3.18.0 | `ev_charger_site_info_model.dart @0x45b092c` |
| `current_site_device_models` | `List<String>` | no | ≤3.18.0 | `ev_charger_site_info_model.dart @0x45b0a3c` |
| `site_device_list` | `List<SiteDevice>` of `SiteDevice` | no | ≤3.18.0 | `ev_charger_site_info_model.dart @0x45b0b48` |

### SiteDevice

One device of the site in `SiteInfo.site_device_list`.

`fromJson` `ev_charger_site_info_model.dart @0x45b0d50`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `user_id` | `String` | yes | ≤3.18.0 | `ev_charger_site_info_model.dart @0x45b0d7c` |
| `site_id` | `String` | yes | ≤3.18.0 | `ev_charger_site_info_model.dart @0x45b0df4` |
| `device_model` | `String` | yes | ≤3.18.0 | `ev_charger_site_info_model.dart @0x45b0e6c` |
| `device_sn` | `String` | yes | ≤3.18.0 | `ev_charger_site_info_model.dart @0x45b0ee4` |
| `status` | `int` | yes | ≤3.18.0 | `ev_charger_site_info_model.dart @0x45b0f5c` |
| `device_type` | `int` | yes | ≤3.18.0 | `ev_charger_site_info_model.dart @0x45b0fd0` |
| `feature` | `DeviceFeature?` | yes | ≤3.18.0 | `ev_charger_site_info_model.dart @0x45b1040` |

### DeviceFeature

Feature relation of a site device.

`fromJson` `ev_charger_site_info_model.dart @0x45b1134`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `rel_type` | `int` | yes | ≤3.18.0 | `ev_charger_site_info_model.dart @0x45b1160` |
| `rel_bizs` | `String` | yes | ≤3.18.0 | `ev_charger_site_info_model.dart @0x45b11d0` |

### GroupDeviceModel

Answer of `get_group_devices`; also the request shape the app builds for the other group endpoints (`toJson`).

`fromJson` `group_device_model.dart @0x45b4ef0`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `data` | `String` (wrapper, decoded as described above) | yes | ≤3.18.0 | `group_device_model.dart @0x45b4f2c` |
| `device_sn` | `String?` | yes | ≤3.18.0 | `group_device_model.dart @0x45b5018` |
| `device_pn` | `String?` | yes | ≤3.18.0 | `group_device_model.dart @0x45b50a0` |
| `sub_device_list` | `unknown` of `SubDeviceModel` | yes | ≤3.18.0 | `group_device_model.dart @0x45b5128` |

### SubDeviceModel

One sub-device of a group (`sub_sn`, `sub_pn`, `rel_bizs`).

`fromJson` `group_device_model.dart @0x45b52fc`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `sub_sn` | `String?` | yes | ≤3.18.0 | `group_device_model.dart @0x45b5328` |
| `sub_pn` | `String?` | yes | ≤3.18.0 | `group_device_model.dart @0x45b5388` |
| `rel_bizs` | `List?` | yes | ≤3.18.0 | `group_device_model.dart @0x45b53e4` |

### OcppListModel

Answer of `get_ocpp_endpoint_list`.

`fromJson` `ocpp_list_model.dart @0x284a6a8`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `list` | `List?` of `OcppItemModel` | yes | ≤3.18.0 | `ocpp_list_model.dart @0x284a6d0` |

### OcppItemModel

One OCPP endpoint in `OcppListModel.list`.

`fromJson` `ocpp_list_model.dart @0x284a9b4`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `id` | `int` | yes | ≤3.18.0 | `ocpp_list_model.dart @0x284a9e0` |
| `name` | `String` | yes | ≤3.18.0 | `ocpp_list_model.dart @0x284aa54` |
| `address` | `String` | yes | ≤3.18.0 | `ocpp_list_model.dart @0x284aac8` |
| `certificate` | `String` | yes | ≤3.18.0 | `ocpp_list_model.dart @0x284ab3c` |
| `icon` | `String` | yes | ≤3.18.0 | `ocpp_list_model.dart @0x284abb4` |
| `source` | `unknown` | yes | ≤3.18.0 | `ocpp_list_model.dart @0x284ac28` |

### OCPPServerLinkInfoModel

Answer of `get_ocpp_info`.

`fromJson` `ocpp_server_link_info_model.dart @0x284aec0`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `data` | `String` (wrapper, decoded as described above) | yes | ≤3.18.0 | `ocpp_server_link_info_model.dart @0x284aee0` |
| `source` | `int?` | yes | ≤3.18.0 | `ocpp_server_link_info_model.dart @0x284afcc` |
| `timestamp` | `int?` | yes | ≤3.18.0 | `ocpp_server_link_info_model.dart @0x284b050` |
| `time_zone` | `String?` | yes | ≤3.18.0 | `ocpp_server_link_info_model.dart @0x284b0d8` |

## Produced by

- [`get_device_cards`](../api/power_service/rfid/get_device_cards.md): `A5190RfidCardModel`
- [`get_tamper_records`](../api/power_service/device/get_tamper_records.md): `A5190SecurityLogsModel`
- [`get_site_detail_by_sn`](../api/power_service/site/get_site_detail_by_sn.md): `EvChargerSiteInfoModel`
- [`get_group_devices`](../api/power_service/app/group/get_group_devices.md): `GroupDeviceModel`; its `toJson` and `SubDeviceModel.toJson` build the bodies of the other group endpoints
- [`get_ocpp_endpoint_list`](../api/power_service/app/get_ocpp_endpoint_list.md): `OcppListModel`
- [`get_ocpp_info`](../api/power_service/app/get_ocpp_info.md): `OCPPServerLinkInfoModel`

## Consumed by

The EV charger settings screens (RFID cards, security logs, load balancing, OCPP) and the add-devices page of the station settings; see "Callers in app" of the endpoint pages. Field-level use is not traced.

## Changed since 3.18.0

All classes are present in 3.18.0 (`since` column); no key is new in 3.24.3 and the tool reports no removed keys.

## Known unknowns

- `rel_bizs` is typed `String` in `DeviceFeature` but `List` in `SubDeviceModel`; the senders send a list of strings (`["greenpro","elb"]`, see `set_device_feature`).
- `OcppItemModel.source` and the Dart type of `OcppListModel.list` are `unknown`/`List?` for the extractor; the element class `OcppItemModel` is inferred from the type argument.
- Meaning of `rel_type`, `status`, `device_type`, `ms_type`, `power_site_type` is not decoded.
