> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# self_check_report

## Purpose

Reports the result of a system self-check to the cloud: site, device, a status, a failure code, a capability flag and the start and end time of the check.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /devicecontrol/v1/app/self_check_report` (asm-traced): URL literal `@0x2acd760` in `SelfCheckController._reportSelfCheckResult` (`flutter_charging_beginning/beginning/state_cards/self_check/self_check_controller.dart @0x2acd180`), method object `Method.post` (pool entry `pp+0xa7e0`, `@0x2acd758`).

## Encrypted?

Yes by wrapper (asm-traced): ``_reportSelfCheckResult`` calls `encryptionRequestHttp` (`flutter_charging_beginning/beginning/state_cards/self_check/self_check_controller.dart @0x2acd784`) without passing `needEncryption`, so the default `true` applies (`api/encryption.md`, [which calls are encrypted](../../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time (SDK login state and a base-URL test, [encryption.md](../../encryption.md)); asm alone does not decide it.

## Request

Map literal with seven pairs, `<String, Object>` (`r2 = 28`, i.e. 14 slots, `@0x2acd518`; map literal at `@0x2acd720`). The function first logs `self_check_report: site_id=..., device_sn=..., self_check_status=..., fail_code=..., capability=..., start_time=..., end_time=...` (`@0x2acd2a4` to `@0x2acd49c`).

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | String | yes | `"<site id>"` | `flutter_charging_beginning/beginning/state_cards/self_check/self_check_controller.dart @0x2acd528`; value is the object field at offset 0x4b (`@0x2acd538`) |
| `device_sn` | String | yes | `"<device sn>"` | `@0x2acd544`; getter on the field at offset 0x47, empty string if null (`@0x2acd58c`) |
| `self_check_status` | int | yes | `1` | `@0x2acd5c4`; computed: 1 when the state observable equals a specific `SelfCheckState` instance (`@0x2acd24c` to `@0x2acd25c`), otherwise 3 when the failure code is one of the two special codes or zero, 2 when it is non-zero (`@0x2acd264` to `@0x2acd280`); the immediates are unboxed register values (`mov x3, #1/#2/#3`), no Smi halving |
| `fail_code` | int | yes | `0` | `@0x2acd5d4`; `0` when `failureCode()` (`@0x2acd0f8`, an unboxed int) equals 20000004 (`mov x17, #0x2d04; movk x17, #0x131, lsl #16`, `@0x2acd1a8`) or 20000002 (`@0x2acd1c0`), compared with `cmp x0, x17` on the untagged value, so the numbers are real; otherwise the field at offset 0x57 (null counts as 0) when a flag field is true, else `failureCode()` (`@0x2acd1ec` to `@0x2acd230`) |
| `capability` | int | yes | `1` | `@0x2acd60c`; computed from a boolean field (offset 0x87, `@0x2acd618`) with `csetm`, `and #2`, `add #2` (`@0x2acd624` to `@0x2acd62c`): tagged Smi 2 when the boolean is true, 1 when false (raw 4 / raw 2) |
| `start_time` | int | yes | `0` | `@0x2acd634`; unboxed int from the field at offset 0x6b (`@0x2acd640`), default `0` (`@0x2acd650`), boxed at `@0x2acd668` |
| `end_time` | int | yes | `0` | `@0x2acd6a4`; same from the field at offset 0x6f (`@0x2acd6b0`, `@0x2acd6c0`, boxed `@0x2acd6d8`) |

The two special codes 20000002 and 20000004 turn into `fail_code` 0; what they stand for is not decoded.

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): no model is parsed.

## Response

No response field is read (asm-traced). The success closure (`flutter_charging_beginning/beginning/state_cards/self_check/self_check_controller.dart @0x2acd818`) logs `self_check_report success` (`@0x2acd82c`); the failure closure (`@0x2acd7a4`) logs `self_check_report fail`.

## Example request/response

Request, synthesized

```json
{ "site_id": "<site id>", "device_sn": "<device sn>", "self_check_status": 1, "fail_code": 0, "capability": 1, "start_time": 0, "end_time": 0 }
```

Response: no captured response; no field is read.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or logs it; the shared transport codes are in [encryption.md](../../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `SelfCheckController._reportSelfCheckResult` (`flutter_charging_beginning/beginning/state_cards/self_check/self_check_controller.dart @0x2acd180`), called from `selfCheck` (calls `@0x2acc4fc`, `@0x2accaa4`): the self-check card of the initial setup flow (package `flutter_charging_beginning`).

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 pool as a code-referenced URL; see the inventory row `since`). 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- The meaning of `self_check_status` 1, 2, 3, of the two special failure codes and of `capability` is not decoded; the numbers above are what the app computes.
- The unit of `start_time` and `end_time` (the fields hold integers; seconds or milliseconds) is not known.
- Server behaviour is not known.

## Device-tested by

none
