> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_support_func

## Purpose

Asks which country codes support the automatic disaster-preparedness (backup power) function for the current site (caller `WeatherManager::fetchSupportCountryCodes`, started from `WeatherDisplayView::_navigateToPlaceSelectionView`) (string-only: inferred from the caller and class names, the chain is not in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_disaster_prepared/get_support_func` (asm-traced): URL string `@0x451d8cc`, method object `Method.post` (pool entry `pp+0xa7e0`) `@0x451d8c4`, in `WeatherManager::fetchSupportCountryCodes` (`unity/src/main/weather/weather_manager.dart @0x451d6dc`), sent through `HttpServiceImpl::encryptionRequestHttp` (`@0x451d8f0`). The call is skipped, with a log line, when the current site id is empty (`cbnz` `@0x451d73c`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(string-only: one field type is not read) One sender. The map literal has the type arguments `<String, Object>` (`unity/src/main/weather/weather_manager.dart @0x451d7ec`), which name no value type.

| field | type | required | example | source |
|---|---|---|---|---|
| `type` | int (Smi, w) | yes | `2` (raw immediate 4, 32-bit store) | `unity/src/main/weather/weather_manager.dart @0x451d7c8` (value store `@0x451d7d4`, constant `@0x451d7d0`) |
| `identifier_id` | ? | yes | `"<site_id>"` | `unity/src/main/weather/weather_manager.dart @0x451d7d8` (value from a manager field, `LoadField` `@0x451d724`, store `@0x451d7e8`) |

## `param_type`/`cmd`

n/a

## Response model (link)

`unity::SupportFunc` (no `models/` page), parsed by `SupportFunc.fromJson` at `unity/src/main/weather/weather_manager.dart @0x451dab4` in the success closure `@0x451da28` of `fetchSupportCountryCodes`; the closure completes the pending `Future<SupportFunc?>` with the result (`complete` `@0x451dbec`) and with null when parsing fails (`@0x451dc64`).

## Response

(asm-traced for the model) Top-level keys of `SupportFunc` (`data/models.json`, `unity::SupportFunc`): `support_auto_disaster` (bool), `support_country_code` (int). The closure maps the parsed object to a list of strings through `ListBase::map` (`unity/src/main/weather/weather_manager.dart @0x451db24`) before it stores the result; the element type and the source field were not followed.

## Example request/response

Request, synthesized (decrypted body as built by `fetchSupportCountryCodes`; `<...>` are placeholders, not captured values)

```json
{
  "type": 2,
  "identifier_id": "<site_id>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure `unity/src/main/weather/weather_manager.dart @0x451d96c` logs `code=` and `msg=`). Code meanings are owned by `api/errors.md`.

## Callers in app

- `unity/src/main/weather/weather_manager.dart`: `fetchSupportCountryCodes` @0x451d6dc (encryptionRequestHttp; encrypted: true)

Called from:

- `unity/src/main/weather/weather_display_view.dart::_navigateToPlaceSelectionView`

## Since/changed

3.18.0: absent. 3.24.3: present (listed under added endpoints in `tools/out/diff_3.18.0_3.24.3.md`). since: 3.24.3.

## Known unknowns

- Type of `identifier_id`: a value loaded from a manager field whose declared type is not visible. — attempted 2026-10-20 (two-hop not readable: the sender is `WeatherManager::fetchSupportCountryCodes` (`unity/src/main/weather/weather_manager.dart @0x451d8cc`), which reads a manager field with no declaration in the asm)
- Why `support_country_code` is typed int in the class while the closure builds a list of strings from the parsed object (`unity/src/main/weather/weather_manager.dart @0x451db10`, type argument `<String>`): the conversion was not followed.
- What `type` 2 selects: the app stores this constant only. — reclassified: server (2026-10-20: the app stores the constant 2 (decoded on this page); what the number selects is not derivable from the app)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
