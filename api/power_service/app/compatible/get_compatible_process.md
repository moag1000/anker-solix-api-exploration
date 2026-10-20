> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_compatible_process

## Purpose

Checks the force-update state of a third-party solar device attached to a solar bank (callers `A17c0homeLogic::checkSolarForceUpdate`, `A17c0settingLogic::checkSolarForceUpdate`, `ZXConfigWifiSuccessLogic::checkSolarForceUpdate`; builder `checkSolarForceUpdateState`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`compatible_process` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/compatible/get_compatible_process` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x26735ac`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x26735a4`, in `HttpRequestControllerImpl::checkSolarForceUpdateState` (`charging/http/http_request_repository_impl.dart @0x26734ec`), sent through `encryptionRequestHttp` (`@0x26735d4`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) The body is one map literal of 2 pairs (`AllocateArray`, raw `r2 = 8` at `@0x2673530`, so 4 slots) with type arguments `<String, String>` at `@0x2673560`, so every value is typed in the literal; all keys are stored unconditionally.

| field | type | required | example | source |
|---|---|---|---|---|
| `solar_sn` | string | yes | `""` | `charging/http/http_request_repository_impl.dart @0x2673538` |
| `solarbank_sn` | string | yes | `"<solarbank_sn>"` | `charging/http/http_request_repository_impl.dart @0x267354c` |

## `param_type`/`cmd`

n/a

## Response model (link)

- [`CheckSolarForceUpdateModel`](../../../../models/other.md#checksolarforceupdatemodel), parsed by `CheckSolarForceUpdateModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x26736a0`

## Response

(asm-traced) For each sender that parses a model, the keys below are the top-level keys of the model; that sender adds no wrapper fields of its own in the code read.

- `CheckSolarForceUpdateModel` top-level keys (`data/models.json`, `charging::CheckSolarForceUpdateModel`): `ota_complete_status` (int?), `process_skip_type` (int?), `solar_info` (SolarInfo?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "solar_sn": "",
  "solarbank_sn": "<solarbank_sn>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `checkSolarForceUpdateState` @0x26734ec (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::checkSolarForceUpdateState`
- `charging/ui/page/device/a17c0/a17c0home/a17c0home_logic.dart::checkSolarForceUpdate`
- `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart::checkSolarForceUpdate`
- `charging/ui/page/device/connect/zx_config_wifi_success/zx_config_wifi_succees_logic.dart::checkSolarForceUpdate`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Why the builder sends `solar_sn` as the constant empty string and what the server does with an empty value.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
