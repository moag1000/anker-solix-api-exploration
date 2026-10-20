> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# device_self_check

## Purpose

Starts the system self-check of an A5101 site from the system-testing page (`SystemTestingLogic::setSelfCheckCommand`; callers `SystemTestingLogic::_showTip` and the time-out view `build`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/device_self_check` (asm-traced): URL string at `charging/ui/page/device/a5101/setting/system_self_check/system_testing/system_testing_logic.dart @0x43300ac`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x43300a4`, in `SystemTestingLogic::setSelfCheckCommand` (`charging/ui/page/device/a5101/setting/system_self_check/system_testing/system_testing_logic.dart @0x432ffa8`), sent through `requestHttp` (`@0x43300d4`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `SystemTestingLogic::setSelfCheckCommand` (`charging/ui/page/device/a5101/setting/system_self_check/system_testing/system_testing_logic.dart`, call `@0x43300d4`, argument list `@0x43300cc`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

(asm-traced) Each sender stores its keys in one map literal with type arguments `<String, String>` read at the cited address, so every value is a String: `SystemTestingLogic::setSelfCheckCommand` (`charging/ui/page/device/a5101/setting/system_self_check/system_testing/system_testing_logic.dart @0x433005c`, 1 key). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `siteId` | string | yes | `"<siteId>"` | `charging/ui/page/device/a5101/setting/system_self_check/system_testing/system_testing_logic.dart @0x432ffec` |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the success closure (`charging/ui/page/device/a5101/setting/system_self_check/system_testing/system_testing_logic.dart @0x43304d4`) logs a fixed text (`@0x43304fc`, `exeSuccess` `@0x4330508`) and calls `_startSelfCheck` (`@0x4330518`); it reads no key and builds no model.

## Response

No response key is read by the app (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "siteId": "<siteId>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

The failure closure (`system_testing_logic.dart @0x43300f0`) compares the code (unboxed 64-bit, raw values): `200000` (`@0x4330168`, `@0x4330170`) shows the offline dialog (`a5101NetworkAbnormal`), `20301` (`@0x43301d0`, `@0x43301d4`) shows `functionLimitingTips`, `1000` (`@0x4330234`) calls `show`, `200218` (`@0x433024c`, `@0x4330254`) calls `_startSelfCheck`; any other code shows `a5101SelfCheckFailTip` (`@0x433026c`). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/device/a5101/setting/system_self_check/system_testing/system_testing_logic.dart`: `setSelfCheckCommand` @0x432ffa8 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/ui/page/device/a5101/setting/system_self_check/system_testing/system_testing_logic.dart::_showTip`
- `charging/ui/page/device/a5101/setting/system_self_check/system_testing/widgets/system_testing_timeOut_view.dart::build`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The result of the check: the app polls `get_device_self_check` for it, this call returns no key the app reads.
- What the server does on code 200218 (the app starts the self-check on that code, `charging/ui/page/device/a5101/setting/system_self_check/system_testing/system_testing_logic.dart @0x4330264`).
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
