> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

3.24.3: string present in the object pool, no code reference found (present in 3.18.0 with a sender)

# get_screensaver_img_url

## Purpose

Fetches the image URL of a screensaver for the preview in the small-charging-platform screen settings (callers `_syncTopPreviewByCurrentSelection` in the clock-style logic and `_syncThumbPreview` in the screen logic) (string-only: the sender body is not in the asm dump; the caller names are read, the meaning comes from names only).

## Upstream name

`none` (no upstream name)

## Method+URL

`/mini_power/v1/app/style/get_screensaver_img_url`, method: not extracted (string-only). The 3.24.3 object pool holds the URL string (`pp+0x9f270`), but no decoded function references it: the senders are mixin-deduplicated functions (`[dart:mixin_deduplication]`) whose bodies Blutter did not write to the asm dump, so neither the method object nor the key stores can be read. Call sites in 3.24.3:

- `small_charging_platform/src/screen_setting/clock_style/page/clock_style_logic.dart`: `_syncTopPreviewByCurrentSelection` (`@0x280297c`) calls the mixin function at `@0x2802a64`, passing an unboxed integer (`LoadInt32Instr` `@0x2802a04`, tested `cmp x2, #0` `@0x2802a14`) and the string `festival` (`@0x2802a58`).
- `small_charging_platform/src/screen_setting/screen/screen_logic.dart`: `_syncThumbPreview` (`@0x2ce7660`) calls it at `@0x2ce7724`.

## Encrypted?

encrypted: `true` per the 3.18.0 inventory (`encryptionRequestHttp`); not re-read in 3.24.3 because the sender body is not in the asm dump. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

Not re-read in 3.24.3: the sender is a mixin-deduplicated function whose body is not in the asm dump (see Method+URL), so the keys below are the 3.18.0 inventory rows (`data/endpoints.json`); their addresses do not exist in the 3.24.3 asm and are therefore not cited. No type, requiredness or value is read.

| field | type | required | example | source |
|---|---|---|---|---|
| `id` | ? | ? | ? | 3.18.0 inventory row, not present in the 3.24.3 asm |
| `type` | ? | ? | ? | 3.18.0 inventory row, not present in the 3.24.3 asm |

3.18.0 builder read (traced 2026-10-20, 3.18.0 asm tree, not the 3.24.3 app): `getScreensaverImgUrl` (`small_charging_platform/src/screen_setting/clock_style/page/clock_style_logic.dart @0x2550030` in the 3.18.0 tree) fills a `<String, Object>` literal (`@0x25500e8`, 4 slots `@0x25500a4`) with `id` (an unboxed integer boxed by `BoxInt64Instr`, `@0x25500c0`) and `type` (a parameter stored as received, `@0x25500e4`) and sends it with `encryptionRequestHttp` (`@0x255015c`) and the method object `Obj!Method@2c736e1` (name `post`), so POST in 3.18.0 with `id` an integer; the success closure is the shared forwarder `charging/http/http_request_repository_impl.dart @0x19dc8a8` (3.18.0). The page stays `string-only` because the 3.24.3 sender body is not in the dump.

## `param_type`/`cmd`

n/a

## Response model (link)

not extracted: the sender body is not in the asm dump, so the response handling cannot be read (the callbacks passed at the first call site are the closures `small_charging_platform/src/screen_setting/clock_style/page/clock_style_logic.dart @0x2803a40` and `@0x28039cc`, not read).

## Response

No response key is confirmed read (see Response model).

Callback keys (traced 2026-10-20, 3.24.3 app side): the success closure `small_charging_platform/src/screen_setting/clock_style/page/clock_style_logic.dart @0x2803a40` requires the answer to be a `Map` (`@0x2803af0`) and reads the keys `img_url` (`String?`, `@0x2803b30`..`@0x2803b7c`) and `url` (`String?`, `@0x2803b98`..`@0x2803be4`); the failure closure (`@0x28039cc`) logs `Failed to get holiday theme image: ` (`@0x28039f0`).

## Example request/response

Request: not synthesized (the keys are not re-read in 3.24.3, see Request).

Response: not synthesized (no capture exists for this endpoint).

## Errors seen

none traced: the sender body is not in the asm dump, so the failure path of the request is not readable. Code meanings are owned by `api/errors.md`.

## Callers in app

- `small_charging_platform/src/screen_setting/clock_style/page/clock_style_logic.dart`: `getScreensaverImgUrl` (3.18.0 inventory, encryptionRequestHttp; address not present in the 3.24.3 asm)

## Since/changed

3.18.0: present (with a sender in the inventory). 3.24.3: the URL string is in the object pool (`pp+0x9f270`) and the callers listed under Method+URL still call the sender, but the sender body is not in the asm dump; `tools/out/diff_3.18.0_3.24.3.md` lists the URL under Removed endpoints (string-level). since: <=3.18.0. Treat the URL as still in use (the callers exist) until a capture says otherwise.

## Known unknowns

- The method, request keys and types of the 3.24.3 sender: the 3.18.0 builder is read (see Request), the 3.24.3 mixin-deduplicated body is not in the dump — traced 2026-10-20
- Which `type` values exist besides `festival`. — traced 2026-10-20: the only 3.24.3 call site that passes a text passes `festival` (`clock_style_logic.dart @0x2802a58`), and the failure text of the callback speaks of a holiday theme image; other values are not passed in the code read
- Header stays `string-only` because Method, request types and the response model are missing. — rechecked 2026-10-20: still true; the typing attempts are recorded on the bullets of this section
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
