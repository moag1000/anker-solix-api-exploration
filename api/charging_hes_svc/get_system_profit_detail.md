> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_system_profit_detail

## Purpose

Reads the profit detail of a site for a start date and date type (`A5101BenifitsReposity::getChartStatistics`) (string-only: no caller chain in `data/endpoints.json`, inferred from the builder name).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_system_profit_detail` (asm-traced): URL string at `charging/ui/page/device/a5101/benifits/a5101_benifits_http_repository.dart @0x2c112ec`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2c112e4`, in `A5101BenifitsReposity::getChartStatistics` (`charging/ui/page/device/a5101/benifits/a5101_benifits_http_repository.dart @0x2c111c4`), sent through `requestHttp` (`@0x2c11320`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `A5101BenifitsReposity::getChartStatistics` (`charging/ui/page/device/a5101/benifits/a5101_benifits_http_repository.dart`, call `@0x2c11320`, argument list `@0x2c11318`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

(asm-traced) Each sender stores its keys in one map literal with type arguments `<String, String>` read at the cited address, so every value is a String: `A5101BenifitsReposity::getChartStatistics` (`charging/ui/page/device/a5101/benifits/a5101_benifits_http_repository.dart @0x2c112b8`, 3 keys). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `siteId` | string | yes | `"<siteId>"` | `charging/ui/page/device/a5101/benifits/a5101_benifits_http_repository.dart @0x2c11280` |
| `start` | string | yes | `"<start>"` | `charging/ui/page/device/a5101/benifits/a5101_benifits_http_repository.dart @0x2c11294` |
| `dateType` | string | yes | `"<dateType>"` | `charging/ui/page/device/a5101/benifits/a5101_benifits_http_repository.dart @0x2c112a4` |

## `param_type`/`cmd`

n/a

## Response model (link)

- `charging::A5101BenifitsModel`, parsed by `A5101BenifitsModel.fromJson` at `charging/ui/page/device/a5101/benifits/a5101_benifits_http_repository.dart @0x2c11eb0` (success closure `@0x2c11e30`, `bl` target `[package:charging/model/a5101/a5101_benifits_model/a5101_benifits_model.dart]`).

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::A5101BenifitsModel`): `savingsUnit` (String?), `saveCarbonsUnit` (String?), `powerGenerationsUnit` (String?), `savings` (List?), `saveCarbons` (List?), `powerGenerations` (List?), `percents` (List?), `selfPowerPercent` (String?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "siteId": "<siteId>",
  "start": "<start>",
  "dateType": "<dateType>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/device/a5101/benifits/a5101_benifits_http_repository.dart`: `getChartStatistics` @0x2c111c4 (requestHttp; encrypted: default-true (requestHttp) — verify)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Which `dateType` values the profit page sends: the three fields are parameters (`charging/ui/page/device/a5101/benifits/a5101_benifits_http_repository.dart @0x2c11290`, `@0x2c112a0`, `@0x2c112b4`) and their callers were not found in `data/endpoints.json`.
- `cacheKey` and `debounceMills` are passed by name (`charging/ui/page/device/a5101/benifits/a5101_benifits_http_repository.dart @0x2c11320`); how the cache key is built was not read.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
