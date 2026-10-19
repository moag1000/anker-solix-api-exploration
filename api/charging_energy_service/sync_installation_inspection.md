> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# sync_installation_inspection

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_energy_service/sync_installation_inspection`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x26eb180`

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x26eb06c` |
| `page` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x26eb06c` |
| `errors` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x26eb06c` |

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

- `charging/http/http_request_repository_impl.dart`: `syncInstallation` @0x26eb06c (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::syncInstallation`
- `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart::createOrJoinSuccess`
- `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart::syncGoHome`
- `charging/ui/page/device/a17b1/a17b1system_test/system_test_logic.dart::handlerSelfCheckComplete`
- `charging/ui/page/green_energy/site/site_logic.dart::toHomeInitialProcess`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
