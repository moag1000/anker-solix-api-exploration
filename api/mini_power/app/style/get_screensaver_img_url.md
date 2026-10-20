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

## `param_type`/`cmd`

n/a

## Response model (link)

not extracted: the sender body is not in the asm dump, so the response handling cannot be read (the callbacks passed at the first call site are the closures `small_charging_platform/src/screen_setting/clock_style/page/clock_style_logic.dart @0x2803a40` and `@0x28039cc`, not read).

## Response

No response key is confirmed read (see Response model).

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

- The method, the request keys (`id`, `type` are 3.18.0 inventory rows), their types and whether they are required: the sender body is not in the asm dump. The call site `@0x2802a64` suggests an integer id and a string type (`festival`), which does not prove the stores.
- Which `type` values exist besides `festival`.
- The response shape and how the callbacks use it.
- Header stays `string-only` because Method, request types and the response model are missing.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
