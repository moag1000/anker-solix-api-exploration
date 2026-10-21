> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# getMiStatus

## Purpose

Reads the current power, status and energy of an A5150 solar micro-inverter for its home page (caller `A5150HomeHttpReposity::getMiStatus`) (string-only: inferred from the function and class names, no caller chain is in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_pv_svc/getMiStatus` (asm-traced): URL string `@0x34ce430`, method object `Method.post` (pool entry `pp+0xa7e0`) `@0x34ce428`, in `A5150HomeHttpReposity::getMiStatus` (`charging/ui/page/device/a5150/homePage/a5150_http_reposity.dart @0x34ce380`), sent through the mixin `HttpRequestMixin::requestHttp` (options `fail`, `isAIotErrorCode`, `loopSeconds`, `success`, descriptor `@0x34ce458`) (`@0x34ce460`).

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) One sender, one key. The map literal has the type arguments `<String, String>` (`charging/ui/page/device/a5150/homePage/a5150_http_reposity.dart @0x34ce3e8`), so the value is a string; it is stored without a guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `sn` | string | yes | `"<sn>"` | `charging/ui/page/device/a5150/homePage/a5150_http_reposity.dart @0x34ce3d4` (value store `@0x34ce3e4`, parameter) |

## `param_type`/`cmd`

n/a

## Response model (link)

`charging::A5150PvTotalModel` (no `models/` page), parsed by `A5150PvTotalModel.fromJson` at `charging/ui/page/device/a5150/homePage/a5150_http_reposity.dart @0x34ce4c8` in the success closure `@0x34ce47c`.

## Response

(asm-traced) Top-level keys of `A5150PvTotalModel` (`data/models.json`, `charging::A5150PvTotalModel`): `power` (int?), `status` (int?), `energy` (int?), `energyUnit` (type not named by the extractor), `reductionCo2` (int?), `reductionCo2Unit` (unknown), `wifiMac` (unknown).

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

- `charging/ui/page/device/a5150/homePage/a5150_http_reposity.dart`: `getMiStatus` @0x34ce380 (requestHttp; encrypted: default-true (requestHttp) — verify)

Call sites (grep of the asm, traced 2026-10-20): `getMiStatus` is called from `A5150HomeLogic::getPvTotalData` (`charging/ui/page/device/a5150/homePage/a5150_home_logic.dart @0x34ce364`).

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The unit of `power` and `energy`: only the class fields are listed. — reclassified: server (2026-10-20: the app reads the numbers from the answer; the unit is not derivable from the code read here)
- Which serial number `A5150HomeLogic::getPvTotalData` passes: the value is a slot or field of its frame (`charging/ui/page/device/a5150/homePage/a5150_home_logic.dart @0x34ce364`); not decoded further — traced 2026-10-20.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
