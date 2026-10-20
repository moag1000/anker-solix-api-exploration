> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# batch_maintain_oil_engine_parts

## Purpose

Records a maintenance of oil-engine parts (A7320 generator) for a device in one request (`A7320RequestApi::batchMaintainOilEnginePartsRequest` and `...RequestList`); no UI caller is recorded in `data/endpoints.json`, so the purpose is inferred from the function names (string-only).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/batch_maintain_oil_engine_parts` (asm-traced): URL string at `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x3a02318`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3a02310`, in `A7320RequestApi::batchMaintainOilEnginePartsRequest` (`oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x3a02130`), sent through `encryptionRequestHttp` (`@0x3a02340`).

Same URL and method object in the other sender(s) read:

- `POST /power_service/v1/app/batch_maintain_oil_engine_parts` (asm-traced): URL string at `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x3a0696c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3a06964`, in `A7320RequestApi::batchMaintainOilEnginePartsRequestList` (`oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x3a06800`), sent through `encryptionRequestHttp` (`@0x3a06994`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) Two senders in `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart`, both with a `<String, Object>` outer literal (`@0x3a022c8` and `@0x3a0691c`). `batchMaintainOilEnginePartsRequest` (`@0x3a02130`) builds `parts_maintenance_list` as a growable list `<Map<String, Object>>` (`@0x3a02284`) with one element map of 3 pairs (raw `r2 = 12` at `@0x3a021dc`, type arguments `<String, Object>` `@0x3a0224c`). `batchMaintainOilEnginePartsRequestList` (`@0x3a06800`) maps a parameter list through `map` with `<Map<String, dynamic>>` (`@0x3a068b0`, `map` call `@0x3a068c4`), so its element shape is decided by the caller.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | yes | ? | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x3a021b8` (and `@0x3a06880` in the list variant) |
| `parts_maintenance_list` | list | yes | ? | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x3a021cc` (and `@0x3a06894`) |
| `parts_maintenance_list[].item_id` | int (unboxed, x) | yes | | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x3a021e8` |
| `parts_maintenance_list[].item_name` | string | yes | | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x3a02210` |
| `parts_maintenance_list[].maintenance_items` | int (unboxed, x) | yes | | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x3a02224` |

Typing (asm-traced): the sender `batchMaintainOilEnginePartsRequest` (`oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x3a02130`) takes five untyped parameters (`SetupParameters(dynamic _ ...)` `@0x3a0213c`). `item_id` and `maintenance_items` are stored through `BoxInt64Instr` (`@0x3a021f8` with store `@0x3a0220c`, and `@0x3a02234` with store `@0x3a02248`), so both are unboxed 64-bit integers; the caller `A7320MaintanceDetailLogic.batchMaintainOilEnginePartsRequest` (`oe_a7320/src/oe_a7320/page/home/setting/maintenance/a7320_maintance_detail_logic.dart @0x3a02108`) passes integers read with `LoadInt32Instr` from an object's Smi fields (`@0x3a02050`, `@0x3a020b8`; defaults 0 `@0x3a02048` and the raw odd immediate 1 `@0x3a020b0`, real 1 in an unboxed register). `item_name` is passed unchanged (`@0x3a0221c`); the caller supplies `field_7` of that object or the String literal `""` (`@0x3a02080`). `device_sn` is `field_6b` of the caller's logic object (`a7320_maintance_detail_logic.dart @0x3a02014`) and keeps `?`. The `...RequestList` sender (`a7320_requet_api.dart @0x3a06800`) builds `parts_maintenance_list` by `map` over a parameter list with the static closure `@0x3a069b4`, whose signature names the element class `A7320MaintenanceResetItemModel` and which only calls `toJson()` on the element (`@0x3a069cc`). `A7320MaintenanceResetItemModel::toJson` (`oe_a7320/src/oe_a7320/module/a7320_maintenance_reset_item_model.dart @0x3a06ad4` calls the body above it) writes `item_id` (`@0x3a06a30`), `item_name` (`@0x3a06a60`) and `maintenance_items` (`@0x3a06a90`) by unconditional `[]=` calls, the same three keys as the single-element sender.

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app in the builders (asm-traced): both pass `fail`, `showLoading` and `success` closures (`r4 = const [0x1, 0x7, 0x7, 0x4, fail, 0x6, showLoading, 0x4, success, 0x5, null]` at `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x3a02338`); the `success` closure is the shared forwarding closure `charging/http/http_request_repository_impl.dart @0x2268374`, which calls the caller's callback with its argument (`ClosureCall` `charging/http/http_request_repository_impl.dart @0x22683a8`). What the callers do (asm-traced): the success closure of `A7320MaintanceDetailLogic` (`oe_a7320/src/oe_a7320/page/home/setting/maintenance/a7320_maintance_detail_logic.dart @0x3a023fc`..`@0x3a0258c`) never loads its argument; the success closure of `A7320MaintanceLogic.batchMaintainOilEnginePartsRequestList` (`oe_a7320/src/oe_a7320/page/home/setting/maintenance/a7320_maintance_logic.dart @0x3a06bd0`) only interpolates it into a log string (`@0x3a06c34`, `@0x3a06c40`) before it calls `resetAllMaintainPartsValue` (`@0x3a06c74`), `getPartsMaintenancePlanRequest` (`@0x3a06c84`) and fires a `MessageEvent` (`@0x3a06cd4`).

## Response

The app does not read the response body in either caller (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<?>",
  "parts_maintenance_list": [
    {
      "item_id": "<int>",
      "item_name": "<string>",
      "maintenance_items": "<int>"
    }
  ]
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `A7320MaintanceLogic.batchMaintainOilEnginePartsRequestList` (`oe_a7320/src/oe_a7320/page/home/setting/maintenance/a7320_maintance_logic.dart @0x3a067b0`)
- `A7320MaintanceDetailLogic.batchMaintainOilEnginePartsRequest` (`oe_a7320/src/oe_a7320/page/home/setting/maintenance/a7320_maintance_detail_logic.dart @0x3a02108`)
- `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart`: `batchMaintainOilEnginePartsRequest` @0x3a02130 (encryptionRequestHttp; encrypted: true); `batchMaintainOilEnginePartsRequestList` @0x3a06800 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Server behaviour is not known from the app: this page states what the app builds and parses.
- Type of `device_sn`: `field_6b` of the caller's logic object (`oe_a7320/src/oe_a7320/page/home/setting/maintenance/a7320_maintance_detail_logic.dart @0x3a02014`) — attempted 2026-10-20 (two-hop not readable: the field declaration is not shown in the asm. Header stays string-only)

## Device-tested by

none
