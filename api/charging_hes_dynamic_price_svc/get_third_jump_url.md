> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_third_jump_url

## Purpose

Asks for the URL of a third-party provider page (Flatpeak) to which the app jumps to link a tariff for a site (callers `ElectricityPlaceConfirmPageLogic::getDynamicPriceCompany`, `_DynamicPriceHttpServer::getThirdJumpUrl`) (string-only: inferred from the function names and the constant company name).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_dynamic_price_svc/get_third_jump_url` (asm-traced for the sender read): `ElectricityPlaceConfirmPageLogic::getDynamicPriceCompany` (`electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29ac204`) loads the URL from the static field `getThirdJumpUrl` (`LoadStaticField(0xae8)` `@0x29ac3c0`, initializer `Api.getThirdJumpUrl`) and calls `HttpHelper::getDataFromService` (`@0x29ac420`), which sends with `Method.post` (pool entry `pp+0xa7e0`, `electricity_price/components/electricity_price_common/http/http_helper.dart @0x27bdb94`) through `encryptionRequestHttp` (`electricity_price/components/electricity_price_common/http/http_helper.dart @0x27bdbc8`).

The URL is chosen at run time by `Api.getThirdJumpUrl` (`base_service/api_url.dart @0x29acc3c`): it loads the static flag at field offset `0xad8` (`@0x29acc3c`, `tbnz` on the Dart false bit) and returns `/charging_hes_dynamic_price_svc/get_third_jump_url` when the flag is false (`@0x29acc54`) and `/charging_hes_installer_svc/get_third_jump_url` when it is true (`@0x29acc48`). The result is cached in the late static field at offset `0xae8`, which the senders read.

A second place loads the static field: `electricity_price/components/dynamic_price/general_kit/http_server/dynamic_price_http_server.dart @0x43918c0` (`_DynamicPriceHttpServer::getThirdJumpUrl`); it was not read.

## Encrypted?

encrypted: `true` (asm-traced: the sender read reaches `encryptionRequestHttp`, `electricity_price/components/electricity_price_common/http/http_helper.dart @0x27bdbc8`). Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(string-only: two field types are not read) One sender read. Its map literal has the type arguments `<String, dynamic>` (`electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29ac278`), which name no value type; the string constants are typed from their loads.

| field | type | required | example | source |
|---|---|---|---|---|
| `pn` | ? | yes | `"<pn>"` | `electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29ac254` (value `LoadField` `@0x29ac26c`, store `@0x29ac274`) |
| `sn` | ? | optional | `"<sn>"` | `electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29ac2e4` (guard: a call result tested `tbnz` `@0x29ac2bc`, length test `cbz` `@0x29ac2d0`; store call `@0x29ac2ec`) |
| `siteId` | ? | yes | `"<site_id>"` | `electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29ac318` (value `LoadField` `@0x29ac304`, store call `@0x29ac320`) |
| `companyName` | string | yes | `"Flatpeak"` | `electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29ac340` (constant `@0x29ac348`) |
| `type` | string | yes | `"IMPORT"` or `"EXPORT"` | `electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29ac37c` (constant `"IMPORT"` `@0x29ac380`); a second store of the same key with `"EXPORT"` (`@0x29ac3a8`, `@0x29ac3ac`) |

## `param_type`/`cmd`

n/a

## Response model (link)

(string-only) not parsed in the sender read: the closures passed to `getDataFromService` were not read.

## Response

(string-only) The answer shape was not read; the function name says the answer holds a URL.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "pn": "<pn>",
  "sn": "<sn>",
  "siteId": "<site_id>",
  "companyName": "Flatpeak",
  "type": "IMPORT"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender read. Code meanings are owned by `api/errors.md`.

## Callers in app

- `base_service/api_url.dart`: `getThirdJumpUrl` @0x29acc3c (URL literal only, no `*Http*` call; sender `HttpHelper::getDataFromService` (`electricity_price/components/electricity_price_common/http/http_helper.dart @0x27bda38`) (HTTP helper wrapper), called from `ElectricityPlaceConfirmPageLogic::getDynamicPriceCompany` (`electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29ac204`); also through `_DynamicPriceHttpServer::getThirdJumpUrl`; resolved from the URL literal at `base_service/api_url.dart @0x29acc54` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. Params changed: removed `companyName`, `pn`, `siteId`, `sn`, `type` (`tools/out/diff_3.18.0_3.24.3.md`, string-level diff on the URL builder `Api.getThirdJumpUrl`). In 3.24.3 the sender read builds all five keys itself (`electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29ac254`..`@0x29ac37c`), so no key is absent.

## Known unknowns

- Types of `pn`, `sn` and `siteId`: fields of the logic object; the literal names no value type.
- Why `type` is stored twice (`"IMPORT"`, then `"EXPORT"`): the two stores sit in different branches of the sender (`@0x29ac370`, `@0x29ac39c`); which condition selects each was not decoded.
- Other companies than `"Flatpeak"`: the sender stores this constant only.
- The response keys and the jump behaviour.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
