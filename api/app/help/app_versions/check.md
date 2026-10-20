> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# check

## Purpose

Asks the server whether a newer app version exists; sent by `AppUpdateUtil::checkAppUpdate` (`charging/util/app_update_util.dart`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /app/help/app_versions/check` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x2609214`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x260920c`, in `HttpRequestControllerImpl::checkUpdateForApp` (`charging/http/http_request_repository_impl.dart @0x260915c`), sent through `encryptionRequestHttp` (`@0x2609234`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `version` | string | yes | `"<version>"` | `charging/http/http_request_repository_impl.dart @0x26091b4` (value store `@0x26091c4`) |

The value is a String: map literal with type arguments `<String, String>` (`@0x26091c8`).

## `param_type`/`cmd`

n/a

## Response model (link)

[`AppUpdateModel`](../../../../models/other.md#appupdatemodel), parsed by `AppUpdateModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x2609848` in the success closure `@0x26097dc` (call target `#0x26094e4`, `charging/model/app_update_model.dart`).

## Response

(asm-traced) Top-level keys of `AppUpdateModel` (`data/models.json`, `charging::AppUpdateModel`): `version` (String?), `push_way` (String?), `desc` (String?). The closure checks three of the parsed fields (`charging/http/http_request_repository_impl.dart @0x2609850`, `@0x2609860`, `@0x260986c`), stores the model with `setAppUpdateInfo` (`@0x26098b0`) and passes it to the callback (`ClosureCall` `@0x26098cc`).

The three checks (traced 2026-10-20): the success closure (`charging/http/http_request_repository_impl.dart`) loads `field_7` (`version`, `@0x2609850`), `field_b` (`push_way`, `@0x2609860`) and `field_f` (`desc`, `@0x2609870`) of the parsed `AppUpdateModel` (offsets per its `fromJson` key order) and tests each against null (`cmp w0, NULL` `@0x2609858`, `@0x2609868`, `@0x2609878`); when any of the three is null the closure returns without storing the model and without calling the callback (`r0 = Null` `@0x2609880`).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "version": "<version>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender, its closures or the caller functions read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `checkUpdateForApp` @0x260915c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::checkUpdateForApp`
- `charging/util/app_update_util.dart::checkAppUpdate`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Values of `push_way` (forced or optional update): the model key is typed `String?`; the allowed values are not visible. — traced 2026-10-20: `push_way` is a `String?` of `AppUpdateModel` (`charging/model/app_update_model.dart @0x2609774`); no function reads it by name, so the compared values were not found
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
