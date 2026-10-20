> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# remove_user_fault_info

## Purpose

Removes a fault entry of a station by id (`FamilyMainHttpReposity::removeException`, string-only: no caller chain in `data/endpoints.json`, inferred from the builder name) (string-only: no caller chain in `data/endpoints.json`, inferred from the builder name).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/remove_user_fault_info` (asm-traced): URL string at `charging/ui/page/family/family_main_http_reposity.dart @0x400c724`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x400c71c`, in `FamilyMainHttpReposity::removeException` (`charging/ui/page/family/family_main_http_reposity.dart @0x400c634`), sent through `requestHttp` (`@0x400c74c`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `FamilyMainHttpReposity::removeException` (`charging/ui/page/family/family_main_http_reposity.dart`, call `@0x400c74c`, argument list `@0x400c744`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

`FamilyMainHttpReposity::removeException` (`charging/ui/page/family/family_main_http_reposity.dart @0x400c634`) stores 3 keys in a map literal with type arguments `<String, Object>` (`@0x400c6d8`), which do not type the values. `id` and `dataSource` are boxed from unboxed 64-bit integers (`BoxInt64Instr` `@0x400c698`, `@0x400c6c0`), so both are integers; `stationId` is stored as received (`@0x400c684`). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `stationId` | ? | yes | ? | `charging/ui/page/family/family_main_http_reposity.dart @0x400c674` |
| `id` | int (unboxed, x) | yes | a fault id | `charging/ui/page/family/family_main_http_reposity.dart @0x400c688` |
| `dataSource` | int (unboxed, x) | yes | a data source number | `charging/ui/page/family/family_main_http_reposity.dart @0x400c6b0` |

## `param_type`/`cmd`

n/a

## Response model (link)

unknown: both callbacks of the call are allocated without a context (`r2 = Null` `charging/ui/page/family/family_main_http_reposity.dart @0x400c6f0`, `@0x400c704`) and their pool entries resolve to a function that Blutter labels `[dart:ui] _NativeScene::_NativeScene._ (0x49c1cac)`, outside the app asm tree, so the response handling could not be read. The worksheet has no response entry for this URL.

## Response

Not stated: the response handling could not be read (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "stationId": "<stationId>",
  "id": "<id>",
  "dataSource": "<dataSource>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: the callbacks could not be read (see Response model).

## Callers in app

- `charging/ui/page/family/family_main_http_reposity.dart`: `removeException` @0x400c634 (requestHttp; encrypted: default-true (requestHttp) — verify)

Caller argument source (traced 2026-10-20): `FamilyMainLogic::closeException` (`charging/ui/page/family/family_main_page_logic.dart @0x400c46c`) calls `removeException` (`@0x400c560`) with three fields of one list element object (`field_b`, `field_4f` and `field_67`, `@0x400c54c`..`@0x400c558`); the field layout equals that of `HesPushMessageModel` (`charging/model/hes_push_message_model.dart`: `stationId` `field_b` cast `String` `@0x23dd0fc`, `id` `field_4f` cast `int` `@0x23dd9f0`, `dataSource` `field_67` cast `int` `@0x23ddbdc`), the class itself is not named at the call. The caller then sets two observables (`value=` `@0x400c5c4`, `@0x400c5e0`) and, after a `Future.delayed` of 3 s (`@0x400c608`, `objs.txt Obj!Duration@4218bf1` = 0x2dc6c0 microseconds), calls `getExceptionMsgList` again (closure `@0x400c768`); it passes no callback, so the answer of this call is not read by the caller.

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The response handling: the callbacks resolve to a function outside the app asm tree. — traced 2026-10-20: the caller `closeException` passes no callback and refreshes the list with `getExceptionMsgList` after 3 s (see Callers in app); the callbacks inside the sender stay outside the app asm tree
- The type of `stationId`: the parameter is stored without conversion into a `<String, Object>` map. — attempted 2026-10-20 (two-hop not readable: `closeException` (`charging/ui/page/family/family_main_page_logic.dart @0x400c560`) pass slots or fields of their own frames; no literal or declared type in the argument setups)
- Which `dataSource` numbers exist: the value is `field_67` of the message object (`int` cast in `HesPushMessageModel.fromJson`, `charging/model/hes_push_message_model.dart @0x23ddbdc`, see Callers in app), i.e. it is read from the data of the fault message and is not enumerated in the app. — reclassified: server (2026-10-20: the set of values is not visible in the app; it comes with the fault message data)
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call. — reclassified: device test row 150 (traced 2026-10-20: per call the SDK login state `AkIotKitFlutter::isLogin` and the base-URL predicate decide, `HttpEncryptionDecorator.dart @0x4869504`, `@0x4869544`; the predicate is a GDT dispatch whose selector the asm does not name, and the login state is runtime data)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
