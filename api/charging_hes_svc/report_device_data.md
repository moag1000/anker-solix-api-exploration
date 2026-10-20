> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# report_device_data

## Purpose

Triggers the renewal of the A5101 data report (`FamilyMainHttpReposity::reportDeviceData`); the success closure logs `====FamilyMainHttpReposity 触发5101设备续约` ("trigger 5101 device renewal", my translation), string-only: no caller chain in `data/endpoints.json` (string-only: no caller chain in `data/endpoints.json`, inferred from the builder name).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/report_device_data` (asm-traced): URL string at `charging/ui/page/family/family_main_http_reposity.dart @0x23ecc14`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x23ecc0c`, in `FamilyMainHttpReposity::reportDeviceData` (`charging/ui/page/family/family_main_http_reposity.dart @0x23eca98`), sent through `requestHttp` (`@0x23ecc3c`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `FamilyMainHttpReposity::reportDeviceData` (`charging/ui/page/family/family_main_http_reposity.dart`, call `@0x23ecc3c`, argument list `@0x23ecc34`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

`FamilyMainHttpReposity::reportDeviceData` (`charging/ui/page/family/family_main_http_reposity.dart @0x23eca98`) creates a map literal without type arguments (`@0x23ecb04`) holding `siteIds` (stored as received, `@0x23ecaf8`) and adds `day` with `[]=` (`@0x23ecbd0`) on one branch only: when the numeric parameter in the closure context is null or not greater than 0 (`cmp w1, NULL` `@0x23ecb1c`, `cmp x2, #0` `@0x23ecb30`, branch `@0x23ecb34`) the builder calls `getCurrentYYMMDDByDateStr` (`@0x23ecbac`) and sets `day`; otherwise it registers a timer entry (`[]=` `@0x23ecb50`, `_startTimer` `@0x23ecba0`) and sends without `day`.

| field | type | required | example | source |
|---|---|---|---|---|
| `siteIds` | list | yes |  | `charging/ui/page/family/family_main_http_reposity.dart @0x23ecaec` |
| `day` | string | optional |  | `charging/ui/page/family/family_main_http_reposity.dart @0x23ecbc8` |

Types (traced 2026-10-20): the only caller `FamilyMainPageLogic::start5101DeviceReport` builds `siteIds` itself as a growable list with the type argument `<String>` holding one element read from the logic object at offset 475 (`AllocateGrowableArray` `@0x23eca2c`, `charging/ui/page/family/family_main_page_logic.dart @0x23eca1c`..`@0x23eca3c`, call `@0x23eca7c`), so `siteIds` is a list of strings; `day` is the result of `DateUtil.getCurrentYYMMDDByDateStr`, declared `static String` (`base_service/util/date_util.dart @0x2352e04`), so it is a string.

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the sender (asm-traced): the success closure (`charging/ui/page/family/family_main_http_reposity.dart @0x23ecc58`) only logs the text with a context value (`exeInfo` `@0x23eccb8`) and reads no key; the failure callback is allocated without a context (`r2 = Null` `@0x23ecbf4`) and resolves to the same unreadable `[dart:ui]` label as in `remove_user_fault_info`.

## Response

No response key is read by the app (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "siteIds": "<siteIds>",
  "day": "<day>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the success closure; the failure callback could not be read.

## Callers in app

- `charging/ui/page/family/family_main_http_reposity.dart`: `reportDeviceData` @0x23eca98 (requestHttp; encrypted: default-true (requestHttp) — verify)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The rule that decides between the timer path and the `day` path (the numeric context value at `charging/ui/page/family/family_main_http_reposity.dart @0x23ecb30`): its source was not decoded.
- What the server renews: the app only logs the success text.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call. — reclassified: device test row 150 (traced 2026-10-20: per call the SDK login state `AkIotKitFlutter::isLogin` and the base-URL predicate decide, `HttpEncryptionDecorator.dart @0x4869504`, `@0x4869544`; the predicate is a GDT dispatch whose selector the asm does not name, and the login state is runtime data)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
