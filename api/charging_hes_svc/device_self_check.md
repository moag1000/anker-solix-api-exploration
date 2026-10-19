> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# device_self_check

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_svc/device_self_check`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/device/a5101/setting/system_self_check/system_testing/system_testing_logic.dart @0x43300ac`

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `siteId` | ? | ? | ? | `charging/ui/page/device/a5101/setting/system_self_check/system_testing/system_testing_logic.dart @0x432ffa8` |

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

- `charging/ui/page/device/a5101/setting/system_self_check/system_testing/system_testing_logic.dart`: `setSelfCheckCommand` @0x432ffa8 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from: `charging/ui/page/device/a5101/setting/system_self_check/system_testing/system_testing_logic.dart::_showTip`, `charging/ui/page/device/a5101/setting/system_self_check/system_testing/widgets/system_testing_timeOut_view.dart::build`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
