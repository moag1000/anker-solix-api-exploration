> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_installation_inspection

## Purpose

Reads the installation-inspection state of an A17B1 station when the home page decides which page to open (caller chain `A17B1HomeLogic::getHomeLatestPage`, `HttpRequestController::getInstallation`, in `data/endpoints.json`) (asm-traced).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_energy_service/get_installation_inspection` (asm-traced): URL string `@0x2375bf4`, method object `Method.post` (pool entry `pp+0xa7e0`) `@0x2375bec`, in `HttpRequestControllerImpl::getInstallation` (`charging/http/http_request_repository_impl.dart @0x2375b38`), sent through `HttpRequestControllerImpl::requestHttp` (`@0x2375c1c`).

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) One sender, one key. The map literal has the type arguments `<String, String>` (`charging/http/http_request_repository_impl.dart @0x2375ba8`), so the value is a string; it is stored without a guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `sn` | string | yes | `"<sn>"` | `charging/http/http_request_repository_impl.dart @0x2375b94` (value store `@0x2375ba4`, parameter) |

## `param_type`/`cmd`

n/a

## Response model (link)

[`InstallationModel`](../../models/connectivity.md#installationmodel), parsed by `InstallationModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x2375c68` in the success closure `@0x2375c38`; the closure then stores the model as JSON in the local preferences (`jsonEncode` `@0x2375ca8`, `SpUtilImpl::set17b1InstallDetail` `@0x2375cb8`).

## Response

(asm-traced) Top-level keys of `InstallationModel` (`data/models.json`, `charging::InstallationModel`): `latest_result` (bool?), `latest_time` (int?), `latest_page` (String?), `need_self_inspection` (bool?). The closure adds no wrapper field.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "sn": "<sn>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure only logs `code` and `msg`). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getInstallation` @0x2375b38 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::getInstallation`
- `charging/ui/page/device/a17b1/device_home/a17b1home_logic.dart::getHomeLatestPage`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Which serial number the caller passes (`A17B1HomeLogic::getHomeLatestPage` was not read).
- What `latest_page` encodes (String?): only the class field is listed; the home logic that reads it was not followed.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
