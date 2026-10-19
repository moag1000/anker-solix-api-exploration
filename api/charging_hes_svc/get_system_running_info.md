> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_system_running_info

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_svc/get_system_running_info`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/family/family_main_http_reposity.dart @0x23e2f80`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `siteId` | ? | ? | ? | `charging/ui/page/family/family_main_http_reposity.dart @0x23e2edc` |

Rows are the union over 2 senders; `source` is the first sender that sets the key.

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

- `charging/ui/page/family/family_main_http_reposity.dart`: `getSystemProfit` @0x23e2edc (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart`: `_requestHesSiteInfo` @0x2923848 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart::fetchHesSites`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
