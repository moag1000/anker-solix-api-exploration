> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# Template: flow page

Copy to `flows/<name>.md`. Tags (see `METHODOLOGY.md`): `asm-traced` · `string-only` · `upstream-confirmed` · `device-tested`. Integers from asm follow the Smi rule in [../../METHODOLOGY.md](../../METHODOLOGY.md); cite `file.dart @0xADDR` next to every number. A fact lives on one owner page (see [../STRUCTURE.md](../STRUCTURE.md)); other pages link. A flow page links to owners and never copies payloads. Section order is fixed.

## Status header

One line, first line of the page: `> Verified against: App 3.24.3 · Date: YYYY-MM-DD · Confidence: <tag> · Owner page: <path or "this page">`.

## Trigger (UI action)

The user action that starts the flow, with UI page and `file.dart @0xADDR`. Tag: `asm-traced`.

## Preconditions

State required before the trigger (login, site, device state, BLE vs cloud). Link owners. Tag: any.

## Steps

Table `# | actor | action | owner page link | asm citation`. Actor is app, cloud, device or user. Link to the owner for every payload. Tag: per row.

## Side effects

State changed elsewhere (cached values, other devices, notifications). Tag: any.

## Timing (delays/polling)

Delays, debounce, polling intervals; integers follow the Smi rule with citation. Tag: `asm-traced` / `string-only`.

## Failure paths

What happens on error or timeout, linking `api/errors.md`. Tag: any.

## Known unknowns

Bullet list of open questions. Tag: none.

---

**Example skeleton — placeholders only, not a fact page**

> Verified against: App 3.24.3 · Date: YYYY-MM-DD · Confidence: <tag> · Owner page: <path or "this page">

# system output limit

## Status header

(see first line above)

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
