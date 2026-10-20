> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_annual_report

## Purpose

Loads the annual report ("Post 2024") for the logged-in account (callers `HttpRequestControllerImpl::getAnnualReport` from `HomeBaseHttpReposity::getAnnualReportPost`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/get_annual_report` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x2404c20`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2404c18`, in `HttpRequestControllerImpl::getAnnualReport` (`charging/http/http_request_repository_impl.dart @0x2404b98`), sent through `requestHttp` (`@0x2404c48`).

## Encrypted?

Plain-wrapper call (asm-traced): the sender calls `HttpRequestControllerImpl::requestHttp` (`charging/http/http_request_repository_impl.dart @0x2264938`) at `charging/http/http_request_repository_impl.dart @0x2404c48` without a `needEncryption` argument. So the default `needEncryption: true` applies and rule 3 of [encryption.md](../../encryption.md#rule-and-resulting-counts) holds: the SDK path is taken whenever the SDK reports a logged-in state and the URL passes the base-URL predicate, otherwise the plain Dio path; that is decided at run time by `HttpEncryptionDecorator::request` (`charging/http/HttpEncryptionDecorator.dart @0x4868ff4`), not by this page.

## Request

(asm-traced) No request fields: the body argument is the empty map literal (`THR::empty_array`, `Map._fromLiteral`) at `charging/http/http_request_repository_impl.dart @0x2404be4`.

## `param_type`/`cmd`

n/a

## Response model (link)

- [`Post2024Model`](../../../models/other.md#post2024model), parsed by `Post2024Model.fromJson` at `charging/http/http_request_repository_impl.dart @0x2404cb8`

## Response

(asm-traced) For each sender that parses a model, the keys below are the top-level keys of the model; that sender adds no wrapper fields of its own in the code read.

- `Post2024Model` top-level keys (`data/models.json`, `charging::Post2024Model`): `status` (int?).

## Example request/response

Request, synthesized: the body is the empty object.

```json
{}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getAnnualReport` @0x2404b98 (requestHttp, default `needEncryption: true`)

Called from:

- `charging/http/http_request_repository.dart::getAnnualReport`
- `charging/ui/page/home/home_base_http_reposity.dart::getAnnualReportPost`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Which account data the annual report covers and when the server has one: server behaviour, not visible in the app.
## Device-tested by

none
