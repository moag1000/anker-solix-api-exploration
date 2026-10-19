> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_entry_show

## Purpose

Asks whether the Anka assistant entry button should be shown for a site on the AI EMS screens (the button's support check).

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /smart_service/v1/app/anka/get_entry_show` (asm-traced). Sender: `AnkaEntryButton.checkAnkaSupport` (`ak_soft_ems/aiems/public_widget/anka_entry_button.dart @0x2bf0cc0`); the URL literal is loaded at `@0x2bf0df0` and the method is `Method.post` (pool entry `pp+0xa7e0`, `@0x2bf0de8`).

## Encrypted?

Yes by wrapper (asm-traced): `checkAnkaSupport` calls `HttpServiceImpl.encryptionRequestHttp` (`anka_entry_button.dart @0x2bf0e14`) with the named arguments `fail` and `success` only and without `needEncryption`, so the default `true` applies ([encryption.md](../../../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time ([encryption.md](../../../encryption.md)); asm alone does not decide it. The inventory lists two extra `url_provider` rows for the URL because the failure closure (`@0x2bf0e34`) and the success path (`@0x2bf0ec4`) mention the literal.

## Request

Body is a `<String, String>` map of two pairs (`r2 = 8`, `@0x2bf0d4c`).

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | String | yes | `<site id>` | `anka_entry_button.dart @0x2bf0d54`; the argument |
| `source` | String | yes (constant) | `"aiems"` | `anka_entry_button.dart @0x2bf0d68`; value `"aiems"` `@0x2bf0d70` |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): no model; the success closure reads one key.

## Response

The function returns a `Future<bool>` (`@0x2bf0ce0`). The success closure (`@0x2bf0ec4`) checks that the data is a `Map<String, dynamic>` (`@0x2bf0f28`), reads the key `show` (`@0x2bf0f70`, default `false` `@0x2bf0f8c`) and completes the future with it (`@0x2bf0fdc`); the failure closure logs `Http request /smart_service/v1/app/anka/get_entry_show failed code: ..., msg: ...` (`@0x2bf0e34`).

| field | type | required | example | source |
|---|---|---|---|---|
| `show` | bool | no | `true` | `anka_entry_button.dart @0x2bf0f70` |

## Example request/response

Request, synthesized

```json
{ "site_id": "<site id>", "source": "aiems" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../errors.md).

## Callers in app

- `_AnkaEntryButtonState._checkSupport` (`ak_soft_ems/aiems/public_widget/anka_entry_button.dart @0x2bf0c5c`), through `AnkaEntryButton.checkAnkaSupport`

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 object pool). 3.24.3: present (pool `pp+0x14e238`). since: 3.24.3.

## Known unknowns

- Whether `source` takes other values on other screens is not known (only `aiems` is sent here; the question-bank call also sends `aiems`).

## Device-tested by

none
