> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_area_by_code

## Purpose

Looks up the supported price areas for a dynamic-price provider group (caller `ElectricityPriceProviderLogic::fetchAreaByCode`) (string-only: inferred from the function and class names; the call itself is asm-traced).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_dynamic_price_svc/get_area_by_code` (asm-traced): in `ElectricityPriceProviderLogic::fetchAreaByCode` (`electricity_price/components/dynamic_price/setting/electricity_price_provider_logic.dart @0x41e44e4`) the URL comes from the static field `getAreaByCode` (`LoadStaticField(0xae4)` `@0x41e4728`, initializer `Api.getAreaByCode`), the method object `Method.post` (pool entry `pp+0xa7e0`) is loaded at `@0x41e477c`, and the request goes through `HttpServiceImpl::encryptionRequestHttp` (`@0x41e47a8`).

The URL is chosen at run time by `Api.getAreaByCode` (`base_service/api_url.dart @0x41e4a70`): it loads the static flag at field offset `0xad8` (`@0x41e4a70`, `tbnz` on the Dart false bit) and returns `/charging_hes_dynamic_price_svc/get_area_by_code` when the flag is false (`@0x41e4a88`) and `/charging_hes_installer_svc/get_area_by_code` when it is true (`@0x41e4a7c`). The result is cached in the late static field at offset `0xae4`, which the senders read.

The installer variant is documented under `charging_hes_installer_svc`.

## Encrypted?

encrypted: `true` (asm-traced: the sender read reaches `encryptionRequestHttp`, `electricity_price/components/dynamic_price/setting/electricity_price_provider_logic.dart @0x41e47a8`). Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(string-only: the three field types are not read) One sender builds a `<String, dynamic>` literal (`electricity_price/components/dynamic_price/setting/electricity_price_provider_logic.dart @0x41e45d0`), which names no value type; the first key is in the literal, the other two are added behind a guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `code` | ? | yes | `"<code>"` | `electricity_price/components/dynamic_price/setting/electricity_price_provider_logic.dart @0x41e45c0` (value stored in the literal, array `@0x41e45bc`) |
| `sn` | ? | optional | `"<sn>"` | `electricity_price/components/dynamic_price/setting/electricity_price_provider_logic.dart @0x41e463c` (guard: a dispatch-table call result tested `tbnz` `@0x41e4614`, length test `cbz` `@0x41e4628`) |
| `siteId` | ? | yes | `"<site_id>"` | `electricity_price/components/dynamic_price/setting/electricity_price_provider_logic.dart @0x41e4670` (value `LoadField` `@0x41e465c`) |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed as a model: the success closure (`electricity_price/components/dynamic_price/setting/electricity_price_provider_logic.dart @0x41e4830`) reads `groupId` (`@0x41e4874`) from the request data and filters the provider's area list (`firstWhereOrNull` `@0x41e492c`, `where` `@0x41e4974`) into a list of strings; the answer's own keys are not read here.

## Response

(string-only) No answer key is read by the closure read; the strings in the result come from a locally held provider list.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "code": "<code>",
  "sn": "<sn>",
  "siteId": "<site_id>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `base_service/api_url.dart`: `getAreaByCode` @0x41e4a70 (URL literal only, no `*Http*` call; sender `ElectricityPriceProviderLogic::fetchAreaByCode` (`electricity_price/components/dynamic_price/setting/electricity_price_provider_logic.dart @0x41e44e4`), reached through callers `ElectricityPriceProviderLogic::fetchAreaByCode` (`electricity_price/components/dynamic_price/setting/electricity_price_provider_logic.dart @0x41e44e4`); resolved from the URL literal at `base_service/api_url.dart @0x41e4a88` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. Params changed: removed `code` (`tools/out/diff_3.18.0_3.24.3.md`, string-level diff on the URL builder `Api.getAreaByCode`); in 3.24.3 the key `code` is built by the sender `fetchAreaByCode` itself (`electricity_price/components/dynamic_price/setting/electricity_price_provider_logic.dart @0x41e45c0`), so the key still exists.

## Known unknowns

- Types of `code`, `sn` and `siteId`: values loaded from fields (`electricity_price/components/dynamic_price/setting/electricity_price_provider_logic.dart @0x41e465c`, `@0x41e460c`); the literal names no value type.
- What the area list the closure builds contains and where `groupId` is read from (`electricity_price/components/dynamic_price/setting/electricity_price_provider_logic.dart @0x41e4874`): the closure works on a locally cached provider list; the answer's role was not decoded.
- What static flag `0xad8` represents (installer mode): the flag's setter was not searched.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
