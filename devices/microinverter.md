> Verified against: App 3.24.3 · Date: 2026-10-23 · Confidence: asm-traced · Page type: device · Owner page: this page

# Microinverter — A5140, A5141, A5143, A5150 (MI60 / MI80)

Family overview for the Anker solar microinverters. This page is a summary with links; the request, response and command facts are owned by the API and BLE pages linked below. The product is not covered by any MQTT page (see [../mqtt/README.md](../mqtt/README.md)); its only command facts are the BLE opcode lists. Method, tags and the Smi rule: [../METHODOLOGY.md](../METHODOLOGY.md).

## Contents

1. [PN, marketing name, generation/family](#pn-marketing-name-generationfamily)
2. [Features matrix](#features-matrix)
3. [Site type](#site-type)
4. [Known firmware notes](#known-firmware-notes)
5. [Known unknowns](#known-unknowns)
6. [Device-tested by](#device-tested-by)

## PN, marketing name, generation/family

Tag: untagged by design (product names). Codes and names from `product_model.dart` (owned by the BLE pages below); product codes index: [../reference/enums.md](../reference/enums.md).

| PN | marketing name | BLE profile | note |
|---|---|---|---|
| `A5140` | MI60 Microinverter | [../ble/a5140.md](../ble/a5140.md) | name-string device, not scanned by UUID |
| `A5141` | MI80 Microinverter | [../ble/a5140.md](../ble/a5140.md) | name-string device, not scanned by UUID |
| `A5143` | MI80 Microinverter (BLE) | [../ble/a5140.md](../ble/a5140.md) | the BLE-map variant of the MI80 |
| `A5150` | A5150 Module | [../ble/a5150.md](../ble/a5150.md) | carries placeholder GATT strings, no usable profile in the table |

The API endpoints below are reached by the A5140 home/chart pages, the A5150 home/solar-detail pages and the shared green-power chart page; which page calls which endpoint is recorded per endpoint in [../api/charging_pv_svc/README.md](../api/charging_pv_svc/README.md).

## Features matrix

Each cell links to the owner page; the confidence tag of each fact lives there (several endpoint pages are `string-only`, inferred from the function and class names).

| feature | API (link) | MQTT | BLE (link) | device-tested? |
|---|---|---|---|---|
| PV status / online state | [getPvStatus](../api/charging_pv_svc/getpvstatus.md) (A5140, device list), [getMiStatus](../api/charging_pv_svc/getmistatus.md) (A5150 home) | none | [a5140.md](../ble/a5140.md), [a5150.md](../ble/a5150.md) | no |
| lifetime PV totals (energy, CO2, saved money) | [getPvTotalStatistics](../api/charging_pv_svc/getpvtotalstatistics.md) (A5140) | none | — | no |
| PV generation statistics (curve, energy, money) for a period | [statisticsPv](../api/charging_pv_svc/statisticspv.md) (A5140, A5150, green-power charts) | none | — | no |
| max output power (APS max power) | [set_aps_power](../api/charging_pv_svc/set_aps_power.md) (A5140) | none | [a5140.md](../ble/a5140.md) | no |
| tiered electricity price (read / save) | [selectUserTieredElecPrice](../api/charging_pv_svc/selectusertieredelecprice.md), [updateUserTieredElecPrice](../api/charging_pv_svc/updateusertieredelecprice.md) | none | — | no |

All other features: unknown (not researched for this page yet).

## Site type

The site-type enum `AnkPowerSiteType` carries members for `a5140` and `a5143`; `a5141` and `a5150` have no member in it. The index and value of each member are owned by [../reference/enums.md](../reference/enums.md) (search `AnkPowerSiteType`). The A5150 is a module rather than a site type of its own.

## Known firmware notes

- none recorded

## Known unknowns

Tag: untagged by design (no API fact).

- Which endpoints an A5150 versus an A5140 actually answers is read from the per-page caller class (A5140… vs A5150… repositories), not from a live capture; the split is the app's, not confirmed on a device.
- The tier semantics of the tiered-price endpoints are taken from the model field names (string-only on [updateUserTieredElecPrice](../api/charging_pv_svc/updateusertieredelecprice.md)); units and currency handling need a capture.
- MI80 (A5141) has no BLE map and no site-type member; whether it is driven only over the cloud endpoints above is not confirmed.

## Device-tested by

none
