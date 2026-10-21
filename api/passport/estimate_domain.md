> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# estimate_domain

## Purpose

Asks the account server for the API host of the user's region; sent by `HttpRequestControllerImpl::getRegionHostRequest` for `RegionSwitchHandler::_getRegionHostAsync`, `RegionLogic::showConfirmDialog` and `SplashLogic::requestHostByRegion` (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /passport/estimate_domain` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x27408ac`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x274093c`, in `HttpRequestControllerImpl::getRegionHostRequest` (`charging/http/http_request_repository_impl.dart @0x274080c`), sent through `requestHttp` (`@0x274097c`).

The URL literal is appended to a base URL: `getLocalHostByRegion` (`@0x27408a8`) returns the host and the `+` operator joins it with the literal (`@0x27408b8`), so this request goes to a regional host, not to the usual base URL; the call passes the named arguments `fail`, `needEncryption`, `needTerminal`, `showLoading`, `useBaseUrl` (`@0x2740974`) with `false` loaded at `@0x2740958`, `@0x2740964` and `@0x2740968`; which argument carries which `false` was not decoded.

## Encrypted?

encrypted: `false` (asm-traced): the sender passes `needEncryption` explicitly in the named arguments (`charging/http/http_request_repository_impl.dart @0x2740974`, list `fail`, `needEncryption`, `needTerminal`, `showLoading`, `useBaseUrl`); by the slot indices in that list the value is the `false` loaded at `charging/http/http_request_repository_impl.dart @0x2740964`, as it is for `needTerminal` and `showLoading`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

Named arguments of the `requestHttp` call (traced 2026-10-20): the descriptor `[0x1, 0xa, 0xa, 0x5, fail, 0x9, needEncryption, 0x8, needTerminal, 0x7, showLoading, 0x6, useBaseUrl, 0x5]` (`charging/http/http_request_repository_impl.dart @0x2740974`) gives each name its stack index counted from the first pushed value; the top of the stack is index 9. `fail` is the last value (`str x0, [SP]` `@0x2740970`), `needEncryption` the next one down (`r30 = false`, `stp lr, x16, [SP, #8]` `@0x274096c`), `needTerminal` the one below it (`r16 = false` `@0x2740968`), `showLoading` the sender parameter `fp-0x28` (`@0x274095c`) and `useBaseUrl` the constant `false` (`@0x2740958`). So `needEncryption` is `false` here, as the page states above; the inventory flag and the stack reading agree.

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `ab` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x27408cc` (value store `@0x27408e4`) |
| `mode` | int (Smi, w) | yes | `1` | `charging/http/http_request_repository_impl.dart @0x27408e8` (value store `@0x27408f8`) |

The map literal has type arguments `<String, Object>` (`@0x27408fc`), which is not evidence of a value type. `mode` is the Smi raw 2 stored with a 32-bit store (`@0x27408f4`, `@0x27408f8`), so 1. `ab` is read from a field of an object held by the sender (`LoadField r1 = r2->field_13`, `@0x27408dc`).

Value of `ab` (traced 2026-10-20, app side): the sender copies the first positional parameter into its closure context (`StoreField` `field_13` `charging/http/http_request_repository_impl.dart @0x2740858`) and `ab` reads it back (`@0x27408dc`). `RegionSwitchHandler::_getRegionHostAsync` (`charging/account/handlers/region_switch_handler.dart`) passes there the same variable that its log line prints as `region:` (`@0x2740730`, call `@0x27407b0`), and `handleRegionSwitch` calls it with its `region` argument when its domain parameter is empty (`@0x273c4e0`..`@0x273c4e4`, log `Domain parameter is empty, querying region host info via API`). The splash call (`SplashLogic::requestHostByRegion`, `charging/ui/page/account/splash/splash_logic.dart @0x296d8bc`) forwards its own argument (`@0x296d89c`). So `ab` is the region value the user or the stored settings selected; no declared type is read (the text of the log line suggests a String).

## `param_type`/`cmd`

n/a

## Response model (link)

[`RegionHostModel`](../../models/other.md#regionhostmodel), parsed by `RegionHostModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x2740b40` in the success closure `@0x2740a6c`, applied to the value of the response key `data` (`"data"` loaded at `@0x2740b08`, map lookup `@0x2740b0c`).

## Response

(asm-traced) Top-level keys of `RegionHostModel` (`data/models.json`, `charging::RegionHostModel`): `domain` (String?), `is_same_region` (bool?). The closure then compares `is_same_region` with `true` (`@0x2740b54`) and calls `handleRegionHostModel` (`@0x2740b74`).

What the domain is used for (traced 2026-10-20, app side): `HttpRequestControllerImpl::handleRegionHostModel` (`charging/http/http_request_repository_impl.dart @0x2740bcc`) reads the model's first field (`domain`, `field_7`, null test `@0x2740be8`) and calls `updateRegionDomain` (`@0x2740bf4`, function `@0x273c954`). That function prefixes `https://` when the text does not already contain it (test `@0x273c998` with the selector `GDT[cid_x0 + -0x1000]`, not named by Blutter, text built `@0x273c9b4`..`@0x273c9c8`), then logs `getRegionHost success: ` (`@0x273ca84`), compares the static `serverEnv` field with 8 (`cmp w0, #8` `@0x273ca3c`, tagged compare, Smi 4) to pick the key `"qa"` or another environment key (`@0x273ca44`, `@0x273ca50`) for the host table, and stores the host with `setHostByRegion` (`@0x273cb48`) after logging `reset local host: ` (`@0x273cab8`). So the value is a host name that the app accepts with or without the scheme.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "ab": "<ab>",
  "mode": 1
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or its closures. The failure closure (`@0x274099c`) logs the code and falls back to `getPrivacyPolicyData` (`@0x2740a1c`). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getRegionHostRequest` @0x274080c (requestHttp; encrypted: false, `needEncryption` passed explicitly)

Called from:

- `charging/account/handlers/region_switch_handler.dart::_getRegionHostAsync`
- `charging/http/http_request_repository.dart::getRegionHostRequest`
- `charging/ui/page/account/region/region_logic.dart::showConfirmDialog`
- `charging/ui/page/account/splash/splash_logic.dart::requestHostByRegion`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The declared type of `ab` (the region value, see Request): `handleRegionSwitch` and `requestHostByRegion` have no type annotations in the dump — attempted 2026-10-20 (two-hop not readable: `region_switch_handler.dart @0x273c4e0`, `splash_logic.dart @0x296d89c`)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
