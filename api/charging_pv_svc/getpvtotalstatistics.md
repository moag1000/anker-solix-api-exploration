> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# getPvTotalStatistics

## Purpose

Reads the lifetime PV totals (energy, CO2 reduction, saved money, power config) of an A5140 device for its home page (caller `A5140HttpReposity::getPvTotalStatistics`) (string-only: inferred from the function and class names, no caller chain is in `data/endpoints.json`).

## Upstream name

`get_device_pv_total_statistics` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /charging_pv_svc/getPvTotalStatistics` (asm-traced): URL string `@0x34d0a8c`, method object `Method.post` (pool entry `pp+0xa7e0`) `@0x34d0a84`, in `A5140HttpReposity::getPvTotalStatistics` (`charging/ui/page/device/a5140/a5140home/a5140home_http_reposity.dart @0x34d0930`), sent through the mixin `encryptionRequestHttp` of `HttpRequestController` (options `cacheKey`, `fail`, `isAIotErrorCode`, `success`, descriptor `@0x34d0ab4`) (`@0x34d0abc`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) One sender, one key. The map literal has the type arguments `<String, String>` (`charging/ui/page/device/a5140/a5140home/a5140home_http_reposity.dart @0x34d0a40`), so the value is a string; it is stored without a guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `sn` | string | yes | `"<sn>"` | `charging/ui/page/device/a5140/a5140home/a5140home_http_reposity.dart @0x34d0a2c` (value store `@0x34d0a3c`, parameter) |

Serial passed (traced 2026-10-20, app side): `A5140homeController::getPvTotalData` takes `deviceSn` (`field_6b`) of its device object (`field_63`) (`charging/ui/page/device/a5140/a5140home/a5140home_logic.dart @0x34d08cc`, `@0x34d08d4`) and calls the repository at `@0x34d0914`.

## `param_type`/`cmd`

n/a

## Response model (link)

`charging::PvTotalStatisticsModel` (no `models/` page), parsed by `PvTotalStatisticsModel.fromJson` at `charging/ui/page/device/a5140/a5140home/a5140home_http_reposity.dart @0x34d1274` in the success closure `@0x34d1208` (and at `@0x34d09f8` for a cached entry read by `getCache` `@0x34d09c8`).

## Response

(asm-traced) Top-level keys of `PvTotalStatisticsModel` (`data/models.json`, `charging::PvTotalStatisticsModel`): `energy` (num?), `energyUnit` (String?), `reductionCo2` (num?), `reductionCo2Unit` (String?), `saveMoney` (num?), `saveMoneyUnit` (String?), `powerConfig` (String?), `powerPopUpFlag` (int?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "sn": "<sn>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure only logs `code` and `msg`). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/device/a5140/a5140home/a5140home_http_reposity.dart`: `getPvTotalStatistics` @0x34d0930 (encryptionRequestHttp; encrypted: true)

Call sites (grep of the asm, traced 2026-10-20): `getPvTotalStatistics` is called from `A5140homeController::getPvTotalData` (`charging/ui/page/device/a5140/a5140home/a5140home_logic.dart @0x34d0914`).

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What `powerPopUpFlag` and `powerConfig` trigger in the UI: only the class fields are listed. — traced 2026-10-20: the names occur as strings only in the model file (`charging/model/a5140_device_info/pv_total_statistics_model.dart`) and in unrelated settings code (`settings/src/service/site_settings_service_impl.dart @0x3514980` logs a `powerConfig=` text of another model); readers of the model fields use field offsets, not names, and were not followed
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
