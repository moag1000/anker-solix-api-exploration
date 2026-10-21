> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_easter_egg_trigger_list

## Purpose

Loads the easter-egg trigger records of a charger for the easter-egg pages (callers `requestEasterEggRecord` in the A2345 easter-egg logic and `_requestEasterEggRecord` in the A91B2 easter-egg logic) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`charger_get_triggers` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /mini_power/v1/app/egg/get_easter_egg_trigger_list` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x276fc94`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x276fc8c`, in `HttpRequestControllerImpl::getEasterEggRecord` (`charging/http/http_request_repository_impl.dart @0x276fbe0`), sent through `encryptionRequestHttp` (`@0x276fcbc`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) `HttpRequestControllerImpl::getEasterEggRecord` (`charging/http/http_request_repository_impl.dart @0x276fbe0`) stores one key, `device_sn`, unconditionally in a map literal with type arguments `<String, String>` (`@0x276fc48`), so the value is a String.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | `charging/http/http_request_repository_impl.dart @0x276fc34` (map literal `<String, String>` `charging/http/http_request_repository_impl.dart @0x276fc48`) |

## `param_type`/`cmd`

n/a

## Response model (link)

- [`EasterEggTiggerRecordModel`](../../../../models/charger.md#eastereggtiggerrecordmodel), parsed per list element by `EasterEggTiggerRecordModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x276fe4c`. The success closure (`@0x276fcd8`) reads the key `egg_trigger_list` (`@0x276fd40`), casts it to `List?` (`@0x276fd80`), replaces `null` by an empty growable list (`cmp w0, NULL` `@0x276fd98`), parses each element and passes the resulting `List<EasterEggTiggerRecordModel>` (`@0x276fd1c`) to the callback (`ClosureCall` `@0x276feec`).

## Response

Top-level key of the response: `egg_trigger_list` (list of records). Keys of one record (`data/models.json`, `charging::EasterEggTiggerRecordModel`): `egg_type` (int?), `egg_name` (String?), `egg_des` (String?), `egg_image` (String?), `trigger_time` (int?), `status` (int?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<device_sn>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure `charging/http/http_request_repository_impl.dart @0x226824c` forwards code and message to a stored callback without reading them). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getEasterEggRecord` @0x276fbe0 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getEasterEggRecord`
- `charging/ui/page/device/a2345/a2345easter_egg/a2345easter_egg_logic.dart::requestEasterEggRecord`
- `charging/ui/page/device/a91b2/a91b2easter_egg/a91b2easter_egg_logic.dart::_requestEasterEggRecord`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Which `egg_type` and `status` values the server returns: the model stores them as `int?` and the pages that read them were not decoded for this.
- Whether the list is ordered or filtered by the server.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
