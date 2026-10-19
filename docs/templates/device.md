> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# Template: device page

Copy to `devices/<pn>.md` (lowercase PN). Tags (see `METHODOLOGY.md`): `asm-traced` · `string-only` · `upstream-confirmed` · `device-tested`. Integers from asm follow the Smi rule in [../../METHODOLOGY.md](../../METHODOLOGY.md); cite `file.dart @0xADDR` next to every number. A fact lives on one owner page (see [../STRUCTURE.md](../STRUCTURE.md)); other pages link. A device page holds links and device-tested status only: no payloads, no field lists, no numbers copied from owner pages. Section order is fixed.

## Status header

One line, first line of the page: `> Verified against: App 3.24.3 · Date: YYYY-MM-DD · Confidence: <tag> · Owner page: <path or "this page">`.

## PN, marketing name, generation/family

Product number, marketing name, generation and family, linking `reference/enums.md` for product codes. Tag: per source.

## Features matrix

Table `feature | API (link) | MQTT (link) | BLE (link) | device-tested?`. Each cell links to the owner page or says `none`; `device-tested?` is yes/no plus a link to the record. Tag: per cell.

## Known firmware notes

Firmware-dependent behavior, each with a link to its owner page and tag. Tag: any.

## Known unknowns

Bullet list of open questions. Tag: none.

## Device-tested by

Who, firmware, client and version, date; `none` if untested. Tag: `device-tested`.

---

**Example skeleton — placeholders only, not a fact page**

> Verified against: App 3.24.3 · Date: YYYY-MM-DD · Confidence: <tag> · Owner page: <path or "this page">

# A17C5 — <marketing name>

## Status header

(see first line above)

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
