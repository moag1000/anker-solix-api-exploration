> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_protocol_status

## Purpose

Reads whether the user has accepted the protocol agreement of an A2687 charger (callers `_fetchProtocolAgreementStatus` and `_resetProtocolAgreementForUserChange` in the A2687 device-info service) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /mini_power/v1/app/setting/get_protocol_status` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x26c2334`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x26c232c`, in `HttpRequestControllerImpl::getA2687ProtocolAgreementStatus` (`charging/http/http_request_repository_impl.dart @0x26c2280`), sent through `encryptionRequestHttp` (`@0x26c235c`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) `HttpRequestControllerImpl::getA2687ProtocolAgreementStatus` (`charging/http/http_request_repository_impl.dart @0x26c2280`) stores one key, `device_sn`, unconditionally in a map literal with type arguments `<String, String>` (`@0x26c22e8`), so the value is a String.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | `charging/http/http_request_repository_impl.dart @0x26c22d4` (map literal `<String, String>` `charging/http/http_request_repository_impl.dart @0x26c22e8`) |

## `param_type`/`cmd`

n/a

## Response model (link)

- [`A2687ProtocolAgreementModel`](../../../../models/charger.md#a2687protocolagreementmodel), parsed by `A2687ProtocolAgreementModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x26c23b0` (success closure `@0x26c2378`; the closure hands the model's first field, `r0->field_13` `@0x26c23b8`, to the callback, `ClosureCall` `@0x26c23cc`).

## Response

Top-level keys (`data/models.json`, `charging::A2687ProtocolAgreementModel`): `protocol_status` (bool?) and `modes` (field type not extracted).

Element shapes (app side, traced 2026-10-20, `charging/model/a2687/a2687_protocol_agreement_model.dart`, `fromJson` casts): `protocol_status` is a `bool?`; `modes` is a list of `A2687ProtocolMode`, which has `mode` (`String?`) and `protocols`, a list of `A2687ProtocolItem` with `protocol_key` (`String?`) and further keys not typed by the cast scan.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<device_sn>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure `charging/http/http_request_repository_impl.dart @0x226824c` forwards code and message to a stored callback without reading them). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getA2687ProtocolAgreementStatus` @0x26c2280 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/ak_iot_kit/business/A2687/service/a2687_device_info_service.dart::_fetchProtocolAgreementStatus`
- `charging/ak_iot_kit/business/A2687/service/a2687_device_info_service.dart::_resetProtocolAgreementForUserChange`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What "protocol" means for the user (a data-sharing or a charging protocol agreement): the key names `protocol_status` and the caller names are the only evidence. — reclassified: server (2026-10-20: the callers `A2687DeviceInfoService::_fetchProtocolAgreementStatus` and `_resetProtocolAgreementForUserChange` name it a protocol agreement of the A2687; the agreement text is not an app-side fact)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
