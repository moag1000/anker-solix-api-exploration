> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_easter_egg_trigger_list

## Purpose

<!-- TODO -->

## Upstream name

`charger_get_triggers` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/mini_power/v1/app/egg/get_easter_egg_trigger_list`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x276fc94`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x276fbe0` |

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

- `charging/http/http_request_repository_impl.dart`: `getEasterEggRecord` @0x276fbe0 (encryptionRequestHttp; encrypted: true)

Called from: `charging/http/http_request_repository.dart::getEasterEggRecord`, `charging/ui/page/device/a2345/a2345easter_egg/a2345easter_egg_logic.dart::requestEasterEggRecord`, `charging/ui/page/device/a91b2/a91b2easter_egg/a91b2easter_egg_logic.dart::_requestEasterEggRecord`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
