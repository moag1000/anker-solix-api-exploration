> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_device_self_check

## Purpose

Polls the result of the system self-check (`SystemSelfCheckResultModel`) on the system-testing page (`SystemTestingLogic::_getSystemTestData`; callers include `onReady`, `onMessageDispatch` and the success-timer helpers) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_device_self_check` (asm-traced): URL string at `charging/ui/page/device/a5101/setting/system_self_check/system_testing/system_testing_logic.dart @0x27c9680`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x27c9678`, in `SystemTestingLogic::_getSystemTestData` (`charging/ui/page/device/a5101/setting/system_self_check/system_testing/system_testing_logic.dart @0x27c9524`), sent through `requestHttp` (`@0x27c96a8`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `SystemTestingLogic::_getSystemTestData` (`charging/ui/page/device/a5101/setting/system_self_check/system_testing/system_testing_logic.dart`, call `@0x27c96a8`, argument list `@0x27c96a0`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

(asm-traced) Each sender stores its keys in one map literal with type arguments `<String, String>` read at the cited address, so every value is a String: `SystemTestingLogic::_getSystemTestData` (`charging/ui/page/device/a5101/setting/system_self_check/system_testing/system_testing_logic.dart @0x27c9618`, 1 key). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `siteId` | string | yes | `"<siteId>"` | `charging/ui/page/device/a5101/setting/system_self_check/system_testing/system_testing_logic.dart @0x27c95a4` |

## `param_type`/`cmd`

n/a

## Response model (link)

- `charging::SystemSelfCheckResultModel`, parsed by `SystemSelfCheckResultModel.fromJson` at `charging/ui/page/device/a5101/setting/system_self_check/system_testing/system_testing_logic.dart @0x27c9708` (success closure `@0x27c96c4`, `bl` target `[package:charging/model/a5101/system_self_check_result_model.dart]`).

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::SystemSelfCheckResultModel`): `completionTime` (String?), `selfCheckStatus` (int?), `selfCheckSource` (String?), `selfCheckOperater` (int?), `selfCheckFaults` (unknown).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "siteId": "<siteId>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/device/a5101/setting/system_self_check/system_testing/system_testing_logic.dart`: `_getSystemTestData` @0x27c9524 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/ui/page/device/a5101/setting/system_self_check/system_testing/system_testing_logic.dart::_handleAppResumed`
- `charging/ui/page/device/a5101/setting/system_self_check/system_testing/system_testing_logic.dart::_restartSuccessTimerWithRemainingTime`
- `charging/ui/page/device/a5101/setting/system_self_check/system_testing/system_testing_logic.dart::_startSuccessTimerAfterSuccess`
- `charging/ui/page/device/a5101/setting/system_self_check/system_testing/system_testing_logic.dart::onMessageDispatch`
- `charging/ui/page/device/a5101/setting/system_self_check/system_testing/system_testing_logic.dart::onReady`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The polling interval and the success-timer rules: only the sender was read.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
