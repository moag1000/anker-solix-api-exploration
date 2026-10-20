> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# app_to_app_access

## Purpose

Asks the account server for the authorization code of the Alexa account link (OAuth app-to-app flow); sent by `AlexaLinkLogic::getAlexaLinkCode` (`charging/ui/page/account/login/alexa_link_logic.dart`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /openapi/oauth/app_to_app_access` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x3bceab4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3bceaac`, in `HttpRequestControllerImpl::getAlexaLinkCodeRequest` (`charging/http/http_request_repository_impl.dart @0x3bce744`), sent through `encryptionRequestHttp` (`@0x3bceae4`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `client_id` | string | yes | `"<client_id>"` | `charging/http/http_request_repository_impl.dart @0x3bce9d4` (value store `@0x3bce9e4`) |
| `redirect_uri` | string | yes | `"<redirect_uri>"` | `charging/http/http_request_repository_impl.dart @0x3bce9e8` (value store `@0x3bce9f8`) |
| `response_type` | string | yes | `"<response_type>"` | `charging/http/http_request_repository_impl.dart @0x3bce9fc` (value store `@0x3bcea0c`) |
| `scope` | string | yes | `"<scope>"` | `charging/http/http_request_repository_impl.dart @0x3bcea10` (value store `@0x3bcea20`) |
| `state` | string | yes | `"<state>"` | `charging/http/http_request_repository_impl.dart @0x3bcea24` (value store `@0x3bcea30`) |

All five values are Strings: the body map literal has type arguments `<String, String>` (`charging/http/http_request_repository_impl.dart @0x3bcea34`). The sender also builds a sanitised copy of the same map for its log line (`sanitize` `@0x3bce7dc`, `@0x3bce888`); only the log copy is masked. The key `Openudid` is in a separate `<String, String>` map (`@0x3bcea68`) with the value of `getTerminalId` (`@0x3bce920`), passed as the `header` named argument (`@0x3bcead4`), so it is a request header, not a body field.

## `param_type`/`cmd`

n/a

## Response model (link)

no model: the sender's success closure (`charging/http/http_request_repository_impl.dart @0x3bcebc8`) tests that the response is a `Map` (`@0x3bcec78`), copies it with `LinkedHashMap.from` (`@0x3bcecb0`), masks the `code` value with `sanitize` (`@0x3bced30`) in that copy only for the log line (`getAlexaLinkCode success: `) and passes the ORIGINAL response value to the stored callback (`ClosureCall` `@0x3bcede0`, argument `@0x3bcedd4`). The caller's success closure (`charging/ui/page/account/login/alexa_link_logic.dart @0x3bcf030`) reads the key `code` (key string `@0x3bcf084`, lookup `@0x3bcf0a0`) and converts it to a String (`@0x3bcf0d0`).

## Response

(asm-traced) One key is read from the top level of the response: `code` (String, nullable), the authorization code of the link (role by name; the value is never documented). An empty or missing value ends the flow with the error `server_error` (`Invalid response from server`, `charging/ui/page/account/login/alexa_link_logic.dart @0x3bcf110`, `@0x3bcf118`); a non-empty value goes into the redirect URL built by `buildRedirectUrl` together with the original `state` (`@0x3bcf16c`) and is handed to `_handleRedirectBackUrl` (`@0x3bcf19c`).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "client_id": "<client_id>",
  "redirect_uri": "<redirect_uri>",
  "response_type": "<response_type>",
  "scope": "<scope>",
  "state": "<state>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced as numeric codes: the caller turns an empty `code` into the OAuth error `server_error` (`charging/ui/page/account/login/alexa_link_logic.dart @0x3bcf110`) and a missing parameter into `invalid_request` (`@0x3bce48c`); no numeric API code is compared. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getAlexaLinkCodeRequest` @0x3bce744 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getAlexaLinkCodeRequest`
- `charging/ui/page/account/login/alexa_link_logic.dart::getAlexaLinkCode`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What the Alexa side does with `code` and the lifetime of the code: not visible in the app. — reclassified: server (2026-10-20: the Alexa side and the code lifetime are outside the app)
- The values of `client_id`, `redirect_uri`, `response_type`, `scope` and `state`: `AlexaLinkLogic::getAlexaLinkCode` takes them from `parseAuthParams` (`charging/ui/page/account/login/alexa_link_logic.dart @0x3bce414`), the query of the opening link (see `/openapi/oauth/authorize`); the concrete values belong to the Alexa skill and are not documented here.
- How `sanitize` masks values (it is used for logging only).
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
