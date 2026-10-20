> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_device_product_info

## Purpose

Reads the product catalogue (icons and names) of HES devices for the main device page (`DeviceMainLogic::_initLogic`, `onMessageDispatch`, through `HttpRequestControllerImpl::getHesDeviceIcons`); the failure closure logs `SnNumberLogic 获取设备图标异常` ("get device icon error", my translation) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_device_product_info` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x2607930`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2607928`, in `HttpRequestControllerImpl::getHesDeviceIcons` (`charging/http/http_request_repository_impl.dart @0x26078cc`), sent through `requestHttp` (`@0x2607960`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `HttpRequestControllerImpl::getHesDeviceIcons` (`charging/http/http_request_repository_impl.dart`, call `@0x2607960`, argument list `@0x2607958`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

(asm-traced) `HttpRequestControllerImpl::getHesDeviceIcons` (`charging/http/http_request_repository_impl.dart @0x26078cc`) sends an empty map: the map literal gets the empty array (`@0x26078e8`) and no type arguments (`@0x26078ec`, `Map._fromLiteral` `@0x26078f0`), and the builder contains no `[]=` call. The named arguments are `fail`, `isLogResponse` and `showLoading`, both flags `false` (`@0x2607948`, `@0x260794c`).

| field | type | required | example | source |
|---|---|---|---|---|


## `param_type`/`cmd`

n/a

## Response model (link)

- [`HesProductsInfoModel`](../../models/hes.md#hesproductsinfomodel), parsed by `HesProductsInfoModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x26079e0` (success closure `@0x26079b8`, `bl` target `[package:charging/model/a5101/hes_products_info_model.dart]`).

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::HesProductsInfoModel`): `productsInfo` (unknown).

## Example request/response

Request: no body keys (empty map literal); response: not synthesized (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getHesDeviceIcons` @0x26078cc (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::getHesDeviceIcons`
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::_initLogic`
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::onMessageDispatch`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What `isLogResponse = false` changes: the HTTP layer was not read for it (the response is probably large; this is not read).
- Whether the server filters the catalogue by user or product line: the app sends no key.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
