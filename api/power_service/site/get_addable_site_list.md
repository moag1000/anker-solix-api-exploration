> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_addable_site_list

## Purpose

Asks which sites an A17B1 (or similar) device can join: `HttpBusinessImpl::getDeviceIsJoinedSite` and `HttpRequestControllerImpl::getAddableSiteList` send the device serial and model; called from the electricity-scene, system-policy, A17C0 switch-mode, A17C1 home, join-system and create-site-progress logics.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/site/get_addable_site_list` (asm-traced) at the senders that load a `Method` object next to the URL string (pool entry `pp+0xa7e0`, `Method.post`):

- `HttpBusinessImpl::getDeviceIsJoinedSite` (`http_business_impl.dart @0x239b964`): URL string `@0x239ba44`, method object `Method.post` (`pp+0xa7e0`) `@0x239ba3c`.
- `HttpRequestControllerImpl::getAddableSiteList` (`http_request_repository_impl.dart @0x262e088`): URL string `@0x262e1a0`, method object `Method.post` (`pp+0xa7e0`) `@0x262e198`.

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

Both senders type their map `<String, String>`, so every value is a String.

Sender `HttpBusinessImpl::getDeviceIsJoinedSite` (`http_business_impl.dart @0x239b964`): 2 pairs (`AllocateArray r2 = 8` `@0x239b9b4`), type arguments `@0x239b9e4`.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | key `@0x239b9bc`, value store `@0x239b9cc` |
| `device_model` | string | yes | `"<device_model>"` | key `@0x239b9d0`, value store `@0x239b9e0` |

Sender `HttpRequestControllerImpl::getAddableSiteList` (`http_request_repository_impl.dart @0x262e088`): two map literals, both typed `<String, String>` (`@0x262e11c`, `@0x262e154`); the sender uses `requestHttp`.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | optional | `"<device_sn>"` | key `@0x262e0f4`, value store `@0x262e104`; present only when the parameter at `fp-0x18` is non-null (`cmp w0, NULL` `@0x262e0dc`, the other branch builds the second literal) |
| `device_model` | string | yes | `"<device_model>"` | first literal key `@0x262e108`, store `@0x262e118`; second literal key `@0x262e140`, store `@0x262e150` |

## `param_type`/`cmd`

n/a

## Response model (link)

`charging::A17B1AddableSiteModel` (`data/models.json` key; fields on [`models/other.md`](../../../models/other.md#a17b1addablesitemodel)), parsed by `A17B1AddableSiteModel.fromJson` in the success closures `http_business_impl.dart @0x239bfe4` and `http_request_repository_impl.dart @0x262e1e4`.

## Response

Top-level keys of the model (from `data/models.json`): `site_list` and `joined_site_id` (types not resolved there).

## Example request/response

Request, synthesized (decrypted body of `getDeviceIsJoinedSite`)

```json
{"device_sn": "<device_sn>", "device_model": "<device_model>"}
```

Response keys: see Response; no capture.

## Errors seen

None traced. The failure callbacks are the forwarding templates (`http_request_repository_impl.dart @0x226824c` and `@0x238cda4`); the callers' failure callbacks were not read. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_business_impl.dart`: `getDeviceIsJoinedSite` @0x239b964 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/http/http_request_repository_impl.dart`: `getAddableSiteList` @0x262e088 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::getAddableSiteList`
- `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart::_getAddableSiteList`
- `charging/ui/page/device/a17b1/system_policy/system_policy_logic.dart::_getSiteConfig`
- `charging/ui/page/device/a17c0/a17c0SwitchMode/a17c0_switch_mode_logic.dart::deviceConnect`
- `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart::getUserSiteListReq`
- `charging/ui/page/device/connect/create_join_device_to_system/join_system/join_system_logic.dart::queryExistSystems`
- `charging/ui/page/device/main/sitation_energy_system/create_site_progress_handler/create_site_progress_handler.dart::checkCreateSiteProgressIsComplete`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta. The model `A17B1AddableSiteModel` is `≤3.18.0` in `data/models.json`.

## Known unknowns

- The element structures of `site_list` and `joined_site_id` (the model keeps them untyped).
- Why `getAddableSiteList` may omit `device_sn`: the app sends the model-only body when the serial is null; the server reaction is not derivable.
- Whether `requestHttp` (`getAddableSiteList`) encrypts the call (non-`encryption` wrapper, default `needEncryption` true, see `api/encryption.md`).

## Device-tested by

none
