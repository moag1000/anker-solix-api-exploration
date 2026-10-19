> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get

## Purpose

Reads the electrician contact data (name and email) stored for a site; the text-info dialog of the AX170 (ATS) setup shows it when it opens.

## Upstream name

`none` (no upstream name). Upstream lists the URL without a key in `api/apitypes.py` (line 271, docstring list of endpoints "neither implemented nor explored"); the comment there ("needs owner, {\"site_id\": siteId}, shows electrician name and email") is the upstream author's note, not a test result.

## Method+URL

`POST /power_service/v1/site/electrician/get` (asm-traced). Sender: `TextInfoDialogLogic.getElectricianInfo` (`base_service/view/text_info_dialog/text_info_dialog_logic.dart` `@0x2bc7bfc`); the path literal has no leading slash (`@0x2bc7cc8`), the method is the string `"POST"` (`@0x2bc7ce0`).

## Encrypted?

Direct SDK call, path C (asm-traced): the dialog logic calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`text_info_dialog_logic.dart @0x2bc7d70`, call `@0x2bc7d80`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively (mechanics: [../../../sdk_senders.md](../../../sdk_senders.md#the-common-envelope), background: [../../../encryption.md](../../../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a `<String, String>` map of one pair (`r2 = 4`, `@0x2bc7cfc`). The function refuses to send with an empty site id (`ax170: getElectricianInfo: siteId is empty`, `@0x2bc7c74`).

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | String | yes | `<site id>` | `text_info_dialog_logic.dart @0x2bc7d04`; value is the dialog controller's site id field |

Upstream confirms the body and notes that the call needs the owner account.

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): no model is parsed; the function decodes JSON text itself.

## Response

After `handle` returns (`@0x2bc7d80`), the function reads the key `data` of the SDK data as a `String?` (`@0x2bc7df0`, `r8 = String?` `@0x2bc7e2c`), defaults it to `"{}"` (`@0x2bc7e48`), decodes it with `JsonCodec.decode` (`@0x2bc7e60`) into a `Map<String, dynamic>?`, logs `ax170: getElectricianInfo jsonData` (`@0x2bc7e94`) and reads two keys, each defaulting to the empty string (`@0x2bc7fd0`, `@0x2bc8000`).

| field | type | required | example | source |
|---|---|---|---|---|
| `data` | String (JSON text) | yes | `"{\"electrician_name\": \"...\", \"electrician_mail\": \"...\"}"` | `text_info_dialog_logic.dart @0x2bc7df0` |
| `electrician_name` | String | no | `Max Muster` | `text_info_dialog_logic.dart @0x2bc7edc` (inside the decoded `data`) |
| `electrician_mail` | String | no | `electrician@example.org` | `text_info_dialog_logic.dart @0x2bc7f50` (inside the decoded `data`) |

## Example request/response

Request, synthesized

```json
{ "site_id": "<site id>" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `_TextInfoDialogState.initState` (`base_service/view/text_info_dialog/text_info_dialog.dart @0x2bc7b10`), through `TextInfoDialogLogic.getElectricianInfo`

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x1037a8`); the sender was not compared function by function. 3.24.3: present, pool `pp+0x153530`. since: ≤3.18.0.

## Known unknowns

- That `data` is a JSON string (not an object) is what the Dart code assumes (`String?` cast, then `decode`); no capture confirms the wire shape.
- The log prefix is `ax170`; whether other site types also store an electrician is not known.

## Device-tested by

none
