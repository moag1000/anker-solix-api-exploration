> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_reminder_list

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/mini_power/v1/app/reminder/get_reminder_list`, method: not extracted by the inventory <!-- TODO -->; string-only: `small_charging_platform/src/custom_reminder/http/custom_reminder_cloud_api.dart @0x2a531bc`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `id` | ? | ? | ? | `small_charging_platform/src/custom_reminder/http/custom_reminder_cloud_api.dart @0x2a530b0` |

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

- `small_charging_platform/src/custom_reminder/http/custom_reminder_cloud_api.dart`: `getReminderList` @0x2a530b0 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: absent. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
