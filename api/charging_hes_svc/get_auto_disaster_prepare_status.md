> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_auto_disaster_prepare_status

## Purpose

Reads the auto disaster-preparedness status of a station for the family page tips (`AutoDisasterTipsLogic::_getNetAutoDisasterPrepareStatus`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_auto_disaster_prepare_status` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x34b6cac`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x34b6ca4`, in `HttpRequestControllerImpl::getAutoDisasterPrepareStatus` (`charging/http/http_request_repository_impl.dart @0x34b6ba0`), sent through `requestHttp` (`@0x34b6cd0`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `HttpRequestControllerImpl::getAutoDisasterPrepareStatus` (`charging/http/http_request_repository_impl.dart`, call `@0x34b6cd0`, argument list `@0x34b6cc8`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

(asm-traced) Each sender stores its keys in one map literal with type arguments `<String, String>` read at the cited address, so every value is a String: `HttpRequestControllerImpl::getAutoDisasterPrepareStatus` (`charging/http/http_request_repository_impl.dart @0x34b6c60`, 1 key). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | string | yes | `"<station_id>"` | `charging/http/http_request_repository_impl.dart @0x34b6c4c` |

## `param_type`/`cmd`

n/a

## Response model (link)

- [`AutoDisasterPrepareStatusModel`](../../models/hes.md#autodisasterpreparestatusmodel), parsed by `AutoDisasterPrepareStatusModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x34b6df0` (success closure `@0x34b6d84`, `bl` target `[package:charging/model/a5101/auto_disaster_prepare_status_model.dart]`).

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::AutoDisasterPrepareStatusModel`): `disasterPrepareStatus` (int?), `events` (unknown).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "station_id": "<station_id>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`. The failure closure (`charging/http/http_request_repository_impl.dart @0x34b6ce4`) logs the code and message and completes the pending future without comparing the code.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getAutoDisasterPrepareStatus` @0x34b6ba0 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/util/demosite_util_impl.dart`: `DemoSiteUtilImpl` @0x4a33a6c (URL literal only, no `*Http*` call)

Called from:

- `charging/boostrap_impl.dart::DIInit`
- `charging/http/http_request_repository.dart::getAutoDisasterPrepareStatus`
- `charging/ui/page/family/auto_disaster/auto_disaster_tips_logic.dart::_getNetAutoDisasterPrepareStatus`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What the callers do when the future completes with the failure value: only the sender was read.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call. — reclassified: device test row 150 (traced 2026-10-20: per call the SDK login state `AkIotKitFlutter::isLogin` and the base-URL predicate decide, `HttpEncryptionDecorator.dart @0x4869504`, `@0x4869544`; the predicate is a GDT dispatch whose selector the asm does not name, and the login state is runtime data)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
