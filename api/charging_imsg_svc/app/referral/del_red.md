> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# del_red

## Purpose

Clears the referral red dot on the server after the user has opened the referral entry.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /charging_imsg_svc/app/referral/del_red` (asm-traced). Sender: `HttpRequestControllerImpl.delReferralRedDot` (`charging/http/http_request_repository_impl.dart @0x46ada3c`); the URL literal is loaded at `@0x46adac8` and the method is `Method.post` (pool entry `pp+0xa7e0`, `@0x46adac0`).

## Encrypted?

Yes by wrapper (asm-traced): `delReferralRedDot` calls `HttpRequestControllerImpl.encryptionRequestHttp` (`charging/http/http_request_repository_impl.dart @0x46adae8`) with named arguments only for the callbacks (`@0x46adae4`) and without `needEncryption`, so the default `true` applies ([encryption.md](../../../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time (SDK login state and a base-URL test, [encryption.md](../../../encryption.md)); asm alone does not decide it.

## Request

No body: the sender builds no parameter map.

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): the answer is not parsed.

## Response

The caller's success closure (`UserMainLogic._delReferralRedDot`, `charging/ui/page/user/main/user_main_page_logic.dart @0x46adb7c`) only logs `Del referral red dot API response success` (`@0x46adba4`) and sets an observable (`value=`, `@0x46adbd0`).

## Example request/response

Request, synthesized

```json
{}
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `HttpRequestController.delReferralRedDot` (`charging/http/http_request_repository.dart @0x46ada14`)
- `UserMainLogic._delReferralRedDot` (`charging/ui/page/user/main/user_main_page_logic.dart @0x46ad9cc`), through `HttpRequestController.delReferralRedDot`

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 object pool). 3.24.3: present (pool `pp+0xc1c18`). since: 3.24.3.

## Known unknowns

- The trigger (which tap calls `_delReferralRedDot`) was not traced beyond the caller function.

## Device-tested by

none
