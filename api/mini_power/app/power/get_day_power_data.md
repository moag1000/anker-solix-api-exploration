> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_day_power_data

## Purpose

Loads the power curve of one day for the power-curve pages (callers `_getPowerCurveData` in the A2345 and A91B2 power-curve logic and `HttpServiceImpl::getDayPowerData`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`charger_get_statistics` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /mini_power/v1/app/power/get_day_power_data` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x28a8538`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x28a8530`, in `HttpRequestControllerImpl::getDayPowerData` (`charging/http/http_request_repository_impl.dart @0x28a8454`), sent through `encryptionRequestHttp` (`@0x28a8560`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) `HttpRequestControllerImpl::getDayPowerData` (`charging/http/http_request_repository_impl.dart @0x28a8454`) stores three keys unconditionally in a map literal with type arguments `<String, String>` (`@0x28a84ec`), so all three values are Strings.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_model` | string | yes | `"<device_model>"` | `charging/http/http_request_repository_impl.dart @0x28a84b0` (map literal `<String, String>` `charging/http/http_request_repository_impl.dart @0x28a84ec`) |
| `device_sn` | string | yes | `"<device_sn>"` | `charging/http/http_request_repository_impl.dart @0x28a84c4` (same literal) |
| `date` | string | yes | `"<date>"` | `charging/http/http_request_repository_impl.dart @0x28a84d8` (same literal) |

## `param_type`/`cmd`

n/a

## Response model (link)

- [`DayPowerModel`](../../../../models/other.md#daypowermodel), parsed per list element by `DayPowerModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x28a8708`. The success closure (`@0x28a857c`) reads the key `output_power_list` (`@0x28a85cc`), casts it to `List?` (`@0x28a860c`), parses each element into a `List<DayPowerModel>` (`@0x28a8620`) and passes it to the callback (`ClosureCall` `@0x28a87a8`).

## Response

Top-level key of the response: `output_power_list` (list of port curves). Keys of one element (`data/models.json`, `base_service::DayPowerModel`): `port_name` (String?), `interval` (int?), `unit` (String?), `power_points` (List?), `power_protos` (field type not extracted).

Element types (app side, traced 2026-10-20, `base_service/bean/model/day_power_model.dart`): `power_points` is cast to `List?` (`@0x28a89dc`) and turned into a list of `double` (`<double>` `@0x28a8a24`), so its entries are numbers; `power_protos` is stored without a cast or conversion (`ArrayStore` `@0x28a8acc`), so the model keeps it as received and its element type is not fixed by the app; `port_name` is a `String?` (`@0x28a8954`).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_model": "<device_model>",
  "device_sn": "<device_sn>",
  "date": "<date>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure `charging/http/http_request_repository_impl.dart @0x226824c` forwards code and message to a stored callback without reading them). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getDayPowerData` @0x28a8454 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getDayPowerData`
- `charging/impl/http_service_impl.dart::getDayPowerData`
- `charging/ui/page/device/a2345/a2345power_curve/a2345power_curve_logic.dart::_getPowerCurveData`
- `charging/ui/page/device/a91b2/a91b2power_curve/a91b2power_curve_logic.dart::_getPowerCurveData`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The format of `date` (the value is a parameter; the callers were not decoded for it).
- The unit and spacing of `power_points` (`interval` and `unit` are model fields; their values were not decoded). — reclassified: server (2026-10-20: `interval` and `unit` arrive in the answer; the app code read here does not name their values)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
