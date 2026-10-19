> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# set_bubble_status

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/smart_service/v1/app/anka/set_bubble_status`, method: not extracted by the inventory <!-- TODO -->; string-only: `anka_agent/http/bubble_http.dart @0x2bc1764`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `status` | ? | ? | ? | `anka_agent/http/bubble_http.dart @0x2bc1558` |
| `bubble_type` | ? | ? | ? | `anka_agent/http/bubble_http.dart @0x2bc1558` |
| `bubble_id` | ? | ? | ? | `anka_agent/http/bubble_http.dart @0x2bc1558` |
| `consume_time` | ? | ? | ? | `anka_agent/http/bubble_http.dart @0x2bc1558` |

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

- `anka_agent/http/bubble_http.dart`: `setBubbleStatus` @0x2bc1558 (encryptionRequestHttpByGHttpRequest; encrypted: true)

## Since/changed

3.18.0: absent. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
