> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# Template: model page

Copy to `models/<class>.md` or a section of `models/<group>.md`, the owner of model field lists. Length: under 600 lines; add a table of contents above 150 lines (see [../STRUCTURE.md](../STRUCTURE.md)). Section order is fixed.

Tags (see [../../METHODOLOGY.md](../../METHODOLOGY.md)): `asm-traced` · `string-only` · `upstream-confirmed` · `device-tested`. Integers from asm follow the Smi rule in the same file; cite `file.dart @0xADDR` next to every number. A fact lives on one owner page (see [../STRUCTURE.md](../STRUCTURE.md)); other pages link.

Link if the target file exists today, otherwise write a code span.

The status header is the first line of the page, before the H1; it is NOT a section heading. Its format: `> Verified against: App 3.24.3 · Date: YYYY-MM-DD · Confidence: <tag> · Owner page: <path or "this page">`. The status-header tag is the LOWEST tag among the facts on the page (METHODOLOGY.md).

Sections that carry no API fact (Known unknowns, link-only "Related ..." sections, "Device-tested by" lists) are untagged by design; their instruction says `Tag: untagged by design (no API fact)`. Every fact-bearing table or section carries a tag.

Section order (status header line first, then):

0. Status header line (first line, before H1)
1. Purpose
2. Dart class + file
3. Fields
4. Produced by
5. Consumed by
6. Changed since 3.18.0
7. Known unknowns

## Purpose

One sentence: what the model carries. Tag: any.

## Dart class + file

Class name, Dart file, and `@0xADDR` of `fromJson`. Tag: `asm-traced`.

## Fields

Table `JSON key | Dart type | nullable | since | source`. `since` is the app version the key first appears in. Row tag goes in the `source` column: an asm citation `file.dart @0xADDR` (= asm-traced), `string-only`, `upstream-confirmed (apitypes.py key)`, or `device-tested (who/device/date)`.

## Produced by

Links to the `api/<service>/<endpoint>.md` pages that return (or accept) this model. Tag: `asm-traced`.

## Consumed by

UI page and Dart file that read it, with `file.dart @0xADDR`. Tag: `asm-traced`.

## Changed since 3.18.0

Added, removed, retyped keys between 3.18.0 and 3.24.3. Tag: `asm-traced` (3.24.3 side).

## Known unknowns

Bullet list of open questions. Tag: untagged by design (no API fact).

---

**Example skeleton — placeholders only, not a fact page**

> Verified against: App 3.24.3 · Date: YYYY-MM-DD · Confidence: <tag> · Owner page: <path or "this page">

# StationPowerLimitModel

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
