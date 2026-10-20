> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_invited_list

## Purpose

Lists the members of a shared site by invite status: `HomeCenterLogic::getInviteMemberInviting` requests status 1 and `HomeCenterLogic::getInviteMemberAlreadyInvited` requests status 2 for the home-center page.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/share_site/get_invited_list` (asm-traced): URL string at `http_request_repository_impl.dart @0x291634c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2916344`, in `HttpRequestControllerImpl::getInviteMember` (`http_request_repository_impl.dart @0x2916284`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is a 2-pair map literal (`AllocateArray` in `getInviteMember`, `http_request_repository_impl.dart @0x2916284`).

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | string | yes | `"<site_id>"` | key `charging/http/http_request_repository_impl.dart @0x29162d4`, value store `@0x29162e4`; both callers pass `field_7` of an Rx value with the empty string for null (`r0 = ""` `home_center_logic.dart @0x291618c` and `@0x2916ce4`) |
| `status` | int (Smi, w) | yes | `1` or `2` | key `charging/http/http_request_repository_impl.dart @0x29162e8`, `lsl x2, x1, #1` `@0x29162f8` (Smi-tagging the unboxed parameter), store `@0x29162fc`; `getInviteMemberInviting` passes `r3 = 1` (`charging/ui/page/user/share_site/home_center/home_center_logic.dart @0x29161c0`, unboxed), `getInviteMemberAlreadyInvited` passes `r3 = 2` (`@0x2916d10`) |

## `param_type`/`cmd`

n/a

## Response model (link)

`charging::SiteInviteMemberModel` (`data/models.json` key; fields listed on [`models/account.md`](../../../../models/account.md)), parsed per list element in the success closure `http_request_repository_impl.dart @0x2916390` (key string `invited_list`, `SiteInviteMemberModel.fromJson`).

## Response

The success closure reads the key `invited_list` of the response data and parses every element with `SiteInviteMemberModel.fromJson`. Keys of one element (from `data/models.json`, all nullable): `site_id` (String), `user_id` (String), `member_id` (String), `email` (String), `phone` (String), `status` (int), `member_type` (int).

## Example request/response

Request, synthesized (decrypted body as built by `getInviteMember`)

```json
{"site_id": "<site_id>", "status": 1}
```

Response, synthesized (keys from `SiteInviteMemberModel.fromJson`; values are placeholders, not a capture)

```json
{"code": 0, "msg": "success", "data": {"invited_list": [{"site_id": "<site_id>", "user_id": "<user_id>", "member_id": "<member_id>", "email": "<email>", "phone": "<phone>", "status": 0, "member_type": 0}]}}
```

## Errors seen

None traced: the success closure `@0x2916390` compares no error code; the builder's failure callback is an unresolved placeholder pool entry (`pp+0xc1390`, `@0x2916324`). Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getInviteMember` @0x2916284 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getInviteMember`
- `charging/ui/page/user/share_site/home_center/home_center_logic.dart::getInviteMemberAlreadyInvited`
- `charging/ui/page/user/share_site/home_center/home_center_logic.dart::getInviteMemberInviting`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`; the model `SiteInviteMemberModel` is `≤3.18.0` in `data/models.json` with no removed keys.

## Known unknowns

- What the status values 1 and 2 stand for on the server: the callers use them for the "inviting" and "already invited" tabs (function names only).
- Whether the response carries keys other than `invited_list` that the app ignores.
- The meaning of `member_type` values: not decoded here. — reclassified: server (the value meanings are defined by the server)

## Device-tested by

none
