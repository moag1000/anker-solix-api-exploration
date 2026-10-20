> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_user_op_shelly_status

## Purpose

Checks which Shelly devices were granted or changed for the account after the user selects a third-party platform (callers `ThirdPartyPlatFormLogic::selectDone`; builder `checkIsGrantedDeviceChanged`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`get_shelly_status` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/get_user_op_shelly_status` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x3f2aa7c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3f2aa74`, in `HttpRequestControllerImpl::checkIsGrantedDeviceChanged` (`charging/http/http_request_repository_impl.dart @0x3f2a9d4`), sent through `encryptionRequestHttp` (`@0x3f2aaa4`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) The body is one map literal of 1 pair (`AllocateArray`, raw `r2 = 4` at `@0x3f2aa14`, so 2 slots) with type arguments `<String, String>` at `@0x3f2aa30`, so every value is typed in the literal; all keys are stored unconditionally.

| field | type | required | example | source |
|---|---|---|---|---|
| `token` | string | yes | `"<token>"` | `charging/http/http_request_repository_impl.dart @0x3f2aa1c` |

## `param_type`/`cmd`

n/a

## Response model (link)

no model file in `data/models.json`: the success closure (`charging/http/http_request_repository_impl.dart @0x3f2aac0`) reads the key `op_list` (string literal `@0x3f2ab0c`), casts it to `List` (`@0x3f2ab4c`), casts each entry to `Map<String, dynamic>` (`@0x3f2abf0`), reads `device_sn` (`@0x3f2ac10`, cast `String` `@0x3f2ac50`) and `op_type` (cast `String`) and builds a `GrantDeviceRecordModel` per entry (`@0x3f2acbc`).

## Response

| field | type | required | example | source |
|---|---|---|---|---|
| `op_list` | list | yes (non-null cast) | `[...]` | `charging/http/http_request_repository_impl.dart @0x3f2ab0c` |
| `op_list[].device_sn` | string (non-null cast) | yes | `"<device_sn>"` | `charging/http/http_request_repository_impl.dart @0x3f2ac10` |
| `op_list[].op_type` | string (cast `String`) | yes | `?` | `charging/http/http_request_repository_impl.dart @0x3f2ac6c` |

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "token": "<token>"
}
```

Response, synthesized (keys read by the success closure; values are placeholders)

```json
{
  "data": {
    "op_list": [
      {
        "device_sn": "<device_sn>",
        "op_type": "<?>"
      }
    ]
  }
}
```

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `checkIsGrantedDeviceChanged` @0x3f2a9d4 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::checkIsGrantedDeviceChanged`
- `charging/ui/page/device/connect/third_party_platform/third_party_platform_logic.dart::selectDone`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What the `op_type` strings mean: the closure casts them to `String` and stores them in `GrantDeviceRecordModel`; the consumer was not decoded. — reclassified: server (the string meanings are defined by the server)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
