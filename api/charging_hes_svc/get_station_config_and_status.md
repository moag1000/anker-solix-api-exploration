> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_station_config_and_status

## Purpose

Loads the grid configuration and status of a station (`A5101StationGridConfigModel`) for the grid-dispatch settings (`GridDispatchLogic::getAdvancedConfigStateFromCloud`) and the auto disaster tips (`AutoDisasterTipsLogic::_getNetAutoDisasterPrepareStatus`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_station_config_and_status` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x27c8844`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x27c883c`, in `HttpRequestControllerImpl::getA5101StationConfigDetail` (`charging/http/http_request_repository_impl.dart @0x27c871c`), sent through `requestHttp` (`@0x27c886c`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `HttpRequestControllerImpl::getA5101StationConfigDetail` (`charging/http/http_request_repository_impl.dart`, call `@0x27c886c`, argument list `@0x27c8864`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

(asm-traced) Each sender stores its keys in one map literal with type arguments `<String, String>` read at the cited address, so every value is a String: `HttpRequestControllerImpl::getA5101StationConfigDetail` (`charging/http/http_request_repository_impl.dart @0x27c87e0`, 1 key). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | string | yes | `"<station_id>"` | `charging/http/http_request_repository_impl.dart @0x27c87cc` |

## `param_type`/`cmd`

n/a

## Response model (link)

- [`A5101StationGridConfigModel`](../../models/hes.md#a5101stationgridconfigmodel), parsed by `A5101StationGridConfigModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x27c8958` (success closure `@0x27c8920`, `bl` target `[package:charging/model/a5101/a5101_station_grid_config_model.dart]`).

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::A5101StationGridConfigModel`): `afci` (Afci?), `rsd` (Rsd?), `dred` (Dred?), `rcr` (Rcr?), `faststop` (Faststop?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "station_id": "<station_id>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getA5101StationConfigDetail` @0x27c871c (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::getA5101StationConfigDetail`
- `charging/ui/page/device/a5101/setting/grid_dispatch/grid_dispatch_logic.dart::getAdvancedConfigStateFromCloud`
- `charging/ui/page/family/auto_disaster/auto_disaster_tips_logic.dart::_getNetAutoDisasterPrepareStatus`

Keys read by the two callers (traced 2026-10-20; the key names follow the field order of `A5101StationGridConfigModel.fromJson`: `afci` `field_7`, `rsd` `field_b`, `dred` `field_f`, `rcr` `field_13`, `faststop` `field_17`): `AutoDisasterTipsLogic::_getNetAutoDisasterPrepareStatus` (`charging/ui/page/family/auto_disaster/auto_disaster_tips_logic.dart`) logs the model with `toJson` (`@0x34b6664`) and reads `dred` (`field_f`, shown by the asm as an `ArrayLoad` of index 0) and its `status` (`field_b`), comparing it with the integer 1 (raw 2 pushed `@0x34b66f4`, tagged compare); the log text it prints next to that value says `faststop`. `GridDispatchLogic::getAdvancedConfigStateFromCloud` (`charging/ui/page/device/a5101/setting/grid_dispatch/grid_dispatch_logic.dart @0x27c7c00`, await `@0x27c7c0c`) reads `dred` (`field_f`, null test `@0x27c7c24`, then its `config` `field_7` `@0x27c7c78`) only when the `isAU` test on a market field of the logic holds (`@0x27c7c38`), and `rcr` (`field_13`, `@0x27c7e1c`, `@0x27c7e8c`) behind the tests `isDE`, `isGB`, `isCZ`, `isAT` (`@0x27c7e40`..`@0x27c7e64`), and writes the values into observable fields of the logic (`value=` `@0x27c7cb4`, `@0x27c7e14`, `@0x27c8054`); the other three model keys are not read by this function.

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call. — reclassified: device test row 150 (traced 2026-10-20: per call the SDK login state `AkIotKitFlutter::isLogin` and the base-URL predicate decide, `HttpEncryptionDecorator.dart @0x4869504`, `@0x4869544`; the predicate is a GDT dispatch whose selector the asm does not name, and the login state is runtime data)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
