> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# join_site

## Purpose

Answers a site-share invitation: `MessageSystemDetailLogic::shareSiteJoin` sends status 2 and `MessageSystemDetailLogic::shareSiteRefuse` sends status 3 from the system-message detail page; `DeviceMainLogic::shareSiteMembersDialog` (device main page) sends both values from its dialog buttons.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/share_site/join_site` (asm-traced): URL string at `http_request_repository_impl.dart @0x2607644`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x260763c`, in `HttpRequestControllerImpl::joinSite` (`http_request_repository_impl.dart @0x26075c0`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The builder `joinSite` (`http_request_repository_impl.dart @0x26075c0`) forwards a body map built by its callers; every caller builds a 2-pair map literal typed `<String, dynamic>` (`AllocateArray r2 = 8`).

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | string | yes | `"<site_id>"` | `shareSiteJoin`: key `@0x4028b90`, store `@0x4028bd0`, empty-string default `r2 = ""` `@0x4028bcc`; `shareSiteRefuse`: key `@0x4029380`, store `@0x40293c0`, default `@0x40293bc`; the two device-main closures read a context field instead (`device_main_logic.dart @0x2607494`, `@0x2607720`, no default) |
| `status` | int (Smi, w) | yes | `2` or `3` | `mov x16, #4` + `stur w16`, tagged, so 2: `shareSiteJoin` `@0x4028be0`, device-main closure `@0x2607738`; `mov x16, #6`, so 3: `shareSiteRefuse` `@0x40293d0`, device-main closure `@0x26074ac` |

## `param_type`/`cmd`

n/a

## Response model (link)

None found in the resolved callbacks, but not complete. The message-detail callbacks (`message_system_detail_logic.dart @0x4028f24`, `@0x4028c58`, `@0x4029448`) load no argument and call no `fromJson` (they update the message list and the site list); the device-main callback `device_main_logic.dart @0x26077b0` loads no argument. The call site at `device_main_logic.dart @0x2607450` passes a second callback that is a pool entry printed as `Function: [dart:ui] _NativeScene::_NativeScene._ (0x49c1cac)` (not readable).

## Response

No response key is read in the resolved callbacks.

## Example request/response

Request, synthesized (decrypted body as built by `shareSiteJoin`)

```json
{"site_id": "<site_id>", "status": 2}
```

Response: none parsed in the resolved callbacks.

## Errors seen

One compare is traced: the device-main failure callback `device_main_logic.dart @0x2607688` compares the code (32-bit compare, raw 42206, so 21103, `@0x26076a0`) and shows the text key `expired`. Meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `joinSite` @0x26075c0 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::joinSite`
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::shareSiteMembersDialog`
- `charging/ui/page/message/messageSystemDetail/message_system_detail_logic.dart::shareSiteJoin`
- `charging/ui/page/message/messageSystemDetail/message_system_detail_logic.dart::shareSiteRefuse`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- Response handling of the device-main call site `@0x2607450`: its second callback is an unresolved placeholder pool entry. Header stays string-only for this reason.
- Type of `site_id` in the two device-main closures: it is read from a closure context field with no default (`@0x2607494`, `@0x2607720`).
- What status 2 and 3 mean to the server: derived only from the caller names `shareSiteJoin` and `shareSiteRefuse`.

## Device-tested by

none
