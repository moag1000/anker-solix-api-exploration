> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# popup_record

## Purpose

Reports that a news popup of the AIoT platform was shown or handled; sent by `AIOTRequestControllerImpl::reportAIOTPopupApi` (the inventory lists no caller, so the screen is unknown, string-only).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /app/news/popup_record` (asm-traced): URL string at `charging/http/aiot/aiot_http_request_repository_impl.dart @0x2618470`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2618468`, in `AIOTRequestControllerImpl::reportAIOTPopupApi` (`charging/http/aiot/aiot_http_request_repository_impl.dart @0x2618388`), sent through `aiotPlatformRequestHttp` (`@0x26184a0`).

## Encrypted?

encrypted: `true` (asm-traced default): `aiotPlatformRequestHttp` (`charging/http/http_request_repository_impl.dart @0x260ddd4`) calls `requestHttp` (`@0x260df68`) without `needEncryption` in its named arguments (`@0x260df60`), and `requestHttp` declares `needEncryption = true` (`charging/http/http_request_repository_impl.dart @0x2264944`). Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `popup_id` | int (unboxed, x) | yes | ? | `charging/http/aiot/aiot_http_request_repository_impl.dart @0x26183d4` (value store `@0x26183f8`) |
| `popup_name` | ? | yes | ? | `charging/http/aiot/aiot_http_request_repository_impl.dart @0x26183fc` (value store `@0x261840c`) |
| `popup_type` | ? | yes | ? | `charging/http/aiot/aiot_http_request_repository_impl.dart @0x2618410` (value store `@0x2618420`) |

The body map literal has type arguments `<String, Object?>` (`charging/http/aiot/aiot_http_request_repository_impl.dart @0x2618424`), not evidence of a value type, so `popup_name` and `popup_type` stay `?`. `popup_id` is boxed by `BoxInt64Instr` (`@0x26183e4`), so it is an unboxed int.

## `param_type`/`cmd`

n/a

## Response model (link)

not resolved (string-only): the function defines no response parser (no `fromJson` and no closure in `charging/http/aiot/aiot_http_request_repository_impl.dart @0x2618388`); the response handling is in the wrapper `aiotPlatformRequestHttp`, which was not read.

## Response

Not listed: no response key is read in the function (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "popup_id": "<popup_id>",
  "popup_name": "<popup_name>",
  "popup_type": "<popup_type>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or its closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/aiot/aiot_http_request_repository_impl.dart`: `reportAIOTPopupApi` @0x2618388 (aiotPlatformRequestHttp; encrypted: true, `needEncryption` default)

Called from:

- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::getAIOTPopupList`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of `popup_name` and `popup_type`: parameters stored into a `<String, Object?>` literal. — traced 2026-10-20: the popup model `AIOTPopup` (see [get_popups.md](get_popups.md#response)) casts `popup_name` to `String?` and `popup_type` to `int?`, the same key names the record sends; whether the closure of `DeviceMainLogic` that calls the sender forwards these fields was not followed
- Whether the wrapper reads the response: `aiotPlatformRequestHttp` was not read. — traced 2026-10-20: it does not; `aiotPlatformRequestHttp` (`charging/http/http_request_repository_impl.dart @0x260ddd4`) passes the success and fail callbacks to `requestHttp` unchanged (see [get_popups.md](get_popups.md#request)) and reads no key; what the caller closure does with the answer is the remaining question (it is the closure `(dynamic, int, String?, int?)` of `DeviceMainLogic`, `device_main_logic.dart @0x2618360`)
- Which popup event the call stands for (shown, closed, clicked): the key `popup_type` is not decoded. — attempted 2026-10-20 (two-hop not readable: the caller is a closure `(dynamic, int, String?, int?)` of `DeviceMainLogic` that forwards its own arguments (`charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x2618360`))
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
