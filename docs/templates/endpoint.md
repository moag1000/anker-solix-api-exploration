> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# Template: endpoint page

Copy to `api/<service>/<last_url_segment>.md` (lowercase, underscores). Keep the page under 600 lines; add a table of contents above 150 lines (see [../STRUCTURE.md](../STRUCTURE.md)). Section order is fixed.

Tags (see [../../METHODOLOGY.md](../../METHODOLOGY.md)): `asm-traced` · `string-only` · `upstream-confirmed` · `device-tested`. Integers from asm follow the Smi rule in the same file; cite `file.dart @0xADDR` next to every number. A fact lives on one owner page (see [../STRUCTURE.md](../STRUCTURE.md)); other pages link.

Link if the target file exists today, otherwise write a code span.

The status header is the first line of the page, before the H1; it is NOT a section heading. Its format: `> Verified against: App 3.24.3 · Date: YYYY-MM-DD · Confidence: <tag> · Owner page: <path or "this page">`. The status-header tag is the LOWEST tag among the facts on the page (METHODOLOGY.md).

Sections that carry no API fact (Known unknowns, link-only "Related ..." sections, "Device-tested by" lists) are untagged by design; their instruction says `Tag: untagged by design (no API fact)`. Every fact-bearing table or section carries a tag.

Section order (status header line first, then):

0. Status header line (first line, before H1)
1. Purpose
2. Upstream name
3. Method+URL
4. Encrypted?
5. Request
6. `param_type`/`cmd`
7. Response model (link)
8. Response
9. Example request/response
10. Errors seen
11. Callers in app
12. Since/changed
13. Known unknowns
14. Device-tested by

## Purpose

One sentence: what the endpoint does for the caller. Tag: any.

## Upstream name

The `apitypes.py` key, or `none` (then mark our name `(no upstream name)`). Tag: `upstream-confirmed` if matched.

## Method+URL

HTTP method and path including the service prefix. Tag: `asm-traced` or `string-only` (cite the asm site or pp.txt entry).

## Encrypted?

Yes/no, with a link to `api/encryption.md`; do not restate the scheme. Tag: `asm-traced` / `string-only` / `device-tested`.

## Request

Table `field | type | required | example | source`. `source` is the asm citation or a tag. Row tag goes in the `source` column: an asm citation `file.dart @0xADDR` (= asm-traced), `string-only`, `upstream-confirmed (apitypes.py key)`, or `device-tested (who/device/date)`.

## `param_type`/`cmd`

Link-only: point to `api/param_types.md`, which owns the value; the value is never written here. Write `n/a` if the endpoint has none. Tag: untagged by design (no API fact).

## Response model (link)

Link to the `models/` owner page for the response class. Tag: `asm-traced`.

## Response

Table `field | type | required | example | source`, same columns as Request; list only endpoint-specific wrapper fields, model fields live on the model page. Row tag goes in the `source` column: an asm citation `file.dart @0xADDR` (= asm-traced), `string-only`, `upstream-confirmed (apitypes.py key)`, or `device-tested (who/device/date)`.

## Example request/response

One request block and one response block, each preceded by a label line `captured (client, version, date)` or `synthesized`. Never present a synthesized block as captured. Tag: `device-tested` only if captured and accepted by a device.

## Errors seen

Link to `api/errors.md`; list only the codes seen on this endpoint, by link. Tag: per code, as in the Request table rule.

## Callers in app

Dart file(s) and UI page(s) that call it, each with `file.dart @0xADDR`. Tag: `asm-traced`.

## Since/changed

Behavior change 3.18.0 to 3.24.3 (new, removed, field changes). Facts only in 3.18.0 appear only here. Tag: `asm-traced` (3.24.3 side).

## Known unknowns

Bullet list of open questions; an unknown is a result, not a gap to hide. Tag: untagged by design (no API fact).

## Device-tested by

Who, device PN and firmware, client and version, date; `none` if untested. Tag: untagged by design (no API fact).

---

**Example skeleton — placeholders only, not a fact page**

> Verified against: App 3.24.3 · Date: YYYY-MM-DD · Confidence: <tag> · Owner page: <path or "this page">

# set_site_device_param

## Purpose

<one sentence>

## Upstream name

`<apitypes_key>` or `none`

## Method+URL

`<METHOD> <service>/<path>` — <tag>, `<file.dart @0xADDR>`

## Encrypted?

<yes/no> — see `api/encryption.md`

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `<site_id>` | <type> | <yes/no> | `<example>` | `<file.dart @0xADDR>` |

## `param_type`/`cmd`

see `api/param_types.md`

## Response model (link)

`models/<class>.md`

## Response

| field | type | required | example | source |
|---|---|---|---|---|
| `<field>` | <type> | <yes/no> | `<example>` | `<file.dart @0xADDR>` |

## Example request/response

Request, synthesized

```json
{ "<field>": "<value>" }
```

Response, captured (<client>, <version>, <YYYY-MM-DD>)

```json
{ "<field>": "<value>" }
```

## Errors seen

`api/errors.md` — <code>

## Callers in app

`<file.dart @0xADDR>`, UI page <name>

## Since/changed

3.18.0: <state>. 3.24.3: <state>.

## Known unknowns

- <open question>

## Device-tested by

<who>, <PN> fw <version>, <client version>, <YYYY-MM-DD>
