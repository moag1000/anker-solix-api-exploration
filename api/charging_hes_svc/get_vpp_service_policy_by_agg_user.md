> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_vpp_service_policy_by_agg_user

## Purpose

Reads the VPP disclaimer (service policy) link for the user (callers `requestVppDisclaimer` in `charging/ui/page/device/a5101/setting/vpp/controller.dart` and `UserMainLogic::requestVppDisclaimer`, through `HttpRequestControllerImpl::getVppDisclaimer`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_vpp_service_policy_by_agg_user` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x2979b78`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2979b70`, in `HttpRequestControllerImpl::getVppDisclaimer` (`charging/http/http_request_repository_impl.dart @0x2979a6c`), sent through `requestHttp` (`@0x2979ba0`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `HttpRequestControllerImpl::getVppDisclaimer` (`charging/http/http_request_repository_impl.dart`, call `@0x2979ba0`, argument list `@0x2979b98`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

(asm-traced) `HttpRequestControllerImpl::getVppDisclaimer` (`charging/http/http_request_repository_impl.dart @0x2979a6c`) stores one key in a map literal with type arguments `<String, int>` (`@0x2979b2c`). The value is the current time in seconds: `_getCurrentMicros` (`@0x2979ac0`) is divided twice by 1000 (`sdiv` `@0x2979ae8`, `@0x2979aec`) and boxed from an unboxed 64-bit integer (`BoxInt64Instr` `@0x2979af0`), then stored in the array (`@0x2979b08`).

| field | type | required | example | source |
|---|---|---|---|---|
| `current_version` | int (unboxed, x) | yes | current time in seconds | `charging/http/http_request_repository_impl.dart @0x2979ab4` |

## `param_type`/`cmd`

n/a

## Response model (link)

read key by key, no `fromJson`: the success closure (`charging/http/http_request_repository_impl.dart @0x2979c34`) casts the response to `Map<String, dynamic>` (`@0x2979c9c`), reads `agreementInfo` (`@0x2979cd8`, cast to `Map<String, dynamic>?` `@0x2979d0c`) and in it `contentUrl` (`@0x2979d28`, cast to `String?` `@0x2979d74`) and passes the URL, or the empty string when it is null (`@0x2979d90`), to the stored callback (`ClosureCall` `@0x2979d9c`). A map method call (`GDT[cid_x0 + 0xbdf]`, selector not named, `@0x2979cbc`) gates the read.

## Response

(asm-traced) Response keys read by the app: `agreementInfo` (Map?) and in it `contentUrl` (String?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "current_version": "<current_version>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getVppDisclaimer` @0x2979a6c (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::getVppDisclaimer`
- `charging/ui/page/device/a5101/setting/vpp/controller.dart::requestVppDisclaimer`
- `charging/ui/page/user/main/user_main_page_logic.dart::requestVppDisclaimer`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Which map method call gates the read at `charging/http/http_request_repository_impl.dart @0x2979cbc` (selector not named by Blutter).
- What the server uses `current_version` for: the app sends the current time in seconds; no capture exists.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
