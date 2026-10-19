> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_entry_show

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/smart_service/v1/app/anka/get_entry_show`, method: not extracted by the inventory <!-- TODO -->; string-only: `ak_soft_ems/aiems/public_widget/anka_entry_button.dart @0x2bf0df0`
(literal also at 2 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | ? | ? | `ak_soft_ems/aiems/public_widget/anka_entry_button.dart @0x2bf0cc0` |
| `source` | ? | ? | ? | `ak_soft_ems/aiems/public_widget/anka_entry_button.dart @0x2bf0cc0` |

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

- `ak_soft_ems/aiems/public_widget/anka_entry_button.dart`: `<anonymous closure>@0x2bf0e34` @0x2bf0e34 (URL literal only, no `*Http*` call); `<anonymous closure>@0x2bf0ec4` @0x2bf0ec4 (URL literal only, no `*Http*` call); `checkAnkaSupport` @0x2bf0cc0 (encryptionRequestHttp; encrypted: true)

Called from:

- `ak_soft_ems/aiems/public_widget/anka_entry_button.dart::_checkSupport`

## Since/changed

3.18.0: absent. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
