> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# set_user_params

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/app/user/set_user_params`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/user/about/about_http_request_repository_impl.dart @0x4036440`
(literal also at 2 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify" / `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `params` | ? | ? | ? | `charging/http/user/about/about_http_request_repository_impl.dart @0x4036308` |
| `params.driving_plan` | ? | ? | ? | `ev_charger/src/ev_charger/page/home/schedule_charge/network/%20schedule_network.dart @0x39682d4` |
| `path` | ? | ? | ? | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x405be14` |
| `method` | ? | ? | ? | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x405be14` |
| `param.params` | ? | ? | ? | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x405be14` |

Rows are the union over 3 senders; `source` is the first sender that sets the key.

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

- `charging/http/user/about/about_http_request_repository_impl.dart`: `setPersonalizationOptionsApi` @0x4036308 (encryptionRequestHttp; encrypted: true)
- `ev_charger/src/ev_charger/page/home/schedule_charge/network/%20schedule_network.dart`: `_setUserParams` @0x39682d4 (_requestHttp; encrypted: default-true (requestHttp) — verify)
- `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart`: `setUserParams` @0x405be14 (URL literal only, no `*Http*` call; sends in the same function (SDK `handle`))

Called from:

- `charging/ui/page/user/about/personalizationOptions/personalization_options_logic.dart::setPersonalizationOptionsStatus`
- `ev_charger/src/ev_charger/base/ev_charger_user_params.dart::setUserParam`
- `ev_charger/src/ev_charger/page/home/schedule_charge/network/%20schedule_network.dart::setDrivingPlan`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
