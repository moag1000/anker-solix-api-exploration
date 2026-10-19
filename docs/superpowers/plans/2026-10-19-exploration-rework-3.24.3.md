# Exploration Rework 3.24.3 — Implementation Plan (TODO) — v2

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild `anker-solix-api-exploration` on App 3.24.3 so it is correct (Smi bug fixed), complete (every endpoint, param_type, model, flow of 3.24.3), and usable (personas, one page template, single source per fact, error catalog, machine-readable export) — starting with the concrete request in issue #1 (10 W output limit).

**Architecture:** Three sources of truth, in priority: (1) Blutter asm of 3.24.3 (`ankerAPK/v3.24.3/blutter_output/asm`), (2) Blutter asm of 3.18.0 (`ankerAPK/blutter_output/asm`) for diffing, (3) upstream `thomluther/anker-solix-api` + live device tests for confirmation. Every number from asm goes through the Smi rule. Facts are generated into JSON by scripts in `tools/`; Markdown pages are rendered/derived from that JSON where possible, so the next APK is a re-run, not a rewrite. Each fact lives in exactly one page; every other page links to it.

**Tech Stack:** Blutter (Dart 3.11.0 VM built at `ankerAPK/blutter/bin/blutter_dartvm3.11.0_android_arm64`), python3 (`-I`, scripts outside the data dirs), ugrep (`grep` on this Mac is ugrep — quote globs), GitHub CLI, GitHub-rendered Markdown (no build step required; mkdocs optional later).

**Spec:** `ankerAPK/v3.24.3/audit/SMI_RULE.md`, `ankerAPK/v3.24.3/audit/00_power_limit_type19_finding.md`, `ankerAPK/v3.24.3/audit/01_endpoint_diff_raw.md`, issue moag1000/anker-solix-api-exploration#1, thomluther/anker-solix-api#339, this plan's review notes (usability gaps 1–17, 2026-10-19).

## Global Constraints

- App version for all new claims: **3.24.3 (versionCode 237), Dart 3.11.0, snapshot `78da37fed6bf1489361a312568249f3f`**, XAPK sha256 `7d6d0deab4834515c41aa5e8bafff03f9735e883f15c4f8d5b7194e871ff6ba5`. 3.18.0 facts stay only as "changed since" notes.
- **Smi rule for every integer taken from asm**: 32-bit store (`stur w`) into field/array/map → value = raw/2; 64-bit store (`stur x`) or arithmetic → raw. Cite `file.dart @0xADDR` for every number.
- **Confidence tags, exactly four**: `asm-traced` · `string-only` · `upstream-confirmed` · `device-tested`. Every table/section carries one.
- **Single source**: a fact (payload, cmd, field list, enum) lives on exactly one page (the owner page named in Task 0.3's ownership map); all other mentions are links. No copy-paste of payloads between pages.
- **Page template** (Task 0.4) is mandatory for every endpoint/command/model page; `tools/lint_docs.py` enforces it.
- **Status header** on every page: `Verified against: App 3.24.3 · Date: YYYY-MM-DD · Confidence: <tag> · Owner page: <path>`.
- Naming follows upstream (`thomluther/anker-solix-api` `apitypes.py`) where an upstream name exists; our name only where upstream has none, marked `(no upstream name)`.
- Disclaimer block in README stays; "No server-side impact analysis" paragraph stays verbatim.
- Do not claim BLE works as live cloud fallback (BLE is disabled while WiFi is active).
- Phase 3 work order = user value: Modbus → Encryption → param_type table → models → new services by relevance → cosmetic services (pet screensaver, Anka) last.

## Review Focus

1. **Odd raw immediate treated as Smi** — a raw odd value in a tagged slot is not an int. Phase 2 audit tables must show no "raw odd → Smi" rows.
2. **Number from a string literal wrongly halved** (`"19"`, `"6"`, hex-string opcodes `"005e"`). Every corrected number must cite a `mov` instruction, not a `= "..."` line.
3. **Endpoint string present but unreachable** (dead code, installer-only, region-locked). Task 3.1 records the calling Dart file; no caller → `string-only` + "no known caller".
4. **Model field attributed to the wrong endpoint** (the old docs' known weakness). Task 3.4 maps model ← function ← URL literal inside the same asm function only.
5. **cmd=123 vs cmd=17 behavioral difference unknown** — Task 1.2 test matrix covers both; the doc states the tested outcome, not an assumption.
6. **Reader lands on a stale copy** — single-source rule + lint (Task 4.6) catches duplicated payload blocks; status header shows verification date.

---

## Phase 0 — Foundations (everything else depends on it)

### Task 0.1: METHODOLOGY.md — Smi rule, sources, confidence tags, known server tolerances
**Files:** Create `METHODOLOGY.md` (from `ankerAPK/v3.24.3/audit/SMI_RULE.md` + three-source priority + tag definitions + "Known server tolerances" placeholder); Modify `README.md` "How this was built" (version/Dart/snapshot/sha256, link METHODOLOGY).
- [ ] Step 1: Write METHODOLOGY.md with the four tag definitions (one sentence each, incl. what evidence earns the tag).
- [ ] Step 2: Update README build table to 3.24.3 values; keep a "History" line for 3.18.0.
- [ ] Step 3: Verify `grep -n "3.4.4\|3.18.0" README.md` hits only History/changed-since lines.
- [ ] Step 4: Commit `docs: METHODOLOGY (Smi rule, sources, tags); bump to 3.24.3`.

### Task 0.2: Personas and reading paths (defines "usable")
**Files:** Create `docs/PERSONAS.md`; Modify `README.md` (top section "Start here by role").
- [ ] Step 1: Define 5 personas with their first question and the page they need first:
  - **Library maintainer** (thomluther): "what exactly does the app send?" → `api/` endpoint page + `data/endpoints.json`.
  - **HA integration dev**: "which setting controls X, GET→SET flow, validation ranges?" → `flows/` + param_type table.
  - **mqtt_monitor user**: "what is field a8 / cmd 0x7c?" → `mqtt/` decoder pages per PN.
  - **BLE project dev**: "opcode, TLV, handshake?" → `ble/` pages.
  - **Curious user / newcomer**: "what can be controlled at all, what is a site/station?" → `GLOSSARY.md` + README use-case index.
- [ ] Step 2: For each persona one reading path (3–5 links in order). Put in README "Start here by role".
- [ ] Step 3: Verify every link resolves (`tools/lint_docs.py --links`, from Task 4.6; until then manual).
- [ ] Step 4: Commit `docs: personas and reading paths`.

### Task 0.3: Information architecture + fact ownership map (single source)
**Files:** Create `docs/STRUCTURE.md`; create directories `api/`, `mqtt/`, `ble/`, `flows/`, `devices/`, `models/`, `reference/`, `data/`, `tools/`.
Target layout:
```
README.md                 entry: role paths, use-case index, version matrix, what changed in 3.24.3
GLOSSARY.md               terms (Task 4.1)
METHODOLOGY.md            how facts are produced, Smi rule, tags
CHANGELOG.md              per-rework entries + Errata
api/<service>/<endpoint>.md   ONE page per endpoint (owner of payload facts)
api/param_types.md        master table (owner of param_type/cmd facts)
api/errors.md             error code catalog (Task 4.2)
api/auth.md               login, headers, token, encryption pointer
api/encryption.md         ECDH payload encryption
mqtt/<pn>.md              decoder per product (owner of MQTT field facts), mqtt/envelope.md
ble/<pn>.md, ble/protocol.md, ble/handshake.md
flows/<name>.md           step traces, link to owners
devices/<pn>.md           product page: links to api/mqtt/ble owners + device-tested status
models/<class>.md or models/<group>.md   response/request models (owner of field lists)
reference/enums.md, reference/business_rules.md, reference/validation_model.md
data/endpoints.json, data/models.json, data/param_types.json, data/errors.json   machine-readable, generated
tools/                    scripts
docs/                     personas, structure, issues, audit tables, plans
```
- [ ] Step 1: Write STRUCTURE.md with the layout above + ownership rule ("payload facts live in api/<endpoint>.md; devices/ and flows/ link").
- [ ] Step 2: Write migration map old file → new location(s) for all 14 root docs + 5 devices + 18 endpoints + 13 models (table in STRUCTURE.md). Old files are not deleted until Phase 4 (Task 4.7) — they get a top banner "superseded by …".
- [ ] Step 3: Split rule for big files: `BLE_COMMAND_MAP.md` → `ble/protocol.md`, `ble/<pn>.md` (one per PN), `mqtt/envelope.md`; no page > 600 lines; each page gets a TOC if > 150 lines.
- [ ] Step 4: Commit `docs: information architecture and ownership map`.

### Task 0.4: Page templates
**Files:** Create `docs/templates/endpoint.md`, `docs/templates/mqtt_command.md`, `docs/templates/ble_command.md`, `docs/templates/model.md`, `docs/templates/device.md`, `docs/templates/flow.md`.
Endpoint template sections (fixed order): Status header · Purpose (1 sentence) · Upstream name (`apitypes.py` key or "none") · Method+URL · Encrypted? · Request (table: field, type, required, example, source) · `param_type`/`cmd` (link to `api/param_types.md`) · Response model (link) · Example request/response (marked `captured` or `synthesized`) · Errors seen (link to `api/errors.md`) · Callers in app (Dart file, UI page) · Since/changed (3.18.0→3.24.3) · Known unknowns · Device-tested by (who, device, date).
- [ ] Step 1: Write the six templates with the section lists (model: field, JSON key, Dart type, nullable, since; device: PN, generation, supported features matrix with links; flow: trigger, steps with owner links, side effects, timing).
- [ ] Step 2: Render one real page from each template by hand (endpoint: `set_site_device_param`; mqtt: A17X8 `007c`; ble: A17C1 `005e`; model: `StationPowerLimitModel`; device: A17C5; flow: output limit) — these are the Phase 1 deliverables, so templates are proven on the concrete request.
- [ ] Step 3: Commit `docs: page templates`.

### Task 0.5: Extraction tooling (reproducible)
**Files:** Create `tools/smi.py`, `tools/endpoint_inventory.py`, `tools/model_fields.py`, `tools/param_types.py`, `tools/diff_versions.py`, `tools/render_pages.py`, `tools/README.md`.
**Interfaces (produces):** `data/endpoints.json` rows `{url, service, function, dart_file, params[], param_type?, cmd?, encrypted, callers[], since, removed_in?}`; `data/models.json` `{class, dart_file, fields[{json_key, dart_type, nullable}], since}`; `data/param_types.json` `{param_type, set_function, get_function, cmd, keys[], get_model}`; `tools/out/diff_3.18.0_3.24.3.md`.
- [ ] Step 1: `smi.py <asm_file> <addr>` → prints raw, next store width, decoded value. Test: `http_request_repository_impl.dart @0x43558c4` → `246 → stur w → 123`; `station_power_limit_logic.dart @0x43550b8` → `100 → stur x → 100`.
- [ ] Step 2: `endpoint_inventory.py <asm_root> --version 3.24.3` → `data/endpoints.json`. Test: row for `setSiteDevicePowerLimit` has param_type `19`, cmd `123`, params `display_type, power_limit.limit, power_limit.limit_real`, encrypted `true`.
- [ ] Step 3: `model_fields.py` → `data/models.json`. Test: `StationPowerLimitModel` has 21 keys incl. `unlock_default_power_type`.
- [ ] Step 4: `param_types.py` → `data/param_types.json` from all `set_/get_site_device_param` callers (trace variable param_types to caller). Test: contains 6, 18, 19, 20, 26 and the dynamic-price/EMS callers.
- [ ] Step 5: `diff_versions.py` → added/removed/changed endpoints+fields. Test: `charging_hes_installer_svc/*` (19) added; `power_service/v1/app/get_device_last_exercise_log` removed.
- [ ] Step 6: `render_pages.py` → fills endpoint/model template skeletons from JSON (status header, URL, params, callers, since) leaving prose sections for humans. Test: renders `api/power_service/site/set_site_device_param.md` skeleton.
- [ ] Step 7: `tools/README.md` (blutter run, venv, order of scripts) → Commit `tools: reproducible extraction + page rendering`.

---

## Phase 1 — Concrete request first: 10 W output limit (issue #1 / upstream #339)

### Task 1.1: Owner pages for param_type 19 (per template, 3.24.3)
**Files:** Create `api/power_service/site/set_site_device_param.md` (owner), `api/param_types.md` (row 19 + all known rows as placeholders), `api/devicecontrol/device/verify_unlock_default_power_code.md`, `api/devicecontrol/README.md` (service: 5 endpoints), `models/station_power_limit.md`, `flows/system_output_limit.md`, `devices/a17c5.md` (links only); Modify `devices/solarbank.md`, `PARAM_DATA_STRUCTURES.md`, `VALIDATION_MODEL.md`, `FLOWS.md` → replace type-19 content with a link to the owner page + "corrected 2026-10: cmd 123, display_type".
Source: `ankerAPK/v3.24.3/audit/00_power_limit_type19_finding.md`.
- [ ] Step 1: Endpoint page: payload `cmd:123`, `param_data={"display_type":1,"power_limit":{"limit":N,"limit_real":N}}` (`@0x435575c`), encrypted `true`, callers `station_power_limit_logic.dart::_setOutputPowerLimit`, since: `display_type` new in 3.24.3, Known unknowns: server meaning of display_type, cmd 17 vs 123.
- [ ] Step 2: Flow page: slider 100 W…`legal_power_limit`, step 10 (`@0x43550b8/@0x43550c8`), ≤ legal → set; > legal → DIY sheet (`unlock_default_power_type` 1=H5, 2=image, else image+password) → `verify_unlock_default_power_code` `{unlock_code, device_sn, site_id}` → `verify_result` → set.
- [ ] Step 3: Model page `StationPowerLimitModel` 21 keys (+4 since 3.18.0), `PowerLimitOption`.
- [ ] Step 4: Verify: `grep -rn "246"` in power-limit context = 0; `grep -rln display_type` = owner + flow + param_types only (others link).
- [ ] Step 5: Commit `docs(power-limit): param_type 19 per 3.24.3 — owner pages, flow, devicecontrol`.

### Task 1.2: Issue #1 answer + test matrix for thomluther
**Files:** Create `docs/issues/2026-10-19-issue1-power-limit-test-matrix.md`.
- [ ] Step 1: Draft comment: 3-bullet finding, exact payload, 3-row matrix (cmd 17 + display_type / cmd 123 + display_type / cmd 123 without), ask for raw 790 W responses and error codes.
- [ ] Step 2: Michael reviews + posts on moag1000/anker-solix-api-exploration#1, links from thomluther/anker-solix-api#339.
- [ ] Step 3: On result: owner page → `device-tested`, winning variant stated; `METHODOLOGY.md` "Known server tolerances" gets the cmd 17/123 outcome; `api/errors.md` gets 10004 with this context.

---

## Phase 2 — Smi correction sweep (every integer from asm in old docs)

Method per task: list integers (not string literals, not upstream, not mqtt_monitor) → asm site in 3.24.3 (fallback 3.18.0) → `tools/smi.py` → fix + citation → audit table `docs/audit/<doc>.md` (`claim | doc line | asm site | raw | store | verdict | new value`) → CHANGELOG "Errata 2026-10 (Smi)" line. Corrections go to the **owner page** of the fact (Task 0.3 map); the old file gets the banner + link.

- [ ] **2.1 FLOWS.md** (21 claims; known: cmd 246 → 17 `setSiteDeviceParam`, 123 power limit).
- [ ] **2.2 BLE_COMMAND_MAP.md** (61 claims) split: 2.2a MQTT envelope (`cmd 34→17, cmd_status 4→2, sign_code 2→1, msg_seq 2→1`, check vs upstream `api/mqtt.py`); 2.2b per-PN opcodes (hex string literals are NOT Smi); 2.2c TLV tag tables + lengths.
- [ ] **2.3 BUSINESS_RULES.md** (24; e.g. `timing_limit` default `#0x18` → store width).
- [ ] **2.4 ENUMS.md** (9; `fromInt` switches `cmp w,#N` → N/2; bit-flag table lines 237–252: unboxed or tagged?).
- [ ] **2.5 VALIDATION_MODEL, PARAM_DATA_STRUCTURES, JSON_EXAMPLES, RESPONSE_EXAMPLES** (ids, `mode_type`, `soc`, `is_ble`, `disaster_type` in examples).
- [ ] **2.6 endpoints/charging_disaster_prepared.md + devices/home_power_panel.md** (`disaster_type 4→2`, `is_ble 4→2`, `backupMode 4→?`); ask ha-anker-solix#480 reporter to confirm live.
- [ ] **2.7 devices/*, models/*, CHANGELOG** (e.g. "0x22=normal, 0x0C=OTA, 0x18=unbind" → 17/6/12); write the Errata section (old → new, citation, date).
- [ ] **2.8 patches/README.md + patches/*.patch** — "Value 2 = enabled (NOT 1)", `fc[14]==2`, `ui_flag==2`, `a4 status_code value=2` are `cmp w,#2` reads → real 1. Re-derive the A17C1 0405 tag list in Task 3.6 from 3.24.3; patches are then archived (Task 4.9), not fixed in place.
- [ ] **Phase gate:** `grep -rnE "\b(246|34)\b" --include='*.md' .` has no cmd-context hit; every corrected integer has `@0x` citation; audit tables complete for 2.1–2.7.

---

## Phase 3 — Completeness vs 3.24.3 (ordered by user value)

### Task 3.1: Definitive endpoint inventory → `data/endpoints.json` + skeleton pages
- [ ] Run Task 0.5 scripts; resolve the ambiguous prefixes seen in strings (`smart_service`, `device_svc`, `privacy_service`, `energy/`, `site/`) → URL or Dart package path, documented either way.
- [ ] Render skeleton pages for all endpoints (`render_pages.py`); 11 removed endpoints keep a page with `removed_in: 3.24.3`.
- [ ] Coverage metric in README: `documented pages / endpoints.json rows` (target 100 % skeletons, prose per priority below).
- [ ] Commit `docs(api): full 3.24.3 endpoint inventory (skeletons)`.

### Task 3.2: Modbus TCP (new, highest HA/Homey value)
- [ ] `devices/modbus.md` + `api/charging_hes_third_party_service_svc/{query,set}_modbus_setting.md` from asm (`tcpModbusIp/Port/MaxCurrent/PhaseLimit/Timeout`, `supportModbusTcp`, `isSupportModbus`, `modbustoha`, `modbustohomey`, `evModbusTips`) + the Dart page trace + which PNs; flow `flows/modbus_setup.md` → commit.

### Task 3.3: Encryption + auth (upstream #70)
- [ ] `api/encryption.md`: endpoints with `encryptionRequestHttp` (from `encrypted=true`), headers `x-encryption-info: algo_ecdh`, `x-replay-info`, key exchange trace; `api/auth.md`: login endpoints, headers (`app_version` 3.24.3, `gtoken`, `country_code`, `timezone`, `model_type`, `appName`), token lifecycle → commit.

### Task 3.4: param_type master table + models
- [ ] `api/param_types.md` from `data/param_types.json` (type, set/get function, cmd decoded, keys, GET model, tag); models regenerated into `models/` from `data/models.json`, "changed since 3.18.0" per class; model ↔ endpoint only via same-function URL literal → commit.

### Task 3.5: New services by relevance
- [ ] `charging_hes_installer_svc` (19 — installer commissioning, AI-EMS authorize, TOU/dynamic price save), `power_service/v2` (9 — energy_options, report_data, timeline events, site savings/scene, region param), `devicecontrol/v1` (5), `charging_common_svc/location`, `app/get_weather`, `everhome/bind`, `set_user_site_param`, standby-exercise + self-check endpoints; then `charging_imsg_svc` (referral), `mini_power` additions (pet screensaver, reminders, greeting, last location), `app/anka` (11, AI assistant) last → commit per service.

### Task 3.6: MQTT decoders per PN (3.24.3)
- [ ] For each decoder in 3.18.0 (a172x, a1771, a1781, a17a3, a17b1, a17c0, a17c1, a17x7, a17x8, a91b2, shelly, iot) plus any new (`i_mqtt_serve.dart`, `mqtt_types.dart`): page `mqtt/<pn>.md` from template, field tables diffed vs 3.18.0, envelope constants decoded (2.2a) → commit per PN.

### Task 3.7: BLE per PN + new PNs
- [ ] `ble/protocol.md`, `ble/handshake.md`, `ble/<pn>.md` from `*_device_commands.dart` (3.24.3); new model tokens (`a17c8, a17cx, a17e2, a17b6, a17a2, a1754, a110b/y, a1115, a1201, a120d, a1289, a146*, a1504/5, a156*, a166*, a546*, a556*, a5560, a566b`): classify, `reference/enums.md` product table, `devices/<pn>.md` where a UI page exists → commit.

### Task 3.8: IoT-Kit channels (+22; plan said +24 — corrected 2026-10-19 from the pools: 68 → 90) 
- [ ] `reference/iot_kit_channels.md`: all `akiot.*` channels, new ones marked (`monitor_ota*`, `is_ota_in_progress`, `get_sub_version_list`, `opening.installer_*`, `pairing.pro_*`, `activate_device_ethernet`, `receive.usb_connect`, `station_scene_bind_event`, `energy.set_device_attrs`, `platform_energy_filter_tree`) → commit.

### Task 3.9: Flows re-traced on 3.24.3
- [ ] All 14 existing flows re-traced (addresses change), moved to `flows/<name>.md`; new: output limit (1.1), Modbus setup, DIY unlock, installer commissioning, OTA monitor → commit.

### Task 3.10: Business rules + validation model re-verified
- [ ] Every rule gets a 3.24.3 citation or "not found in 3.24.3"; safe-polling facts (RefreshManager intervals, retry/backoff) extracted here for Task 4.4 → commit.

### Task 3.11: App architecture note
- [ ] README/`ankerAPK/REVERSE_ENGINEERING_REPORT.md`: native lib changes (`libunity/il2cpp` 3D viewer, `libdartjni`, `libquickjs`, `libsqlcipher`, `libak_logan`; removed Ali phone-auth, Baidu push), Dart 3.11, libapp 78 MB, new hosts (openweathermap, openai policy → Anka) → commit.

---

## Phase 4 — Usability

### Task 4.1: GLOSSARY.md
- [ ] Terms with one-line definitions + links: site, station, scene/scene_info, device/sub-device, PN vs SN, param_type vs cmd, HES/PPS/Solarbank gen 1–4, EMS modes, legal vs user power limit, display_type, DIY unlock, encrypted request, akiot/IoT-Kit, mqtt_monitor → commit.

### Task 4.2: Error code catalog
- [ ] `api/errors.md` + `data/errors.json`: codes from asm (`code=` log strings, error enum classes), from upstream (`errors.py`), from issues (10004 ItemNotFoundError + context); columns `code | message | seen on endpoint | meaning | source tag` → commit.

### Task 4.3: Known Unknowns + device-tested backlog
- [ ] Each owner page ends with "Known unknowns"; `docs/DEVICE_TEST_BACKLOG.md` lists every `asm-traced` fact that a device owner could confirm (what to send, what to look for, who has the device) → commit.

### Task 4.4: Safe-usage guidance
- [ ] `docs/SAFE_USAGE.md`: app polling intervals (3.10), do-not-do list (no tight loops, no fuzzing set_ endpoints, respect rate limits), link from disclaimer → commit.

### Task 4.5: Feedback loop
- [ ] `.github/ISSUE_TEMPLATE/device_tested.md` (fields: page, device PN/FW, request sent, response, verdict), `.github/ISSUE_TEMPLATE/correction.md`; `CONTRIBUTING.md` (how to cite asm, Smi rule pointer, how to run tools) → commit.

### Task 4.6: Lint + link check
- [ ] `tools/lint_docs.py`: status header present; template section order; every integer in tables has `@0x` citation or tag `upstream-confirmed`/`device-tested`; no duplicated payload code blocks across pages (hash compare); all relative links resolve; page length ≤ 600 lines. Run, fix all findings → commit.

### Task 4.7: README rewrite + migration finish
- [ ] README: role paths (0.2), use-case index ("set output limit" → owner page…), version matrix 3.18.0/3.24.3, "What changed in 3.24.3", coverage metric, statistics regenerated from JSON, legend; superseded root files get their final banner (deletion is Task 4.9) → commit.

### Task 4.8: Machine-readable export as deliverable
- [ ] `data/README.md` describing the four JSON files' schemas + stability promise; mention in README for library maintainers; validate JSON against a small schema in `tools/` → commit.

### Task 4.9: Repo cleanup (bereinigen)
Current state (2026-10-19): 59 commits, tracked = 14 root `.md` + `devices/`(5) + `endpoints/`(18) + `models/`(13) + `patches/`(README + 1 patch) + LICENSE + .gitignore; untracked: `patches/a17c1_a17x8_apk_tags.patch`, `docs/`; ignored: `easter_eggs/` (11 zips, local only).
- [ ] Step 1: `patches/` → `docs/archive/patches-2026-03/` with a banner "stale: based on 3.18.0, contains Smi misreads (value 2 = real 1), upstream PRs #281/#283 closed; superseded by mqtt/a17c1.md" — nothing in `patches/` stays at root.
- [ ] Step 2: Superseded root docs (after Phase 3 owners exist): delete `BLE_COMMAND_MAP.md`, `ENDPOINT_FIELDS.md`, `REQUIRED_FIELDS.md`, `FIELD_TYPES.md`, `JSON_EXAMPLES.md`, `RESPONSE_EXAMPLES.md`, `PARAM_DATA_STRUCTURES.md`, `VALIDATION_MODEL.md`, `BUSINESS_RULES.md`, `ENUMS.md`, `FLOWS.md`, `DART_PYTHON_MAPPING.md`, old `endpoints/`, `models/`, `devices/*.md` that moved — only once `tools/lint_docs.py --links` passes with zero inbound links to them. Root keeps: README, GLOSSARY, METHODOLOGY, CHANGELOG, CONTRIBUTING, LICENSE.
- [ ] Step 3: `docs/audit/` tables (Phase 2) stay as provenance; `docs/superpowers/plans/` stays; `ankerAPK/v3.24.3/audit/*` findings that are facts move into owner pages, the rest is not committed here (lives in the private `ankerAPK` workspace).
- [ ] Step 4: `.gitignore`: keep `easter_eggs/`; add `tools/out/`, `__pycache__/`, `.venv*/`. Decide easter eggs: stay ignored (no spoilers, APK assets = Anker copyright) — write that reason into CONTRIBUTING.
- [ ] Step 5: Git hygiene: no history rewrite; one commit per task; squash nothing; tag before cleanup `v2026.04-app3.18.0` on the current HEAD so the old state stays reachable.
- [ ] Step 6: Verify: `git ls-files | grep -vE '^(README|GLOSSARY|METHODOLOGY|CHANGELOG|CONTRIBUTING)\.md$|^(api|mqtt|ble|flows|devices|models|reference|data|tools|docs|\.github)/|^LICENSE$|^\.gitignore$'` prints nothing → commit `chore: repo cleanup after 3.24.3 rework`.

### Task 4.10: CHANGELOG + release + close-out
- [ ] CHANGELOG "2026-10 — 3.24.3 rework" (new services, removed, Errata, issue #1 result, cleanup); tag `v2026.10-app3.24.3`; final comment on issue #1 with links; ask thomluther to confirm.

---

## Not in scope (explicitly)
- Implementing anything in `anker-solix-api` / `ha-anker-solix`.
- Re-decompiling the React-Native charging bundle (`libhermes`) unless a flow needs it.
- Unity/il2cpp content (3D product viewer) — note only.
- mkdocs/GitHub Pages site — optional follow-up once Phase 4 is done.

---

## Added 2026-10-19 (owner: "Kümmer dich um alles") — controller rulings folded into the plan

### Task 3.1c: caller resolution for url_provider rows (after 3.7)
- [ ] `tools/endpoint_inventory.py`: for a URL literal with no `*Http*` call in its function, follow the function's callers (grep `Class::fn` in `bl` comments) up to 3 levels; if a caller reaches an `*Http*`/SDK sender, record it as the sender (`sender_via: [chain]`); if the chain enters a mixin-dedup region absent from the dump, mark `reference: "mixin-gap"` (UNCONFIRMED). Tests on 3 known cases (set_user_site_param → setUserParamsAsync; a standby-exercise-plan literal; one that stays unresolved). Regenerate JSON + re-render only the upgraded skeletons (no-clobber). Report before/after url_provider count.
### Task 3.6c: generic `iot` MQTT decoder page (fold into 3.7 dispatch or run right after)
- [ ] `mqtt/iot.md` from the audit rows that cover the generic/iot decoder + new 3.24.3 reads; EverFrost and A17D0 stay "not covered" (niche / no UI page).
### Task 1.2c: fold the issue #1 thread back into the owner pages (right after 4.7-pre)
- [ ] `api/power_service/site/set_site_device_param.md` Device-tested: thomluther 2026-10-19 — `display_type: 1` enables free 10 W values; `display_type` 0/absent → option-list values only; API does not enforce `legal_limit`. `flows/system_output_limit.md`: note that the legacy `PowerSliderView` is the per-device AC INPUT limit (`set_device_attrs ac_power_limit`, A17C1/A17C3 gate, `supportAcLimit` AE103/A17E2/AE111) and that the entry gate is `_updateStationPowerLimitStatus` (get_power_limit with app_ability). `devices/a17c5.md` row → device-tested yes.
### Task 4.7-pre addendum: status column
- [ ] `tools/service_index.py`: per-page status column (`owner` = no TODO purpose; `skeleton`; `pool-only`; `removed`) in every service README + counts in api/README.md.
### Task 4.8 addendum
- [ ] `data/models.json`: drop Sentry/field-less classes behind a `--include-noise` flag; key `package::Class` to disambiguate the 111 duplicate names.
### Decisions (no task)
- Preset-key literal stays redacted (role + pp.txt offset only). Trailer mix stays (CHANGELOG note). Merge to main = merge commit, no squash; tag `v2026.10-app3.24.3`.
### Task 4.11: pointer comment to thomluther (after 4.7-pre is pushed)
- [ ] Short comment on issue #1 linking `api/param_types.md`, `mqtt/README.md`, `api/encryption.md` on the branch.
