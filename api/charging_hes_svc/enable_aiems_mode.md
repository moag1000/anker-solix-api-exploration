> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# enable_aiems_mode

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_svc/enable_aiems_mode`, method: not extracted by the inventory <!-- TODO -->; string-only: `ak_soft_ems/http/ems_api.dart @0x379e6e8`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `siteId` | ? | ? | ? | `charging/ui/page/device/a5101/setting/smartMode/smart_mode_logic.dart @0x3eaee94` |

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

- `ak_soft_ems/http/ems_api.dart`: `enableAiEmsMode` @0x379e6d0 (URL literal only, no `*Http*` call; sender found through callers: `EmsAiModeConditionLogic::_enableLargeSmartMode` (`ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x379e4b8`) via `EmsAiModeConditionLogic::_enableLargeSmartMode` (`ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x379e4b8`))
- `charging/ui/page/device/a5101/setting/smartMode/smart_mode_logic.dart`: `enableSmartMode` @0x3eaee94 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/ui/page/device/a5101/setting/smartMode/smart_mode_view.dart::build`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
