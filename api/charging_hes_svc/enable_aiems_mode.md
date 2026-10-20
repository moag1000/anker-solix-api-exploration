> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# enable_aiems_mode

## Purpose

Switches the AI-EMS smart mode on for a site (`SmartModeLogic::enableSmartMode`, called from `SmartModePage::build`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/enable_aiems_mode` (asm-traced): URL string at `charging/ui/page/device/a5101/setting/smartMode/smart_mode_logic.dart @0x3eaefa0`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3eaef98`, in `SmartModeLogic::enableSmartMode` (`charging/ui/page/device/a5101/setting/smartMode/smart_mode_logic.dart @0x3eaee94`), sent through `encryptionRequestHttp` (`@0x3eaefc8`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- `encryptionRequestHttp` forwards `needEncryption` with its default true to `requestHttp` (`api/encryption.md`): `SmartModeLogic::enableSmartMode` (`charging/ui/page/device/a5101/setting/smartMode/smart_mode_logic.dart`, call `@0x3eaefc8`).

## Request

(asm-traced) Each sender stores its keys in one map literal with type arguments `<String, String>` read at the cited address, so every value is a String: `SmartModeLogic::enableSmartMode` (`charging/ui/page/device/a5101/setting/smartMode/smart_mode_logic.dart @0x3eaef50`, 1 key). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `siteId` | string | yes | `"<siteId>"` | `charging/ui/page/device/a5101/setting/smartMode/smart_mode_logic.dart @0x3eaef14` |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the success closure (`charging/ui/page/device/a5101/setting/smartMode/smart_mode_logic.dart @0x3eaf020`) logs a fixed text (`@0x3eaf038`) and opens the named route `/smartModeStartSuccessPage` (`GetNavigation.toNamed` `@0x3eaf078`); it reads no response key and builds no model.

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

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `ak_soft_ems/http/ems_api.dart`: `enableAiEmsMode` @0x379e6d0 (URL literal only, no `*Http*` call; sender `EmsAiModeConditionLogic::_enableLargeSmartMode` (`ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x379e4b8`), reached through callers `EmsAiModeConditionLogic::_enableLargeSmartMode` (`ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x379e4b8`); resolved from the URL literal at `ak_soft_ems/http/ems_api.dart @0x379e6e8` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))
- `charging/ui/page/device/a5101/setting/smartMode/smart_mode_logic.dart`: `enableSmartMode` @0x3eaee94 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/ui/page/device/a5101/setting/smartMode/smart_mode_view.dart::build`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What the server answers or changes besides the mode flag: the app ignores the body.
- Whether the failure closure (`charging/ui/page/device/a5101/setting/smartMode/smart_mode_logic.dart @0x3eaefe4`) distinguishes error codes: it logs a fixed text and was not read further.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
