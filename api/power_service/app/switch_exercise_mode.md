> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# switch_exercise_mode

## Purpose

Switches the effective exercise mode of the A7320 oil machine: `A7320OilMachineExerciseLogic::switchExerciseModeRequest` is called when the user changes the mode and posts the new mode value.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/switch_exercise_mode` (asm-traced): URL string at `a7320_requet_api.dart @0x3a1a110`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3a1a108`, in `A7320RequestApi::switchExerciseModeRequest` (`a7320_requet_api.dart @0x3a1a01c`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is a 2-pair map literal (`<String, Object>`, `AllocateArray r2 = 8`, `@0x3a1a090`). The caller passes `ankerDevice.field_6b` (`@0x3a19fa0`); `field_6b` is the `deviceSn` getter, typed `String` in `String dyn:get:deviceSn(AnkerDevice)` at `anker_device.dart @0x22053d4`.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | key `@0x3a1a098`, value store `@0x3a1a0a8` (parameter r1) |
| `effective_mode` | int (Smi, w) | yes | | key `@0x3a1a0ac`, `lsl x2, x1, #1` `@0x3a1a0bc` (Smi-tagging the unboxed parameter), store `@0x3a1a0c0`; the caller computes the value from a compare with the pool object `Instance_EffectiveMode` (`csetm`, `and #0xfffffffffffffffe`, `add #4`, `@0x3a19fb8`..`@0x3a19fc0`, then `LoadInt32Instr` `@0x3a19fc4`): tagged 2 (value 1) when equal, tagged 4 (value 2) otherwise |

## `param_type`/`cmd`

n/a

## Response model (link)

None: the response body is not parsed by the app. The success callback `a7320_oil_machine_exercise_logic.dart @0x3a1a158` loads its argument once for the log string `"switchExerciseModeRequest ---"`, then sets two Rx values and shows the `saveSuccessful` toast (`showSuccessToast`). The failure callback is the shared `commonOK` dialog closure (`@0x2ad6164`).

## Response

No response key is read by the app.

## Example request/response

Request, synthesized (types only, decrypted body as built by `switchExerciseModeRequest`)

```json
{"device_sn": "<device_sn>", "effective_mode": "<effective_mode>"}
```

Response: none parsed.

## Errors seen

None traced. The failure callback is the shared `commonOK` dialog closure (`a7320_run_out_of_gasoline_logic.dart @0x2ad6164`); no code is compared. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart`: `switchExerciseModeRequest` @0x3a1a01c (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- Which mode the values 1 and 2 of `effective_mode` stand for: the app derives them from a compare with the pool object `Instance_EffectiveMode`, whose class was not decoded.
- The response body: not read by the app, so its keys are unknown.
- What the server does when the mode equals the current mode: not derivable from the app.

## Device-tested by

none
