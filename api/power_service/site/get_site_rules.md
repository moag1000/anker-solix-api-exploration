> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_site_rules

## Purpose

Reads the site rule list of an A17B1 site: `SiteLogic::_getSiteRules` (`green_energy/site/site_logic.dart`) and `HomeBaseHttpReposity::checkNetworkConnect` call `getSiteRules`.

## Upstream name

`site_rules` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/site/get_site_rules` (asm-traced): URL string at `http_request_repository_impl.dart @0x2910c14`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2910c0c`, in `HttpRequestControllerImpl::getSiteRules` (`http_request_repository_impl.dart @0x2910b84`).

## Encrypted?

Plain-wrapper call (asm-traced): the sender calls `HttpRequestControllerImpl::requestHttp` (`charging/http/http_request_repository_impl.dart @0x2264938`) at `charging/http/http_request_repository_impl.dart @0x2910c3c` without a `needEncryption` argument. So the default `needEncryption: true` applies and rule 3 of [encryption.md](../../encryption.md#rule-and-resulting-counts) holds: the SDK path is taken whenever the SDK reports a logged-in state and the URL passes the base-URL predicate, otherwise the plain Dio path; that is decided at run time by `HttpEncryptionDecorator::request` (`charging/http/HttpEncryptionDecorator.dart @0x4868ff4`), not by this page.

## Request

The body is an empty map literal (`ldr x16, [THR, #0xa8]` empty array `@0x2910bcc`, `Map._fromLiteral` `@0x2910bd4`); the builder contains no `[]=` call, so no key is added. The map goes to `requestHttp` (`@0x2910c3c`). This sender uses `requestHttp`, not `encryptionRequestHttp`.

## `param_type`/`cmd`

n/a

## Response model (link)

`charging::A17B1SiteRules` (`data/models.json` key; fields on [`models/other.md`](../../../models/other.md#a17b1siterules)), parsed in the builder's success closure `http_request_repository_impl.dart @0x2910c58` by `A17B1SiteRules.fromJson`.

## Response

The model has the single top-level key `rule_list` (element type not resolved in `data/models.json`).

## Example request/response

Request, synthesized

```json
{}
```

Response keys: see Response; no capture.

## Errors seen

None traced: the builder passes the `postJML` failure template (`@0x226824c`) to the callers' failure callbacks, which were not read. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getSiteRules` @0x2910b84 (requestHttp, default `needEncryption: true`)

Called from:

- `charging/http/http_request_repository.dart::getSiteRules`
- `charging/ui/page/green_energy/site/site_logic.dart::_getSiteRules`
- `charging/ui/page/home/home_base_http_reposity.dart::checkNetworkConnect`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta. The model `A17B1SiteRules` is `≤3.18.0` in `data/models.json`.

## Known unknowns

- The element structure of `rule_list`. — reclassified: server (not visible in the app: the model keeps the items untyped)
- Failure handling in the two callers was not read. — traced 2026-10-20: the call sites pass no `fail` closure among their named arguments: `HomeBaseHttpReposity.checkNetworkConnect` (`charging/ui/page/home/home_base_http_reposity.dart @0x34bc90c`): no named argument; `SiteLogic._getSiteRules` (`charging/ui/page/green_energy/site/site_logic.dart @0x2910ad0`): named arguments `dialog`. Failure then falls to the callee's default or to the awaiting code, neither of which was read

## Device-tested by

none
