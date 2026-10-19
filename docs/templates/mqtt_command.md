> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# Template: MQTT command page

Copy to a section (or page) of `mqtt/<pn>.md`, the owner of MQTT field maps. Tags (see `METHODOLOGY.md`): `asm-traced` · `string-only` · `upstream-confirmed` · `device-tested`. Integers from asm follow the Smi rule in [../../METHODOLOGY.md](../../METHODOLOGY.md); cite `file.dart @0xADDR` next to every number. A fact lives on one owner page (see [../STRUCTURE.md](../STRUCTURE.md)); other pages link. Section order is fixed.

## Status header

One line, first line of the page: `> Verified against: App 3.24.3 · Date: YYYY-MM-DD · Confidence: <tag> · Owner page: <path or "this page">`.

## Purpose

One sentence: what the command does. Tag: any.

## Upstream name

`mqttmap.py` / `mqttcmdmap.py` name, or `none` (mark ours `(no upstream name)`). Tag: `upstream-confirmed` if matched.

## Command code

Hex string exactly as in Dart, e.g. `"007c"`. Hex-string opcodes are string literals, not Smi: no halving. Tag: `asm-traced` / `string-only`.

## Direction

`app→device`, `device→app` or `both`. Tag: `asm-traced`.

## Topic pattern

Link to `mqtt/envelope.md`; never copy the topic or envelope here. Tag: per owner page.

## Payload fields

Table `tag | name | type | unit/scale | required | source`. Integers follow the Smi rule; scale factors link to `ble/protocol.md`. Tag: per row.

## Example

Code block preceded by a label line `captured (client, version, date)` or `synthesized`. Tag: `device-tested` only if captured and accepted.

## Related API endpoint

Link to the `api/<service>/<endpoint>.md` owner, if the same function exists over the cloud API. Tag: none.

## Since/changed

3.18.0 to 3.24.3 change. Tag: `asm-traced` (3.24.3 side).

## Known unknowns

Bullet list of open questions. Tag: none.

## Device-tested by

Who, device PN and firmware, client and version, date; `none` if untested. Tag: `device-tested`.

---

**Example skeleton — placeholders only, not a fact page**

> Verified against: App 3.24.3 · Date: YYYY-MM-DD · Confidence: <tag> · Owner page: <path or "this page">

# A17X8 command `"007c"`

## Status header

(see first line above)

## Purpose

<one sentence>

## Upstream name

`<mqttmap_name>` or `none`

## Command code

`"<hex>"` — string literal, `<file.dart @0xADDR>`

## Direction

<app→device / device→app / both>

## Topic pattern

`mqtt/envelope.md`

## Payload fields

| tag | name | type | unit/scale | required | source |
|---|---|---|---|---|---|
| `<tag>` | <name> | <type> | <unit/scale> | <yes/no> | `<file.dart @0xADDR>` |

## Example

synthesized

```json
{ "<field>": "<value>" }
```

## Related API endpoint

`api/<service>/<endpoint>.md`

## Since/changed

3.18.0: <state>. 3.24.3: <state>.

## Known unknowns

- <open question>

## Device-tested by

<who>, <PN> fw <version>, <client version>, <YYYY-MM-DD>
