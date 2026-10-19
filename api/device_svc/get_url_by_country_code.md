> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_url_by_country_code

## Purpose

Returns the URL of the device shop (mall) for a country code; the user main page uses it to show the shop entry.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /device_svc/v1/get_url_by_country_code` (asm-traced). Sender: `ProfileHttpRequestControllerImpl.getShopUrlFromCountryCode` (`charging/http/user/profile/profile_http_request_repository_impl.dart @0x2988680`); the URL literal is loaded at `@0x2988750` and the method is `Method.post` (pool entry `pp+0xa7e0`, `@0x2988748`).

## Encrypted?

Yes by wrapper (asm-traced): `getShopUrlFromCountryCode` calls `HttpRequestControllerImpl.encryptionRequestHttp` (`charging/http/user/profile/profile_http_request_repository_impl.dart @0x2988780`) without passing `needEncryption`, so the default `true` applies ([encryption.md](../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time (SDK login state and a base-URL test, [encryption.md](../encryption.md)); asm alone does not decide it.

## Request

Body is a `<String, String?>` map of one pair (`r2 = 4`, `@0x29886e8`).

| field | type | required | example | source |
|---|---|---|---|---|
| `country_code` | String? | yes | `DE` | `profile_http_request_repository_impl.dart @0x29886f0`; the value is an argument of the function; the caller `UserMainLogic.requestShopLink` takes the country from `getCurrentRegion()` (`user_main_page_logic.dart @0x29885f4`) |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): no model; the caller reads one key from the answer map.

## Response

The success closure `UserMainLogic.requestShopLink` (`charging/ui/page/user/main/user_main_page_logic.dart @0x2988814`) checks that the data is a map, reads the key `url` (`@0x2988884`), stores it (default `""` when missing, `@0x29888b0`) and sends the analytics event `APP_DEVICE_MALL_ENTRY_EXPOSURE` (`@0x298891c`). The failure closure (`@0x298879c`) logs `requestShopLink failed: code=...`.

| field | type | required | example | source |
|---|---|---|---|---|
| `url` | String | no | `https://shop.example/de` | `user_main_page_logic.dart @0x2988884` |

## Example request/response

Request, synthesized

```json
{ "country_code": "DE" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../encryption.md](../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `UserMainLogic.requestShopLink` (`charging/ui/page/user/main/user_main_page_logic.dart @0x2988658`)

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 object pool). 3.24.3: present (pool `pp+0x118e40`). since: 3.24.3.

## Known unknowns

- The country code format (ISO 3166-1 alpha-2) is an assumption of the example; the app passes whatever `getCurrentRegion()` returns.
- The shop URL host and whether it varies per account region are not known.

## Device-tested by

none
