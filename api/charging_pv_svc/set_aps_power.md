> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# set_aps_power

## Purpose

Sets the maximum output power (APS max power) of an A5140 device (caller `A5140HttpReposity::requestApsMaxPower`) (string-only: inferred from the function name, no caller chain is in `data/endpoints.json`).

## Upstream name

`set_device_pv_power` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /charging_pv_svc/set_aps_power` (asm-traced): URL string `@0x3ee90e0`, method object `Method.post` (pool entry `pp+0xa7e0`) `@0x3ee90d8`, in `A5140HttpReposity::requestApsMaxPower` (`charging/ui/page/device/a5140/a5140home/a5140home_http_reposity.dart @0x3ee8ffc`), sent through the mixin `encryptionRequestHttp` of `HttpRequestController` (`@0x3ee9104`; options `fail`, `success`, descriptor `@0x3ee90fc`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(string-only: one field type is not read) One sender. The map literal has the type arguments `<String, Object>` (`charging/ui/page/device/a5140/a5140home/a5140home_http_reposity.dart @0x3ee9094`), which name no value type; both keys are stored without a guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `sn` | ? | yes | `"<sn>"` | `charging/ui/page/device/a5140/a5140home/a5140home_http_reposity.dart @0x3ee9058` (value store `@0x3ee9068`, parameter) |
| `power` | int (unboxed, x) | yes | `<power>` | `charging/ui/page/device/a5140/a5140home/a5140home_http_reposity.dart @0x3ee906c` (parameter converted with `BoxInt64Instr` `@0x3ee907c`, store `@0x3ee9090`) |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed as a model: the success closure (`charging/ui/page/device/a5140/a5140home/a5140home_http_reposity.dart @0x3ee91d4`) logs `requestApsMaxPower success, data:` (`@0x3ee9208`) and forwards a value to the caller (`LoadField` `@0x3ee9234`); it reads no response key.

## Response

No response key is read by the app (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "sn": "<sn>",
  "power": "<int>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure only logs `code` and `msg`). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/device/a5140/a5140home/a5140home_http_reposity.dart`: `requestApsMaxPower` @0x3ee8ffc (encryptionRequestHttp; encrypted: true)

Call sites (grep of the asm, traced 2026-10-20): `requestApsMaxPower` is called from `A5140settingController::setMaxOutputPowerRequest` (`charging/ui/page/device/a5140/a5140setting/a5140setting_logic.dart @0x3ee8fdc`).

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Type of `sn`: wrapper parameter; the literal `<String, Object>` names no value type. — attempted 2026-10-20 (two-hop not readable: `setMaxOutputPowerRequest` (`charging/ui/page/device/a5140/a5140setting/a5140setting_logic.dart @0x3ee8fdc`) pass slots or fields of their own frames; no literal or declared type in the argument setups)
- The unit and range of `power`: the app passes an integer parameter; its callers were not found in the call index. — traced 2026-10-20: the only caller is `A5140settingController::setMaxOutputPowerRequest` (`charging/ui/page/device/a5140/a5140setting/a5140setting_logic.dart @0x3ee8fdc`); the range checks of its page were not read
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
