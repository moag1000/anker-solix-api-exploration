> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# Template: model page

Copy to `models/<class>.md` or a section of `models/<group>.md`, the owner of model field lists. Tags (see `METHODOLOGY.md`): `asm-traced` · `string-only` · `upstream-confirmed` · `device-tested`. Integers from asm follow the Smi rule in [../../METHODOLOGY.md](../../METHODOLOGY.md); cite `file.dart @0xADDR` next to every number. A fact lives on one owner page (see [../STRUCTURE.md](../STRUCTURE.md)); other pages link. Section order is fixed.

## Status header

One line, first line of the page: `> Verified against: App 3.24.3 · Date: YYYY-MM-DD · Confidence: <tag> · Owner page: <path or "this page">`.

## Purpose

One sentence: what the model carries. Tag: any.

## Dart class + file

Class name, Dart file, and `@0xADDR` of `fromJson`. Tag: `asm-traced`.

## Fields

Table `JSON key | Dart type | nullable | since | source`. `since` is the app version the key first appears in; `source` is `file.dart @0xADDR` or a tag. Tag: per row.

## Produced by

Links to the `api/<service>/<endpoint>.md` pages that return (or accept) this model. Tag: `asm-traced`.

## Consumed by

UI page and Dart file that read it, with `file.dart @0xADDR`. Tag: `asm-traced`.

## Changed since 3.18.0

Added, removed, retyped keys between 3.18.0 and 3.24.3. Tag: `asm-traced` (3.24.3 side).

## Known unknowns

Bullet list of open questions. Tag: none.

---

**Example skeleton — placeholders only, not a fact page**

> Verified against: App 3.24.3 · Date: YYYY-MM-DD · Confidence: <tag> · Owner page: <path or "this page">

# StationPowerLimitModel

## Status header

(see first line above)

## Purpose

<one sentence>

## Dart class + file

`<ClassName>`, `<file.dart>`, fromJson `@0x<ADDR>`

## Fields

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `<json_key>` | <type> | <yes/no> | <version> | `<file.dart @0xADDR>` |

## Produced by

`api/<service>/<endpoint>.md`

## Consumed by

<UI page>, `<file.dart @0xADDR>`

## Changed since 3.18.0

- <added/removed/retyped>: `<json_key>`

## Known unknowns

- <open question>
