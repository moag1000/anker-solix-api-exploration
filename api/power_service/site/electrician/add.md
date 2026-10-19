> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# add

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/site/electrician/add`, method: not extracted by the inventory <!-- TODO -->; string-only: `base_service/view/text_info_dialog/text_info_dialog_logic.dart @0x2e22c38`

## Encrypted?

encrypted: "unknown (URL literal only, no `*Http*` call)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `isPass` | ? | ? | ? | `base_service/view/text_info_dialog/text_info_dialog_logic.dart @0x2e22a60` |
| `message` | ? | ? | ? | `base_service/view/text_info_dialog/text_info_dialog_logic.dart @0x2e22a60` |
| `path` | ? | ? | ? | `base_service/view/text_info_dialog/text_info_dialog_logic.dart @0x2e22a60` |
| `method` | ? | ? | ? | `base_service/view/text_info_dialog/text_info_dialog_logic.dart @0x2e22a60` |
| `param.site_id` | ? | ? | ? | `base_service/view/text_info_dialog/text_info_dialog_logic.dart @0x2e22a60` |
| `param.electrician_name` | ? | ? | ? | `base_service/view/text_info_dialog/text_info_dialog_logic.dart @0x2e22a60` |
| `param.electrician_mail` | ? | ? | ? | `base_service/view/text_info_dialog/text_info_dialog_logic.dart @0x2e22a60` |

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

- `base_service/view/text_info_dialog/text_info_dialog_logic.dart`: `_setElectricianInfo` @0x2e22a60 (URL literal only, no `*Http*` call)

Called from:

- `base_service/view/text_info_dialog/text_info_dialog_logic.dart::onBottomButtonTap`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
