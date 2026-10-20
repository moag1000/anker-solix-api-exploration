> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_comb_addable_sites

## Purpose

Lists the sites a set of devices can join: `A1782ElectricitySceneLogic::_getAddableSiteList` and `OpenProcessLogic::getUserSiteListReq` (A17C1 open process) call `getDeviceJoinSiteList` with a list of device descriptions.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/site/get_comb_addable_sites` (asm-traced): URL string at `http_request_repository_impl.dart @0x28bb218`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x28bb210`, in `HttpRequestControllerImpl::getDeviceJoinSiteList` (`http_request_repository_impl.dart @0x28bb164`).

## Encrypted?

Plain-wrapper call (asm-traced): the sender calls `HttpRequestControllerImpl::requestHttp` (`charging/http/http_request_repository_impl.dart @0x2264938`) at `charging/http/http_request_repository_impl.dart @0x28bb240` without a `needEncryption` argument. So the default `needEncryption: true` applies and rule 3 of [encryption.md](../../encryption.md#rule-and-resulting-counts) holds: the SDK path is taken whenever the SDK reports a logged-in state and the URL passes the base-URL predicate, otherwise the plain Dio path; that is decided at run time by `HttpEncryptionDecorator::request` (`charging/http/HttpEncryptionDecorator.dart @0x4868ff4`), not by this page.

## Request

The body is a 1-pair map literal typed `<String, List<DeviceJoinSiteModel>?>` (type arguments `@0x28bb1cc`) built in `getDeviceJoinSiteList` (`http_request_repository_impl.dart @0x28bb164`; `Map._fromLiteral` `@0x28bb1d8`). The sender is `requestHttp` (`@0x28bb240`), not `encryptionRequestHttp`.

| field | type | required | example | source |
|---|---|---|---|---|
| `devices` | list | yes | | key `@0x28bb1b8`, value store `@0x28bb1c8` (parameter at `fp-0x10`; the map type says a list of `DeviceJoinSiteModel` objects, possibly null) |

Elements of `devices` (asm-traced): `DeviceJoinSiteModel::toJson` (`charging/ui/page/device/a17c1/open_process/open_process_state.dart @0x28bb364`) writes two keys unconditionally, `device_sn` (`@0x28bb390`) and `device_model` (`@0x28bb3ac`), from two fields of the object (`field_7`, `field_b`); the class has no `fromJson` in the asm, so the field types are not declared anywhere the app shows. The list holds `DeviceJoinSiteModel` objects (map type argument above), so each element carries these two keys if the HTTP layer serialises the objects with `toJson`; that step is outside the Dart code read.

## `param_type`/`cmd`

n/a

## Response model (link)

`charging::A17B1AddableSiteModel` (`data/models.json` key; fields on [`models/other.md`](../../../models/other.md#a17b1addablesitemodel)), parsed in the success closure `http_request_repository_impl.dart @0x262e1e4` by `A17B1AddableSiteModel.fromJson` (the closure is the one `getAddableSiteList` uses; the code is shared).

## Response

Top-level keys of the model (from `data/models.json`): `site_list` and `joined_site_id` (types not resolved there).

## Example request/response

Request, synthesized

```json
{"devices": ["<DeviceJoinSiteModel objects>"]}
```

Response keys: see Response; no capture.

## Errors seen

None traced. The builder's failure callback `@0x238cda4` is a forwarding template closure that loads its two arguments and calls nothing itself; no code is compared in it. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getDeviceJoinSiteList` @0x28bb164 (requestHttp, default `needEncryption: true`)

Called from:

- `charging/http/http_request_repository.dart::getDeviceJoinSiteList`
- `charging/ui/page/device/a1782/station/electricity_scene/a1782_electricity_scene_logic.dart::_getAddableSiteList`
- `charging/ui/page/device/a17c1/open_process/open_process_logic.dart::getUserSiteListReq`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta. The model `A17B1AddableSiteModel` is `≤3.18.0` in `data/models.json`.

## Known unknowns

- The element structure of `site_list`. — reclassified: server (elements of an untyped list; the content is server data)

## Device-tested by

none
