> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# set_user_site_param

## Purpose

Sets user-level site parameters in the cloud; the only traced wrapper takes the parameter map from its caller and has no caller in the asm, so what it carries is not known.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`). The matching reader is `/site/v1/get_user_site_param` (not described here).

## Method+URL

`POST /power_service/v1/set_user_site_param` (asm-traced): URL literal `@0x2886e20` in `HttpRequestControllerImpl.setUserParams` (`charging/http/http_request_repository_impl.dart @0x2886da0`), method object `Method.post` (pool entry `pp+0xa7e0`, `@0x2886e18`). Do not confuse it with the EV charger command `AKIotEVChargeCommand.setUserParams` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x405be14`), which sends `power_service/v1/app/user/set_user_params` through the SDK.

## Encrypted?

Yes by wrapper (asm-traced): ``setUserParams`` calls `encryptionRequestHttp` (`charging/http/http_request_repository_impl.dart @0x2886e48`) without passing `needEncryption`, so the default `true` applies (`api/encryption.md`, [which calls are encrypted](../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time (SDK login state and a base-URL test, [encryption.md](../encryption.md)); asm alone does not decide it. The loading overlay is off (`r30 = false`, `@0x2886e38`).

## Request

The body is the argument that `setUserParams` receives in register `r3` (stored at `@0x2886db4`, pushed for the call at `@0x2886e2c`); the other two arguments (`r2`, `r6`) become the callback closures. The function builds no keys itself. No call site of `HttpRequestControllerImpl::setUserParams` (or of an interface method that forwards to it) was found in the 3.24.3 asm, so the body is unknown.

| field | type | required | example | source |
|---|---|---|---|---|
| (caller-supplied map) | map | yes | not known | `charging/http/http_request_repository_impl.dart @0x2886da0`; no caller found |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): no model is parsed; the success and failure closures are shared static closures (`@0x2268374`, `@0x226824c`).

## Response

No response field is read (asm-traced). The two callbacks are shared closures that forward to the caller's callbacks; their bodies were not read.

## Example request/response

No example: the request body is not known.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or logs it; the shared transport codes are in [encryption.md](../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `HttpRequestControllerImpl.setUserParams` (`charging/http/http_request_repository_impl.dart @0x2886da0`): no caller found in the asm (the inventory lists no caller either). It may be reached through an interface method that Blutter shows only in the object pool.

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 pool as a code-referenced URL; see the inventory row `since`). 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- The request body keys are unknown (no caller found).
- Which user-level site parameters the endpoint stores is not known.
- Whether the app calls it at all in 3.24.3 is not established; the wrapper is present.

## Device-tested by

none
