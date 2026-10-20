> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_device_last_exercise_log

## Purpose

Reads the last exercise (self-test run) log entry of an A7320 generator (caller `A7320HomeLogic`; builder `A7320RequestApi::getDeviceLastExerciseLogRequest`) (asm-traced for the call site; no entry in `data/endpoints.json` callers).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/get_device_last_exercise_log` (asm-traced): URL string at `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x29dcd68`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x29dcd60`, in `A7320RequestApi::getDeviceLastExerciseLogRequest` (`oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x29dcc7c`), sent through `encryptionRequestHttp` (`@0x29dcd90`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) The body is one map literal of 2 pairs (`AllocateArray`, raw `r2 = 8` at `@0x29dccec`, so 4 slots) with type arguments `<String, Object>` at `@0x29dcd1c`, so every value is typed in the literal; all keys are stored unconditionally. `exercise_type` is the constant raw 2 stored by a 32-bit store (`@0x29dcd18`), so 1.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x29dccf4` |
| `exercise_type` | int (Smi, w) | yes | `1` | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x29dcd08` |

Typing (two-hop, asm-traced): in `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart` the first parameter of the builder is untyped (`SetupParameters(dynamic _ ...)`); its only caller, `A7320HomeLogic.getDeviceLastExerciseLogReqest` (`oe_a7320/src/oe_a7320/page/home/a7320_home_logic.dart @0x29dcc6c`), reads `field_6b` of an object held in `field_4f` and replaces a null value by the String literal `""` (`r0 = ""` `@0x29dcc34`), so `device_sn` is a string.

## `param_type`/`cmd`

n/a

## Response model (link)

- `oe_a7320::A7320LastExerciseLogModel`, parsed by `A7320LastExerciseLogModel.fromJson` at `oe_a7320/src/oe_a7320/page/home/a7320_home_logic.dart @0x29dce60`. Parsed in the UI logic, not in the builder: `A7320HomeLogic` calls the builder at `oe_a7320/src/oe_a7320/page/home/a7320_home_logic.dart @0x29dcc6c` and its success closure `@0x29dce28` runs `A7320LastExerciseLogModel.fromJson` (`@0x29dce60`).

## Response

(asm-traced) For each sender that parses a model, the keys below are the top-level keys of the model; that sender adds no wrapper fields of its own in the code read.

- `A7320LastExerciseLogModel` top-level keys (`data/models.json`, `oe_a7320::A7320LastExerciseLogModel`): `device_sn` (String?), `effective_mode` (int?), `last_exercise_log` (ManualExerciseLog?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<device_sn>",
  "exercise_type": 1
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `A7320HomeLogic.getDeviceLastExerciseLogReqest` (`oe_a7320/src/oe_a7320/page/home/a7320_home_logic.dart @0x29dcc6c`)
- `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart`: `getDeviceLastExerciseLogRequest` @0x29dcc7c (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What other `exercise_type` values select (the builder sends the constant 1). — reclassified: server (not visible in the app: the builder sends only the constant 1)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
