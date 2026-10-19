> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# Template: MQTT command page

`mqtt/<pn>.md` is ONE page per PN, the owner of MQTT field maps. The page has ONE status header (lowest tag across the page) and ONE H1; each command is an H3 section `### <command>`, and the sections below are its H4 subsections. A single-command page is allowed only when the PN has exactly one command. Length: under 600 lines; add a table of contents above 150 lines (see [../STRUCTURE.md](../STRUCTURE.md)). Section order is fixed.

Tags (see [../../METHODOLOGY.md](../../METHODOLOGY.md)): `asm-traced` · `string-only` · `upstream-confirmed` · `device-tested`. Integers from asm follow the Smi rule in the same file; cite `file.dart @0xADDR` next to every number. A fact lives on one owner page (see [../STRUCTURE.md](../STRUCTURE.md)); other pages link.

Link if the target file exists today, otherwise write a code span.

The status header is the first line of the page, before the H1; it is NOT a section heading. Its format: `> Verified against: App 3.24.3 · Date: YYYY-MM-DD · Confidence: <tag> · Owner page: <path or "this page">`. The status-header tag is the LOWEST tag among the facts on the page (METHODOLOGY.md).

Sections that carry no API fact (Known unknowns, link-only "Related ..." sections, "Device-tested by" lists) are untagged by design; their instruction says `Tag: untagged by design (no API fact)`. Every fact-bearing table or section carries a tag.

Section order (status header line first, then):

0. Status header line (first line, before H1)
1. Purpose
2. Upstream name
3. Command code
4. Direction
5. Topic pattern
6. Payload fields
7. Example
8. Related API endpoint
9. Since/changed
10. Known unknowns
11. Device-tested by

Per command, under `### <command>`:

#### Purpose

One sentence: what the command does. Tag: any.

#### Upstream name

`mqttmap.py` / `mqttcmdmap.py` name, or `none` (mark ours `(no upstream name)`). Tag: `upstream-confirmed` if matched.

#### Command code

Hex string exactly as in Dart, e.g. `"007c"`. Hex-string opcodes are string literals, not Smi: no halving. Tag: `asm-traced` / `string-only`.

#### Direction

`app→device`, `device→app` or `both`. Tag: `asm-traced`.

#### Topic pattern

Link to `mqtt/envelope.md`; never copy the topic or envelope here. Tag: per owner page.

#### Payload fields

Table `tag | name | type | unit/scale | required | source`. Scale factors link to `ble/protocol.md`. Row tag goes in the `source` column: an asm citation `file.dart @0xADDR` (= asm-traced), `string-only`, `upstream-confirmed (apitypes.py key)`, or `device-tested (who/device/date)`.

#### Example

Code block preceded by a label line `captured (client, version, date)` or `synthesized`. Tag: `device-tested` only if captured and accepted.

#### Related API endpoint

Link to the `api/<service>/<endpoint>.md` owner. Tag: untagged by design (no API fact).

#### Since/changed

3.18.0 to 3.24.3 change. Tag: `asm-traced` (3.24.3 side).

#### Known unknowns

Bullet list of open questions. Tag: untagged by design (no API fact).

#### Device-tested by

Who, device PN and firmware, client and version, date; `none` if untested. Tag: untagged by design (no API fact).

---

**Example skeleton — placeholders only, not a fact page**

> Verified against: App 3.24.3 · Date: YYYY-MM-DD · Confidence: <tag> · Owner page: <path or "this page">

# <PN> MQTT commands

<!-- brief example: A17X8 `"007c"` -->

### <command name>

#### Purpose

<one sentence>

#### Upstream name

`<mqttmap_name>` or `none`

#### Command code

`"<hex>"` — string literal, `<file.dart @0xADDR>`

#### Direction

<app→device / device→app / both>

#### Topic pattern

`mqtt/envelope.md`

#### Payload fields

| tag | name | type | unit/scale | required | source |
|---|---|---|---|---|---|
| `<tag>` | <name> | <type> | <unit/scale> | <yes/no> | `<file.dart @0xADDR>` |

#### Example

synthesized

```
<payload>
```

#### Related API endpoint

`api/<service>/<endpoint>.md`

#### Since/changed

3.18.0: <state>. 3.24.3: <state>.

#### Known unknowns

- <open question>

#### Device-tested by

<who>, <PN> fw <version>, <client version>, <YYYY-MM-DD>
