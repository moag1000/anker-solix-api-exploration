> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_vpp_check_code

## Purpose

Reads the VPP participation state of a station: `HttpRequestControllerImpl::getVppInfo` (callers `HomeSettingLogic::requestVppInfo` and `requestVppInfo` in `charging/ui/page/device/a5101/setting/vpp/controller.dart`) and `VppMenuController::checkSupport` (called from `onInit` of `settings/src/common/menu_controller/vpp_menu_controller.dart`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_vpp_check_code` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x292c70c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x292c704`, in `HttpRequestControllerImpl::getVppInfo` (`charging/http/http_request_repository_impl.dart @0x292c5a0`), sent through `requestHttp` (`@0x292c734`).

Same URL and method object in the other sender(s) read:

- `VppMenuController::checkSupport` (`settings/src/common/menu_controller/vpp_menu_controller.dart @0x367abf4`): URL string `@0x367ad7c`, method object `Method.post` (`pp+0xa7e0`) at `@0x367ad74`, sent through `encryptionRequestHttp` (`@0x367ada4`).

## Encrypted?

encrypted: `true` for the `encryptionRequestHttp` sender(s), "default-true (requestHttp)" for the `requestHttp` sender(s). Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- `encryptionRequestHttp` forwards `needEncryption` with its default true to `requestHttp` (`api/encryption.md`): `VppMenuController::checkSupport` (`settings/src/common/menu_controller/vpp_menu_controller.dart`, call `@0x367ada4`).
- No named argument `needEncryption` is passed by `HttpRequestControllerImpl::getVppInfo` (`charging/http/http_request_repository_impl.dart`, call `@0x292c734`, argument list `@0x292c72c`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

Both senders store 3 keys in a map literal with type arguments `<String, Object>` (`charging/http/http_request_repository_impl.dart @0x292c6a4`, `settings/src/common/menu_controller/vpp_menu_controller.dart @0x367ad2c`), which do not type the values. `current_version` is the current time in seconds in both: `_getCurrentMicros` is divided twice by 1000 (`sdiv` `@0x292c660`, `@0x292c664`; `settings/src/common/menu_controller/vpp_menu_controller.dart @0x367ace8`, `@0x367acec`) and boxed from an unboxed 64-bit integer (`BoxInt64Instr` `@0x292c668`, `settings/src/common/menu_controller/vpp_menu_controller.dart @0x367acf0`). In `checkSupport`, `get_code` is the constant `false` (`@0x367acac`) and `station_id` is a value that falls back to the empty string (`@0x367ac98`). In `getVppInfo`, `station_id` and `get_code` come from parameters (`@0x292c610`, `@0x292c624`), stored as received.

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x292c600`; `settings/src/common/menu_controller/vpp_menu_controller.dart @0x367ac60` |
| `get_code` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x292c614`; `settings/src/common/menu_controller/vpp_menu_controller.dart @0x367aca0` |
| `current_version` | int (unboxed, x) | yes | current time in seconds | `charging/http/http_request_repository_impl.dart @0x292c628`; `settings/src/common/menu_controller/vpp_menu_controller.dart @0x367acb4` |

Values of `get_code` (app side, traced 2026-10-20): `HomeSettingLogic::requestVppInfo` passes the bool constant `false` as the second argument of `getVppInfo` (`r3 = false`, `charging/ui/page/device/a5101/setting/homeSetting/home_setting_logic.dart @0x292c488`, call `@0x292c494`) and `VppMenuController::onInit` calls `checkSupport` with `false` (`r2 = false`, `settings/src/common/menu_controller/vpp_menu_controller.dart @0x367abc4`, call `@0x367abd8`); `VppController::requestVppInfo` (`charging/ui/page/device/a5101/setting/vpp/controller.dart @0x2978a84`, call `@0x2978a94`) passes a slot of its own frame. So `get_code` is a bool in two of the three call paths and `false` in both of them.

## `param_type`/`cmd`

n/a

## Response model (link)

- [`VppInfoModel`](../../models/hes.md#vppinfomodel), parsed by `VppInfoModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x292c874` (success closure `@0x292c808`, `bl` target `[package:charging/ui/page/device/a5101/setting/vpp/vpp_info_model.dart]`). This parse belongs to `getVppInfo`. The sender `VppMenuController::checkSupport` has no `fromJson`: its success closure (`settings/src/common/menu_controller/vpp_menu_controller.dart @0x367ae38`) reads the keys `joinStatus` (`@0x367af38`, default `false`), `vppEnable` (`@0x367af74`, default `false`), `hasIncompatibleDevice` (`@0x367b050`) and `parallelSupportDeviceNames` (`@0x367b0a4`, a list copied to a `List<String>` `@0x367b1d0`) into controller fields.

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::VppInfoModel`): `vppEnable` (bool?), `joinStatus` (bool?), `leftTime` (int?), `currentVpp` (String?), `checkCode` (String?), `systemCode` (String?), `joinTime` (String?), `vppType` (List?), `processingStatus` (int?), `sn` (String?), `needFirmwareUpgrade` (bool), `publicProtocolBusinesses` (List?), `privateProtocolBusinesses` (List?), `vppServicePolicy` (VppServicePolicyModel?).

`VppMenuController::checkSupport` reads these keys directly: `joinStatus` (bool, default false), `vppEnable` (bool, default false), `hasIncompatibleDevice` (bool) and `parallelSupportDeviceNames` (List of String).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "station_id": "<station_id>",
  "get_code": "<get_code>",
  "current_version": "<current_version>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`. The failure closure of `getVppInfo` (`charging/http/http_request_repository_impl.dart @0x292c750`) forwards the code and message to the stored callback when one is set (`ClosureCall` `@0x292c794`) and logs `---> getVppInfo failed, code`; the failure closure of `checkSupport` (`settings/src/common/menu_controller/vpp_menu_controller.dart @0x367adc4`) logs `requestVppInfo failed: `.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getVppInfo` @0x292c5a0 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `settings/src/common/menu_controller/vpp_menu_controller.dart`: `checkSupport` @0x367abf4 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getVppInfo`
- `charging/ui/page/device/a5101/setting/homeSetting/home_setting_logic.dart::requestVppInfo`
- `charging/ui/page/device/a5101/setting/vpp/controller.dart::requestVppInfo`
- `settings/src/common/menu_controller/vpp_menu_controller.dart::onInit`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The type of `station_id` and of the `get_code` value passed by `VppController::requestVppInfo`: slots of the caller frames (`charging/ui/page/device/a5101/setting/homeSetting/home_setting_logic.dart @0x292c47c`, `charging/ui/page/device/a5101/setting/vpp/controller.dart @0x2978a80`); `get_code` is a bool constant in the other two paths (Request) — attempted 2026-10-20 (two-hop not readable).
- What `get_code` selects: `checkSupport` sends the constant false, `getVppInfo` a caller value. — traced 2026-10-20: the app sends `false` from `HomeSettingLogic::requestVppInfo` and `checkSupport`, and a frame slot from `VppController::requestVppInfo` (Request); what `true` selects on the server is not known from the app
- Why `current_version` is the current time: the app sends seconds since the epoch (two integer divisions of the microsecond clock); the server meaning is not known.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call. — reclassified: device test row 150 (traced 2026-10-20: per call the SDK login state `AkIotKitFlutter::isLogin` and the base-URL predicate decide, `HttpEncryptionDecorator.dart @0x4869504`, `@0x4869544`; the predicate is a GDT dispatch whose selector the asm does not name, and the login state is runtime data)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
