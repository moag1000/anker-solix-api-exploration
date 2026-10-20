> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_tou_price_plan_detail

## Purpose

Reads the time-of-use price plan (`UtilityRatePlan`) of a NEM rate template; two senders, `NemPlanEditLogic::resetNemPeakData` (called from `NemPlanEditLogic::showTipsDialog`) and `NemRateLogic::nextStep` (called from `NemRatePage::build`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_tou_price_plan_detail` (asm-traced): URL string at `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_plan_edit/nem_plan_edit_logic.dart @0x3ed5af4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3ed5aec`, in `NemPlanEditLogic::resetNemPeakData` (`charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_plan_edit/nem_plan_edit_logic.dart @0x3ed59ac`), sent through `requestHttp` (`@0x3ed5b1c`).

Same URL and method object in the other sender(s) read:

- `NemRateLogic::nextStep` (`charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_rate_logic.dart @0x29746e8`): URL string `@0x29749f4`, method object `Method.post` (`pp+0xa7e0`) at `@0x29749ec`, sent through `requestHttp` (`@0x2974a1c`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `NemPlanEditLogic::resetNemPeakData` (`charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_plan_edit/nem_plan_edit_logic.dart`, call `@0x3ed5b1c`, argument list `@0x3ed5b14`), `NemRateLogic::nextStep` (`charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_rate_logic.dart`, call `@0x2974a1c`, argument list `@0x2974a14`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

Both senders store 3 keys in a map literal with type arguments `<String, Object>` (`charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_plan_edit/nem_plan_edit_logic.dart @0x3ed5aa8`, `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_rate_logic.dart @0x29749a8`), which do not type the values. Each value is read from a field of a plan object with a fallback: `template_id` falls back to the tagged immediate 0 (`@0x3ed5a38` in the first sender), `template_name` and `customer_segment_type` fall back to the empty string (`@0x3ed5a6c`, `@0x3ed5aa0`); the fallbacks are not constants of the request, the primary value is the object field, so the types stay `?`. No key is behind a null guard of its own.

| field | type | required | example | source |
|---|---|---|---|---|
| `template_id` | ? | yes | ? | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_plan_edit/nem_plan_edit_logic.dart @0x3ed59f8`; `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_rate_logic.dart @0x29748fc` |
| `template_name` | ? | yes | ? | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_plan_edit/nem_plan_edit_logic.dart @0x3ed5a40`; `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_rate_logic.dart @0x297493c` |
| `customer_segment_type` | ? | yes | ? | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_plan_edit/nem_plan_edit_logic.dart @0x3ed5a74`; `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_rate_logic.dart @0x2974970` |

## `param_type`/`cmd`

n/a

## Response model (link)

- `charging::UtilityRatePlan`, parsed by `UtilityRatePlan.fromJson` at `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_plan_edit/nem_plan_edit_logic.dart @0x3ed5b70` (success closure `@0x3ed5b38`, `bl` target `[package:charging/model/a5101/a5101_device_command_model.dart]`).
- Also parsed by `UtilityRatePlan.fromJson` at `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_rate_logic.dart @0x2974a78` (success closure `@0x2974a40`, `bl` target `[package:charging/model/a5101/a5101_device_command_model.dart]`).

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::UtilityRatePlan`): `peak_sessions` (unknown), `nem_plan_info` (NemPlanInfo?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "template_id": "<template_id>",
  "template_name": "<template_name>",
  "customer_segment_type": "<customer_segment_type>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`. The failure closure of `NemRateLogic::nextStep` is the closure `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_rate_logic.dart @0x2974664`, which logs the code and the message (`exeInfo` `@0x29746c0`) and shows the message (`show` `@0x29746cc`) without comparing the code.

## Callers in app

- `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_plan_edit/nem_plan_edit_logic.dart`: `resetNemPeakData` @0x3ed59ac (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_rate_logic.dart`: `nextStep` @0x29746e8 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_plan_edit/nem_plan_edit_logic.dart::showTipsDialog`
- `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_rate_view.dart::build`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The types of the three keys: the values are fields of the plan object (`field_7` for `template_id` `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_plan_edit/nem_plan_edit_logic.dart @0x3ed5a28` and `field_b` for `template_name` `@0x3ed5a5c` in the first sender), fields not resolved to a class.
- Which template ids the server knows: the fallback value 0 is sent when the plan object has no id.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
