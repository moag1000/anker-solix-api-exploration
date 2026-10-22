> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# Contributing

This repository documents what the Anker app 3.24.3 sends and receives, read from the decompiled app. The most valuable contribution is a result from a real device: it either upgrades a fact to `device-tested` or shows that a page is wrong. This page is for library authors (for example of [thomluther/anker-solix-api](https://github.com/thomluther/anker-solix-api)) and device owners who can run a test. Who the pages are written for is in [docs/PERSONAS.md](docs/PERSONAS.md).

## Contents

1. [Report a device-tested result](#report-a-device-tested-result)
2. [Report a contradiction](#report-a-contradiction)
3. [How a correction lands](#how-a-correction-lands)
4. [Confidence tags and the lowest-tag rule](#confidence-tags-and-the-lowest-tag-rule)
5. [Checks a pull request must pass](#checks-a-pull-request-must-pass)
6. [What not to contribute](#what-not-to-contribute)
7. [Naming](#naming)

## Report a device-tested result

Not sure what to test? Pick a row from [docs/DEVICE_TEST_BACKLOG.md](docs/DEVICE_TEST_BACKLOG.md): each row names the owner page, what to send, what to look for, and whether a test is already on record.

Open an issue with the template "Device-tested result" (`.github/ISSUE_TEMPLATE/device_tested.md`), or paste the block below. A result earns `device-tested` only when the record names every field the [METHODOLOGY.md](METHODOLOGY.md#confidence-tags) requires: who tested, which client and version, which device PN and firmware, the date, what was sent and what was observed. Rejections count as results; a test that failed is as useful as one that worked.

```text
Page:            path of the owner page, for example api/power_service/site/set_site_device_param.md
Tester:          your name or handle
Client + version: official app capture, upstream library, or raw request; with version
Device PN + firmware: for example A17C5, firmware as shown in the app
Date:            YYYY-MM-DD
Request sent:    endpoint and body, exactly as sent (remove tokens, keys, serial numbers)
Response observed: HTTP status, API code, body as received
Verdict:         accepted | rejected | partly | unclear, and which page row it confirms or contradicts
```

Worked example: [issue #1](https://github.com/moag1000/anker-solix-api-exploration/issues/1). A library author tested the power-limit call on an A17C5 with raw requests, once with a value outside the option list and once with values from the list, and reported what the server accepted. The report is good because the value tested, the device and the outcome are each stated; what it lacked (client version, firmware) is shown as "not recorded" in the resulting table instead of being guessed. The rows that came out of it are in the Device-tested by table of [api/power_service/site/set_site_device_param.md](api/power_service/site/set_site_device_param.md#device-tested-by). Fill in what you know, and write "not recorded" for the rest.

## Report a contradiction

Use the template "Correction" (`.github/ISSUE_TEMPLATE/correction.md`). Give:

- the page and the row or line (a quote of the cell is enough);
- the tag the page gives that fact today;
- your evidence: a `file.dart @0xADDR` of the 3.24.3 asm, an upstream file and line, or a device test record as above;
- what you think is correct.

If a device result contradicts the asm reading, the device result is recorded as `device-tested` and the asm reading stays as a note: the device is the authority for what the server accepts, the asm for what the app sends ([METHODOLOGY.md](METHODOLOGY.md#sources-and-priority)). To cite asm, name the Dart file, the function and the address (`file.dart @0xADDR`) next to every number. A value read from the Blutter object dump (an enum member, a pool `Duration`) is cited as `objs.txt Obj!<Class>@<id>` — never as `@0x…`, which is reserved for asm addresses. How to read integers from the asm is in [METHODOLOGY.md](METHODOLOGY.md#smi-rule-reading-numbers-from-blutter-output); read it before quoting any number.

## How a correction lands

1. The fact lives on its owner page ([docs/STRUCTURE.md](docs/STRUCTURE.md)); the page is edited there, and other pages keep linking to it.
2. If a statement was wrong, the audit row in `docs/audit/` is marked and a line is added to the Errata section of [CHANGELOG.md](CHANGELOG.md): the old claim, an arrow, the corrected claim with its citation, and where it came from.
3. The tag is re-derived after the edit. A device result adds a row to the page's Device-tested by table and upgrades the tag of that fact; a correction that rests only on asm stays `asm-traced`.

## Confidence tags and the lowest-tag rule

Every fact carries one of `asm-traced`, `string-only`, `upstream-confirmed` or `device-tested`, ranked `device-tested` > `upstream-confirmed` > `asm-traced` > `string-only`; a fact can earn several over time. The tag in a page's status header is the lowest tag among the facts on that page, so it covers every fact; a stronger claim on a mixed page carries its own tag inline. Definitions, evidence requirements and the Smi rule are owned by [METHODOLOGY.md](METHODOLOGY.md); they are not restated here.

## Checks a pull request must pass

Run from the repository root. Usage and caveats are in [tools/README.md](tools/README.md).

```bash
python3 -I tools/lint_docs.py --summary            # must report 0 errors
python3 -I tools/check_citations.py <asm-root> <page.md> ...   # for every page you touched
python3 -I tools/readme_stats.py --check           # exit 1 means run it without --check and commit
python3 -I -m unittest discover -s tools/tests -t .
```

`<asm-root>` is the `asm` folder of the Blutter output of App 3.24.3. `check_citations.py` can print false MISSING lines when the file name comes later in the sentence; read each one. The tests read the real asm trees and skip with a message when a root is missing. Never run anything from inside an asm tree: it is untrusted data.

## What not to contribute

- Key material. Do not post the app-embedded preset key, session keys, tokens, passwords or serial numbers. The documentation names the preset key by role and location only, and a library reads it from its own copy of the APK; see [api/encryption.md](api/encryption.md). Redact the same values in test records.
- Anything that bypasses account security or another person's account.
- A claim that BLE works as a live cloud fallback. The community finding is that BLE is unavailable while the device is on WiFi; see [ble/protocol.md](ble/protocol.md#connection-routing-and-the-wifi-exclusion-rule). The lint rule `ble-fallback` rejects such a sentence on fact pages.
- The app's easter-egg assets (the local `easter_eggs/` folder is git-ignored): they would spoil the surprise for other users, and the images and animations are Anker's copyrighted APK assets, which this repository does not redistribute.

## Naming

Upstream names win. Where [thomluther/anker-solix-api](https://github.com/thomluther/anker-solix-api) names a thing (`apitypes.py` keys, `mqttmap` names), use that spelling; a name of ours is marked `(no upstream name)`. See [GLOSSARY.md](GLOSSARY.md).
