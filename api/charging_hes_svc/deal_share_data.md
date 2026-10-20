> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# deal_share_data

## Purpose

Sends the decision of the user on the VPP disclaimer (`agreeOrRefuseVpp` in `charging/ui/page/device/a5101/setting/vpp/controller.dart` through `HttpRequestControllerImpl::agreeOrRefuseVppDisclaimer`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/deal_share_data` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x3edb688`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3edb680`, in `HttpRequestControllerImpl::agreeOrRefuseVppDisclaimer` (`charging/http/http_request_repository_impl.dart @0x3edb5c8`), sent through `requestHttp` (`@0x3edb6b0`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `HttpRequestControllerImpl::agreeOrRefuseVppDisclaimer` (`charging/http/http_request_repository_impl.dart`, call `@0x3edb6b0`, argument list `@0x3edb6a8`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

`HttpRequestControllerImpl::agreeOrRefuseVppDisclaimer` (`charging/http/http_request_repository_impl.dart @0x3edb5c8`) stores 2 keys in a map literal with type arguments `<String, Object>` (`@0x3edb63c`), which do not type the values. `action` is an integer: the unboxed parameter is tagged to a Smi by `lsl x2, x1, #1` (`@0x3edb634`) before the store (`@0x3edb638`), so the number is the parameter value. `sn` is stored as received (`@0x3edb624`), so its type stays `?`. No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `sn` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3edb614` |
| `action` | int (Smi, w) | yes | a number from the caller | `charging/http/http_request_repository_impl.dart @0x3edb628` |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the sender (asm-traced): the success closure (`charging/http/http_request_repository_impl.dart @0x3edb744`) logs `---> agreeOrRefuseVppDisclaimer success ` with the response (`@0x3edb778`, `exeSuccess` `@0x3edb79c`) and passes the response object unchanged to the stored callback (`ClosureCall` `@0x3edb7b8`). What the callback reads was not followed.

## Response

No response key is read in the sender.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "sn": "<sn>",
  "action": "<action>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`. The failure closure (`charging/http/http_request_repository_impl.dart @0x3edb6cc`) logs the code (`@0x3edb6f0`) and calls `exeError` without comparing it.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `agreeOrRefuseVppDisclaimer` @0x3edb5c8 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::agreeOrRefuseVppDisclaimer`
- `charging/ui/page/device/a5101/setting/vpp/controller.dart::agreeOrRefuseVpp`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The type of `sn`: the parameter is stored without a conversion (`charging/http/http_request_repository_impl.dart @0x3edb624`) into a `<String, Object>` map.
- Which `action` numbers mean agree and refuse: the value is a parameter of the builder and the caller was not decoded.
- What the callback of `agreeOrRefuseVpp` does with the raw response.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
