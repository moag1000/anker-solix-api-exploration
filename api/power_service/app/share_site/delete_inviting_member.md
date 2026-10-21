> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# delete_inviting_member

## Purpose

Deletes an invited (not yet joined) member of a shared site: `HomeCenterLogic::deleteInviteMemberReq` builds the body from the selected invite item and calls `deleteInviteMember`.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/share_site/delete_inviting_member` (asm-traced): URL string at `http_request_repository_impl.dart @0x405e314`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x405e30c`, in `HttpRequestControllerImpl::deleteInviteMember` (`http_request_repository_impl.dart @0x405e294`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is built by the caller `HomeCenterLogic::deleteInviteMemberReq` (`home_center_logic.dart @0x405e140`): a 2-pair map literal typed `<String, dynamic>` (`AllocateArray r2 = 8`, `@0x405e17c`); the builder `deleteInviteMember` (`http_request_repository_impl.dart @0x405e294`) forwards it unchanged to `encryptionRequestHttp` (`@0x405e33c`).

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | string | yes | `"<site_id>"` | key `@0x405e184`, value store `@0x405e1a8`; the value is `field_7` of the item with the empty string substituted for null (`r2 = ""` `@0x405e1a4`) |
| `member_id` | string | yes | `"<member_id>"` | key `@0x405e1ac`, value store `@0x405e1d4`; `field_f` of the item with the empty string for null (`r1 = ""` `@0x405e1c8`) |

## `param_type`/`cmd`

n/a

## Response model (link)

None: no response model is parsed. The caller's two callbacks `home_center_logic.dart @0x405e358` (loads its first argument at `fp+0x18`, calls `getData()`) and `station_energy_system_logic.dart @0x238c8d0` (loads `fp+0x10`, calls `show()`) contain no `fromJson` call.

## Response

No response key is read by the app.

## Example request/response

Request, synthesized (decrypted body as built by `deleteInviteMemberReq`)

```json
{"site_id": "<site_id>", "member_id": "<member_id>"}
```

Response: none parsed.

## Errors seen

None traced: neither callback of the sender compares an error code. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `deleteInviteMember` @0x405e294 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::deleteInviteMember`
- `charging/ui/page/user/share_site/home_center/home_center_logic.dart::deleteInviteMemberReq`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- The response body: not read by the app, so its keys are unknown. — reclassified: server (not visible in the app: the app does not read the body)
- Whether `member_id` here is the id returned by [get_invited_list](get_invited_list.md) (the item class `SiteInviteMemberModel` has a `member_id`): not followed from the item to the key. — traced 2026-10-20: `SiteInviteMemberModel` carries `member_id` (String?, `data/models.json`); the delete callers' source of the id was not followed
- What the server does for an unknown `member_id`: not derivable from the app.

## Device-tested by

none
