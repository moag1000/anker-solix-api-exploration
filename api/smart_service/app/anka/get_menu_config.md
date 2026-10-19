> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_menu_config

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/smart_service/v1/app/anka/get_menu_config`, method: not extracted by the inventory <!-- TODO -->; string-only: `anka_agent/http/anka_agent_http.dart @0x35c53b4`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No request keys found by the extractor. <!-- TODO -->

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

- `anka_agent/http/anka_agent_http.dart`: `getAnkaAgentMenuConfig` @0x35c5310 (encryptionRequestHttpByGHttpRequest; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
