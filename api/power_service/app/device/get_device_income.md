> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_device_income

## Purpose

Reads the income statistics of a PPS TOU device for a period (builders `PPSTouHttpService::getChartStatistics` and `PPSTouHttpService::getTotalBenefit`); no UI caller is recorded in `data/endpoints.json`, so the purpose is inferred from the function names (string-only).

## Upstream name

`get_device_income` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/device/get_device_income` (asm-traced): URL string at `ak_soft_pps_ems/src/modules/pps_tou/service/pps_tou_http_service.dart @0x2eecce0`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2eeccd8`, in `PPSTouHttpService::getChartStatistics` (`ak_soft_pps_ems/src/modules/pps_tou/service/pps_tou_http_service.dart @0x2eecbdc`), sent through `encryptionRequestHttp` (`@0x2eecd08`).

Same URL and method object in the other sender(s) read:

- `POST /power_service/v1/app/device/get_device_income` (asm-traced): URL string at `ak_soft_pps_ems/src/modules/pps_tou/service/pps_tou_http_service.dart @0x29fa1dc`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x29fa1d4`, in `PPSTouHttpService::getTotalBenefit` (`ak_soft_pps_ems/src/modules/pps_tou/service/pps_tou_http_service.dart @0x29fa084`), sent through `encryptionRequestHttp` (`@0x29fa204`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) Two senders in `ak_soft_pps_ems/src/modules/pps_tou/service/pps_tou_http_service.dart` (`pps_tou_http_service.dart`), each with one `<String, String>` literal of 3 pairs (type arguments `@0x2eecc94` and `@0x29fa18c`), so every value is a String. `getTotalBenefit` (`@0x29fa084`) sends `type = ""` (`@0x29fa11c`) and builds `start_time` by string interpolation of the current year with the literal `"-01-01"` (`@0x29fa150`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | `ak_soft_pps_ems/src/modules/pps_tou/service/pps_tou_http_service.dart @0x2eecc5c` |
| `type` | string | yes | `"<type>"` | `ak_soft_pps_ems/src/modules/pps_tou/service/pps_tou_http_service.dart @0x2eecc70` |
| `start_time` | string | yes | `"<year>-01-01"` in `getTotalBenefit`; `"<start_time>"` in `getChartStatistics` | `ak_soft_pps_ems/src/modules/pps_tou/service/pps_tou_http_service.dart @0x2eecc80` |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed in the builders (asm-traced): both pass `fail`, `showLoading` and `success` closures to `encryptionRequestHttp` (`r4 = const [0x1, 0x7, 0x7, 0x4, fail, 0x6, showLoading, 0x4, success, 0x5, null]` at `ak_soft_pps_ems/src/modules/pps_tou/service/pps_tou_http_service.dart @0x2eecd00`); the callers' parse was not read.

## Response

Not read: the response is handed to the callers of the two builders.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<device_sn>",
  "type": "<type>",
  "start_time": "<start_time>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `ak_soft_pps_ems/src/modules/pps_tou/service/pps_tou_http_service.dart`: `getChartStatistics` @0x2eecbdc (encryptionRequestHttp; encrypted: true); `getTotalBenefit` @0x29fa084 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The response keys: the builders hand the object to their callers; the parsers were not decoded and no UI caller is recorded in `data/endpoints.json`.
- Which `type` strings select which period (`getTotalBenefit` sends the empty string; the other builder takes it as a parameter).
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
