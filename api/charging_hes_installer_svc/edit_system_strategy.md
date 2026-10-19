> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# edit_system_strategy

## Purpose

Sends a device command that edits the system strategy of a large (HES) station; the only traced sender, the new TOU flow, uses it to save the peak sessions and the price unit of a time-of-use plan.

## Upstream name

`none` (no upstream name). The consumer twin `/charging_hes_svc/device_command` is mentioned in the list of known endpoints in `api/apitypes.py` (line 431), without a key.

## Method+URL

`POST /charging_hes_installer_svc/edit_system_strategy` (asm-traced). The URL comes from the static getter `Api.sendDeviceCommand` (`base_service/api_url.dart @0x249e524`; the Dart name is the consumer name `sendDeviceCommand`): installer string `pp+0x8ade0` (`@0x249e530`) when `isProApp` is true, otherwise `/charging_hes_svc/device_command` (`pp+0x44720`, `@0x249e53c`); see [the variant selector](README.md#variant-selector-installer-app-versus-consumer-app). The sender `TouHttpService.sendDeviceCommand` (`electricity_price/components/tou/impl_v2/service/tou_http_service.dart @0x4884e40`) loads the field at `@0x4884e5c` (`InitLateStaticField` `@0x4884e70`) and calls `HttpHelper.request` (`@0x4884ec8`) with `Method.post` (pool entry `pp+0xa7e0`, `@0x4884eb4`). Other functions load the field only to compare it with a URL (`getSaveDeviceEMSPrice` `electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x249e46c`, `setManualSetTOUDetail` `@0x31b8da8`, `getSetElectricityUsagePolicyUrl` `@0x31b9e7c`) and do not send this URL themselves.

## Encrypted?

Yes by wrapper (asm-traced): `HttpHelper.request` calls `HttpServiceImpl::encryptionRequestHttp` (`api/encryption.md`, wrapper table); `needEncryption` is not passed, so the default `true` applies ([which calls are encrypted](../encryption.md#which-calls-are-encrypted)). Whether the call goes through the SDK is decided at run time; asm alone does not decide it.

## Request

The body is the map built by `SendDeviceCommandRequest.toParams` (`electricity_price/components/tou/impl_v2/model/request_param/send_device_command_request.dart @0x4884ee0`): a map literal with three pairs (`r2 = 12`, `@0x4884f04`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | String | yes | `"<device sn or site id>"` | `send_device_command_request.dart @0x4884f10`; the value is the first request field (`@0x4884f20`); `LargeTouRepository.saveTouMode` fills it with the first non-null of two station fields (offsets 0xf then 0xb, `large_tou_repository.dart @0x4884d8c` to `@0x4884da8`), so it is either a device serial or a site id |
| `cmd` | int | yes | see [../param_types.md](../param_types.md#device-command-cmd-device_command-family) | `send_device_command_request.dart @0x4884f2c`; the value is the unboxed request field (`BoxInt64Instr` `@0x4884f3c`) set by `saveTouMode`; decode and store width are owned by `param_types.md` |
| `data` | map | yes | see below | `@0x4884f54`; the value is the request field at offset 0x13, set by `saveTouMode` (`@0x4884e1c`) |

`data` as built by `LargeTouRepository.saveTouMode` (`large_tou_repository.dart @0x4884d38`), a map literal of two pairs (`r2 = 8`, `@0x4884dbc`):

| field | type | required | example | source |
|---|---|---|---|---|
| `peak_sessions` | list | yes | not decoded | `@0x4884dc4`; value from `toPeakSessions()` of the TOU plan (`@0x4884d7c`), or the plan's alternative field when the first is null |
| `price_unit` | String | yes | `"EUR"` | `@0x4884dd8`; value is a field of the plan object (`@0x4884de8`) |

The `cmd` of this request is the device-command code, not a `param_type` command; its decoded value, raw immediate, store width and address are owned by [../param_types.md](../param_types.md#device-command-cmd-device_command-family).

## `param_type`/`cmd`

See [../param_types.md](../param_types.md#device-command-cmd-device_command-family) (device-command section); the value is not repeated here.

## Response model (link)

n/a (asm-traced): no response model; see Response.

## Response

The success handling is inside `HttpHelper.request` (`electricity_price/components/electricity_price_common/http/http_helper.dart @0x2c1447c`), which returns a `ServerResponse`; `LargeTouRepository.saveTouMode` returns it as `ServerResponse<void>` (`InitAsync` `@0x4884d6c`), so no response field is read.

## Example request/response

Request, synthesized

```json
{ "device_sn": "<device sn or site id>", "cmd": "<cmd, see param_types.md>", "data": { "peak_sessions": [], "price_unit": "EUR" } }
```

Response: no captured response; no field is read.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or shows a toast; the shared transport codes are in [../encryption.md](../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `LargeTouRepository.saveTouMode` (`electricity_price/components/tou/impl_v2/repository/large_tou_repository.dart @0x4884d38`) via `TouHttpService.sendDeviceCommand` (call `@0x4884e24`), the new TOU flow of the price module (package `electricity_price`).

## Since/changed

3.18.0: absent as an installer URL (the 3.18.0 pool holds no `installer_svc` string); the consumer twin `/charging_hes_svc/device_command` is in the 3.18.0 pool. 3.24.3: present (new). since: 3.24.3. `SendDeviceCommandRequest` and `TouHttpService` (`impl_v2`) are new in the 3.24.3 `electricity_price` package.

## Known unknowns

- Which other `cmd` values the installer endpoint accepts is not known; only one sender is traced.
- The element layout of `peak_sessions` is not traced.
- Server behaviour and the consumer twin (`device_command`, which has other senders) are not compared.

## Device-tested by

none
