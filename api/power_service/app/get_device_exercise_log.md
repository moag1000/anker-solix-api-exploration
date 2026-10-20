> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_device_exercise_log

## Purpose

Reads the page-wise exercise (self-test run) history of an A7320 generator (caller `A7320OilHistoryRecordLogic`; builder `A7320RequestApi::getDeviceExerciseLogRequest`) (asm-traced for the call site; no entry in `data/endpoints.json` callers).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/get_device_exercise_log` (asm-traced): URL string at `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x2ad857c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2ad8574`, in `A7320RequestApi::getDeviceExerciseLogRequest` (`oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x2ad845c`), sent through `encryptionRequestHttp` (`@0x2ad85a4`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) The body is one map literal of 3 pairs (`AllocateArray`, raw `r2 = 12` at `@0x2ad84d4`, so 6 slots) with type arguments `<String, Object>` at `@0x2ad8530`, so every value is typed in the literal; all keys are stored unconditionally. The `cmp w0, NULL` at `@0x2ad84c8` tests the `HttpService` lookup, not a field. `page_size` is the constant raw 20 stored by a 32-bit store (`@0x2ad8528`), so 10.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | yes | ? | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x2ad84e0` |
| `page` | int (unboxed, x) | yes | `?` | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x2ad84f4` (value boxed by `BoxInt64Instr` `@0x2ad8504`) |
| `page_size` | int (Smi, w) | yes | `10` | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x2ad851c` |

## `param_type`/`cmd`

n/a

## Response model (link)

- `oe_a7320::A7320OilExecutionRecordModel`, parsed by `A7320OilExecutionRecordModel.fromJson` at `oe_a7320/src/oe_a7320/page/home/setting/oil_machine_exercise/a7320_oil_history_record_logic.dart @0x2ad86f4`. Parsed in the UI logic, not in the builder: `A7320OilHistoryRecordLogic` calls the builder at `oe_a7320/src/oe_a7320/page/home/setting/oil_machine_exercise/a7320_oil_history_record_logic.dart @0x2ad8448` and its success closure `@0x2ad8670` runs `A7320OilExecutionRecordModel.fromJson` (`@0x2ad86f4`).

## Response

(asm-traced) For each sender that parses a model, the keys below are the top-level keys of the model; that sender adds no wrapper fields of its own in the code read.

- `A7320OilExecutionRecordModel` top-level keys (`data/models.json`, `oe_a7320::A7320OilExecutionRecordModel`): `device_sn` (String?), `total_times` (int?), `success_times` (int?), `fail_times` (int?), `exercise_log` (unknown), `exercise_log_list` (unknown), `exercise_log` (unknown), `exercise_log_list` (unknown).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<?>",
  "page": "<?>",
  "page_size": 10
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart`: `getDeviceExerciseLogRequest` @0x2ad845c (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Type of `device_sn` (parameter; `<String, Object>` only says non-null); this is why the page stays string-only.
- Whether the server counts pages from 0 or 1 (the app passes `page` from its own state).
- No `data/endpoints.json` caller is recorded for this builder; the call site above was found by searching the A7320 logic files.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
