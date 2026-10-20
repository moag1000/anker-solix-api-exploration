> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# set_oil_consumption_reminder_plan

## Purpose

Sets the oil-consumption reminder interval of an A7320 device: the run-out-of-gasoline page and the A7320 home logic send month and week values (`setOilConsumptionReminderPlanRequest`), and the restore-defaults controller sends fixed defaults (`setOilConsumptionReminderPlanDefaultRequest`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/set_oil_consumption_reminder_plan` (asm-traced) in every sender listed here; each sender loads the URL string and the method object (pool entry `pp+0xa7e0`, `Method.post`) in one call setup:

- `A7320RequestApi::setOilConsumptionReminderPlanDefaultRequest` (`a7320_requet_api.dart @0x2ce32b4`): URL string `@0x2ce33b0`, method object `Method.post` (`pp+0xa7e0`) `@0x2ce33a8`.
- `A7320RequestApi::setOilConsumptionReminderPlanRequest` (`a7320_requet_api.dart @0x29dbd68`): URL string `@0x29dbed8`, method object `Method.post` (`pp+0xa7e0`) `@0x29dbed0`.

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

Two builders send this URL; each body is a 3-pair map literal (`<String, Object>`, `AllocateArray r2 = 12`, `@0x2ce3324` and `@0x29dbe1c`, 6 slots). Both callers load `ankerDevice.field_6b`; `field_6b` is the `deviceSn` getter, typed `String` in `String dyn:get:deviceSn(AnkerDevice)` at `anker_device.dart @0x22053d4`.

Builder `setOilConsumptionReminderPlanDefaultRequest` (`a7320_requet_api.dart @0x2ce32b4`, caller `restore_default_a7320_controller.dart @0x2ce323c`):

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | key `@0x2ce332c`, value store `@0x2ce333c` (caller read `@0x2ce325c`) |
| `interval_period_month` | int (Smi, w) | yes | `1` | key `@0x2ce3340`, `mov x16, #2` `@0x2ce334c` + `stur w16` `@0x2ce3350`, tagged, so 1 |
| `interval_period_week` | int (Smi, w) | yes | `0` | key `@0x2ce3354`, `stur wzr` `@0x2ce3360`, Smi 0 |

Builder `setOilConsumptionReminderPlanRequest` (`a7320_requet_api.dart @0x29dbd68`, callers `a7320_run_out_of_gasoline_logic.dart @0x2ad61f0` and `a7320_home_logic.dart @0x29dbca4`):

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | key `@0x29dbe28`, value store `@0x29dbe38`; the home logic substitutes the empty string for null (`r0 = ""` `@0x29dbcfc`) |
| `interval_period_month` | int (unboxed, x) | yes | | key `@0x29dbe3c`, `BoxInt64Instr` `@0x29dbe4c`, store `@0x29dbe60`; the home logic passes the constant 1 (`r3 = 1` `@0x29dbd3c`), the run-out page boxes its own Int64 parameter (`BoxInt64Instr` `@0x2ad6234`) |
| `interval_period_week` | int (unboxed, x) | yes | | key `@0x29dbe64`, `BoxInt64Instr` `@0x29dbe74`, store `@0x29dbe88`; the home logic passes the constant 0 (`r5 = 0` `@0x29dbd40`), the run-out page boxes its own parameter (`BoxInt64Instr` `@0x2ad6250`) |

## `param_type`/`cmd`

n/a

## Response model (link)

Not determined for the defaults builder: its callers pass two pool Function objects (`restore_default_a7320_controller.dart @0x2ce3268`, pool `pp+0x168bd8`, and `@0x2ce3278`, pool `pp+0x168be0`) that Blutter prints as `Function: [dart:ui] _NativeScene::_NativeScene._ (0x49c1cac)`, a placeholder label that 790 pool entries in the asm share, so the callback code cannot be read. For the other builder the response body is not parsed: the home logic success callback `a7320_home_logic.dart @0x29dbf94` uses its argument only in the log string `"setOilConsumptionReminderIntervalPeriod --data n--"` (`@0x29dbfc8`, load `@0x29dbfd4`) and then calls `setOilConsumptionReminderNotification`; the run-out page success callback `a7320_run_out_of_gasoline_logic.dart @0x2ad62ec` loads no argument and re-requests the reminder (`getOilConsumptionReminderReqest`).

## Response

No response key is read by the app.

## Example request/response

Request, synthesized (types only, `setOilConsumptionReminderPlanRequest`)

```json
{"device_sn": "<device_sn>", "interval_period_month": 0, "interval_period_week": 0}
```

Request of the defaults builder, constants as read: month 1, week 0 (see the Request section).

## Errors seen

None traced. The failure callback of the home logic (`a7320_home_logic.dart @0x29dbf20`) logs the code (`"setOilConsumptionReminderIntervalPeriod --code n--"`) and a message; the run-out page uses the shared `commonOK` dialog closure (`@0x2ad6164`); no code is compared. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart`: `setOilConsumptionReminderPlanDefaultRequest` @0x2ce32b4 (encryptionRequestHttp; encrypted: true); `setOilConsumptionReminderPlanRequest` @0x29dbd68 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- Response handling of the defaults builder: its two callbacks are unresolved placeholder pool entries (see Response model), so whether that sender reads the body is not known. Header stays string-only for this reason.
- What the defaults builder's month 1 / week 0 mean to the server (a monthly interval is implied by the key names only): not derivable from the app.
- The accepted ranges of `interval_period_month` and `interval_period_week`: the app only passes its own parameters through.
- The response body: not read by the app, so its keys are unknown.

## Device-tested by

none
