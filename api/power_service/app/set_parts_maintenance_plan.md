> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# set_parts_maintenance_plan

## Purpose

Sent by `A7320HomeLogic` (`setPartsMaintenancePlanRequest`, `a7320_home_logic.dart @0x27dfd7c`) to store the maintenance plan of the parts of an A7320 device as a list of items.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/set_parts_maintenance_plan` (asm-traced): URL string at `a7320_requet_api.dart @0x27e015c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x27e0154`, in `A7320RequestApi::setPartsMaintenancePlanRequest` (`a7320_requet_api.dart @0x27dfff0`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is a 2-pair map literal (`<String, Object>`, `AllocateArray r2 = 8`, `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x27e0064`). The caller builds a growable list (`AllocateGrowableArray` `a7320_home_logic.dart @0x27dff50`) and passes `ankerDevice.field_6b` with the empty string for null (`r0 = ""` `@0x27dff98`); `field_6b` is the `deviceSn` getter, typed `String` in `String dyn:get:deviceSn(AnkerDevice)` at `anker_device.dart @0x22053d4`.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | key `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x27e0070`, value store `@0x27e0080` (parameter r1) |
| `parts_maintenance_items` | ? | yes | | key `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x27e0084`, value store `@0x27e00e8`: the result of `map()` (`@0x27e00b4`, closure `@0x27e01a4` calls `toJson()` on each element, `@0x27e01bc`) followed by a dispatch-table call (`GDT[cid_x0 + 0x506a]` `@0x27e00d0`) whose selector name Blutter does not print |

Items (asm-traced): the closure `@0x27e01a4` of the sender maps each `MaintanceItem` through `MaintanceItem::toJson` (`oe_a7320/src/oe_a7320/module/a7320_parts_maintenance_item.dart @0x27e01d4`, called from the closure at `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x27e01bc`), which writes `item_name` (`oe_a7320/src/oe_a7320/module/a7320_parts_maintenance_item.dart @0x27e0220`) and the nested object `check_frequency` (`@0x27e028c`), itself a `<String, int?>` map with `operate_item` (`@0x27e0240`) and `calendar_maintenance_frequency` (`@0x27e025c`).

## `param_type`/`cmd`

n/a

## Response model (link)

None: the response body is not parsed by the app. The success callback `a7320_home_logic.dart @0x27e0428` uses its argument only in the log string `"setPartsMaintenancePlanRequest--"`; the failure callback `@0x27e0368` logs the code and shows a `commonOK` dialog.

## Response

No response key is read by the app.

## Example request/response

Request, synthesized (decrypted body shape as built by `setPartsMaintenancePlanRequest`; the item keys come from the element class's `toJson()` and are not read here)

```json
{"device_sn": "<device_sn>", "parts_maintenance_items": ["<item toJson() maps>"]}
```

Response: none parsed.

## Errors seen

None traced. The failure callback `@0x27e0368` logs the code (`"setPartsMaintenancePlanRequest code--"`) and shows a `commonOK` dialog; no code is compared. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart`: `setPartsMaintenancePlanRequest` @0x27dfff0 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- Type of `parts_maintenance_items`: the value is `iterable.map(...)` followed by a dispatch-table call with an unnamed selector (`@0x27e00d0`); that it is a `List` (`toList`) is the expectation, not read. Header stays string-only for this reason. — traced 2026-10-20: the same unnamed selector (`GDT[cid_x0 + 0x3506a]`) follows `map()` in the other list sender of this family (`oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x3a068e0`) and in two other files of the asm, and its result is stored into a map slot (`@0x27e00e8`); Blutter prints no name for it
- The response body: not read by the app, so its keys are unknown. — reclassified: server

## Device-tested by

none
