> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# Template: device page

Copy to `devices/<pn>.md` (lowercase PN). A device page holds links and device-tested status only: no payloads, no field lists, no numbers copied from owner pages. The page gives PN and marketing name only; product-code and enum facts are linked to `reference/enums.md`. A links-only page carries `asm-traced` at best in its status header, and `device-tested` only if every feature row is device-tested; the `device-tested?` column is not itself a tag. Section order is fixed.

Tags (see [../../METHODOLOGY.md](../../METHODOLOGY.md)): `asm-traced` · `string-only` · `upstream-confirmed` · `device-tested`. Integers from asm follow the Smi rule in the same file; cite `file.dart @0xADDR` next to every number. A fact lives on one owner page (see [../STRUCTURE.md](../STRUCTURE.md)); other pages link.

Link if the target file exists today, otherwise write a code span.

The status header is the first line of the page, before the H1; it is NOT a section heading. Its format: `> Verified against: App 3.24.3 · Date: YYYY-MM-DD · Confidence: <tag> · Owner page: <path or "this page">`. The status-header tag is the LOWEST tag among the facts on the page (METHODOLOGY.md).

Sections that carry no API fact (Known unknowns, link-only "Related ..." sections, "Device-tested by" lists) are untagged by design; their instruction says `Tag: untagged by design (no API fact)`. Every fact-bearing table or section carries a tag.

Section order (status header line first, then):

0. Status header line (first line, before H1)
1. PN, marketing name, generation/family
2. Features matrix
3. Known firmware notes
4. Known unknowns
5. Device-tested by

## PN, marketing name, generation/family

Product number, marketing name, generation and family; product codes link `reference/enums.md`. Tag: per source.

## Features matrix

Table `feature | API (link) | MQTT (link) | BLE (link) | device-tested?`. Each cell links to the owner page, or says `none` (device has no such channel) or `unknown` (not researched yet). `device-tested?` is yes/no plus a link to the record. Tag: per cell.

## Known firmware notes

Firmware-dependent behavior, each with a link to its owner page and tag. Tag: any.

## Known unknowns

Bullet list of open questions. Tag: untagged by design (no API fact).

## Device-tested by

Who, firmware, client and version, date; `none` if untested. Tag: untagged by design (no API fact).

---

**Example skeleton — placeholders only, not a fact page**

> Verified against: App 3.24.3 · Date: YYYY-MM-DD · Confidence: <tag> · Owner page: <path or "this page">

# A17C5 — <marketing name>

## PN, marketing name, generation/family

`<PN>`, <marketing name>, <generation>, <family>

## Features matrix

| feature | API (link) | MQTT (link) | BLE (link) | device-tested? |
|---|---|---|---|---|
| <feature> | `api/<service>/<endpoint>.md` | `mqtt/<pn>.md` | `ble/<pn>.md` | <yes/no> |

## Known firmware notes

- <note>, see `<owner page>`

## Known unknowns

- <open question>

## Device-tested by

<who>, fw <version>, <client version>, <YYYY-MM-DD>
