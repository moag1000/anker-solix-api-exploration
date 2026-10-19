> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# quit_auto_disaster_prepare

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_svc/quit_auto_disaster_prepare`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x27ad66c`

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x27ad518` |
| `unix` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x27ad518` |
| `far_field` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x27ad518` |

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

- `charging/http/http_request_repository_impl.dart`: `quitAutoDisasterPrepare` @0x27ad518 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::quitAutoDisasterPrepare`
- `charging/ui/page/family/auto_disaster/auto_disaster_tips_logic.dart::_quitAutoDisasterPrepareFromNet`
- `charging/ui/page/family/auto_disaster/auto_disaster_tips_logic.dart::onMessageDispatch`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
