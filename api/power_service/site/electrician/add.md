> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# add

## Purpose

Stores the contact data (name and email) of the electrician of a site; the text-info dialog of the AX170 (ATS) setup asks the user for them and sends them.

## Upstream name

`none` (no upstream name). Upstream lists the URL without a key in `api/apitypes.py` (docstring list, no comment); the read side `electrician/get` has the comment "needs owner, {\"site_id\": siteId}, shows electrician name and email".

## Method+URL

`POST /power_service/v1/site/electrician/add` (asm-traced). Sender: `TextInfoDialogLogic._setElectricianInfo` (`base_service/view/text_info_dialog/text_info_dialog_logic.dart` `@0x2e22a60`); the path literal has no leading slash (`@0x2e22c38`), the method is the string `"POST"` (`@0x2e22c50`).

## Encrypted?

Direct SDK call, path C (asm-traced): the dialog logic calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`text_info_dialog_logic.dart @0x2e22d08`, call `@0x2e22d18`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively (mechanics: [../../../sdk_senders.md](../../../sdk_senders.md#the-common-envelope), background: [../../../encryption.md](../../../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a `<String, String>` map of three pairs (`r2 = 12`, `@0x2e22c6c`). The function logs `ax170: _setElectricianInfo` and refuses to send with an empty site id (`isPass: false`, message `siteId is empty`, `@0x2e22b54`).

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | String | yes | `<site id>` | `text_info_dialog_logic.dart @0x2e22c74`; value is the dialog controller's site id field (`@0x2e22c84`) |
| `electrician_name` | String | yes | `Max Muster` | `text_info_dialog_logic.dart @0x2e22c90` |
| `electrician_mail` | String | yes | `electrician@example.org` | `text_info_dialog_logic.dart @0x2e22ca4` |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): `handle` is called without a type argument (`stp x16, NULL`, `@0x2e22d04`).

## Response

The function compares the result type with a success instance (`@0x2e22d34`); on success it logs `ax170: _setElectricianInfo success` and completes with `{isPass: true, message: "success"}` (`@0x2e22d8c`, `@0x2e22da8`); otherwise it logs the failure and completes with `{isPass: false, message: <failure text or the translation commonNetWorkErrorFix>}` (`@0x2e22e8c`, `@0x2e22eb0`). The answer body is not read.

## Example request/response

Request, synthesized

```json
{ "site_id": "<site id>", "electrician_name": "Max Muster", "electrician_mail": "electrician@example.org" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `TextInfoDialogLogic.onBottomButtonTap` (`base_service/view/text_info_dialog/text_info_dialog_logic.dart` `@0x2e22a2c`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x103710`); the sender was not compared function by function. 3.24.3: present, pool `pp+0x1534b0`. since: ≤3.18.0.

## Known unknowns

- Whether the electrician data is used for AX170 only or for any site type is not known (the log prefix is `ax170`).
- The server-side validation of the email address is not known.

## Device-tested by

none
