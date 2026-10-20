> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# update_hes_utility_rate_plan

## Purpose

Writes the peak-and-valley price plan of a site from the peaks-and-valleys page (`PeaksAndValleysLogic::submitPeakAndValley` through `HttpRequestControllerImpl::updatePeakAndValley`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/update_hes_utility_rate_plan` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x4326e40`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x4326e38`, in `HttpRequestControllerImpl::updatePeakAndValley` (`charging/http/http_request_repository_impl.dart @0x4326d40`), sent through `requestHttp` (`@0x4326e68`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `HttpRequestControllerImpl::updatePeakAndValley` (`charging/http/http_request_repository_impl.dart`, call `@0x4326e68`, argument list `@0x4326e60`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

`HttpRequestControllerImpl::updatePeakAndValley` (`charging/http/http_request_repository_impl.dart @0x4326d40`) stores 2 keys in a map literal with type arguments `<String, Object>` (`@0x4326df0`), which do not type the values. `siteId` is the constant empty string (`r16 = ""` `@0x4326dac`, stored `@0x4326db0`); `peakValleyPriceSeason` is the result of a `toJson` call (`@0x4326dc4`, stored `@0x4326dcc`) whose return type was not resolved, so the type stays `?`.

| field | type | required | example | source |
|---|---|---|---|---|
| `siteId` | string | yes | `""` (constant empty string) | `charging/http/http_request_repository_impl.dart @0x4326da0` |
| `peakValleyPriceSeason` | ? | yes | the result of a `toJson` call on the parameter | `charging/http/http_request_repository_impl.dart @0x4326db4` |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the sender (asm-traced): the success closure is the folded forwarder `charging/http/http_request_repository_impl.dart @0x2268374`, which passes the response object unchanged to the callback stored in the context (`ClosureCall` `@0x22683a8`); the failure closure is the folded forwarder `@0x226824c` (`ClosureCall` `@0x2268288`).

## Response

No response key is read in the sender.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "siteId": "",
  "peakValleyPriceSeason": "<peakValleyPriceSeason>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `updatePeakAndValley` @0x4326d40 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::updatePeakAndValley`
- `charging/ui/page/device/a5101/setting/peaksAndValleys/peaks_valleys_logic.dart::submitPeakAndValley`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Why `siteId` is always sent as the empty string: the builder stores the constant; the site is probably carried inside `peakValleyPriceSeason`, which is not read here.
- The structure of `peakValleyPriceSeason`: the `toJson` of the parameter class was not read.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call. — reclassified: device test row 150 (traced 2026-10-20: per call the SDK login state `AkIotKitFlutter::isLogin` and the base-URL predicate decide, `HttpEncryptionDecorator.dart @0x4869504`, `@0x4869544`; the predicate is a GDT dispatch whose selector the asm does not name, and the login state is runtime data)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
