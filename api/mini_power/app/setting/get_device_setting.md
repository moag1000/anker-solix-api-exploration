> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_device_setting

## Purpose

Reads the laboratory-function settings of an A2345 or A2687 charger when the home, charging-mode, laboratory or setting pages open (callers `getLaboratorySwitch` in the A2345 charging-model, home, laboratory and setting logic classes and in the A2687 home logic) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`charger_get_device_setting` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /mini_power/v1/app/setting/get_device_setting` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x28a7cf0`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x28a7ce8`, in `HttpRequestControllerImpl::getCustomChargeModeSetting` (`charging/http/http_request_repository_impl.dart @0x28a7c38`), sent through `encryptionRequestHttp` (`@0x28a7d18`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) `HttpRequestControllerImpl::getCustomChargeModeSetting` (`charging/http/http_request_repository_impl.dart @0x28a7c38`) stores one key, `device_sn`, unconditionally in a map literal with type arguments `<String, String>` (`@0x28a7ca4`), so the value is a String.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | `charging/http/http_request_repository_impl.dart @0x28a7c90` (map literal `<String, String>` `charging/http/http_request_repository_impl.dart @0x28a7ca4`) |

## `param_type`/`cmd`

n/a

## Response model (link)

No model class (asm-traced): the success closure (`charging/http/http_request_repository_impl.dart @0x28a7d34`) reads the key `device_setting` (`@0x28a7d68`), casts it to `Map<String, dynamic>` (`@0x28a7d8c`), reads the keys `charging_mode_status` (`@0x28a7dac`), `compatibility_status` (`@0x28a7e20`) and `charging_device_identity_status` (`@0x28a7e90`), replaces `null` by `0` for each (`cmp w0, NULL` `@0x28a7dc0`, `@0x28a7e34`, `@0x28a7ea4`), casts each to `int` (`r8 = int` `@0x28a7e00`, `@0x28a7e74`, `@0x28a7eec`) and passes a three-entry map to the callback (`ClosureCall` `@0x28a7f68`).

## Response

Top-level key read by the app: `device_setting` (object) with the integer keys `charging_mode_status`, `compatibility_status` and `charging_device_identity_status` (each `0` when absent). Other keys of the object are not read.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<device_sn>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure `charging/http/http_request_repository_impl.dart @0x226824c` forwards code and message to a stored callback without reading them). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getCustomChargeModeSetting` @0x28a7c38 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getCustomChargeModeSetting`
- `charging/ui/page/device/a2345/a2345charging_model/a2345charging_model_logic.dart::getLaboratorySwitch`
- `charging/ui/page/device/a2345/a2345home/a2345home_logic.dart::getLaboratorySwitch`
- `charging/ui/page/device/a2345/a2345laboratory/a2345laboratory_logic.dart::getLaboratorySwitch`
- `charging/ui/page/device/a2345/a2345setting/a2345setting_logic.dart::getLaboratorySwitch`
- `charging/ui/page/device/a2687/a2687home/a2687_home_logic.dart::getLaboratorySwitch`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The value domain of the three integers: the closure casts them to `int`; the pages that use them were not decoded (the matching setters are `set_charging_mode_status`, `set_compatibility_status` and `set_charging_device_identity_status`).
- Whether the object `device_setting` can be absent: the closure casts it without a null default (no null branch before the cast).
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
