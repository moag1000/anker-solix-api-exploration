> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_mi_layout

## Purpose

Reads the micro-inverter layout of an A5150 solar site (`SolarLayoutModel`) through `A5150SolarDetailsReposity::getSolarMiLayout` (string-only: no caller chain in `data/endpoints.json`, inferred from the builder name).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_mi_layout` (asm-traced): URL string at `charging/ui/page/device/a5150/solarDetails/a5150_solar_details_http_repository.dart @0x2931220`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2931218`, in `A5150SolarDetailsReposity::getSolarMiLayout` (`charging/ui/page/device/a5150/solarDetails/a5150_solar_details_http_repository.dart @0x2931054`), sent through `requestHttp` (`@0x293125c`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `A5150SolarDetailsReposity::getSolarMiLayout` (`charging/ui/page/device/a5150/solarDetails/a5150_solar_details_http_repository.dart`, call `@0x293125c`, argument list `@0x2931254`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

(asm-traced) Each sender stores its keys in one map literal with type arguments `<String, String?>` read at the cited address, so every value is a String: `A5150SolarDetailsReposity::getSolarMiLayout` (`charging/ui/page/device/a5150/solarDetails/a5150_solar_details_http_repository.dart @0x29311d0`, 4 keys). No key is behind a null guard. The `String?` value type allows a null value for a key; the key itself is stored unconditionally.

| field | type | required | example | source |
|---|---|---|---|---|
| `siteId` | string | yes | `"<siteId>"` | `charging/ui/page/device/a5150/solarDetails/a5150_solar_details_http_repository.dart @0x293118c` |
| `type` | string | yes | `"<type>"` | `charging/ui/page/device/a5150/solarDetails/a5150_solar_details_http_repository.dart @0x29311a0` |
| `start` | string | yes | `"<start>"` | `charging/ui/page/device/a5150/solarDetails/a5150_solar_details_http_repository.dart @0x29311b0` |
| `end` | string | yes | `"<end>"` | `charging/ui/page/device/a5150/solarDetails/a5150_solar_details_http_repository.dart @0x29311c0` |

## `param_type`/`cmd`

n/a

## Response model (link)

- `charging::SolarLayoutModel`, parsed by `SolarLayoutModel.fromJson` at `charging/ui/page/device/a5150/solarDetails/a5150_solar_details_http_repository.dart @0x2932540` (success closure `@0x29324c0`, `bl` target `[package:charging/model/a5150/solar_layout_model/solar_layout_model.dart]`).

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::SolarLayoutModel`): `siteId` (unknown), `ecuSn` (unknown), `maxRow` (int?), `maxCol` (int?), `layout` (List?), `layoutImg` (unknown), `pvInstallCapacity` (unknown), `localTime` (unknown).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "siteId": "<siteId>",
  "type": "<type>",
  "start": "<start>",
  "end": "<end>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/device/a5150/solarDetails/a5150_solar_details_http_repository.dart`: `getSolarMiLayout` @0x2931054 (requestHttp; encrypted: default-true (requestHttp) — verify)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The meaning of `type`, `start` and `end`: the four fields are parameters and no UI caller is recorded in `data/endpoints.json`. — reclassified: server (2026-10-20: request parameters of a server query)
- What `loopSeconds` and `cacheKey` (argument list `charging/ui/page/device/a5150/solarDetails/a5150_solar_details_http_repository.dart @0x293125c`) do in the HTTP layer: it was not read for them. — traced 2026-10-20: the arguments are consumed by `HttpRequestMixin` code that Blutter does not emit (`charging/http/http_request_mixin.dart` holds only `Debouncer::run` `@0x230f7f0`), so their effect is not in the asm
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call. — reclassified: device test row 150 (traced 2026-10-20: per call the SDK login state `AkIotKitFlutter::isLogin` and the base-URL predicate decide, `HttpEncryptionDecorator.dart @0x4869504`, `@0x4869544`; the predicate is a GDT dispatch whose selector the asm does not name, and the login state is runtime data)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
