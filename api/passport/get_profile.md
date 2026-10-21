> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_profile

## Purpose

Reloads the profile (e-mail, nick name, avatar) of the logged-in user; sent by `UserMainPageLogic::_listenEvenBus` when the profile page gets an event (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /passport/get_profile` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x34e6dc0`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x34e6db8`, in `HttpRequestControllerImpl::getUserProfileRequest` (`charging/http/http_request_repository_impl.dart @0x34e6d48`), sent through `encryptionRequestHttp` (`@0x34e6de0`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No body field: the sender builds an empty map literal (`Map._fromLiteral` `@0x34e6d80`, no key store before it).

## `param_type`/`cmd`

n/a

## Response model (link)

[`UserModel`](../../models/account.md#usermodel), parsed by `UserModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x34e6ebc` in the success closure `@0x34e6e60`.

## Response

(asm-traced) Top-level keys of `UserModel` (`data/models.json`, `charging::UserModel`): `email` (String?), `phone_number` (String?), `nick_name` (String?), `phone` (String?), `avatar` (String?), `country` (String?), `promo_email` (bool?), `access_token` (String?), `id` (int?). The closure copies five of the fields into the stored user model (`StoreField` `@0x34e6ef4`..`@0x34e6f84`) and then calls `updateIotUserInfo` (`@0x34e6fb0`).

Copy into the stored user (app side, traced 2026-10-20, `charging/http/http_request_repository_impl.dart`): the success closure copies the model fields at the first to fifth offsets, `field_7` (`email`, `@0x34e6f34`), `field_b` (`phone_number`, `@0x34e6f58`), `field_f` (`nick_name`, `@0x34e6eec`), `field_13` (`phone`, `@0x34e6f10`) and the fifth field (`avatar`, load `@0x34e6f7c`) into the user model returned by `getUserModel` (stores `@0x34e6ef4`, `@0x34e6f18`, `@0x34e6f3c`, `@0x34e6f60`, `@0x34e6f84`) and then calls `updateIotUserInfo` (`@0x34e6fb0`); the destination fields have no names in the asm. `country`, `promo_email`, `access_token` and `id` are not copied there. The field-to-key order is the field order of `UserModel` (`charging/model/user_model.dart`).

## Example request/response

Request: no body fields are built (see Request). Response: not synthesized; no capture exists for this endpoint.

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getUserProfileRequest` @0x34e6d48 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getUserProfileRequest`
- `charging/ui/page/user/main/user_main_page_logic.dart::_listenEvenBus`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
