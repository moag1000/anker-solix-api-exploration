> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# set_maintain_parts_ignore_reminders

## Purpose

Called by the A7320 maintenance detail page (`A7320MaintanceDetailLogic::setMaintainPartsIgnoreRemindersRequest`) to send the ignore-reminders value of one maintenance part together with the item id, item name and the item's `maintenance_items` count.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/set_maintain_parts_ignore_reminders` (asm-traced): URL string at `a7320_requet_api.dart @0x39ff1bc`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x39ff1b4`, in `A7320RequestApi::setMaintainPartsIgnoreRemindersRequest` (`a7320_requet_api.dart @0x39fefe8`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is a 5-pair map literal (`<String, Object>`, `AllocateArray r2 = 20` = 10 slots, `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x39ff068`). The device serial comes from the caller, which passes `ankerDevice.field_6b` (`a7320_maintance_detail_logic.dart @0x39feec4`); `field_6b` is the `deviceSn` getter, typed `String` in `String dyn:get:deviceSn(AnkerDevice)` at `anker_device.dart @0x22053d4`.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | key `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x39ff074`, value store `@0x39ff084` (parameter r1; caller read at `a7320_maintance_detail_logic.dart @0x39feec4`) |
| `item_id` | int (unboxed, x) | yes | | key `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x39ff088`, `BoxInt64Instr` `@0x39ff098`, store `@0x39ff0b0`; caller untags a Smi field (`LoadInt32Instr` `a7320_maintance_detail_logic.dart @0x39fef00`) with null default 0 (`@0x39feef8`) |
| `item_name` | string | yes | | key `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x39ff0d4`, store `@0x39ff0e8`; caller null default is the empty string (`r6 = ""` `a7320_maintance_detail_logic.dart @0x39fef30`) |
| `maintenance_items` | int (unboxed, x) | yes | | key `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x39ff10c`, `BoxInt64Instr` `@0x39ff11c`, store `@0x39ff134`; caller null default 1 (`mov x7, #1` `a7320_maintance_detail_logic.dart @0x39fef60`, 64-bit, so 1) |
| `ignore_reminders` | int (Smi, w) | yes | | key `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x39ff158`, the unboxed parameter is Smi-tagged (`lsl x1, x0, #1` `@0x39ff168`) and stored (`stur w1` `@0x39ff16c`); the caller compares the same parameter with `cmp x3, #2` (64-bit, so 2) at `a7320_maintance_detail_logic.dart @0x39fee94` only to pick the string "0" or "1" for a callback context |

## `param_type`/`cmd`

n/a

## Response model (link)

None: the response body is not parsed by the app. The success callback `a7320_maintance_detail_logic.dart @0x39ff2c4` uses its argument once, in the log string `"setMaintainPartsIgnoreRemindersRequest---"` (`@0x39ff2f8`, argument load `@0x39ff304`, `_interpolate` `@0x39ff310`), then branches on `MaintanceItemType` and calls `setCalendarExpirationReminde` (`@0x39ff378`, `@0x39ff3c8`, ...).

## Response

No response key is read by the app. The builder passes two callback closures (`postJML` closure templates in `http_request_repository_impl.dart`: `@0x2268374` and `@0x226824c`, `pp+0xaaa10`/`pp+0xaaa18`) that forward to the callbacks the caller supplied (`a7320_maintance_detail_logic.dart @0x39ff2c4` success, `@0x39ff204` failure).

## Example request/response

Request, synthesized (types only, decrypted body as built by `setMaintainPartsIgnoreRemindersRequest`)

```json
{"device_sn": "<device_sn>", "item_id": "<item_id>", "item_name": "<item_name>", "maintenance_items": "<maintenance_items>", "ignore_reminders": "<ignore_reminders>"}
```

Response: none parsed.

## Errors seen

None traced. The failure callback `a7320_maintance_detail_logic.dart @0x39ff204` logs the code (label string `"getPartsMaintenancePlanRequest code--"`, `@0x39ff230`) and shows a `commonOK` dialog (`showDialog` `@0x39ff2a4`); no code is compared. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart`: `setMaintainPartsIgnoreRemindersRequest` @0x39fefe8 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- What the server does with `ignore_reminders`: the app passes an integer through unchanged, the values it uses are not decoded here (the page-level callers `a7320_maintance_detail_page.dart @0x39fee3c` and `@0x3a01e68` supply it).
- The response body: the app does not read it, so its keys are unknown. — reclassified: server
- Whether the server rejects `item_id` values it does not know: not derivable from the app.

## Device-tested by

none
