> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# enable_aiems_mode

## Purpose

Switches the AI EMS mode (the "smart mode" of a large HES system) on for a site; on success the app opens the smart-mode start-success page.

## Upstream name

`none` (no upstream name). The consumer twin `/charging_hes_svc/enable_aiems_mode` is mentioned in the list of known endpoints in `api/apitypes.py` (line 435), without a key.

## Method+URL

`POST /charging_hes_installer_svc/enable_aiems_mode` (asm-traced). The URL comes from the static getter `EmsApi.enableAiEmsMode` (`ak_soft_ems/http/ems_api.dart @0x379e6d0`): installer string `pp+0xe8748` (`@0x379e6dc`) when `isProApp` is true, otherwise `/charging_hes_svc/enable_aiems_mode` (`pp+0xbdfb0`, `@0x379e6e8`); see [the variant selector](README.md#variant-selector-installer-app-versus-consumer-app). The sender `EmsAiModeConditionLogic._enableLargeSmartMode` (`ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x379e4b8`) loads the field at `@0x379e51c` and passes `Method.post` (pool entry `pp+0xa7e0`, `@0x379e5ac`). A second, consumer-only sender (`SmartModeLogic.enableSmartMode`, `charging/ui/page/device/a5101/setting/smartMode/smart_mode_logic.dart @0x3eaee94`) uses the literal consumer URL and is described on the page of the consumer URL.

## Encrypted?

Yes by wrapper (asm-traced): ``_enableLargeSmartMode`` calls `encryptionRequestHttp` (`ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x379e5d8`) without passing `needEncryption`, so the default `true` applies (`api/encryption.md`, [which calls are encrypted](../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time (SDK login state and a base-URL test, [encryption.md](../encryption.md)); asm alone does not decide it. The loading overlay is on (`showLoading: true`, `@0x379e5c0`).

## Request

Map literal with one string pair (`r2 = 4`, `@0x379e540`). The function returns without a request when the site id string is empty (length load `@0x379e4dc`, test `cbnz` at `@0x379e4e0`).

| field | type | required | example | source |
|---|---|---|---|---|
| `siteId` | String | yes | `"<site id>"` | `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x379e54c`; value is the object field at offset 0x4b (`@0x379e55c`) |

No `isProApp` branch: both variants send `siteId`.

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): no model is parsed.

## Response

No response field is read (asm-traced). The success closure `@0x379e65c` logs `enableAiEmsMode success` (`@0x379e674`) and navigates to the named route `/smartModeStartSuccessPage` (`@0x379e6a4`). The failure closure `@0x379e5f8` only logs `enableAiEmsMode fail, code: ...` (`@0x379e61c`).

## Example request/response

Request, synthesized

```json
{ "siteId": "<site id>" }
```

Response: no captured response; the app ignores the payload.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or shows a toast; the shared transport codes are in [../encryption.md](../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../errors.md).

## Callers in app

- `EmsAiModeConditionLogic._enableLargeSmartMode` (`ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x379e4b8`), the AI mode condition screen of the `ak_soft_ems` package (class `EmsAiModeConditionLogic`). The UI element that triggers it was not traced.

## Since/changed

3.18.0: absent as an installer URL (the 3.18.0 pool holds no `installer_svc` string); the consumer twin `/charging_hes_svc/enable_aiems_mode` is in the 3.18.0 pool. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- Server behaviour (preconditions such as a prior [authorize_aiems](authorize_aiems.md), which strategy runs afterwards) is not known.
- The trigger in the UI is not traced.

## Device-tested by

none
