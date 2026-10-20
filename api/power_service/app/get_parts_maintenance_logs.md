> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_parts_maintenance_logs

## Purpose

Reads the page-wise maintenance log of A7320 generator parts for the maintenance record and detail pages (callers `A7320MaintanceRecordLogic`, `A7320MaintanceDetailLogic`; builder `A7320RequestApi::getPartsMaintenanceLogsRequest`) (asm-traced for the call sites; no entry in `data/endpoints.json` callers).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/get_parts_maintenance_logs` (asm-traced): URL string at `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x2ad611c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2ad6114`, in `A7320RequestApi::getPartsMaintenanceLogsRequest` (`oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x2ad5edc`), sent through `encryptionRequestHttp` (`@0x2ad6144`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) The body is one map literal of 6 pairs (`AllocateArray`, raw `r2 = 24` at `@0x2ad5f5c`, so 12 slots) with type arguments `<String, Object>` at `@0x2ad60d0`, so every value is typed in the literal; all keys are stored unconditionally. The `cmp w0, NULL` at `@0x2ad5f50` tests the `HttpService` lookup, not a field. `page_size` is the constant raw 20 stored by a 32-bit store (`@0x2ad60c8`), so 10.

| field | type | required | example | source |
|---|---|---|---|---|
| `item_id` | int (unboxed, x) | yes | | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x2ad5f68` |
| `item_name` | string | yes | | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x2ad5fb4` |
| `maintenance_items` | int (unboxed, x) | yes | | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x2ad5fec` |
| `device_sn` | ? | yes | ? | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x2ad6038` |
| `page` | int (unboxed, x) | yes | | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x2ad6070` |
| `page_size` | int (Smi, w) | yes | `10` | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x2ad60bc` |

Typing (asm-traced, `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart`): the builder takes six untyped parameters (`SetupParameters(dynamic _ ...)` `@0x2ad5ee8`): `device_sn` is the first (`fp-0x8`, `@0x2ad6048`), `item_id` the third (`fp-0x18`) stored through `BoxInt64Instr` (`@0x2ad5f78`), `item_name` the fifth (`fp-0x20`, `@0x2ad5fc4`), `maintenance_items` the sixth (`fp-0x28`, `BoxInt64Instr` `@0x2ad5ffc`) and `page` the seventh (`fp-0x30`, `BoxInt64Instr` `@0x2ad6080`), so `item_id`, `maintenance_items` and `page` are unboxed 64-bit integers. `item_name` is typed at the caller `A7320MaintanceRecordLogic.getPartsMaintenanceLogsRequest` (`oe_a7320/src/oe_a7320/page/home/setting/maintenance/a7320_maintance_record_logic.dart @0x2ad7958`), which replaces a null value by the String literal `""` (`r5 = ""` `@0x2ad78cc`). The detail-page caller `A7320MaintanceDetailLogic.getPartsMaintenanceLogsRequest` (`oe_a7320/src/oe_a7320/page/home/setting/maintenance/a7320_maintance_detail_logic.dart @0x2ad5eb4`) passes the immediate 1 for the seventh parameter (`r7 = 1` `@0x2ad5eb0`, unboxed, real 1: the first page) and an integer read with default 1 for the sixth (`r6 = 1` `@0x2ad5e50`); the record-page caller reads the sixth from a Smi field with default 1 (`r6 = 1` `@0x2ad78ec`).

## `param_type`/`cmd`

n/a

## Response model (link)

- `oe_a7320::A7320PartsMaintenanceLogsModel`, parsed by `A7320PartsMaintenanceLogsModel.fromJson` at `oe_a7320/src/oe_a7320/page/home/setting/maintenance/a7320_maintance_record_logic.dart @0x2ad7a74`. Parsed in the UI logic, not in the builder: `A7320MaintanceRecordLogic` calls the builder at `oe_a7320/src/oe_a7320/page/home/setting/maintenance/a7320_maintance_record_logic.dart @0x2ad7958` and its success closure `@0x2ad7a30` runs `A7320PartsMaintenanceLogsModel.fromJson` (`@0x2ad7a74`).

## Response

(asm-traced) For each sender that parses a model, the keys below are the top-level keys of the model; that sender adds no wrapper fields of its own in the code read.

- `A7320PartsMaintenanceLogsModel` top-level keys (`data/models.json`, `oe_a7320::A7320PartsMaintenanceLogsModel`): `device_sn` (String?), `total_times` (int?), `parts_maintenance_log_list` (unknown).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "item_id": "<int>",
  "item_name": "<string>",
  "maintenance_items": "<int>",
  "device_sn": "<?>",
  "page": "<int>",
  "page_size": 10
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `A7320MaintanceRecordLogic.getPartsMaintenanceLogsRequest` (`oe_a7320/src/oe_a7320/page/home/setting/maintenance/a7320_maintance_record_logic.dart @0x2ad7958`)
- `A7320MaintanceDetailLogic.getPartsMaintenanceLogsRequest` (`oe_a7320/src/oe_a7320/page/home/setting/maintenance/a7320_maintance_detail_logic.dart @0x2ad5eb4`)
- `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart`: `getPartsMaintenanceLogsRequest` @0x2ad5edc (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Type of `device_sn`: the first parameter of the builder (`oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x2ad6048`) — attempted 2026-10-20 (two-hop not readable: both callers read it from fields with no default and no declared type in the asm. Header stays string-only)
- Server behaviour is not known from the app: this page states what the app builds and parses.
- Which item keys each caller fills with real values: the detail caller passes page 1 and defaults of 1 for `maintenance_items`; the values of `item_id`, `item_name` and `device_sn` come from field reads (`oe_a7320/src/oe_a7320/page/home/setting/maintenance/a7320_maintance_detail_logic.dart @0x2ad5e2c`, `a7320_maintance_record_logic.dart @0x2ad78dc`) that are not decoded — traced 2026-10-20: the builder always sends all six keys

## Device-tested by

none
