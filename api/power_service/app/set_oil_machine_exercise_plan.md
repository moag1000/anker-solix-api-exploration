> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# set_oil_machine_exercise_plan

## Purpose

Sets the exercise plan (effective mode plus automatic and manual exercise intervals) of the A7320 oil machine: the oil-machine exercise page sends the user's plan (`A7320OilMachineExerciseLogic`), the restore-defaults controller sends fixed defaults.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/set_oil_machine_exercise_plan` (asm-traced) at the senders that load a `Method` object next to the URL string (pool entry `pp+0xa7e0`, `Method.post`):

- `A7320RequestApi::setOilMachineExercisePlanDefaultRequest` (`a7320_requet_api.dart @0x2ce3470`): URL string `@0x2ce3678`, method object `Method.post` (`pp+0xa7e0`) `@0x2ce3670`.
- `A7320RequestApi::setOilMachineExercisePlanRequest` (`a7320_requet_api.dart @0x29dd6ec`): URL string `@0x29dd98c`, method object `Method.post` (`pp+0xa7e0`) `@0x29dd984`.

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

Two builders send this URL. Both callers pass `ankerDevice.field_6b` as the serial; `field_6b` is the `deviceSn` getter, typed `String` in `String dyn:get:deviceSn(AnkerDevice)` at `anker_device.dart @0x22053d4`. Inner maps are added to the base map with `Map.[]=` (`GDT[cid_x0 + 0x6a9]` calls `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x29dd854`, `@0x29dd920`).

Builder `setOilMachineExercisePlanDefaultRequest` (`a7320_requet_api.dart @0x2ce3470`, caller `restore_default_a7320_controller.dart @0x2ce33f8`): a 4-pair map literal (`AllocateArray r2 = 16`, `@0x2ce34b8`), inner maps typed `<String, int>`.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | key `@0x2ce34c4`, value store `@0x2ce34d4` (caller read `@0x2ce3418`) |
| `effective_mode` | int (Smi, w) | yes | `2` | key `@0x2ce34d8`, `mov x16, #4` `@0x2ce34e4` + `stur w16` `@0x2ce34e8`, tagged, so 2 |
| `automatic_exercise` | object | yes | | key `@0x2ce34ec`; inner keys below |
| `automatic_exercise.exercise_type` | int (Smi, w) | yes | `1` | key `@0x2ce3504`, `mov x16, #2` `@0x2ce3510` + `stur w16` `@0x2ce3514`, so 1 |
| `automatic_exercise.next_automatic_exercise` | int (Smi, w) | yes | `0` | key `@0x2ce3518`, `stur wzr` `@0x2ce3524` |
| `automatic_exercise.interval_period_month` | int (Smi, w) | yes | `0` | key `@0x2ce3528`, `stur wzr` `@0x2ce3534` |
| `automatic_exercise.interval_period_week` | int (Smi, w) | yes | `0` | key `@0x2ce3538`, `stur wzr` `@0x2ce3544` |
| `manual_exercise` | object | yes | | key `@0x2ce3580`; inner keys below |
| `manual_exercise.exercise_type` | int (Smi, w) | yes | `2` | key `@0x2ce3598`, `mov x16, #4` `@0x2ce35a4` + `stur w16` `@0x2ce35a8`, so 2 |
| `manual_exercise.interval_period_month` | int (Smi, w) | yes | `1` | key `@0x2ce35ac`, `mov x16, #2` `@0x2ce35b8` + `stur w16` `@0x2ce35bc`, so 1 |
| `manual_exercise.interval_period_week` | int (Smi, w) | yes | `0` | key `@0x2ce35c0`, `stur wzr` `@0x2ce35cc` |

Builder `setOilMachineExercisePlanRequest` (`a7320_requet_api.dart @0x29dd6ec`, caller `a7320_oil_machine_exercise_logic.dart @0x3a1c644`): a 2-pair map literal (`AllocateArray r2 = 8`, `@0x29dd77c`) plus two optional inner maps typed `<String, int?>`.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | key `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x29dd784`, value store `@0x29dd794` (caller read `a7320_oil_machine_exercise_logic.dart @0x3a1c6dc`) |
| `effective_mode` | int (Smi, w) | yes | | key `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x29dd798`, `lsl x2, x1, #1` `@0x29dd7a8` (Smi-tagging the unboxed parameter), store `@0x29dd7ac`; the caller computes 1 or 2 (`csetm`/`and`/`add` then `LoadInt32Instr` `a7320_oil_machine_exercise_logic.dart @0x3a1c71c`) |
| `manual_exercise` | object | optional | | key `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x29dd84c`, added with `[]=` `@0x29dd854` only when parameter r6 is non-null (`cmp w0, NULL` `@0x29dd7c8`) |
| `manual_exercise.exercise_type` | int (Smi, w) | yes | `2` | key `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x29dd7dc`, `mov x16, #4` `@0x29dd7e8` + `stur w16` `@0x29dd7ec`, so 2 |
| `manual_exercise.interval_period_month` | int (Smi, w) or null | yes | | key `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x29dd7f0`, store `@0x29dd808` (`field_f` of the manual object; map typed `<String, int?>`) |
| `manual_exercise.interval_period_week` | int (Smi, w) or null | yes | | key `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x29dd80c`, store `@0x29dd820` (`field_13` of the manual object) |
| `automatic_exercise` | object | optional | | key `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x29dd918`, added with `[]=` `@0x29dd920` only when parameter r2 is non-null (`cmp w0, NULL` `@0x29dd864`) |
| `automatic_exercise.exercise_type` | int (Smi, w) | yes | `1` | key `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x29dd878`, `mov x16, #2` `@0x29dd884` + `stur w16` `@0x29dd888`, so 1 |
| `automatic_exercise.next_automatic_exercise` | int (Smi, w) or null | yes | | key `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x29dd88c`, store `@0x29dd8bc`; null when the automatic object's `field_7` is null (`@0x29dd8a4`..`@0x29dd8ac`) |
| `automatic_exercise.interval_period_month` | int (Smi, w) or null | yes | | key `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x29dd8c0`, store `@0x29dd8d4` |
| `automatic_exercise.interval_period_week` | int (Smi, w) or null | yes | | key `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x29dd8d8`, store `@0x29dd8ec` |

Meaning of the constants (asm-traced): The enum `EffectiveMode` (`oe_a7320/src/oe_a7320/module/a7320_oil_exercise_details.dart`, `enum EffectiveMode extends _Enum`) has two pool objects: `Obj!EffectiveMode@38fb8c1` (`pp+0x6baf0`, enum index 0, name string "automatic") and `Obj!EffectiveMode@38fb8e1` (`pp+0x6baf8`, index 1, name "manual") (`pp.txt` lines 228214 and 228220). The sender `setOilMachineExercisePlanRequest` gets `effective_mode` from a caller that loads the "manual" object `pp+0x6baf8` (`a7320_oil_machine_exercise_logic.dart @0x3a1c6f4`), compares it with the mode (`cmp w0, w16` `@0x3a1c6fc`) and builds tagged 4 (value 2) when equal and tagged 2 (value 1) otherwise (`csetm`/`and #2`/`add #2` `@0x3a1c700`..`@0x3a1c708`): 2 = `EffectiveMode.manual`, 1 = `EffectiveMode.automatic`, the same mapping as in [switch_exercise_mode](switch_exercise_mode.md#request). The defaults builder sends `effective_mode` 2 and its caller sets the restored state to the "manual" object (`restore_default_a7320_controller.dart @0x2ce3714`, `value=` `@0x2ce371c`). `exercise_type` is a property of the inner object: the literal under `automatic_exercise` carries 1 and the one under `manual_exercise` carries 2 (tables above), so 1 and 2 are the app's automatic and manual exercise kinds by the key names the app gives the objects.

## `param_type`/`cmd`

n/a

## Response model (link)

None: the response body is not parsed by the app. The restore-defaults caller's success callback `restore_default_a7320_controller.dart @0x2ce36c0` loads no argument; it only sets an Rx value to the pool constant `Instance_EffectiveMode` (`@0x2ce3714`..`@0x2ce371c`), and its failure callback is an unresolved placeholder pool entry (`pp+0x168c00`, `@0x2ce3434`, `Function: [dart:ui] _NativeScene::_NativeScene._ (0x49c1cac)`). The exercise page success callback `a7320_oil_machine_exercise_logic.dart @0x3a1c840` loads no argument; it reads `oilExerciseDetailsModel.value.manual_exercise`, stores exercise info (`setSPExerciseInfo`) and logs.

## Response

No response key is read by the app.

## Example request/response

Request, synthesized (types only, `setOilMachineExercisePlanRequest` with both inner maps)

```json
{
  "device_sn": "<device_sn>",
  "effective_mode": "<effective_mode>",
  "manual_exercise": {"exercise_type": 2, "interval_period_month": "<interval_period_month>", "interval_period_week": "<interval_period_week>"},
  "automatic_exercise": {"exercise_type": 1, "next_automatic_exercise": "<next_automatic_exercise>", "interval_period_month": "<interval_period_month>", "interval_period_week": "<interval_period_week>"}
}
```

Response: none parsed.

## Errors seen

None traced. The failure callback of the defaults sender is an unresolved placeholder pool entry (see Response model). The failure callback of the other sender, `a7320_oil_machine_exercise_logic.dart @0x3a1c780`, logs the code (`"setOilMachineManualExercisePlan --code n--"`) and shows a `commonOK` dialog; no code is compared. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart`: `setOilMachineExercisePlanDefaultRequest` @0x2ce3470 (encryptionRequestHttp; encrypted: true); `setOilMachineExercisePlanRequest` @0x29dd6ec (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- Whether the server accepts a body with only one of the two optional inner maps: the app omits a map when its parameter is null, the server reaction is not derivable.
- The response body: not read by the app, so its keys are unknown. — reclassified: server (not visible in the app: the app does not read the body)

## Device-tested by

none
