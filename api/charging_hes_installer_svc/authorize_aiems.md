> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# authorize_aiems

## Purpose

Authorizes the AI EMS (AI energy management) of a site in the cloud; the app sends the site id and, on success, marks the site as authorized and closes the current page.

## Upstream name

`none` (no upstream name). The consumer twin `/charging_hes_svc/authorize_aiems` has no upstream key and is not mentioned in `api/apitypes.py`.

## Method+URL

`POST /charging_hes_installer_svc/authorize_aiems` (asm-traced). The URL comes from the static getter `EmsApi.authorizeAiEms` (`ak_soft_ems/http/ems_api.dart @0x37a447c`): installer string `pp+0xe88c0` (`@0x37a4488`) when `isProApp` is true, otherwise `/charging_hes_svc/authorize_aiems` (`pp+0xbe0e0`, `@0x37a4494`); see [the variant selector](README.md#variant-selector-installer-app-versus-consumer-app). The sender `EmsAiModeConditionLogic.authorizeAiEmsToCloud` (`ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x37a4244`) loads the field at `@0x37a42a0` (`InitLateFinalStaticField` `@0x37a42bc`) and passes `Method.post` (pool entry `pp+0xa7e0`, `@0x37a4330`).

## Encrypted?

Yes by wrapper (asm-traced): ``authorizeAiEmsToCloud`` calls `encryptionRequestHttp` (`ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x37a435c`) without passing `needEncryption`, so the default `true` applies (`api/encryption.md`, [which calls are encrypted](../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time (SDK login state and a base-URL test, [encryption.md](../encryption.md)); asm alone does not decide it. The loading overlay is off (`showLoading: false`, `@0x37a4344`).

## Request

Map literal with one string pair (`r2 = 4`, `@0x37a42c4`).

| field | type | required | example | source |
|---|---|---|---|---|
| `siteId` | String | yes | `"<site id>"` | `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x37a42d0`; value is the object field at offset 0x4b (`@0x37a42e0`), the same field `_enableLargeSmartMode` and `_getLargeAuthorizationStatus` use as site id |

Unlike [check_function](check_function.md) and [get_system_strategy](get_system_strategy.md), this body has no `isProApp` branch: both variants send `siteId`.

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): no model is parsed.

## Response

No response field is read (asm-traced). The success closure `@0x37a43e0` logs `authorizeAiEms success` (`@0x37a4408`), sets the observable at field offset 0x97 to `true` (`@0x37a4430`, a `value=` call) and calls `GetNavigation.back` (`@0x37a4460`). The failure closure `@0x37a437c` only logs `authorizeAiEms fail, code: ...` (`@0x37a43a0`).

## Example request/response

Request, synthesized

```json
{ "siteId": "<site id>" }
```

Response: no captured response; the app ignores the payload.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or shows a toast; the shared transport codes are in [../encryption.md](../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../errors.md).

## Callers in app

- `EmsAiModeConditionLogic.authorizeAiEmsToCloud` (`ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x37a4244`), the AI mode condition screen of the `ak_soft_ems` package (class `EmsAiModeConditionLogic`). The UI element that triggers it was not traced.

## Since/changed

3.18.0: absent as an installer URL (the 3.18.0 pool holds no `installer_svc` string); the consumer twin `/charging_hes_svc/authorize_aiems` is in the 3.18.0 pool. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- Server behaviour (what the authorization changes, whether it can be revoked) is not known; the matching read is the `isAuthorizeAIEms` flag of [get_system_strategy](get_system_strategy.md#response).
- The trigger in the UI (which button calls `authorizeAiEmsToCloud`) is not traced.

## Device-tested by

none
