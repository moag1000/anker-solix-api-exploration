> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# EV charger charging-session models

## Contents

1. [A5190ChargeSessionsModel](#a5190chargesessionsmodel)
2. [SessionsList](#sessionslist)
3. [A5190ExportChargeOrderModel](#a5190exportchargeordermodel)
4. [ChargerSessionChartModel](#chargersessionchartmodel)
5. [ChartState](#chartstate)
6. [DateList](#datelist)
7. [DateRange](#daterange)
8. [ChargerSessionOrderListModel](#chargersessionorderlistmodel)
9. [OrderList](#orderlist)
10. [A5190SessionsDetailModel](#a5190sessionsdetailmodel)
11. [ChargeVehicleInfo](#chargevehicleinfo)
12. [ChargeSocInfo](#chargesocinfo)
13. [ChargeTouInfo](#chargetouinfo)
14. [DataPoint](#datapoint)
15. [PricePoint](#pricepoint)
16. [SocPoint](#socpoint)
17. [A5190SessionsOrderSecDetail](#a5190sessionsordersecdetail)
18. [A5190SessionsOrderSecPreview](#a5190sessionsordersecpreview)
19. [PowerList](#powerlist)

## Purpose

Carries the answers of the EV charger charging-order endpoints: the order list, one order in detail with its power, SoC and price curves, the per-second power points, the statistics chart, the statistics order list and the export file name.

## Dart class + file

`A5190ChargeSessionsModel` (`ev_charger/src/ev_charger/model/a5190_charge_sessions_model.dart`); `SessionsList` (`ev_charger/src/ev_charger/model/a5190_charge_sessions_model.dart`); `A5190ExportChargeOrderModel` (`ev_charger/src/ev_charger/model/A5190_export_charge_order_Model.dart`); `ChargerSessionChartModel` (`ev_charger/src/ev_charger/page/home/charge_sessions/model/charger_session_chart_model.dart`); `ChartState` (`ev_charger/src/ev_charger/page/home/charge_sessions/model/charger_session_chart_model.dart`); `DateList` (`ev_charger/src/ev_charger/page/home/charge_sessions/model/charger_session_chart_model.dart`); `DateRange` (`ev_charger/src/ev_charger/page/home/charge_sessions/model/charger_session_chart_model.dart`); `ChargerSessionOrderListModel` (`ev_charger/src/ev_charger/page/home/charge_sessions/model/charger_session_order_list_model.dart`); `OrderList` (`ev_charger/src/ev_charger/page/home/charge_sessions/model/charger_session_order_list_model.dart`); `A5190SessionsDetailModel` (`ev_charger/src/ev_charger/model/a5190_sessions_detail_model.dart`); `ChargeVehicleInfo` (`ev_charger/src/ev_charger/model/a5190_sessions_detail_model.dart`); `ChargeSocInfo` (`ev_charger/src/ev_charger/model/a5190_sessions_detail_model.dart`); `ChargeTouInfo` (`ev_charger/src/ev_charger/model/a5190_sessions_detail_model.dart`); `DataPoint` (`ev_charger/src/ev_charger/model/a5190_sessions_detail_model.dart`); `PricePoint` (`ev_charger/src/ev_charger/model/a5190_sessions_detail_model.dart`); `SocPoint` (`ev_charger/src/ev_charger/model/a5190_sessions_detail_model.dart`); `A5190SessionsOrderSecDetail` (`ev_charger/src/ev_charger/model/a5190_sessions_order_sec_detail.dart`); `A5190SessionsOrderSecPreview` (`ev_charger/src/ev_charger/model/a5190_sessions_order_sec_preview.dart`); `PowerList` (`ev_charger/src/ev_charger/model/a5190_sessions_order_sec_preview.dart`). `fromJson` addresses are under each class below.

## Fields

Every `source` address is the string load of the JSON key inside the class `fromJson` and was re-read in the asm. Dart types and nullability come from `tools/model_fields.py` (`data/models.json`); `unknown` means the extractor could not resolve the type, and an "of `X`" note is the list element class read from the `<X>` type argument next to the key. The top-level answer classes below are registered in `AnkerJsonUtils.initAnkerModelSerializable` (`ev_charger_json_factory.internal.dart @0x45ab020`, see [../api/sdk_senders.md](../api/sdk_senders.md#response-typing-and-the-model-registry)). Where a top-level class lists `data` as its first field, that field is the wrapper: if `json["data"]` is a String, `fromJson` decodes it with `jsonDecode` and reads the keys below from the decoded map, otherwise from the map itself.

### A5190ChargeSessionsModel

Answer of `get_charging_order_list`: a page of charging orders.

`fromJson` `a5190_charge_sessions_model.dart @0x45b2b30`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `data` | `String` (wrapper, decoded as described above) | yes | ≤3.18.0 | `a5190_charge_sessions_model.dart @0x45b2b6c` |
| `page_size` | `int?` | yes | ≤3.18.0 | `a5190_charge_sessions_model.dart @0x45b2c58` |
| `list` | `unknown` of `SessionsList` | yes | ≤3.18.0 | `a5190_charge_sessions_model.dart @0x45b2ce0` |
| `total_count` | `int?` | yes | ≤3.18.0 | `a5190_charge_sessions_model.dart @0x45b2da4` |
| `page_num` | `int?` | yes | ≤3.18.0 | `a5190_charge_sessions_model.dart @0x45b2e2c` |

### SessionsList

One charging order in `A5190ChargeSessionsModel.list`.

`fromJson` `a5190_charge_sessions_model.dart @0x45b2fac`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `charge_unit` | `String?` | yes | ≤3.18.0 | `a5190_charge_sessions_model.dart @0x45b2fcc` |
| `charge_time` | `int?` | yes | ≤3.18.0 | `a5190_charge_sessions_model.dart @0x45b3054` |
| `cost` | `unknown` | ? | ≤3.18.0 | `a5190_charge_sessions_model.dart @0x45b30dc` |
| `cost_unit` | `String?` | yes | ≤3.18.0 | `a5190_charge_sessions_model.dart @0x45b3170` |
| `reason` | `List<String>` | no | ≤3.18.0 | `a5190_charge_sessions_model.dart @0x45b31f8` |
| `start_time` | `int?` | yes | ≤3.18.0 | `a5190_charge_sessions_model.dart @0x45b32d4` |
| `order_id` | `String?` | yes | ≤3.18.0 | `a5190_charge_sessions_model.dart @0x45b335c` |
| `end_time` | `int?` | yes | ≤3.18.0 | `a5190_charge_sessions_model.dart @0x45b33e4` |
| `order_status` | `int?` | yes | ≤3.18.0 | `a5190_charge_sessions_model.dart @0x45b346c` |
| `charge_total` | `unknown` | ? | ≤3.18.0 | `a5190_charge_sessions_model.dart @0x45b34f4` |
| `time_zone` | `String?` | yes | ≤3.18.0 | `a5190_charge_sessions_model.dart @0x45b3588` |

### A5190ExportChargeOrderModel

Answer of `export_charge_order`: where to download the exported file.

`fromJson` `A5190_export_charge_order_Model.dart @0x45b181c`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `data` | `String` (wrapper, decoded as described above) | yes | ≤3.18.0 | `A5190_export_charge_order_Model.dart @0x45b183c` |
| `file_url` | `String?` | yes | ≤3.18.0 | `A5190_export_charge_order_Model.dart @0x45b1928` |
| `file_name` | `String?` | yes | ≤3.18.0 | `A5190_export_charge_order_Model.dart @0x45b19b0` |

### ChargerSessionChartModel

Answer of `get_charge_order_stats`: totals and per-period buckets for the statistics chart.

`fromJson` `charger_session_chart_model.dart @0x45ae8d0`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `data` | `String` (wrapper, decoded as described above) | yes | ≤3.18.0 | `charger_session_chart_model.dart @0x45ae90c` |
| `total_stats` | `ChartState?` | yes | ≤3.18.0 | `charger_session_chart_model.dart @0x45ae9f0` |
| `date_list` | `unknown` of `DateList` | yes | ≤3.18.0 | `charger_session_chart_model.dart @0x45aea8c` |

### ChartState

Totals of one bucket (and the overall total) in `ChargerSessionChartModel`.

`fromJson` `charger_session_chart_model.dart @0x45aeb60`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `charge_unit` | `unknown` | yes | ≤3.18.0 | `charger_session_chart_model.dart @0x45aeb80` |
| `charge_time` | `num?` | yes | ≤3.18.0 | `charger_session_chart_model.dart @0x45aec04` |
| `charge_count` | `num?` | yes | ≤3.18.0 | `charger_session_chart_model.dart @0x45aec90` |
| `cost_unit` | `unknown` | yes | ≤3.18.0 | `charger_session_chart_model.dart @0x45aed1c` |
| `cost_saving` | `unknown` | yes | ≤3.18.0 | `charger_session_chart_model.dart @0x45aeda0` |
| `co2_saveing_unit` | `unknown` | yes | ≤3.18.0 | `charger_session_chart_model.dart @0x45aee24` |
| `charge_total` | `num` | no | ≤3.18.0 | `charger_session_chart_model.dart @0x45aef18` |
| `co2_saving` | `num` | no | ≤3.18.0 | `charger_session_chart_model.dart @0x45aefa0` |
| `cost` | `num` | no | ≤3.18.0 | `charger_session_chart_model.dart @0x45af028` |
| `mile_age` | `num` | no | ≤3.18.0 | `charger_session_chart_model.dart @0x45af0b0` |

### DateList

One period bucket in `ChargerSessionChartModel.date_list`.

`fromJson` `charger_session_chart_model.dart @0x45af23c`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `date_number` | `int?` | yes | ≤3.18.0 | `charger_session_chart_model.dart @0x45af25c` |
| `date_range` | `DateRange?` | yes | ≤3.18.0 | `charger_session_chart_model.dart @0x45af2e4` |
| `date_stats` | `ChartState?` | yes | ≤3.18.0 | `charger_session_chart_model.dart @0x45af380` |

### DateRange

Start and end date of one bucket.

`fromJson` `charger_session_chart_model.dart @0x45af430`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `start_date` | `String?` | yes | ≤3.18.0 | `charger_session_chart_model.dart @0x45af450` |
| `end_date` | `String?` | yes | ≤3.18.0 | `charger_session_chart_model.dart @0x45af4d8` |

### ChargerSessionOrderListModel

Answer of `get_charge_order_stats_list`: the orders of a period.

`fromJson` `charger_session_order_list_model.dart @0x45af708`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `data` | `String` (wrapper, decoded as described above) | yes | ≤3.18.0 | `charger_session_order_list_model.dart @0x45af744` |
| `page` | `int?` | yes | ≤3.18.0 | `charger_session_order_list_model.dart @0x45af830` |
| `page_size` | `int?` | yes | ≤3.18.0 | `charger_session_order_list_model.dart @0x45af8b8` |
| `total` | `int?` | yes | ≤3.18.0 | `charger_session_order_list_model.dart @0x45af940` |
| `start_use_time` | `int?` | yes | ≤3.18.0 | `charger_session_order_list_model.dart @0x45af9c8` |
| `order_list` | `unknown` of `OrderList` | yes | ≤3.18.0 | `charger_session_order_list_model.dart @0x45afa50` |

### OrderList

One order in `ChargerSessionOrderListModel.order_list`.

`fromJson` `charger_session_order_list_model.dart @0x45afc08`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `order_id` | `String?` | yes | ≤3.18.0 | `charger_session_order_list_model.dart @0x45afc28` |
| `device_sn` | `String?` | yes | ≤3.18.0 | `charger_session_order_list_model.dart @0x45afcb0` |
| `device_name` | `String?` | yes | ≤3.18.0 | `charger_session_order_list_model.dart @0x45afd38` |
| `transaction_id` | `num?` | yes | ≤3.18.0 | `charger_session_order_list_model.dart @0x45afdc0` |
| `start_time` | `int?` | yes | ≤3.18.0 | `charger_session_order_list_model.dart @0x45afe4c` |
| `end_time` | `int?` | yes | ≤3.18.0 | `charger_session_order_list_model.dart @0x45afed4` |
| `time_zone` | `String?` | yes | ≤3.18.0 | `charger_session_order_list_model.dart @0x45aff5c` |
| `order_status` | `num?` | yes | ≤3.18.0 | `charger_session_order_list_model.dart @0x45affe4` |
| `charge_unit` | `String?` | yes | ≤3.18.0 | `charger_session_order_list_model.dart @0x45b0070` |
| `charge_total` | `num?` | yes | ≤3.18.0 | `charger_session_order_list_model.dart @0x45b00f8` |
| `charge_time` | `int?` | yes | ≤3.18.0 | `charger_session_order_list_model.dart @0x45b0184` |
| `cost` | `num?` | yes | ≤3.18.0 | `charger_session_order_list_model.dart @0x45b020c` |
| `cost_unit` | `String?` | yes | ≤3.18.0 | `charger_session_order_list_model.dart @0x45b0298` |

### A5190SessionsDetailModel

Answer of `get_charging_order_detail`: one charging order with vehicle, SoC and price information and the power curve.

`fromJson` `a5190_sessions_detail_model.dart @0x36f964c`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `data` | `String` (wrapper, decoded as described above) | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36f969c` |
| `order_status` | `int?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36f97a4` |
| `charge_unit` | `String?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36f9828` |
| `end_way` | `int?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36f98ac` |
| `charge_total` | `unknown` | ? | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36f9930` |
| `reason` | `unknown` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36f99c0` |
| `start_time` | `int?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36f9a7c` |
| `cost_unit` | `String?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36f9b00` |
| `start_way` | `int?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36f9b84` |
| `end_time` | `int?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36f9c08` |
| `data_point` | `unknown` of `DataPoint` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36f9c8c` |
| `order_id` | `String?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36f9d4c` |
| `cost` | `unknown` | ? | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36f9dd0` |
| `cost_saving` | `unknown` | ? | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36f9e60` |
| `device_sn` | `String?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36f9ef0` |
| `charge_time` | `int?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36f9f74` |
| `device_name` | `String?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36f9ff8` |
| `transaction_id` | `int?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fa07c` |
| `charge_from_solar` | `unknown` | ? | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fa0f4` |
| `rfid_no` | `String?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fa130` |
| `time_zone` | `String?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fa1b4` |
| `co2_saving` | `unknown` | ? | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fa25c` |
| `co2_saving_unit` | `String?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fa298` |
| `charge_vehicle_info` | `ChargeVehicleInfo?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fa31c` |
| `charge_soc_info` | `ChargeSocInfo?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fa448` |
| `charge_tou_info` | `ChargeTouInfo?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fa4e0` |

### ChargeVehicleInfo

The vehicle assigned to an order.

`fromJson` `a5190_sessions_detail_model.dart @0x36fae88`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `id` | `String?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36faea8` |
| `vehicle_name` | `String?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36faf30` |
| `brand` | `String?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fafb8` |
| `model` | `String?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fb040` |
| `productive_year` | `int?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fb0c8` |
| `is_default_vehicle` | `bool?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fb150` |
| `is_smart_charging` | `bool?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fb1bc` |
| `is_connected_to_enodeapi` | `bool?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fb228` |
| `battery_capacity` | `num?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fb294` |
| `target_soc` | `int?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fb350` |
| `target_charge_value` | `num?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fb3d8` |

### ChargeSocInfo

State of charge at start and end of an order, with SoC points.

`fromJson` `a5190_sessions_detail_model.dart @0x36fa9c4`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `from` | `int?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36faa00` |
| `to` | `int?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36faa84` |
| `soc_points` | `unknown` of `SocPoint` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fab08` |

### ChargeTouInfo

Price unit and price points of an order.

`fromJson` `a5190_sessions_detail_model.dart @0x36fa5b8`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `unit` | `String?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fa5f4` |
| `price_points` | `unknown` of `PricePoint` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fa67c` |

### DataPoint

One power point of the order curve.

`fromJson` `a5190_sessions_detail_model.dart @0x36fb6ac`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `upload_time` | `int?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fb6cc` |
| `power_val` | `unknown` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fb754` |
| `power_unit` | `String?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fb820` |
| `is_predict` | `bool?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fb8a8` |
| `price` | `num?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fb914` |
| `price_unit` | `String?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fb9d0` |
| `charge_total` | `num?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fba58` |

### PricePoint

One price point.

`fromJson` `a5190_sessions_detail_model.dart @0x36fa834`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `timestamp` | `int?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fa854` |
| `price` | `num?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fa8dc` |

### SocPoint

One SoC point.

`fromJson` `a5190_sessions_detail_model.dart @0x36facc0`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `timestamp` | `int?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36face0` |
| `soc` | `int?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fad68` |
| `is_predict` | `bool?` | yes | ≤3.18.0 | `a5190_sessions_detail_model.dart @0x36fadf0` |

### A5190SessionsOrderSecDetail

Answer of `get_charging_order_sec_detail`: power points of one order.

`fromJson` `a5190_sessions_order_sec_detail.dart @0x45b2588`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `data` | `String` (wrapper, decoded as described above) | yes | ≤3.18.0 | `a5190_sessions_order_sec_detail.dart @0x45b25f0` |
| `order_id` | `String?` | yes | ≤3.18.0 | `a5190_sessions_order_sec_detail.dart @0x45b26dc` |
| `power_points` | `unknown` | yes | ≤3.18.0 | `a5190_sessions_order_sec_detail.dart @0x45b2764` |
| `power_unit` | `String?` | yes | ≤3.18.0 | `a5190_sessions_order_sec_detail.dart @0x45b2824` |
| `start_time` | `int?` | yes | ≤3.18.0 | `a5190_sessions_order_sec_detail.dart @0x45b28ac` |

### A5190SessionsOrderSecPreview

Answer of `get_charging_order_sec_preview`: a page of power-point blocks of one order.

`fromJson` `a5190_sessions_order_sec_preview.dart @0x45b1a90`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `data` | `String` (wrapper, decoded as described above) | yes | ≤3.18.0 | `a5190_sessions_order_sec_preview.dart @0x45b1acc` |
| `page_num` | `int?` | yes | ≤3.18.0 | `a5190_sessions_order_sec_preview.dart @0x45b1bb8` |
| `order_id` | `String?` | yes | ≤3.18.0 | `a5190_sessions_order_sec_preview.dart @0x45b1c40` |
| `list` | `unknown` of `PowerList` | yes | ≤3.18.0 | `a5190_sessions_order_sec_preview.dart @0x45b1cc8` |
| `page_size` | `int?` | yes | ≤3.18.0 | `a5190_sessions_order_sec_preview.dart @0x45b1d8c` |
| `total` | `int?` | yes | ≤3.18.0 | `a5190_sessions_order_sec_preview.dart @0x45b1e14` |

### PowerList

One block in `A5190SessionsOrderSecPreview.list`.

`fromJson` `a5190_sessions_order_sec_preview.dart @0x45b1f94`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `power_unit` | `String?` | yes | ≤3.18.0 | `a5190_sessions_order_sec_preview.dart @0x45b1fb4` |
| `start_time` | `int?` | yes | ≤3.18.0 | `a5190_sessions_order_sec_preview.dart @0x45b203c` |

## Produced by

- [`get_charging_order_list`](../api/power_service/app/order/get_charging_order_list.md): `A5190ChargeSessionsModel`
- [`export_charge_order`](../api/power_service/app/order/export_charge_order.md): `A5190ExportChargeOrderModel`
- [`get_charge_order_stats`](../api/power_service/app/order/get_charge_order_stats.md): `ChargerSessionChartModel`
- [`get_charge_order_stats_list`](../api/power_service/app/order/get_charge_order_stats_list.md): `ChargerSessionOrderListModel`
- [`get_charging_order_detail`](../api/power_service/app/order/get_charging_order_detail.md): `A5190SessionsDetailModel`
- [`get_charging_order_sec_detail`](../api/power_service/app/order/get_charging_order_sec_detail.md): `A5190SessionsOrderSecDetail`
- [`get_charging_order_sec_preview`](../api/power_service/app/order/get_charging_order_sec_preview.md): `A5190SessionsOrderSecPreview`

The model is named as the type argument of `handle<T>` at each sender (asm-traced, addresses on the endpoint pages).

## Consumed by

The EV charger app screens listed under "Callers in app" of each endpoint page (home card, charging sessions list and detail, second-level power chart, statistics chart); field-level use is not traced.

## Changed since 3.18.0

All classes are present in 3.18.0 (`data/models.json`, `since` column). Keys marked `3.24.3` in the table are new; the tool reports no removed keys.

## Known unknowns

- The Dart types `unknown` (for example `cost`, `charge_total`, `power_val`, `co2_saving`) are numbers whose exact Dart type the extractor could not resolve (int or double).
- Meaning and unit of `order_status`, `end_way`, `start_way` and `reason` are not decoded; upstream only notes that the order status values are unknown (`apitypes.py`, comment at the `get_device_charge_order_stats_list` entry).
- Whether the server wraps the answer in a `data` string (the reason for the `jsonDecode` branch) or always sends an object is not known; no capture exists.
- Time fields (`start_time`, `end_time`, `upload_time`, `timestamp`) carry no unit in the asm; the order-list request sends date strings, the second-level requests send an integer `start_time`.
