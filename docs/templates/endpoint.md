> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# Template: endpoint page

Copy to `api/<service>/<last_url_segment>.md` (lowercase, underscores). Tags (see `METHODOLOGY.md`): `asm-traced` · `string-only` · `upstream-confirmed` · `device-tested`. Integers from asm follow the Smi rule in [../../METHODOLOGY.md](../../METHODOLOGY.md); cite `file.dart @0xADDR` next to every number. A fact lives on one owner page (see [../STRUCTURE.md](../STRUCTURE.md)); other pages link. Keep the page under 600 lines; add a table of contents above 150 lines. Section order is fixed.

## Status header

One line, first line of the page: `> Verified against: App 3.24.3 · Date: YYYY-MM-DD · Confidence: <tag> · Owner page: <path or "this page">`. The tag is the LOWEST tag among the facts on the page.

## Purpose

One sentence: what the endpoint does for the caller. Tag: any.

## Upstream name

The `apitypes.py` key, or `none` (then mark our name `(no upstream name)`). Tag: `upstream-confirmed` if matched, else none.

## Method+URL

HTTP method and path including the service prefix (`<service>/<path>`). Tag: `asm-traced` or `string-only` (cite the asm site or pp.txt entry).

## Encrypted?

Yes/no, with a link to `api/encryption.md`; do not restate the scheme. Tag: `asm-traced` / `string-only` / `device-tested`.

## Request

Table `field | type | required | example | source`. `source` is the asm citation (`file.dart @0xADDR`) or a tag. Tag: per row.

## `param_type`/`cmd`

Link to `api/param_types.md`; the value itself lives there, not here. Write `n/a` if the endpoint has none. Tag: per owner page.

## Response model (link)

Link to the `models/` owner page for the response class. Tag: `asm-traced`.

## Response

Table `field | type | required | example | source`, same columns as Request. Fields of the linked model are not copied if the model page owns them; list only endpoint-specific wrapper fields. Tag: per row.

## Example request/response

Code blocks, each preceded by a label line `captured (client, version, date)` or `synthesized`. Never present a synthesized block as captured. Tag: `device-tested` only if captured and accepted by a device.

## Errors seen

Link to `api/errors.md`; list only the codes seen on this endpoint, by link. Tag: per code.

## Callers in app

Dart file(s) and UI page(s) that call it, each with `file.dart @0xADDR`. Tag: `asm-traced`.

## Since/changed

Behavior change 3.18.0 to 3.24.3 (new, removed, field changes). Facts only in 3.18.0 appear only here. Tag: `asm-traced` (3.24.3 side).

## Known unknowns

Bullet list of open questions; an unknown is a result, not a gap to hide. Tag: none.

## Device-tested by

Who, device PN and firmware, client and version, date. `none` if untested. Tag: `device-tested`.

---

**Example skeleton — placeholders only, not a fact page**

> Verified against: App 3.24.3 · Date: YYYY-MM-DD · Confidence: <tag> · Owner page: <path or "this page">

# set_site_device_param

## Status header

(see first line above)

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
| `<field>` | <type> | <yes/no> | `<example>` | <tag> |

## `param_type`/`cmd`

`<N>` — see `api/param_types.md`

## Response model (link)

`models/<class>.md`

## Response

| field | type | required | example | source |
|---|---|---|---|---|
| `<field>` | <type> | <yes/no> | `<example>` | `<file.dart @0xADDR>` |

## Example request/response

synthesized

```json
{ "<field>": "<value>" }
```

captured (<client>, <version>, <YYYY-MM-DD>)

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
