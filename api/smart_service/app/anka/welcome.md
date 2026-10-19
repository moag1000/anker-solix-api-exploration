> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# welcome

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/smart_service/v1/app/anka/welcome`, method: not extracted by the inventory <!-- TODO -->; string-only: `anka_agent/http/anka_agent_http.dart @0x35c710c`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `current_time` | ? | ? | ? | `anka_agent/http/anka_agent_http.dart @0x35c6e48` |

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

- `anka_agent/http/anka_agent_http.dart`: `getWelcomeGreeting` @0x35c6e48 (encryptionRequestHttpByGHttpRequest; encrypted: true)

## Since/changed

3.18.0: absent. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
