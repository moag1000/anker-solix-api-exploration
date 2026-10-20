> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# dst

## Purpose

Reads the time-zone and daylight-saving information of the phone's city; sent by `HttpRequestControllerImpl::getCloudCurrentTimezone` and `::getDaylightSavingTime` for `A1340HomeLogic::_getDst` and `DeviceMainLogic::onInit` / `didChangeAppLifecycleState` (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /app/help/dst` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x33c8944`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x33c893c`, in `HttpRequestControllerImpl::getCloudCurrentTimezone` (`charging/http/http_request_repository_impl.dart @0x33c8864`), sent through `requestHttp` (`@0x33c8968`).

Same URL in the other sender(s) read:

- `POST /app/help/dst` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x286bcb8`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x286bcb0`, in `HttpRequestControllerImpl::getDaylightSavingTime` (`charging/http/http_request_repository_impl.dart @0x286bbe8`), sent through `encryptionRequestHttp` (`@0x286bcd8`).

## Encrypted?

encrypted: `true` for both senders (asm-traced): `getDaylightSavingTime` uses `encryptionRequestHttp`; `getCloudCurrentTimezone` calls `requestHttp` with the named argument `fail` only (`charging/http/http_request_repository_impl.dart @0x33c8960`), and `requestHttp` declares `needEncryption = true` (`charging/http/http_request_repository_impl.dart @0x2264944`). Scheme and header rules: `api/encryption.md`.

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `city` | string | yes | `"<city>"` | `charging/http/http_request_repository_impl.dart @0x33c88e4` (value store `@0x33c88f4`) |

The value is a String: both senders use a map literal with type arguments `<String, String>` (`@0x33c88f8`, `@0x286bc6c`); it comes from `getLocalTimezone` (`@0x33c889c`, `@0x286bc38`).

## `param_type`/`cmd`

n/a

## Response model (link)

no model: both success closures read one key from a map. `getCloudCurrentTimezone` (`charging/http/http_request_repository_impl.dart @0x33c897c`) tests the response with `Map` (`@0x33c8a38`), reads `timezone` (`@0x33c8a74`, default `"GMT0"` when absent, `@0x33c8a90`), casts it to `String` (`@0x33c8ad0`), builds a map with the keys `timeZoneName` and `timeZoneGMT` (`@0x33c8aec`, `@0x33c8b08`), serialises it with `jsonEncode` (`@0x33c8b34`) and stores it with `setCurrentTimezoneInfo`. `getDaylightSavingTime` (`@0x286bd7c`, argument typed `Map<String, dynamic>`) reads `timezone` as `String?` (`@0x286bdb0`, default empty string `@0x286be18`) and passes it to the callback (`ClosureCall` `@0x286be24`).

## Response

(asm-traced) One key is read from the top level of the response: `timezone` (String).

Consumer of the wrapped map (traced 2026-10-20, app side): `DeviceUtil::getCurrentTimezoneGMT` (`charging/util/device_util.dart @0x36c21e4`) reads the stored text with `getCurrentTimezoneInfo` (`@0x36c226c`), JSON-decodes it (`@0x36c2280`) and takes `timeZoneName` (`@0x36c2288`) and `timeZoneGMT` (`@0x36c22ec`), both cast to String. It first asks for the local time zone name (`getLocalTimezone` `@0x36c2208`); when the stored `timeZoneName` equals it (`==` `@0x36c23b8`, branch `@0x36c23bc`) the function returns the stored `timeZoneGMT` (`@0x36c23c8`), otherwise it calls `getTimezone` (`@0x36c23cc`). So the map is a cache of the cloud answer under the name it was fetched for; the first sender writes the same value into both keys.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "city": "<city>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender, its closures or the caller functions read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getCloudCurrentTimezone` @0x33c8864 (requestHttp; encrypted: default-true (requestHttp) — verify); `getDaylightSavingTime` @0x286bbe8 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getCloudCurrentTimezone`
- `charging/http/http_request_repository.dart::getDaylightSavingTime`
- `charging/ui/page/device/a1340/a1340home/a1340home_logic.dart::_getDst`
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::didChangeAppLifecycleState`
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::onInit`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What the `timezone` string looks like (an IANA name or a GMT offset): the app uses the value as stored name and as `timeZoneGMT`; its format was not read. — reclassified: server (2026-10-20: the app stores and forwards the string; its format is not derivable from the app code read here)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
