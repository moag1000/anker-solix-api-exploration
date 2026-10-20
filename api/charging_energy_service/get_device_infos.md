> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_device_infos

## Purpose

Reads the device information of a list of device serial numbers when the user taps the A1790 card on the A17B1 station page (caller chain `A17b1StationLogic::onA1790CardPressed`, `HttpRequestController::getDeviceInfos`, in `data/endpoints.json`) (asm-traced).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_energy_service/get_device_infos` (asm-traced): URL string `@0x25f98dc`, method object `Method.post` (pool entry `pp+0xa7e0`) `@0x25f98d4`, in `HttpRequestControllerImpl::getDeviceInfos` (`charging/http/http_request_repository_impl.dart @0x25f9824`), sent through `HttpRequestControllerImpl::requestHttp` (`@0x25f9904`).

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) One sender, one key. The map literal has the type arguments `<String, List<String>>` (`charging/http/http_request_repository_impl.dart @0x25f9890`), so the value is a list of strings; it is stored without a guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `sns` | list | yes | `["<sn>"]` | `charging/http/http_request_repository_impl.dart @0x25f987c` (value store `@0x25f988c`, parameter) |

## `param_type`/`cmd`

n/a

## Response model (link)

[`DeviceInfosModel`](../../models/device.md#deviceinfosmodel), parsed by `DeviceInfosModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x25f9950` in the success closure `@0x25f9920`.

## Response

(asm-traced) Top-level keys of `DeviceInfosModel` (`data/models.json`, `charging::DeviceInfosModel`): `device_infos` (Iterable). The closure forwards the parsed model to the caller's callback; the field names inside the elements are listed on [models/device.md](../../models/device.md#deviceinfosmodel).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "sns": ["<sn>"]
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure only logs `code` and `msg`). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getDeviceInfos` @0x25f9824 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::getDeviceInfos`
- `charging/ui/page/station/A17b1/a17b1_station_logic.dart::onA1790CardPressed`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Which serial numbers the caller sends: `A17b1StationLogic::onA1790CardPressed` passes the list; its content was not decoded.
- The element structure of `device_infos`: owned by the model page.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
