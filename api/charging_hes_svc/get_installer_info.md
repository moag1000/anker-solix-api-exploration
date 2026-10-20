> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_installer_info

## Purpose

Loads the installer information of a site for the install-information page (`A5101InstallInformationLogic::_getInstallerInfo` through `HttpRequestControllerImpl::getInstallerInfo`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_installer_info` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x2971be8`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2971be0`, in `HttpRequestControllerImpl::getInstallerInfo` (`charging/http/http_request_repository_impl.dart @0x2971b34`), sent through `requestHttp` (`@0x2971c10`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `HttpRequestControllerImpl::getInstallerInfo` (`charging/http/http_request_repository_impl.dart`, call `@0x2971c10`, argument list `@0x2971c08`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

(asm-traced) Each sender stores its keys in one map literal with type arguments `<String, String>` read at the cited address, so every value is a String: `HttpRequestControllerImpl::getInstallerInfo` (`charging/http/http_request_repository_impl.dart @0x2971b9c`, 1 key). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `siteId` | string | yes | `"<siteId>"` | `charging/http/http_request_repository_impl.dart @0x2971b88` |

## `param_type`/`cmd`

n/a

## Response model (link)

- [`A5101InstallInformationModel`](../../models/hes.md#a5101installinformationmodel), parsed by `A5101InstallInformationModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x2971d1c` (success closure `@0x2971cd4`, `bl` target `[package:charging/ui/page/device/a5101/setting/install_information/a5101_install_information_model.dart]`).

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::A5101InstallInformationModel`): `companyName` (unknown), `address` (unknown), `contactEmail` (unknown), `contactPhone` (unknown).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "siteId": "<siteId>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getInstallerInfo` @0x2971b34 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::getInstallerInfo`
- `charging/ui/page/device/a5101/setting/install_information/a5101_install_information_logic.dart::_getInstallerInfo`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Which keys of the model the page shows for a user who is not the installer: only the parse was read.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call. — reclassified: device test row 150 (traced 2026-10-20: per call the SDK login state `AkIotKitFlutter::isLogin` and the base-URL predicate decide, `HttpEncryptionDecorator.dart @0x4869504`, `@0x4869544`; the predicate is a GDT dispatch whose selector the asm does not name, and the login state is runtime data)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
