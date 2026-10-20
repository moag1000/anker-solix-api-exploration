> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# set_oil_consumption_reminder_switch

## Purpose

Switches the oil-consumption reminder of an A7320 device on or off; sent from the run-out-of-gasoline page (`A7320RunOutOfGasolineLogic::setOilConsumptionReminderNotification`) and from `A7320HomeLogic::setOilConsumptionReminderNotification`.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/set_oil_consumption_reminder_switch` (asm-traced): URL string at `a7320_requet_api.dart @0x29dc1f0`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x29dc1e8`, in `A7320RequestApi::setOilConsumptionReminderSwitchRequest` (`a7320_requet_api.dart @0x29dc0c4`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is a 2-pair map literal (`<String, Object>`, `AllocateArray r2 = 8`, `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x29dc174`). Both callers load `ankerDevice.field_6b`; `field_6b` is the `deviceSn` getter, typed `String` in `String dyn:get:deviceSn(AnkerDevice)` at `anker_device.dart @0x22053d4`.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | key `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x29dc17c`, value store `@0x29dc18c` (parameter r1; the home logic substitutes the empty string for null, `r0 = ""` `a7320_home_logic.dart @0x29dc05c`) |
| `oil_consumption_reminder_switch` | bool | yes | `true` | key `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x29dc190`, value store `@0x29dc1a0` (parameter r3); the home logic passes the literal `true` (`r3 = true` `a7320_home_logic.dart @0x29dc09c`), the run-out page forwards a bool it tests with `tbnz w2, #4` (`a7320_run_out_of_gasoline_page.dart @0x3a1e9b8`) |

## `param_type`/`cmd`

n/a

## Response model (link)

None: the response body is not parsed by the app. The run-out page success callback `a7320_run_out_of_gasoline_logic.dart @0x3a1ebc4` loads no argument, fires a `MessageEvent` and re-requests the reminder; the home logic success callback `a7320_home_logic.dart @0x29dc238` uses its argument only in the log string `"setOilConsumptionReminderNotification --data n--"` (`@0x29dc25c`, load `@0x29dc268`).

## Response

No response key is read by the app.

## Example request/response

Request, synthesized (decrypted body as built by `setOilConsumptionReminderSwitchRequest`)

```json
{"device_sn": "<device_sn>", "oil_consumption_reminder_switch": true}
```

Response: none parsed.

## Errors seen

None traced. The run-out page failure callback `a7320_run_out_of_gasoline_logic.dart @0x3a1eb78` only calls `showFailGetOilConsumptionReminderPlanDetails` (no code compared); the home logic call passes an unresolved placeholder pool entry as failure callback. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart`: `setOilConsumptionReminderSwitchRequest` @0x29dc0c4 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- The response body: not read by the app, so its keys are unknown. — reclassified: server
- What the server does when the switch is set while no reminder plan exists (the plan is set through [set_oil_consumption_reminder_plan](set_oil_consumption_reminder_plan.md)): not derivable from the app.

## Device-tested by

none
