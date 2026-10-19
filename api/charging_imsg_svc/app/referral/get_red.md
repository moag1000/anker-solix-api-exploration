> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_red

## Purpose

Reads whether the referral entry should show a red dot (new referral news); the user main page asks on opening.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /charging_imsg_svc/app/referral/get_red` (asm-traced). Sender: `HttpRequestControllerImpl.getReferralRedDot` (`charging/http/http_request_repository_impl.dart @0x34e66e4`); the URL literal is loaded at `@0x34e6770` and the method is `Method.post` (pool entry `pp+0xa7e0`, `@0x34e6768`).

## Encrypted?

Yes by wrapper (asm-traced): `getReferralRedDot` calls `HttpRequestControllerImpl.encryptionRequestHttp` (`charging/http/http_request_repository_impl.dart @0x34e6790`) with named arguments only for the callbacks (`@0x34e678c`) and without `needEncryption`, so the default `true` applies ([encryption.md](../../../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time (SDK login state and a base-URL test, [encryption.md](../../../encryption.md)); asm alone does not decide it.

## Request

No body: the sender builds no parameter map.

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): the caller reads one key.

## Response

The caller's success closure (`UserMainLogic._requestReferralRedDot`, `charging/ui/page/user/main/user_main_page_logic.dart @0x34e6824`) logs `Referral red dot API response success` and calls `_handleReferralRedDotResponse` (`@0x34e6890`), which checks that the data is a `Map<String, dynamic>` (`@0x34e6944`) and reads the key `is_red` as `bool` (`@0x34e6984`, default `false` `@0x34e69a0`).

| field | type | required | example | source |
|---|---|---|---|---|
| `is_red` | bool | no | `true` | `user_main_page_logic.dart @0x34e6984` |

## Example request/response

Request, synthesized

```json
{}
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../errors.md).

## Callers in app

- `HttpRequestController.getReferralRedDot` (`charging/http/http_request_repository.dart @0x34e66bc`)
- `UserMainLogic._requestReferralRedDot` (`charging/ui/page/user/main/user_main_page_logic.dart @0x34e6674`), through `HttpRequestController.getReferralRedDot`

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 object pool). 3.24.3: present (pool `pp+0x118fc8`). since: 3.24.3.

## Known unknowns

- The wire shape of the empty request is not shown (no map is built).
- How the red dot is cleared on the server is [del_red](del_red.md).

## Device-tested by

none
