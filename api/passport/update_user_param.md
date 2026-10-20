> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# update_user_param

## Purpose

Saves one analytics or privacy switch of the user; sent by `AnalyticsAndImprovementLogic::setAppSwitchStatus` (`charging/ui/page/user/about/analyticsAndImprovement/analytics_and_improvement_logic.dart`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /passport/update_user_param` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x293fa08`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x293fa00`, in `HttpRequestControllerImpl::setAppSwitchApi` (`charging/http/http_request_repository_impl.dart @0x293f888`), sent through `encryptionRequestHttp` (`@0x293fa30`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `user_params` | list | yes | one element (list length raw 2, `@0x293f984`, so 1) | `charging/http/http_request_repository_impl.dart @0x293f8e4` (store `@0x293f994`, growable list of `Map<String, Object>` `@0x293f96c`) |
| `user_params[].param_type` | int (Smi, w) | yes | | `charging/http/http_request_repository_impl.dart @0x293f8fc` (value store `@0x293f910`, an unboxed int argument is tagged by `lsl x2, x1, #1` `@0x293f90c` and stored with a 32-bit store) |
| `user_params[].param_value` | string | yes | `"1"` or `"0"` | `charging/http/http_request_repository_impl.dart @0x293f914` (value store `@0x293f938`, constants `"1"` `@0x293f928` and `"0"` `@0x293f934`, chosen by a bool argument `tbnz` `@0x293f924`) |

The element map literal has type arguments `<String, Object>` (`@0x293f93c`), the outer map `<String, List<Map<String, Object>>>` (`@0x293f9b8`).

## `param_type`/`cmd`

see `api/param_types.md`

`param_type` is not a constant at this sender: it is an unboxed int parameter tagged by `lsl` (`charging/http/http_request_repository_impl.dart @0x293f90c`); the callers' values are listed under Known unknowns.

## Response model (link)

not parsed by the app (asm-traced): the success closure (`charging/http/http_request_repository_impl.dart @0x261b9a0`, shared with other senders) reads no response key and calls the stored callback with `true` (`@0x261b9cc`, `ClosureCall` `@0x261b9d4`).

## Response

No response key is read by the app (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` is a placeholder, not a captured value)

```json
{
  "user_params": [
    {
      "param_type": "<int>",
      "param_value": "1"
    }
  ]
}
```

Response: not synthesized; no capture exists for this endpoint.

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `setAppSwitchApi` @0x293f888 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`)

Called from:

- `charging/http/http_request_repository.dart::setAppSwitchApi`
- `charging/ui/page/user/about/analyticsAndImprovement/analytics_and_improvement_logic.dart::setAppSwitchStatus`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Which `param_type` values the caller sends (probably the ids that `get_user_param` asks for, 20000 and 20001): the argument is a parameter of the sender and was not traced to the UI constants.
- Whether `param_value` can take values other than `"1"` and `"0"`: the sender produces only these two.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
