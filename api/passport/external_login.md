> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# external_login

## Purpose

A login URL the app knows by name but never sends in 3.24.3: the string is only passed to a string predicate (selector not named by Blutter) together with the URL of a failed request to decide whether the login screen must be started again after a forced logout.

## Upstream name

`none` (no upstream name): `api/apitypes.py` has no key for this URL; it is listed in the upstream comment block of known passport URLs (upstream-confirmed as a known URL name, not as a tested call).

## Method+URL

`/passport/external_login`, method unknown (string-only): URL string `pp+0x4b550` used at `charging/http/HttpEncryptionDecorator.dart @0x486ba30`, inside the closure created by `HttpEncryptionDecorator::_handler401` (closure `@0x486b958`). The string is passed to a string predicate on the failed request URL, together with `/passport/third_party_login` (`@0x486ba00`); if either matches, the closure does not call `startLoginFlow` (`@0x486ba7c`). No `*Http*` sender with this URL exists in the 3.24.3 asm (grep over all Dart files finds only this site).

## Encrypted?

Unknown: there is no sender (string-only). Reading of the inventory flag: this URL is not in `data/endpoints.json`, because the inventory only lists URL literals next to a traced sender or a URL provider function; see [../encryption.md](../encryption.md#which-calls-are-encrypted).

## Request

No request keys are known: no sender was found.

| field | type | required | example | source |
|---|---|---|---|---|
| (unknown) | | | | string-only |

## `param_type`/`cmd`

n/a

## Response model (link)

Unknown (string-only).

## Response

Unknown (string-only).

| field | type | required | example | source |
|---|---|---|---|---|
| (unknown) | | | | string-only |

## Example request/response

None: nothing to synthesize without a sender.

## Errors seen

The code catalog is [errors.md](../errors.md). None specific.

## Callers in app

None as a sender. The only reference is the exemption check in the logout-complete closure of `_handler401` (`HttpEncryptionDecorator.dart @0x486ba30`, closure `@0x486b958`); see [../encryption.md](../encryption.md#response-handling-and-error-codes).

## Since/changed

3.18.0: the string is present in the 3.18.0 object pool and in one Dart file. 3.24.3: still only that one site. since: ≤3.18.0.

## Known unknowns

- Request body, method and response: no sender; the URL may be used by native code or be a leftover. — reclassified: device test row 153 (2026-10-20: the URL string appears once in the Dart code, in the exemption check of `_handler401`, `HttpEncryptionDecorator.dart @0x486ba30`; a request to it can only come from the native SDK, which the Dart asm does not show)
- Whether it is related to the `third_party_login` flow (the app handles both names the same way in the exemption check). — traced 2026-10-20: the only code that names both URLs is the same exemption check (`HttpEncryptionDecorator.dart @0x486ba00` for `/passport/third_party_login`, `@0x486ba30` for this one); `/passport/third_party_login` has a Dart sender (`charging/http/http_request_repository_impl.dart @0x3bd1a9c`), this URL has none; whether the native login uses it is device-side — reclassified: device test row 153

## Device-tested by

none
