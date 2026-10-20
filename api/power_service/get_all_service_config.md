> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_all_service_config

## Purpose

Fills the QA environment list of the app's environment picker: `EnvListPageLogic::getAllEnvList` (`env_list_page_logic.dart @0x2986154`) calls `getAllQaEnvConfig`.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/get_all_service_config` (asm-traced): URL string at `http_request_repository_impl.dart @0x2986310`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2986308`, in `HttpRequestControllerImpl::getAllQaEnvConfig` (`http_request_repository_impl.dart @0x2986280`).

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is an empty map literal (`ldr x16, [THR, #0xa8]` empty array `@0x29862c8`, `Map._fromLiteral` `@0x29862d0`); the builder contains no `[]=` call, so no key is added. The map goes to `requestHttp` (`@0x2986338`). This sender uses `requestHttp`, not `encryptionRequestHttp`.

## `param_type`/`cmd`

n/a

## Response model (link)

`charging::QaEnvListModel` (`data/models.json` key, no model page), parsed by the caller's success callback `env_list_page_logic.dart @0x29863b8` with `QaEnvListModel.fromJson` after a `Map<String, dynamic>` cast, then `RxList.from` fills the list. The builder only passes the `postJML` closure templates (`pp+0xbb010`, `pp+0xbb018`) through to the caller's callbacks.

## Response

The model has the single top-level key `env_data` (element type not resolved in `data/models.json`).

## Example request/response

Request, synthesized

```json
{}
```

Response keys: see Response; no capture.

## Errors seen

None traced. The caller's failure callback `env_list_page_logic.dart @0x2986354` logs `"Failed to obtain the environment list: "` and calls `exeError()`; no code is compared. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getAllQaEnvConfig` @0x2986280 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::getAllQaEnvConfig`
- `charging/ui/page/user/envList/env_list_page_logic.dart::getAllEnvList`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta. The model `QaEnvListModel` is `≤3.18.0` in `data/models.json`.

## Known unknowns

- The element structure of `env_data`.
- Whether production servers answer this URL: the function and page names (`getAllQaEnvConfig`, `EnvListPageLogic`) point at a QA environment list; the app sends it only from the environment picker page.
- Whether `requestHttp` encrypts this call: it is the non-`encryption` wrapper (default `needEncryption` true, see `api/encryption.md`); not decoded further.

## Device-tested by

none
