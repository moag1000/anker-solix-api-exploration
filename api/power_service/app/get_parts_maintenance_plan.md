> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_parts_maintenance_plan

## Purpose

Reads the parts-maintenance plan of an A7320 generator (callers in `A7320HomeLogic`, `A7320MaintanceLogic` and `A7320MaintanceDetailLogic`; builder `A7320RequestApi::getPartsMaintenancePlanRequest`) (asm-traced for the call sites).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/get_parts_maintenance_plan` (asm-traced): URL string at `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x27df508`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x27df500`, in `A7320RequestApi::getPartsMaintenancePlanRequest` (`oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x27df3f4`), sent through `encryptionRequestHttp` (`@0x27df530`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) The body is one map literal of 1 pair (`AllocateArray`, raw `r2 = 4` at `@0x27df4a0`, so 2 slots) with type arguments `<String, String>` at `@0x27df4bc`, so every value is typed in the literal; all keys are stored unconditionally.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x27df4a8` |

## `param_type`/`cmd`

n/a

## Response model (link)

- `oe_a7320::MaintanceDetail`, parsed by `MaintanceDetail.fromJson` at `oe_a7320/src/oe_a7320/page/home/a7320_home_logic.dart @0x27df5d4`. Parsed in the UI logic, not in the builder: `A7320HomeLogic` calls the builder at `oe_a7320/src/oe_a7320/page/home/a7320_home_logic.dart @0x27df3d8` and its success closure `@0x27df550` runs `MaintanceDetail.fromJson` (`@0x27df5d4`).

## Response

(asm-traced) For each sender that parses a model, the keys below are the top-level keys of the model; that sender adds no wrapper fields of its own in the code read.

- `MaintanceDetail` top-level keys (`data/models.json`, `oe_a7320::MaintanceDetail`): `device_sn` (String?), `notice_switch` (bool), `parts_maintenance_list` (unknown).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<device_sn>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart`: `getPartsMaintenancePlanRequest` @0x27df3f4 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The success closure of `A7320RequestApi::getPartsMaintenancePlanRequest` forwards the response object to the caller; the parse is in the UI logic, named above. No server behaviour is claimed.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
