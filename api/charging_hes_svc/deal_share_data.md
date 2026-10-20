> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

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

`HttpRequestControllerImpl::agreeOrRefuseVppDisclaimer` (`charging/http/http_request_repository_impl.dart @0x3edb5c8`) stores 2 keys in a map literal with type arguments `<String, Object>` (`@0x3edb63c`), which do not type the values. `action` is an integer: the unboxed parameter is tagged to a Smi by `lsl x2, x1, #1` (`@0x3edb634`) before the store (`@0x3edb638`), so the number is the parameter value. `sn` is stored as received (`@0x3edb624`); the one caller passes `controller().field_9b.value` (`charging/ui/page/device/a5101/setting/vpp/view.dart @0x3edb4d4`), and `field_9b` of `VppController` is created as `"".obs` (`StringExtension.obs`, `charging/ui/page/device/a5101/setting/vpp/controller.dart @0x4158ca8`, store `@0x4158cb0`), a `String` observable, so `sn` is a string (two-hop, declared type read). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `sn` | string | yes |  | `charging/http/http_request_repository_impl.dart @0x3edb614` |
| `action` | int (Smi, w) | yes |  | `charging/http/http_request_repository_impl.dart @0x3edb628` |

Callers (app side, traced 2026-10-20): `VppPage::evergenVppButtonWidget` (`charging/ui/page/device/a5101/setting/vpp/view.dart`) builds two buttons whose tap closures call `agreeOrRefuseVpp` with the raw argument `r3 = 1` (closure `@0x3edb828`, call `@0x3edb88c`) and `r3 = 2` (closure `@0x3edb480`, call `@0x3edb4e4`); the closure with 1 is created next to the label string `"Agree"` (`@0x3edb068`, `@0x3edb080`), the closure with 2 after the string `"refuse"` (`@0x3edb22c`, `@0x3edb2d4`). `action` is an unboxed parameter, so the values are 1 (agree button) and 2 (refuse button) as the app sends them; the meaning on the server is not known from the app.

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the sender (asm-traced): the success closure (`charging/http/http_request_repository_impl.dart @0x3edb744`) logs `---> agreeOrRefuseVppDisclaimer success ` with the response (`@0x3edb778`, `exeSuccess` `@0x3edb79c`) and passes the response object unchanged to the stored callback (`ClosureCall` `@0x3edb7b8`). The callback does not read the response (see Response).

## Response

No response key is read in the sender.

The success callback `VppController::agreeOrRefuseVpp` passes (`charging/ui/page/device/a5101/setting/vpp/controller.dart @0x3edb7dc`) does not read the response: it calls `requestVppInfo` (`@0x3edb80c`) with no argument.

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

- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call. — reclassified: device test row 150 (traced 2026-10-20: per call the SDK login state `AkIotKitFlutter::isLogin` and the base-URL predicate decide, `HttpEncryptionDecorator.dart @0x4869504`, `@0x4869544`; the predicate is a GDT dispatch whose selector the asm does not name, and the login state is runtime data)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
