> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# invite_member

## Purpose

Invites a person to a shared site by email or by phone number: `InviteMembersLogic::sendInviteMessage` (`invite_members_logic.dart @0x40613d0`) builds one of two bodies from the invite form and calls `inviteMemberSite`.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/share_site/invite_member` (asm-traced): URL string at `http_request_repository_impl.dart @0x4061808`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x4061800`, in `HttpRequestControllerImpl::inviteMemberSite` (`http_request_repository_impl.dart @0x4061788`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The caller builds the body (`<String, dynamic>` maps) and passes it to `inviteMemberSite` (`http_request_repository_impl.dart @0x4061788`), which forwards it to `encryptionRequestHttp`. Two branches exist, selected by an Rx flag (`charging/ui/page/user/share_site/invite_members/invite_members_logic.dart @0x4061434`..`@0x4061534`).

Email branch:

| field | type | required | example | source |
|---|---|---|---|---|
| `email` | ? | yes | | key `charging/ui/page/user/share_site/invite_members/invite_members_logic.dart @0x4061550`, value store `@0x4061578` (read as `field_27` then `field_7` of a form object, `@0x4061568`, `@0x4061570`) |
| `site_id` | ? | yes | | key `charging/ui/page/user/share_site/invite_members/invite_members_logic.dart @0x406157c`, value store `@0x40615a8` (`field_7` of an Rx value, `@0x4061598`) |

Phone branch:

| field | type | required | example | source |
|---|---|---|---|---|
| `phone` | ? | yes | | key `charging/ui/page/user/share_site/invite_members/invite_members_logic.dart @0x40615fc`, value store `@0x4061624` (`field_27` then `field_7`, `@0x4061614`, `@0x406161c`) |
| `phone_code` | ? | yes | | key `charging/ui/page/user/share_site/invite_members/invite_members_logic.dart @0x4061628`, value store `@0x4061648` (`value()` of an Rx object, `@0x4061640`) |
| `site_id` | ? | yes | | key `charging/ui/page/user/share_site/invite_members/invite_members_logic.dart @0x4061670`, value store `@0x40616a0` (`field_7` of an Rx value, `@0x4061690`) |

## `param_type`/`cmd`

n/a

## Response model (link)

None: the response body is not parsed. The success callback `invite_members_logic.dart @0x4061b64` loads no argument (it shows the `joinMemberSuccess` toast and closes the page); the failure callback `@0x40618cc` loads only the code (`fp+0x18`).

## Response

No response key is read by the app.

## Example request/response

Request, synthesized (key sets as built; value types unresolved)

```json
{"phone": "<phone>", "phone_code": "<phone_code>", "site_id": "<site_id>"}
```

Email branch: `{"email": "<email>", "site_id": "<site_id>"}`. Response: none parsed.

## Errors seen

The failure callback `invite_members_logic.dart @0x40618cc` compares 64-bit values (`cmp x, x17`, raw immediates, no halving) with 21100 (`@0x4061904`), 21101 (`@0x4061970`), 21102 (`@0x40619dc`), 21104 (`@0x4061a48`) and 21106 (`@0x4061ab4`) and shows a text key for each. Meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `inviteMemberSite` @0x4061788 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::inviteMemberSite`
- `charging/ui/page/user/share_site/invite_members/invite_members_logic.dart::sendInviteMessage`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- Types of `email`, `phone`, `phone_code` and `site_id`: they are field reads on form and Rx objects (the cited addresses); the object classes were not followed. Header stays string-only. — attempted 2026-10-20 (two-hop not readable: the only caller, `InviteMembersLogic.sendInviteMessage` (`charging/ui/page/user/share_site/invite_members/invite_members_logic.dart @0x4061710`), reads form and Rx fields with no declared type. Header stays string-only)
- Whether the server requires `phone_code` as a number or a string (the value comes from an Rx object).
- Which of the two branches runs for a given user: it depends on the Rx flags at `@0x4061434`..`@0x4061534`, not decoded. — not traced 2026-10-20 in this pass (Rx flags `@0x4061434`..`@0x4061534`); the reason given in the bullet stands

## Device-tested by

none
