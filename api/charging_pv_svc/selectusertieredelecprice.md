> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# selectUserTieredElecPrice

## Purpose

<!-- TODO -->

## Upstream name

`get_device_pv_price` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/charging_pv_svc/selectUserTieredElecPrice`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x2401458`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x24013a0` |

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

- `charging/http/http_request_repository_impl.dart`: `selectUserTieredElecPrice` @0x24013a0 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::selectUserTieredElecPrice`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
