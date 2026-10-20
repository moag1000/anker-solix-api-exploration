> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# start_oil_machine_exercise

## Purpose

Reports the outcome of a manual exercise start of the A7320 oil machine: `A7320OilMachineExerciseLogic::startOilMachineExerciseRequest` is called from the device-command result handler (`a7320_oil_machine_exercise_logic.dart @0x3a17720`) with a success or failure flag and posts it with a timestamp.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/start_oil_machine_exercise` (asm-traced): URL string at `a7320_requet_api.dart @0x3a17e60`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3a17e58`, in `A7320RequestApi::startOilMachineExerciseRequest` (`a7320_requet_api.dart @0x3a17ce0`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is a 2-pair map literal (`<String, Object>`, `AllocateArray r2 = 8`, `@0x3a17d54`); the value of `manual_exercise_log` is a 3-pair map typed `<String, Object?>` (`AllocateArray r2 = 12`, `@0x3a17d84`) filled from a `ManualExerciseLog` object that the caller builds (`@0x3a17be4`). The caller passes `ankerDevice.field_6b` (`@0x3a17c84`); `field_6b` is the `deviceSn` getter, typed `String` in `String dyn:get:deviceSn(AnkerDevice)` at `anker_device.dart @0x22053d4`.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | key `@0x3a17d60`, value store `@0x3a17d70` (parameter r1) |
| `manual_exercise_log` | object | yes | | key `@0x3a17d74`, value store `@0x3a17dec` |
| `manual_exercise_log.execution_result` | bool | yes | `true` | key `@0x3a17d8c`, store `@0x3a17da4` (`ManualExerciseLog.field_f` = the flag parameter, tested with `tbnz w2, #4` `@0x3a17bd0`; the callers pass the literals `true` `@0x3a178d0` and `false` `@0x3a17a2c`) |
| `manual_exercise_log.description` | int (Smi, w) | yes | `1` | key `@0x3a17da8`, store `@0x3a17dbc` (`field_13`): `r3 = 2` (`@0x3a17bd4`, tagged, so 1) when the flag is true, otherwise the named argument `failCode` (`@0x3a17bdc`), which the caller takes from a value it untags with `LoadInt32Instr` (`@0x3a17888`) |
| `manual_exercise_log.execution_time` | int (unboxed, x) | yes | | key `@0x3a17dc0`, store `@0x3a17dd4` (`ArrayLoad r1[0]`, written by `BoxInt64Instr` of `getTimeStamp()` `@0x3a17c40`, store `@0x3a17c58`) |

## `param_type`/`cmd`

n/a

## Response model (link)

None: the response body is not parsed by the app. The success callback `a7320_oil_machine_exercise_logic.dart @0x3a17ea8` loads no argument; it calls `getDeviceExerciseDetailsReqest` and `setOilMachineAutomaticExercisePlanCommand`. The failure callback is the shared `commonOK` dialog closure (`a7320_run_out_of_gasoline_logic.dart @0x2ad6164`).

## Response

No response key is read by the app.

## Example request/response

Request, synthesized (types only, decrypted body as built by `startOilMachineExerciseRequest`)

```json
{"device_sn": "<device_sn>", "manual_exercise_log": {"execution_result": true, "description": "<description>", "execution_time": "<execution_time>"}}
```

Response: none parsed.

## Errors seen

None traced as HTTP codes. The caller of the builder compares the value returned by the device command (not an HTTP error code): `cmp x2, #1` (`@0x3a17898`, 64-bit, so 1) takes the success path and `cmp x0, #7` (`@0x3a179cc`, 64-bit, so 7) shows the text key `"a7320ExerciseAbnormalCommunication"` (`@0x3a179d4`); every other value goes to the failure path with `failCode`. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart`: `startOilMachineExerciseRequest` @0x3a17ce0 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- The unit and zero point of `execution_time` (`getTimeStamp()` is boxed as an Int64 at `@0x3a17c40`; its implementation was not followed).
- What the server stores for `description` besides 1 for success: the failure codes come from the A7320 device command result, the full set was not decoded.
- The response body: not read by the app, so its keys are unknown.

## Device-tested by

none
