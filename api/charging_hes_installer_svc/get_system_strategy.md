> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_system_strategy

## Purpose

Reads the current system strategy of a site from the cloud; the AI mode condition screen uses only its `electricity_strategy.isAuthorizeAIEms` flag to learn whether the AI EMS is already authorized.

## Upstream name

`none` (no upstream name). The consumer twin `/charging_hes_svc/get_device_command` is mentioned in the list of known endpoints in `api/apitypes.py` (line 441), without a key.

## Method+URL

`POST /charging_hes_installer_svc/get_system_strategy` (asm-traced). The URL comes from the static getter `EmsApi.getDeviceCommand` (`ak_soft_ems/http/ems_api.dart @0x2a31618`; the Dart name is the consumer name `getDeviceCommand`): installer string `pp+0xe86d0` (`@0x2a31624`) when `isProApp` is true, otherwise `/charging_hes_svc/get_device_command` (`pp+0x8fb00`, `@0x2a31630`); see [the variant selector](README.md#variant-selector-installer-app-versus-consumer-app). The sender `EmsAiModeConditionLogic._getLargeAuthorizationStatus` (`ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x2a31278`) loads the field at `@0x2a312d4` and passes `Method.post` (pool entry `pp+0xa7e0`, `@0x2a313dc`).

## Encrypted?

Yes by wrapper (asm-traced): ``_getLargeAuthorizationStatus`` calls `encryptionRequestHttp` (`ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x2a31408`) without passing `needEncryption`, so the default `true` applies (`api/encryption.md`, [which calls are encrypted](../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time (SDK login state and a base-URL test, [encryption.md](../encryption.md)); asm alone does not decide it. The loading overlay is off (`showLoading: false`, `@0x2a313f0`).

## Request

Map literal with two pairs, `<String, Object>` (`r2 = 8`). The key of the first pair depends on `isProApp` (`LoadStaticField(0xad8)` `@0x2a312f8`, `tbnz` `@0x2a31300`).

| field | type | required | example | source |
|---|---|---|---|---|
| `system_code` | String | yes (installer variant) | `"<system code>"` | `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x2a31314`; value is the object field at offset 0x77 (`@0x2a31324`) |
| `station_id` | String | yes (consumer variant) | `"<site id>"` | `@0x2a31368`; value is the object field at offset 0x4b (`@0x2a31378`) |
| `accuracy` | int | yes | `5` | `@0x2a31330` (installer), `@0x2a31384` (consumer); raw `10` stored with `stur w16` (`@0x2a3133c`, `@0x2a31390`), Smi, so 5 (`tools/smi.py`) |

The meaning of `accuracy` (probably the number of decimal places for prices) is not documented; the same value 5 is sent by [get_utility_rate_plans](get_utility_rate_plans.md).

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): no model is parsed; the success closure reads one nested key from the raw map.

## Response

The success closure `@0x2a314bc` checks that the payload is a `Map<String, dynamic>` and reads one nested value.

| field | type | required | example | source |
|---|---|---|---|---|
| `electricity_strategy` | map | no | `{ "isAuthorizeAIEms": 1 }` | `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x2a3155c` |
| `electricity_strategy.isAuthorizeAIEms` | int (null counts as 0) | no | `1` | `@0x2a31580`; read through a pool helper with default 0 (`r4 = 0`, `@0x2a3158c`); the closure compares the value with raw `2` (`@0x2a315e0`, a Smi argument of a dispatch-table call, so 1; the call is most likely `==`) and stores the result with `value=` in the field at offset 0x97 (`@0x2a315fc`), the same observable that [authorize_aiems](authorize_aiems.md) sets to `true` |

Everything else in the answer is ignored by this sender, although the consumer URL name (`get_device_command`) suggests a larger device-command document.

## Example request/response

Request, synthesized

```json
{ "system_code": "<system code>", "accuracy": 5 }
```

Response, synthesized

```json
{ "electricity_strategy": { "isAuthorizeAIEms": 1 } }
```

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or shows a toast; the shared transport codes are in [../encryption.md](../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `EmsAiModeConditionLogic._getLargeAuthorizationStatus` (`ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x2a31278`), the AI mode condition screen of the `ak_soft_ems` package (class `EmsAiModeConditionLogic`). The failure closure (`@0x2a31428`) only logs `getDeviceCommand fail, code: ...`.

## Since/changed

3.18.0: absent as an installer URL (the 3.18.0 pool holds no `installer_svc` string); the consumer twin `/charging_hes_svc/get_device_command` is in the 3.18.0 pool. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- The full response layout is not traced; only `electricity_strategy.isAuthorizeAIEms` is read.
- The meaning of `accuracy` and the type of `isAuthorizeAIEms` on the wire (int versus bool) are not verified; the app compares with the integer 1 after a default of 0.
- Server behaviour is not known.

## Device-tested by

none
