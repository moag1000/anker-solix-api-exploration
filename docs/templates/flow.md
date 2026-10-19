> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# Template: flow page

Copy to `flows/<name>.md`. A flow page links to owners and never copies payloads. Section order is fixed.

Tags (see [../../METHODOLOGY.md](../../METHODOLOGY.md)): `asm-traced` · `string-only` · `upstream-confirmed` · `device-tested`. Integers from asm follow the Smi rule in the same file; cite `file.dart @0xADDR` next to every number. A fact lives on one owner page (see [../STRUCTURE.md](../STRUCTURE.md)); other pages link.

Link if the target file exists today, otherwise write a code span.

The status header is the first line of the page, before the H1; it is NOT a section heading. Its format: `> Verified against: App 3.24.3 · Date: YYYY-MM-DD · Confidence: <tag> · Owner page: <path or "this page">`. The status-header tag is the LOWEST tag among the facts on the page (METHODOLOGY.md).

Sections that carry no API fact (Known unknowns, link-only "Related ..." sections, "Device-tested by" lists) are untagged by design; their instruction says `Tag: untagged by design (no API fact)`. Every fact-bearing table or section carries a tag.

Section order (status header line first, then):

0. Status header line (first line, before H1)
1. Trigger (UI action)
2. Preconditions
3. Steps
4. Side effects
5. Timing (delays/polling)
6. Failure paths
7. Known unknowns

## Trigger (UI action)

The user action that starts the flow, with UI page and `file.dart @0xADDR`. Tag: `asm-traced`.

## Preconditions

State required before the trigger (login, site, device state, BLE vs cloud). Link owners. Tag: any.

## Steps

Table `# | actor | action | owner page link | asm citation`. Actor is app, cloud, device or user. Row tag goes in the `asm citation` column: an asm citation `file.dart @0xADDR` (= asm-traced), `string-only`, `upstream-confirmed (apitypes.py key)`, or `device-tested (who/device/date)`. For rows whose actor is cloud or device (no asm site): cite the owner page link and tag `string-only` or `device-tested (who/device/date)` in that column.

## Side effects

State changed elsewhere (cached values, other devices, notifications). Tag: any.

## Timing (delays/polling)

Delays, debounce, polling intervals; integers follow the Smi rule with citation. Tag: `asm-traced` / `string-only`.

## Failure paths

What happens on error or timeout, linking `api/errors.md`. Tag: any.

## Known unknowns

Bullet list of open questions. Tag: untagged by design (no API fact).

---

**Example skeleton — placeholders only, not a fact page**

> Verified against: App 3.24.3 · Date: YYYY-MM-DD · Confidence: <tag> · Owner page: <path or "this page">

# system output limit

## Trigger (UI action)

<action> on <UI page>, `<file.dart @0xADDR>`

## Preconditions

- <precondition>, see `<owner page>`

## Steps

| # | actor | action | owner page link | asm citation |
|---|---|---|---|---|
| 1 | <app/cloud/device/user> | <action> | `api/<service>/<endpoint>.md` | `<file.dart @0xADDR>` |

## Side effects

- <effect>

## Timing (delays/polling)

<delay or interval>, `<file.dart @0xADDR>`

## Failure paths

- <failure>, see `api/errors.md`

## Known unknowns

- <open question>
