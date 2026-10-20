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

(asm-traced) Two senders in `oe_a7320/src/oe_a7320/network/a7320_requet_api.dart`, both with a `<String, Object>` outer literal (`@0x3a022c8` and `@0x3a0691c`). `batchMaintainOilEnginePartsRequest` (`@0x3a02130`) builds `parts_maintenance_list` as a growable list `<Map<String, Object>>` (`@0x3a02284`) with one element map of 3 pairs (raw `r2 = 12` at `@0x3a021dc`, type arguments `<String, Object>` `@0x3a0224c`). `batchMaintainOilEnginePartsRequestList` (`@0x3a06800`) maps a parameter list through `map` with `<Map<String, dynamic>>` (`@0x3a068b0`, `map` call `@0x3a068c4`), so its element shape is decided by the caller.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | yes | ? | `oe_a7320/src/oe_a7320/network/a7320_requet_api.dart @0x3a021b8` (and `@0x3a06880` in the list variant) |
| `parts_maintenance_list` | list | yes | ? | `oe_a7320/src/oe_a7320/network/a7320_requet_api.dart @0x3a021cc` (and `@0x3a06894`) |
| `parts_maintenance_list[].item_id` | ? | yes | ? | `oe_a7320/src/oe_a7320/network/a7320_requet_api.dart @0x3a021e8` |
| `parts_maintenance_list[].item_name` | ? | yes | ? | `oe_a7320/src/oe_a7320/network/a7320_requet_api.dart @0x3a02210` |
| `parts_maintenance_list[].maintenance_items` | ? | yes | ? | `oe_a7320/src/oe_a7320/network/a7320_requet_api.dart @0x3a02224` |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app in the builders (asm-traced): both pass `fail`, `showLoading` and `success` closures (`r4 = const [0x1, 0x7, 0x7, 0x4, fail, 0x6, showLoading, 0x4, success, 0x5, null]` at `oe_a7320/src/oe_a7320/network/a7320_requet_api.dart @0x3a02338`); the `success` closure is the shared forwarding closure `@0x2268374`, which calls the caller's callback with its argument (`ClosureCall` `@0x22683a8`). What the caller parses was not read.

## Response

Not read: the response object is handed to the caller of the two builders.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<?>",
  "parts_maintenance_list": [
    {
      "item_id": "<?>",
      "item_name": "<?>",
      "maintenance_items": "<?>"
    }
  ]
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart`: `batchMaintainOilEnginePartsRequest` @0x3a02130 (encryptionRequestHttp; encrypted: true); `batchMaintainOilEnginePartsRequestList` @0x3a06800 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of `device_sn`, `item_id`, `item_name` and `maintenance_items` (parameters/fields; `<String, Object>` only says non-null).
- Element shape of the list in the `...RequestList` variant (decided by the caller of `map`).
- The response: the success closure forwards it; the caller was not decoded. No UI caller is recorded in `data/endpoints.json`.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
