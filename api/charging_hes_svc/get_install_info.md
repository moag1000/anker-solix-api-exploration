> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_install_info

## Purpose

Loads the installation address of a site for the install-address page (`A5101InstallAddressLogic::_getInstallAddressInfo` through `HttpRequestControllerImpl::getDeviceInstallAddress`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_install_info` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x34d8214`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x34d820c`, in `HttpRequestControllerImpl::getDeviceInstallAddress` (`charging/http/http_request_repository_impl.dart @0x34d8160`), sent through `requestHttp` (`@0x34d823c`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `HttpRequestControllerImpl::getDeviceInstallAddress` (`charging/http/http_request_repository_impl.dart`, call `@0x34d823c`, argument list `@0x34d8234`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

(asm-traced) Each sender stores its keys in one map literal with type arguments `<String, String>` read at the cited address, so every value is a String: `HttpRequestControllerImpl::getDeviceInstallAddress` (`charging/http/http_request_repository_impl.dart @0x34d81c8`, 1 key). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `siteId` | string | yes | `"<siteId>"` | `charging/http/http_request_repository_impl.dart @0x34d81b4` |

## `param_type`/`cmd`

n/a

## Response model (link)

- [`A5101InstallAddressModel`](../../models/hes.md#a5101installaddressmodel), parsed by `A5101InstallAddressModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x34d8348` (success closure `@0x34d8300`, `bl` target `[package:charging/ui/page/device/a5101/setting/install_address/a5101_install_address_model.dart]`).

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::A5101InstallAddressModel`): `installLocation` (unknown), `installEnv` (unknown).

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

- `charging/http/http_request_repository_impl.dart`: `getDeviceInstallAddress` @0x34d8160 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::getDeviceInstallAddress`
- `charging/ui/page/device/a5101/setting/install_address/a5101_install_address_logic.dart::_getInstallAddressInfo`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Which address fields the server leaves empty for a site without an installer: no capture exists.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
