> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# Template: BLE command page

`ble/<pn>.md` is ONE page per PN, the owner of BLE opcodes and TLV. The page has ONE status header (lowest tag across the page) and ONE H1; each command is an H3 section `### <command>`, and the sections below are its H4 subsections. A single-command page is allowed only when the PN has exactly one command. Length: under 600 lines; add a table of contents above 150 lines (see [../STRUCTURE.md](../STRUCTURE.md)). Section order is fixed.

Tags (see [../../METHODOLOGY.md](../../METHODOLOGY.md)): `asm-traced` · `string-only` · `upstream-confirmed` · `device-tested`. Integers from asm follow the Smi rule in the same file; cite `file.dart @0xADDR` next to every number. A fact lives on one owner page (see [../STRUCTURE.md](../STRUCTURE.md)); other pages link.

Link if the target file exists today, otherwise write a code span.

The status header is the first line of the page, before the H1; it is NOT a section heading. Its format: `> Verified against: App 3.24.3 · Date: YYYY-MM-DD · Confidence: <tag> · Owner page: <path or "this page">`. The status-header tag is the LOWEST tag among the facts on the page (METHODOLOGY.md).

Sections that carry no API fact (Known unknowns, link-only "Related ..." sections, "Device-tested by" lists) are untagged by design; their instruction says `Tag: untagged by design (no API fact)`. Every fact-bearing table or section carries a tag.

Section order (status header line first, then):

0. Status header line (first line, before H1)
1. Purpose
2. Upstream name
3. Opcode
4. Direction
5. Packet framing
6. Handshake prerequisite
7. TLV tags
8. Example
9. Related API endpoint
10. Since/changed
11. Known unknowns
12. Device-tested by

Per command, under `### <command>`:

#### Purpose

One sentence: what the command does. Tag: any.

#### Upstream name

Upstream (AnkerSolixBLE / SolixBLE / mqttmap) name, or `none` (mark ours `(no upstream name)`). Tag: `upstream-confirmed` if matched.

#### Opcode

Opcode as in Dart. A hex string (`"005e"`) is a string literal, not Smi; an int literal follows the Smi rule. Tag: `asm-traced` / `string-only`.

#### Direction

`app→device`, `device→app` or `both`. Tag: `asm-traced`.

#### Packet framing

Link to `ble/protocol.md`; never restate frame layout. Tag: per owner page.

#### Handshake prerequisite

Link to `ble/handshake.md`; state only whether the command needs a completed handshake. Tag: per owner page.

#### TLV tags

Table `tag | name | type | length | source`. Row tag goes in the `source` column: an asm citation `file.dart @0xADDR` (= asm-traced), `string-only`, `upstream-confirmed (apitypes.py key)`, or `device-tested (who/device/date)`.

#### Example

Code block preceded by a label line `captured (client, version, date)` or `synthesized`. Tag: `device-tested` only if captured and accepted.

#### Related API endpoint

Link to the `api/<service>/<endpoint>.md` owner, or the MQTT twin in `mqtt/<pn>.md`. Tag: untagged by design (no API fact).

#### Since/changed

3.18.0 to 3.24.3 change. Tag: `asm-traced` (3.24.3 side).

#### Known unknowns

Bullet list of open questions. Tag: untagged by design (no API fact). The section ends with the fixed note line below.

BLE is unavailable while the device is on WiFi; see `ble/protocol.md`.

#### Device-tested by

Who, device PN and firmware, client and version, date; `none` if untested. Tag: untagged by design (no API fact).

---

**Example skeleton — placeholders only, not a fact page**

> Verified against: App 3.24.3 · Date: YYYY-MM-DD · Confidence: <tag> · Owner page: <path or "this page">

# <PN> BLE commands

<!-- brief example: A17C1 `005e` -->

### <command name>

#### Purpose

<one sentence>

#### Upstream name

`<upstream_name>` or `none`

#### Opcode

`<opcode>` — `<file.dart @0xADDR>`

#### Direction

<app→device / device→app / both>

#### Packet framing

`ble/protocol.md`

#### Handshake prerequisite

`ble/handshake.md` — <needed / not needed>

#### TLV tags

| tag | name | type | length | source |
|---|---|---|---|---|
| `<tag>` | <name> | <type> | <N> | `<file.dart @0xADDR>` |

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

BLE is unavailable while the device is on WiFi; see `ble/protocol.md`.

#### Device-tested by

<who>, <PN> fw <version>, <client version>, <YYYY-MM-DD>
