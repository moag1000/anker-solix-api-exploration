> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_phonecode_list

## Purpose

Reads the list of country phone codes for the invite-members page (caller `InviteMembersLogic::getSharePhoneCode`; builder `HttpRequestControllerImpl::sharePhoneCode`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/get_phonecode_list` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x2917d74`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2917d6c`, in `HttpRequestControllerImpl::sharePhoneCode` (`charging/http/http_request_repository_impl.dart @0x2917cf4`), sent through `encryptionRequestHttp` (`@0x2917d9c`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) No request fields: the body argument is the empty map literal (`THR::empty_array`, `Map._fromLiteral`) at `charging/http/http_request_repository_impl.dart @0x2917d34`.

## `param_type`/`cmd`

n/a

## Response model (link)

no model file in `data/models.json`: the success closure (`charging/http/http_request_repository_impl.dart @0x2917db8`) reads the key `phone_code_list` (string literal `@0x2917dec`) and builds a `SharePhoneCodeModel` per entry (`@0x2917fb0`) from the entry keys `country_code` (`@0x2917f50`) and `phone_code` (`@0x2917fc8`); the keys `isSelected` (`@0x2918050`) and `i18nCountry` (`@0x29180b8`) are read from the same entry and stored in the same model (`StoreField` `@0x2918098`..`@0x2918120`), each through the same dynamic index call and a nullable type check.

## Response

| field | type | required | example | source |
|---|---|---|---|---|
| `phone_code_list` | list of objects | optional | `[...]` | `charging/http/http_request_repository_impl.dart @0x2917dec` |
| `phone_code_list[].country_code` | string (type-checked `String?`) | optional | | `charging/http/http_request_repository_impl.dart @0x2917f50` (check `r8 = String?` `@0x2917fa0`) |
| `phone_code_list[].phone_code` | string (type-checked `String?`) | optional | | `charging/http/http_request_repository_impl.dart @0x2917fc8` (check `r8 = String?` `@0x2918018`) |
| `phone_code_list[].isSelected` | bool (type-checked `bool?`) | optional | | `charging/http/http_request_repository_impl.dart @0x2918050` (check `r8 = bool?` `@0x2918098`) |
| `phone_code_list[].i18nCountry` | string (type-checked `String?`) | optional | | `charging/http/http_request_repository_impl.dart @0x29180b8` (check `r8 = String?` `@0x2918108`) |

## Example request/response

Request, synthesized: the body is the empty object.

```json
{}
```

Response, synthesized (keys read by the success closure; values are placeholders)

```json
{
  "data": {
    "phone_code_list": [
      {
        "country_code": "<string>",
        "phone_code": "<string>",
        "isSelected": "<bool>",
        "i18nCountry": "<string>"
      }
    ]
  }
}
```

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `sharePhoneCode` @0x2917cf4 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::sharePhoneCode`
- `charging/ui/page/user/share_site/invite_members/invite_members_logic.dart::getSharePhoneCode`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
