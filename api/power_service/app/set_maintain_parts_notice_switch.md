> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# set_maintain_parts_notice_switch

## Purpose

Called by the A7320 maintenance page (`A7320MaintanceLogic::setMaintainPartsNoticeSwitchRequest`, fired from the notice switch of `a7320_maintance_page.dart`) to turn the maintenance-part notice on or off.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/set_maintain_parts_notice_switch` (asm-traced): URL string at `a7320_requet_api.dart @0x3a0a55c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3a0a554`, in `A7320RequestApi::setMaintainPartsNoticeSwitchRequest` (`a7320_requet_api.dart @0x3a0a46c`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is a 2-pair map literal (`<String, Object>`, `AllocateArray r2 = 8`, `@0x3a0a4e0`). The caller passes `ankerDevice.field_6b` (`@0x3a0a404`), `field_6b` is the `deviceSn` getter, typed `String` in `String dyn:get:deviceSn(AnkerDevice)` at `anker_device.dart @0x22053d4`.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | key `@0x3a0a4e8`, value store `@0x3a0a4f8` (parameter r1; caller `a7320_maintance_logic.dart @0x3a0a404`) |
| `notice_switch` | bool | yes | `true` | key `@0x3a0a4fc`, value store `@0x3a0a50c` (parameter r3); the two call sites in `a7320_maintance_page.dart` pass the literals `true` (`r2 = true` `@0x3a0a220`) and `false` (`r2 = false` `@0x3a0a390`) |

## `param_type`/`cmd`

n/a

## Response model (link)

None: the response body is not parsed by the app. The success callback `a7320_maintance_logic.dart @0x3a0a6a0` uses its argument once, in the log string `"setMaintainPartsNoticeSwitchRequest--"` (`@0x3a0a6f8`, argument load `@0x3a0a704`), then stores a value into an Rx field (`value=` `@0x3a0a760`) and fires a `MessageEvent` (`@0x3a0a7a0`).

## Response

No response key is read by the app. The builder wraps the callbacks the caller supplied (`postJML` closure templates `@0x2268374`/`@0x226824c`, `pp+0xaa630`/`pp+0xaa638`).

## Example request/response

Request, synthesized (decrypted body as built by `setMaintainPartsNoticeSwitchRequest`)

```json
{"device_sn": "<device_sn>", "notice_switch": true}
```

Response: none parsed.

## Errors seen

None traced. The failure callback `@0x3a0a5a4` logs the code (`"setMaintainPartsNoticeSwitchRequest code--"` `@0x3a0a5ec`) and shows a `commonOK` dialog (`showDialog` `@0x3a0a680`); no code is compared. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart`: `setMaintainPartsNoticeSwitchRequest` @0x3a0a46c (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- The response body: the app does not read it, so its keys are unknown.
- Whether the server treats a repeated call with the same `notice_switch` as a no-op: not derivable from the app.
- The effect of the `MessageEvent` fired by the success callback on other pages was not followed.

## Device-tested by

none
