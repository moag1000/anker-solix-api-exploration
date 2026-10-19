> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# del_reminder

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/mini_power/v1/app/reminder/del_reminder`, method: not extracted by the inventory <!-- TODO -->; string-only: `small_charging_platform/src/custom_reminder/http/custom_reminder_cloud_api.dart @0x2f2d864`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `id` | ? | ? | ? | `small_charging_platform/src/custom_reminder/http/custom_reminder_cloud_api.dart @0x2f2d794` |

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

- `small_charging_platform/src/custom_reminder/http/custom_reminder_cloud_api.dart`: `deleteReminder` @0x2f2d794 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: absent. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
