> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# clear_share

## Purpose

Removes the sharing of a device when the owner removes it; sent by `RemoveDeviceController::_clearShareDevice` (`base_service/view/general_setting/remove_device_controller.dart @0x2816cb0`) from `_handleDeviceRemoval` (also `Ae100RemoveDeviceController::_handleDeviceRemoval`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /app/devicerelation/clear_share` (asm-traced): URL string at `base_service/view/general_setting/remove_device_controller.dart @0x2816d4c`, in `RemoveDeviceController::_clearShareDevice` (`base_service/view/general_setting/remove_device_controller.dart @0x2816cb0`), sent through `AkNetwork::requestHttp` (`@0x2816d5c`; `base_service/util/ak_util/src/ak_network.dart @0x21c3444`). That function builds a map with the keys `path` (`@0x21c34e0`), `method` with the constant string `"POST"` (`@0x21c34fc`) and `param` (`@0x21c3508`) and hands it to the SDK handler `akiot.cloud_api` (`@0x21c3534`, `handle` `@0x21c3544`).

## Encrypted?

not decided by the Dart sender: the request goes through the SDK handler `akiot.cloud_api` (`base_service/util/ak_util/src/ak_network.dart @0x21c3544`), so the signing and encryption rules of the SDK path in `api/encryption.md` apply (the inventory flag "default-true (requestHttp)" came from the name `requestHttp`).

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | yes | ? | `base_service/view/general_setting/remove_device_controller.dart @0x2816d14` (value store `@0x2816d24`) |
| `member_type` | int (Smi, w) | yes | `1` | `base_service/view/general_setting/remove_device_controller.dart @0x2816d28` (value store `@0x2816d38`) |

The map literal has type arguments `<String, dynamic>` (`base_service/view/general_setting/remove_device_controller.dart @0x2816d3c`), not evidence of a value type, so `device_sn` stays `?`. The sender returns early with the log `clearDeviceSn is empty` when the argument is null or empty (`@0x2816ce8`, `@0x2816cec`). `member_type` is the Smi raw 2 stored with a 32-bit store (`@0x2816d34`, `@0x2816d38`), so 1.

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced for the sender): `_clearShareDevice` awaits the result of `AkNetwork::requestHttp` (`Await` `@0x2816d68`) and returns without reading it (`@0x2816d70`).

## Response

No response key is read by the sender (see Response model). `AkNetwork::requestHttp` itself reads the key `data` from the handler result (`base_service/util/ak_util/src/ak_network.dart @0x21c3630`) and returns it as `Map<String, dynamic>?`.

Result handling (traced 2026-10-20, app side): `RemoveDeviceController::_clearShareDevice` (`base_service/view/general_setting/remove_device_controller.dart @0x2816cb0`) awaits `requestHttp` (`@0x2816d68`) and then returns null (`@0x2816d6c`, `ReturnAsyncNotFuture` `@0x2816d70`); the result map is not read and no error is propagated to the callers `_handleDeviceRemoval`.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<device_sn>",
  "member_type": 1
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `base_service/view/general_setting/remove_device_controller.dart`: `_clearShareDevice` @0x2816cb0 (`AkNetwork::requestHttp`, SDK handler `akiot.cloud_api`; encryption per the SDK path, see Encrypted?)

Called from:

- `balcony/src/ae100/settings/ae100_remove_device_controller.dart::_handleDeviceRemoval`
- `base_service/view/general_setting/remove_device_controller.dart::_handleDeviceRemoval`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Type of `device_sn`: a parameter stored into a `<String, dynamic>` literal. — attempted 2026-10-20 (two-hop not readable: `_handleDeviceRemoval` (`balcony/src/ae100/settings/ae100_remove_device_controller.dart @0x471b384`), `_handleDeviceRemoval` (`base_service/view/general_setting/remove_device_controller.dart @0x2815ebc`) pass slots or fields of their own frames; no literal or declared type in the argument setups)
- What `member_type` 1 means (owner versus sharer): the value is a constant; the server table is not visible.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
