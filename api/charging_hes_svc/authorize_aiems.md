> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# authorize_aiems

## Purpose

Authorizes the AI-EMS data usage of a site towards the cloud after the user confirms the data-authorization dialog (`SmartModeLogic::showDataAuthorizationDialog` leads to `SmartModeLogic::authorizeAiEmsToCloud`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/authorize_aiems` (asm-traced): URL string at `charging/ui/page/device/a5101/setting/smartMode/smart_mode_logic.dart @0x3eb26d8`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3eb26d0`, in `SmartModeLogic::authorizeAiEmsToCloud` (`charging/ui/page/device/a5101/setting/smartMode/smart_mode_logic.dart @0x3eb25d8`), sent through `encryptionRequestHttp` (`@0x3eb2700`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- `encryptionRequestHttp` forwards `needEncryption` with its default true to `requestHttp` (`api/encryption.md`): `SmartModeLogic::authorizeAiEmsToCloud` (`charging/ui/page/device/a5101/setting/smartMode/smart_mode_logic.dart`, call `@0x3eb2700`).

## Request

(asm-traced) Each sender stores its keys in one map literal with type arguments `<String, String>` read at the cited address, so every value is a String: `SmartModeLogic::authorizeAiEmsToCloud` (`charging/ui/page/device/a5101/setting/smartMode/smart_mode_logic.dart @0x3eb2688`, 1 key). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `siteId` | string | yes | `"<siteId>"` | `charging/ui/page/device/a5101/setting/smartMode/smart_mode_logic.dart @0x3eb264c` |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the success closure (`charging/ui/page/device/a5101/setting/smartMode/smart_mode_logic.dart @0x3eb27c8`) logs a fixed text (`@0x3eb27f0`), sets a flag to `true` (`value=` `@0x3eb2820`) and calls `GetNavigation.back` (`@0x3eb284c`); it reads no response key and builds no model.

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

- `ak_soft_ems/http/ems_api.dart`: `authorizeAiEms` @0x37a447c (URL literal only, no `*Http*` call; sender `EmsAiModeConditionLogic::authorizeAiEmsToCloud` (`ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x37a4244`), reached through callers `EmsAiModeConditionLogic::authorizeAiEmsToCloud` (`ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x37a4244`); resolved from the URL literal at `ak_soft_ems/http/ems_api.dart @0x37a4494` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))
- `charging/ui/page/device/a5101/setting/smartMode/smart_mode_logic.dart`: `authorizeAiEmsToCloud` @0x3eb25d8 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/ui/page/device/a5101/setting/smartMode/smart_mode_logic.dart::showDataAuthorizationDialog`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What the `true` flag set in the success closure controls on the smart-mode page: the field is reached by two `LoadField` steps (`charging/ui/page/device/a5101/setting/smartMode/smart_mode_logic.dart @0x3eb2804`, `@0x3eb280c`) that were not resolved to a name.
- What the server does with the authorization or whether it answers with a body (the app ignores the answer).
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
