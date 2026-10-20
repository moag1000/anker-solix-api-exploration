> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# export_account_data

## Purpose

Requests an export of the user's account data and optionally mails it; sent by `DataExportReposity::exportAccountData` (`charging/ui/page/user/dataExport/data_export_reposity.dart @0x29854bc`) (asm-traced for the sender; the inventory lists no caller, so the screen is not in the chain, string-only).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /privacy_service/v1/export_account_data` (asm-traced): URL string at `charging/ui/page/user/dataExport/data_export_reposity.dart @0x298560c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2985604`, in `DataExportReposity::exportAccountData` (`charging/ui/page/user/dataExport/data_export_reposity.dart @0x29854bc`), sent through `encryptionRequestHttp` (`@0x2985634`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `account` | ? | yes | ? | `charging/ui/page/user/dataExport/data_export_reposity.dart @0x2985574` (value store `@0x2985584`) |
| `send_email` | ? | yes | ? | `charging/ui/page/user/dataExport/data_export_reposity.dart @0x2985588` (value store `@0x2985598`) |
| `access_token` | ? | yes | ? | `charging/ui/page/user/dataExport/data_export_reposity.dart @0x298559c` (value store `@0x29855ac`) |
| `export_data_type` | ? | yes | ? | `charging/ui/page/user/dataExport/data_export_reposity.dart @0x29855b0` (value store `@0x29855c0`) |

The body map literal has type arguments `<String, Object>` (`charging/ui/page/user/dataExport/data_export_reposity.dart @0x29855c4`), not evidence of a value type, so all four values stay `?`. `access_token` is the proof of a prior password check (role by name; never documented as a value).

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the success closure (`charging/ui/page/user/dataExport/data_export_reposity.dart @0x2985650`) never reads its response argument; it logs `exportAccountData success` (`@0x2985684`) and calls the stored callback with the empty string (`@0x2985694`, `ClosureCall` `@0x29856a0`).

## Response

No response key is read by the app (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "account": "<account>",
  "send_email": "<send_email>",
  "access_token": "<access_token>",
  "export_data_type": "<export_data_type>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or its closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/user/dataExport/data_export_reposity.dart`: `exportAccountData` @0x29854bc (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of `account`, `send_email`, `access_token` and `export_data_type`: parameters stored into a `<String, Object>` literal.
- Which `export_data_type` values exist and what `send_email` changes: the callers' arguments were not decoded.
- Whether the export arrives by mail or as a record in `export_record_list`: not visible in the app.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
