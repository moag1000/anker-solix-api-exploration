> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# updateUserTieredElecPrice

## Purpose

Saves the tiered electricity price (currency and price tiers) a user entered for a PV device (caller chain `HttpRequestController::updateUserTieredElecPrice`, in `data/endpoints.json`) (asm-traced for the call; the meaning of the tiers is taken from the model field names, string-only).

## Upstream name

`set_device_pv_price` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /charging_pv_svc/updateUserTieredElecPrice` (asm-traced): URL string `@0x304f9f8`, method object `Method.post` (pool entry `pp+0xa7e0`) `@0x304f9f0`, in `HttpRequestControllerImpl::updateUserTieredElecPrice` (`charging/http/http_request_repository_impl.dart @0x304f960`), sent through `HttpRequestControllerImpl::encryptionRequestHttp` (`@0x304fa20`; option `showLoading`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(string-only: the tier price type is not a listed type) The wrapper builds no literal; it sends the result of `CurrencyElecModel.toJson` (`charging/http/http_request_repository_impl.dart @0x304f9b8`). `CurrencyElecModel.toJson` (`charging/ui/page/price_setting_page/currency_elec_model.dart @0x2401844`) builds a `<String, dynamic>` map (`@0x2401860`); the field types are read from the class: `CurrencyElecModel.fromJson` (`charging/ui/page/price_setting_page/currency_elec_model.dart @0x24015b8`) stores `sn` and `currencyUnit` after a `String?` type test (`@0x2401644`, `@0x24016f0`) and `tieredElecPrices` as a list of `TieredElecPrices` (`@0x2401758`, store `@0x240176c`).

| field | type | required | example | source |
|---|---|---|---|---|
| `sn` | string | yes | `"<sn>"` | `charging/ui/page/price_setting_page/currency_elec_model.dart @0x2401890` (load `@0x240187c`; declared `String?` at `@0x2401650`, store `@0x240165c`) |
| `currencyUnit` | string | yes | `"<currency>"` | `charging/ui/page/price_setting_page/currency_elec_model.dart @0x24018c0` (load `@0x24018a8`; declared `String?` at `@0x24016fc`, store `@0x2401708`) |
| `tieredElecPrices` | list | optional | `[{"from": "<from>", "to": "<to>", "price": <price>}]` | `charging/ui/page/price_setting_page/currency_elec_model.dart @0x240195c` (guard: `cmp w3, NULL` `@0x24018e4`; list type `@0x2401758`) |

Each `tieredElecPrices` element is built by `TieredElecPrices.toJson` (`charging/ui/page/price_setting_page/currency_elec_model.dart @0x24019b8`, `<String, dynamic>` `@0x24019d4`):

| field | type | required | example | source |
|---|---|---|---|---|
| `from` | string | yes | `"<from>"` | `charging/ui/page/price_setting_page/currency_elec_model.dart @0x2401a04` (load `@0x24019f0`; declared `String?` at `@0x2401c50`, store `@0x2401c5c`) |
| `to` | string | yes | `"<to>"` | `charging/ui/page/price_setting_page/currency_elec_model.dart @0x2401a30` (load `@0x2401a18`; declared `String?` at `@0x2401cd4`, store `@0x2401ce0`) |
| `price` | ? | yes | `<price>` | `charging/ui/page/price_setting_page/currency_elec_model.dart @0x2401a5c` (the boxed double field `@0x2401a44`; `fromJson` stores `double.parse` of the text `@0x2401d54`, store `@0x2401d88`) |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed as a model: the success closure (`charging/http/http_request_repository_impl.dart @0x304fab4`) logs `updateUserTieredElecPrice success, data:` (`@0x304fae8`) and calls the caller's callback; it reads no response key.

## Response

No response key is read by the app (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "sn": "<sn>",
  "currencyUnit": "<currency>",
  "tieredElecPrices": [
    {
      "from": "<from>",
      "to": "<to>",
      "price": "<price>"
    }
  ]
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure only logs `code` and `msg`). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `updateUserTieredElecPrice` @0x304f960 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::updateUserTieredElecPrice`

Call sites (grep of the asm, traced 2026-10-20): the name `updateUserTieredElecPrice` has no call site outside the interface wrapper `charging/http/http_request_repository.dart`, so no screen builds the model for this sender in 3.24.3.

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The JSON type of `price`: the field is a double in the class, and `toJson` stores the field object itself (`charging/ui/page/price_setting_page/currency_elec_model.dart @0x2401a44`); whether the encoder sends a number or text was not decoded.
- The meaning of `from` and `to` (kWh bounds or time bounds): both are strings in the class; no reader was followed.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
