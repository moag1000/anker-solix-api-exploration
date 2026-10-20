> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# site_data_check

## Purpose

Checks whether a site has exportable data for the chosen time range: `SiteEnergyExportLogic::updateMode` (`site_energy_export_logic.dart`) calls `_checkDataOfSiteSupportExport` (`@0x2c34c20`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/site/site_data_check` (asm-traced): URL string at `site_energy_export_logic.dart @0x2c34e68`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2c34e60`, in `SiteEnergyExportLogic::_checkDataOfSiteSupportExport` (`site_energy_export_logic.dart @0x2c34c20`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is a 2-pair map literal typed `<String, String>` (type arguments `@0x2c34e1c`, pool `pp+0xa4d0`) built in `_checkDataOfSiteSupportExport` (`AllocateArray r2 = 8` `@0x2c34de4`); the method returns early when the site id or the time parameter is empty (`cbz` `@0x2c34d28`, `cbnz` `@0x2c34d30`).

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | string | yes | `"<site_id>"` | key `@0x2c34dec`, value store `@0x2c34e04` (`field_13` of the closure context, `@0x2c34dfc`) |
| `current_time` | string | yes | `"<current_time>"` | key `@0x2c34e08`, value store `@0x2c34e18` (result of `timeParamOfDate()` `@0x2c34d10`) |

## `param_type`/`cmd`

n/a

## Response model (link)

None: no model class is parsed. The success closure `site_energy_export_logic.dart @0x2c35174` checks that the response is a `Map` (`InstanceOfStub` `@0x2c3523c`) and reads the key `exist_data` (`@0x2c35264`; null becomes `false`, `@0x2c35280`).

## Response

Key read by the app: `exist_data` (bool-like; null is treated as false).

## Example request/response

Request, synthesized (decrypted body as built by `_checkDataOfSiteSupportExport`)

```json
{"site_id": "<site_id>", "current_time": "<current_time>"}
```

Response, synthesized (the one key read; value is a placeholder, not a capture)

```json
{"code": 0, "msg": "success", "data": {"exist_data": true}}
```

## Errors seen

None traced. The failure callback `site_energy_export_logic.dart @0x2c350b4` logs the site id, the code and the message and completes the future; no code is compared (the 64-bit compares in the success closure, 16075, are class-id tests). Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/widgets/data_export/energy_flow/site_energy_export_logic.dart`: `_checkDataOfSiteSupportExport` @0x2c34c20 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/widgets/data_export/energy_flow/site_energy_export_logic.dart::updateMode`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- The format of `current_time` (it comes from `timeParamOfDate()`, not decoded here).
- Whether the server answers with other keys than `exist_data`.
- How the app decides export support beyond this call (`supportExportWithSiteType`, `@0x2c352ac`).

## Device-tested by

none
