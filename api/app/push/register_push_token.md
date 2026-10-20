> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# register_push_token

## Purpose

Registers the push token of the phone with the account and tells the server that notifications are enabled; sent by `HttpRequestControllerImpl::uploadDeviceToken` (also called from the same file's interface) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /app/push/register_push_token` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x2741938`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2741930`, in `HttpRequestControllerImpl::uploadDeviceToken` (`charging/http/http_request_repository_impl.dart @0x2741818`), sent through `encryptionRequestHttp` (`@0x2741960`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `is_notification_enable` | bool | yes | `true` | `charging/http/http_request_repository_impl.dart @0x2741890` (value store `@0x27418a0`) |
| `token` | string | yes |  | `charging/http/http_request_repository_impl.dart @0x27418a4` (value store `@0x27418b4`) |

The body map literal has type arguments `<String, Object>` (`charging/http/http_request_repository_impl.dart @0x27418b8`), not evidence of a value type; `token` is typed through the declared parameter (see below). `is_notification_enable` is the constant `true`. The key `Openudid` is in a separate `<String, String>` map (`@0x27418ec`) with the value of `getTerminalId` (`@0x274187c`) passed as the `header` named argument (`@0x2741958`), so it is a request header, not a body field.

Type and provider of `token` (app side, traced 2026-10-20): the interface method `HttpRequestController::uploadDeviceToken` takes the token as a declared `String` (the tear-off signature `uploadDeviceToken(dynamic, String, {success, fail})` at `charging/http/http_request_repository.dart` line 9706, call `@0x34c51cc`), so `token` is a string. The token comes from `MessagePushHandler::uploadPushToken` (`charging/push/message_push_handler.dart @0x273a110`), which awaits `PushServiceOversea::getPushToken` (`@0x273a16c`); that function asks `FirebaseMessaging.getToken` (`push_service/src/push_service_oversea.dart @0x273a22c`), so the token of this build is a Firebase Cloud Messaging token; the log text is `pushToken: ` (`@0x273a18c`) and a null token ends the function (`cmp w0, NULL` `@0x273a1b8`). `uploadPushToken` is called from `MessagePushHandler::initMessagePush` (`@0x2703e00`).

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the success closure (`charging/http/http_request_repository_impl.dart @0x27419c4`) logs `uploadDeviceToken success` (`@0x27419d8`) and never reads its response argument. No `fromJson`.

## Response

No response key is read by the app (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "is_notification_enable": true,
  "token": "<token>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or its closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `uploadDeviceToken` @0x2741818 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::uploadDeviceToken`
- `charging/http/http_request_repository_impl.dart::uploadDeviceToken`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The caller's conditions (when the token is registered): not traced beyond the interface. — traced 2026-10-20: `uploadPushToken` runs from `initMessagePush` (`charging/push/message_push_handler.dart @0x2703e00`) and returns without a request when the token is null (`@0x273a1b8`); whether other screens call the interface method (the login and bind-phone logic files reference `uploadDeviceToken`) with their own conditions was not decoded
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
