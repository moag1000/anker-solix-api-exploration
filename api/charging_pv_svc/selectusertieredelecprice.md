> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# selectUserTieredElecPrice

## Purpose

Reads the tiered electricity price (currency and price tiers) a user saved for a PV device (caller chain `HttpRequestController::selectUserTieredElecPrice`, in `data/endpoints.json`) (asm-traced).

## Upstream name

`get_device_pv_price` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /charging_pv_svc/selectUserTieredElecPrice` (asm-traced): URL string `@0x2401458`, method object `Method.post` (pool entry `pp+0xa7e0`) `@0x2401450`, in `HttpRequestControllerImpl::selectUserTieredElecPrice` (`charging/http/http_request_repository_impl.dart @0x24013a0`), sent through `HttpRequestControllerImpl::encryptionRequestHttp` (the closures are positional arguments, argument descriptor `@0x2401474` names no option) (`@0x2401478`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) One sender, one key. The map literal has the type arguments `<String, String>` (`charging/http/http_request_repository_impl.dart @0x240140c`), so the value is a string; it is stored without a guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `sn` | string | yes | `"<sn>"` | `charging/http/http_request_repository_impl.dart @0x24013f8` (value store `@0x2401408`, parameter) |

## `param_type`/`cmd`

n/a

## Response model (link)

[`CurrencyElecModel`](../../models/pricing.md#currencyelecmodel), parsed by `CurrencyElecModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x2401578` in the success closure `@0x240150c`.

## Response

(asm-traced) Top-level keys of `CurrencyElecModel` (`data/models.json`, `charging::CurrencyElecModel`): `sn` (String?), `currencyUnit` (String?), `tieredElecPrices` (list of `TieredElecPrices`, each with `from`, `to`, `price`; see [updateUserTieredElecPrice](updateusertieredelecprice.md) for the field types read from `charging/ui/page/price_setting_page/currency_elec_model.dart @0x2401bd8`).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "sn": "<sn>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure only logs `code` and `msg`). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `selectUserTieredElecPrice` @0x24013a0 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::selectUserTieredElecPrice`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Which serial number the caller passes (no direct caller outside the wrapper is listed on this page).
- Why the model page [models/pricing.md](../../models/pricing.md#currencyelecmodel) lists only `from`: that stub is owned by the model page and is not changed here.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
