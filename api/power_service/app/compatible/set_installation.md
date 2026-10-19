> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# set_installation

## Purpose

<!-- TODO -->

## Upstream name

`set_installation` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/app/compatible/set_installation`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x3d65450`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `install_mode` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3d6528c` |
| `site_id` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3d6528c` |
| `is_save` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3d6528c` |
| `solarbank_sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3d6528c` |

## `param_type`/`cmd`

n/a

## Response model (link)

<!-- TODO -->

## Response

<!-- TODO -->

## Example request/response

<!-- TODO -->

## Errors seen

`api/errors.md`: <!-- TODO -->

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `setInstallationApi` @0x3d6528c (encryptionRequestHttp; encrypted: true)

Called from: `charging/http/http_request_repository.dart::setInstallationApi`, `charging/ui/page/device/a17c0/ez1_select_mode/ez1_select_mode_logic.dart::getOTAUpdateStatus`, `charging/ui/page/device/a17c0/ez1_select_mode/ez1_select_mode_logic.dart::next`, `charging/ui/page/device/a17y0/a17y0ota/a17y0_use_a17c0_ota_logic.dart::startOTA`, `charging/ui/page/device/anker_ota/poll_progress_ota_page/poll_progress_ota_logic.dart::startOTA`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
