> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# entrance_check

## Purpose

Asks whether the referral (invite-a-friend) entrance should be shown to the user; the user main page calls it to set the visibility of the referral entry.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /marketing/v1/app/referral/entrance_check` (asm-traced). Sender: `HttpRequestControllerImpl.getReferralEntranceCheck` (`charging/http/http_request_repository_impl.dart @0x2701a04`); the URL literal is loaded at `@0x2701a90` and the method is `Method.post` (pool entry `pp+0xa7e0`, `@0x2701a88`).

## Encrypted?

Yes by wrapper (asm-traced): `getReferralEntranceCheck` calls `HttpRequestControllerImpl.encryptionRequestHttp` (`charging/http/http_request_repository_impl.dart @0x2701ab0`) with named arguments only for the callbacks (`@0x2701aac`) and without `needEncryption`, so the default `true` applies ([encryption.md](../../../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time (SDK login state and a base-URL test, [encryption.md](../../../encryption.md)); asm alone does not decide it.

## Request

No body: the sender builds no parameter map.

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): the answer is a plain value.

## Response

The caller's success closure (`UserMainLogic._updateReferralEnabled`, `charging/ui/page/user/main/user_main_page_logic.dart @0x26ffe4c`) casts the data to `bool` (`@0x26ffeb4`) and stores it in an observable (`value=`, `@0x26ffec0`); the caller then calls `getReferralEntranceVisible` (`@0x2701928`) and `_showReferralDialogIfNeeded` (`@0x2701954`).

| field | type | required | example | source |
|---|---|---|---|---|
| `<data>` | bool | yes | `true` | `user_main_page_logic.dart @0x26ffeb4` (the data itself is the boolean, not a key) |

## Example request/response

Request, synthesized

```json
{}
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../errors.md).

## Callers in app

- `HttpRequestController.getReferralEntranceCheck` (`charging/http/http_request_repository.dart @0x27019dc`)
- `UserMainLogic._updateReferralEnabled` (`charging/ui/page/user/main/user_main_page_logic.dart @0x2701988`), through `HttpRequestController.getReferralEntranceCheck`

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 object pool). 3.24.3: present (pool `pp+0x11340`). since: 3.24.3.

## Known unknowns

- Whether the data is a bare boolean on the wire or a wrapped value that the SDK unwraps is not known (the Dart cast is `bool`).
- The referral program itself (reward, codes) is not part of the traced endpoints. — reclassified: server (2026-10-20: the program rules are not an app-side fact)

## Device-tested by

none
