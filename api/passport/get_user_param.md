> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_user_param

## Purpose

Reads the user's privacy and analytics switches at app start and on the analytics settings page; sent by `SplashLogic::requestAppSwitchApi` and `AnalyticsAndImprovementLogic::requestAppSwitchApi`, which pick entries with value `"1"` and call `saveAppAnalytics` and `saveDeviceAnalytics` (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /passport/get_user_param` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x293e86c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x293e864`, in `HttpRequestControllerImpl::getAppSwitchApi` (`charging/http/http_request_repository_impl.dart @0x293e778`), sent through `encryptionRequestHttp` (`@0x293e894`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `param_types` | list | yes | `[20000, 20001]` (two Smi elements; raw 40000 and 40002 stored with 32-bit stores, so halved) | `charging/http/http_request_repository_impl.dart @0x293e7d0` (store `@0x293e81c`, list `AllocateGrowableArray` `@0x293e800`, element type `<int>`, elements `@0x293e7f0` and `@0x293e7f8`) |

The map literal has type arguments `<String, List<int>>` (`@0x293e820`); the list length raw 4 (`@0x293e80c`, `@0x293e814`) is two elements.

## `param_type`/`cmd`

n/a

## Response model (link)

[`UserParamModel`](../../models/account.md#userparammodel), parsed by `UserParamModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x293e8e8` in the success closure `@0x293e8b0`.

## Response

(asm-traced) Top-level key of `UserParamModel` (`data/models.json`, `charging::UserParamModel`): `user_params` (type not read, an element class `UserParams` appears in the callers as `<UserParams>`, `charging/ui/page/account/splash/splash_logic.dart @0x293f020`). The callers pick elements with `firstWhereOrNull` (`charging/ui/page/account/splash/splash_logic.dart @0x293f038`) and compare a field with the string `"1"` (`@0x293f058`).

## Example request/response

Request, synthesized (decrypted body as built by the sender; no captured values)

```json
{
  "param_types": [20000, 20001]
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getAppSwitchApi` @0x293e778 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getAppSwitchApi`
- `charging/ui/page/account/splash/splash_logic.dart::requestAppSwitchApi`
- `charging/ui/page/user/about/analyticsAndImprovement/analytics_and_improvement_logic.dart::requestAppSwitchApi`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What the two `param_types` values 20000 and 20001 select on the server, and which element is the app analytics switch and which the device analytics switch: the callers pick entries with closures (`@0x293f5d4`, `@0x293f3c0`) that were not decoded.
- The element fields of `UserParams` (the name of the field compared with `"1"`): only the field offset (`field_7`) was read.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
