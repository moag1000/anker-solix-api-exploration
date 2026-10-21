> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# list

## Purpose

Loads the customer-service phone numbers per market for the call-us page; sent by `UserCallUsLogic::onReady` (`charging/ui/page/user/callUs/user_call_us_logic.dart`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /app/help/dynamic/config/list` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x2983f00`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2983ef8`, in `HttpRequestControllerImpl::getCustomerServicePhoneList` (`charging/http/http_request_repository_impl.dart @0x2983e74`), sent through `encryptionRequestHttp` (`@0x2983f28`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No body field: the sender builds an empty map literal (`Map._fromLiteral` `charging/http/http_request_repository_impl.dart @0x2983ec0`, no key store before it).

## `param_type`/`cmd`

n/a

## Response model (link)

[`CustomerServicePhoneInfos`](../../../../../models/other.md#customerservicephoneinfos), parsed by `CustomerServicePhoneInfos.fromJson` at `charging/http/http_request_repository_impl.dart @0x2983f7c` in the success closure `@0x2983f44` (argument typed `Map<String, dynamic>`; call target `#0x2983fec`, `charging/model/service_phone_number_model.dart`).

## Response

(asm-traced) Top-level key of `charging::CustomerServicePhoneInfos` (`data/models.json`): `customer_service_phone_infos` (type not read; the element class is `ServicePhoneNumberModel`, `<ServicePhoneNumberModel>` `@0x2983fa4` for the empty fallback). Keys of `charging::ServicePhoneNumberModel`: `id` (int?), `service_market` (String?), `service_brand` (String?), `service_phone` (String?), `work_days` (String?), `work_time` (String?), `sort_order` (int?). The closure passes the list (or an empty list) to the callback (`ClosureCall` `@0x2983fc8`).

Element type and use (traced 2026-10-20): the callback of `UserCallUsLogic::onReady` (`charging/ui/page/user/callUs/user_call_us_logic.dart`, sender call `@0x2983dfc`, success closure `@0x2984ca0`) is declared with the parameter type `List<ServicePhoneNumberModel>` (`[closure] Null <anonymous closure>(dynamic, List<ServicePhoneNumberModel>)`), so `customer_service_phone_infos` is a list of `ServicePhoneNumberModel`. The closure tests the list with a no-argument bool selector (`GDT[cid_x0 + 0x34bca]` `@0x2984cd8`, same selector as used for list emptiness elsewhere, not named), writes observables of the logic (`value=` `@0x2984d0c`, `@0x2984d80`) and stores the list with `setCustomerServicePhoneList` (`@0x2984da0`); the failure closure (`@0x2984928`) logs `fail:` and resets the observable (`value=` `@0x29849ec`, `@0x2984a14`).

## Example request/response

Request: no body fields are built (see Request). Response: not synthesized; no capture exists for this endpoint.

## Errors seen

none traced: no numeric error code is compared in the sender, its closures or the caller functions read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getCustomerServicePhoneList` @0x2983e74 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getCustomerServicePhoneList`
- `charging/ui/page/user/callUs/user_call_us_logic.dart::onReady`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- How the page picks the market (`service_market`): not read here. — traced 2026-10-20: the logic closure does not read `service_market` (see Response); the market choice, if any, is in the view `charging/ui/page/user/callUs/user_call_us_view.dart`, which was not decoded for it
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
