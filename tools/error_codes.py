"""Extract the error-code catalog (upstream errors.py, 3.24.3 asm, issue reports).

Usage (repo root):
  python3 -I tools/error_codes.py [--repo .] [--asm ROOT] [--upstream errors.py] [--pool pp.txt] [--check]

Writes data/errors.json and nothing else (the path is fixed, there is no --out).
With --check nothing is written: exit 1 when data/errors.json is missing or stale,
or when api/errors.md exists and lacks a table row for a code in the JSON.
Standard library only; the asm tree and the upstream file are only read
(upstream is parsed with ast, never imported).

Asm rows also carry `message_keys` (every localization key loaded in the equal-path
block after the compare that exists in the app's en_US translation table, read from the
Blutter pool dump `pp.txt`, `--pool`), `message_key` (the first; may be a dialog title,
not the body), `message_en` (its text) and `message_tag` (`asm-traced (proximity)`,
only when a key exists).  The equal-path block is the fall-through of `b.ne` or the
target of `b.eq`, up to an unconditional branch, `ret`, the `b.ne` target or the next
compare; a range split (gt/lt) has none.  `common*` button labels and GENERIC_KEYS
are skipped.  Proximity, not proof of what the user sees.

Row sources (field `source`):
  upstream  class ERRORS entry of upstream api/errors.py, tag upstream-confirmed
  asm       a compare of an error code in a handler function of the app, tag
            asm-traced (the compare is traced; what the code means is only as
            good as the localization key or log text next to it)
  issue     a code reported in a GitHub issue, tag device-tested

Every row has `kind`: `api` (an error code) or `message-type-excluded` (an asm compare
of 10000..10007 in an onMessageDispatch function or MQTT closure listed in MSG_SITES:
a device message type that shares numbers with API codes; kept as data, not catalogued).

Smi rule for the asm rows (METHODOLOGY.md): a 32-bit compare (`cmp wN, #imm` or
`r17 = imm; cmp wN, w17`) works on a tagged int, so value = raw / 2; a 64-bit
compare (`cmp xN, #imm` or `cmp xN, x17`) works on an unboxed int, value = raw.
Every asm row keeps `width` and `raw` so a reader can redo the step, and `branch`
(the conditional branch right after the compare: eq/ne for a plain test, gt/lt/ge/le
where the compiler split a switch into a binary search; the flags are then reused by
the later branches, so the value is still one case label of the switch).

The handler functions are listed in SITES by file and function address and are
valid for App 3.24.3 only.  They were picked by reading the asm: a sweep of every
compare against a 4 to 6 digit constant finds mostly class ids, message types and
UI limits, so the tool does not guess; it reads the listed functions only.
"""
import argparse
import ast
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import asmparse as A  # noqa: E402

TOOL = 'tools/error_codes.py'
APP_VERSION = '3.24.3'
OUT_REL = os.path.join('data', 'errors.json')
PAGE_REL = os.path.join('api', 'errors.md')

ISSUE_ROWS = [
    {'code': 10004, 'source': 'issue', 'tag': 'device-tested',
     'name': 'ItemNotFoundError',
     'endpoint': '/power_service/v1/site/set_site_device_param',
     'kind': 'api',
     'context': 'A17C5, 790 W (not in power_limit_option) sent with the upstream '
                'library payload and no display_type, rejected with 10004 '
                '(thomluther); the Device-tested table of the endpoint page owns '
                'the record and the later tests',
     'url': 'https://github.com/moag1000/anker-solix-api-exploration/issues/1'
            '#issuecomment-6263845744',
     'reported_by': 'thomluther', 'reported': '2026-10-18'},
]

# (file under the asm root, function address, label, smallest value to keep)
_ACC = 'charging/ui/page/account/'
SITES = [
    ('charging/http/HttpEncryptionDecorator.dart', '0x486aed0', '_handleSdkError', 400),
    ('charging/http/HttpEncryptionDecorator.dart', '0x486afc0', 'handleStatusCode', 400),
    ('charging/http/HttpEncryptionDecorator.dart', '0x486b2bc', '_handler401', 400),
    ('charging/util/manager/http_manager.dart', '0x2cf6370', 'fail callback', 1000),
    ('charging/http/http_request_repository_impl.dart', '0x2265bb0', 'fail callback', 1000),
    (_ACC + 'login/login_logic.dart', '0x3bd2210', 'handleLoginFail', 1000),
    (_ACC + 'login/login_logic.dart', '0x2fb09dc', 'send email code closure', 1000),
    (_ACC + 'login/login_logic.dart', '0x3bd9eb8', 'send SMS code closure', 1000),
    (_ACC + 'privacy_policy/verification/verification_logic.dart', '0x2faf718',
     '_handleVerifyFail', 1000),
    (_ACC + 'privacy_policy/verification/verification_logic.dart', '0x2fb0608',
     'send email code closure', 1000),
    (_ACC + 'forget_pwd/forget_pwd_logic.dart', '0x3bc8bf0', 'closure', 1000),
    (_ACC + 'forget_pwd/forget_pwd_logic.dart', '0x3bc8e84', 'closure', 1000),
    (_ACC + 'forget_pwd/forget_pwd_logic.dart', '0x3bc9fdc', 'closure', 1000),
    (_ACC + 'forget_pwd/forget_pwd_logic.dart', '0x3bcbba0', 'closure', 1000),
    (_ACC + 'bind_phone_number/bind_phone_number_logic.dart', '0x3bc35f8', 'closure', 1000),
    (_ACC + 'bind_phone_number/bind_phone_number_logic.dart', '0x3bc4660', 'closure', 1000),
    (_ACC + 'bind_phone_number/bind_phone_number_logic.dart', '0x3bc58f4', 'closure', 1000),
    (_ACC + 'register/register_logic.dart', '0x3be2760', 'closure', 1000),
    (_ACC + 'register/register_logic.dart', '0x3be33e0', 'closure', 1000),
    (_ACC + 'register/register_logic.dart', '0x3be5698', 'closure', 1000),
    ('charging/ui/page/user/routerInfo/account_verification/account_verification_logic.dart',
     '0x4055a2c', 'closure', 1000),
    ('charging/http/http_exception.dart', '0x27a1308', 'handleNetErrorMsg', 20000),
    ('charging/ui/page/user/share_site/invite_members/invite_members_logic.dart',
     '0x40618cc', 'sendInviteMessage closure', 20000),
    ('charging/ui/page/device/a1782/station/electricity_scene/'
     'a1782_electricity_scene_logic.dart', '0x28d3528', 'closure', 20000),
    ('charging/ui/page/device/a17c0/ez1_select_mode/ez1_select_mode_logic.dart',
     '0x3d65494', 'closure', 20000),
    ('charging/ui/page/device/a17c0/select_brand/select_brand_logic.dart',
     '0x2753758', 'closure', 20000),
    ('charging/ui/page/device/a17c0/select_solar_power/select_solar_power_logic.dart',
     '0x3d73364', 'closure', 20000),
    ('charging/ui/page/device/a5101/setting/device_manager/ev_charger/'
     'add_ev_charger_logic.dart', '0x24560d0', 'closure', 20000),
    ('charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart',
     '0x42ea800', 'closure', 20000),
    ('charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart',
     '0x24a13ec', 'closure', 20000),
    ('charging/ui/page/device/a5101/setting/system_self_check/system_testing/'
     'system_testing_logic.dart', '0x43300f0', 'closure', 20000),
    ('charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/'
     'fixed_rate/fixed_rate_logic.dart', '0x3ecff9c', 'closure', 20000),
    ('charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/'
     'nem_rate/nem_plan_edit/nem_plan_edit_logic.dart', '0x278fe28', 'closure', 20000),
    ('charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/'
     'nem_rate/nem_plan_edit/nem_plan_edit_logic.dart', '0x3ed5218', 'closure', 20000),
    ('charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/'
     'nem_rate/nem_rate_plan/nem_rate_plan_logic.dart', '0x3ed64b0', 'closure', 20000),
    ('charging/ui/page/device/a5140/wifi/network_inspection/network_inspection_logic.dart',
     '0x3eebb8c', 'closure', 20000),
    ('charging/ui/page/device/a5150/setting/three_part_solar_setting_logic.dart',
     '0x42fd7ec', 'closure', 20000),
    ('charging/ui/page/device/main/sitation_energy_system/station_home_settings/'
     'add_devices/add_devices_logic.dart', '0x3f9a788', '_handleEvErrorDialog', 20000),
    ('charging/ui/page/device/main/sitation_energy_system/station_home_settings/'
     'add_devices/add_devices_logic.dart', '0x3f9aa7c', 'closure', 20000),
    ('charging/ui/page/device/main/station_device_home/device_main_page/'
     'device_main_logic.dart', '0x2607688', 'closure', 20000),
    ('charging/ui/page/device/main/station_device_home/station_home_info/controller/'
     'station_home_info_logic.dart', '0x27a1234', 'closure', 20000),
    ('charging/ui/page/device/main/station_device_home/station_home_info/controller/'
     'station_home_info_logic.dart', '0x30c7704', 'closure', 20000),
    ('charging/ui/page/device/main/station_device_home/station_main_page/'
     'station_main_page_logic.dart', '0x23f115c', 'closure', 20000),
    ('charging/ui/page/green_energy/site/site_logic.dart', '0x27b72b0', 'toInitFlow', 20000),
    ('charging/ui/page/qr_Scanner/qr_scanner_logic.dart', '0x33fb024',
     'showInvalidQRCodeDialog', 20000),
    ('charging/ui/page/qr_Scanner/qr_scanner_logic.dart', '0x33fd334', 'closure', 20000),
    ('device/src/station_setting/controller/common_station_name/station_name_view_model.dart',
     '0x2cb57c8', 'closure', 20000),
    ('device_bind/src/device_bind/ble_connect/ble_connect/ble_connect_logic.dart',
     '0x35116e0', 'closure', 20000),
    ('electricity_price/components/dynamic_price/util/local_auto_disaster_feature.dart',
     '0x2c13f58', 'closure', 20000),
    ('ev_charger/src/ev_charger/page/home/load_balancing/select_station/'
     'evselect_station_logic.dart', '0x3963488', '_handleAddSiteDeviceError', 20000),
    ('ev_charger/src/ev_charger/page/home/load_balancing/select_station/'
     'evselect_station_logic.dart', '0x39646cc', '_handleSetStationEvChargersError', 20000),
    ('ev_charger/src/ev_charger/page/home/setting/device_share_members/'
     'device_share_list_page/device_share_list_logic.dart', '0x430b1e0', 'closure', 20000),
    ('ev_charger/src/ev_charger/page/vehicle/vehicle_edit_logic.dart', '0x2cf994c',
     'closure', 20000),
    ('ev_charger/src/ev_charger/page/vehicle/vehicle_edit_logic.dart', '0x39836c4',
     '_doDelete', 20000),
    ('ev_charger/src/ev_charger/sdk/extension/iot_ak_result_extension.dart', '0x2cdbecc',
     'ResultCodeExtension.isTimeout', 20000),
    ('flutter_charging_beginning/beginning/pages/select_scene/select_scene_controller.dart',
     '0x398c8d4', '_createSiteForMain', 20000),
    ('flutter_charging_beginning/beginning/state_cards/rename_device/'
     'rename_device_controller.dart', '0x47a6308', 'save', 20000),
    ('micro_hes/src/common_business/basic_station/basic_station_setting/component/'
     'general_setting/station_name_controller.dart', '0x2cd3174', 'closure', 20000),
    ('small_charging_platform/src/screen_setting/clock_style/weather/'
     'weather_clock_location_helper.dart', '0x2cbc298', 'closure', 20000),
    ('unity/src/main/weather/weather_manager.dart', '0x451e5c0', 'syncLocationToCloud', 20000),
]

# onMessageDispatch functions and two MQTT-model closures that compare 10000..10007:
# device message types, not API error codes.  Recorded as kind "message-type-excluded"
# so that the exclusion is data (file, function address, label, smallest, largest).
_SET = 'charging/ui/page/device/a5101/setting/'
MSG_SITES = [
    (_SET + 'advanced_config/advanced_config_logic.dart', '0x277c6cc', 'onMessageDispatch'),
    (_SET + 'cls_setting/cls_setting_logic.dart', '0x27c6d34', 'onMessageDispatch'),
    (_SET + 'device_manager/ev_charger/ev_charger_manager_logic.dart', '0x27854c8',
     'onMessageDispatch'),
    (_SET + 'device_manager/heat_pump/controller.dart', '0x2785830', 'onMessageDispatch'),
    (_SET + 'device_manager/heat_pump/timer_setting/timer_setting_logic.dart', '0x2785a20',
     'onMessageDispatch'),
    (_SET + 'device_manager/oil_engine/manage_devices_logic.dart', '0x2786af0',
     'onMessageDispatch'),
    (_SET + 'grid_sensitivity/a5101_grid_sensitivity_logic.dart', '0x27c9204',
     'onMessageDispatch'),
    (_SET + 'homeSetting/save_tou_plan_logic.dart', '0x27ce290', 'onMessageDispatch'),
    (_SET + 'remote_switch/remote_switch_logic.dart', '0x27ce5e0', 'onMessageDispatch'),
    (_SET + 'screen_timeout/screen_timeout_logic.dart', '0x2786dd4', 'onMessageDispatch'),
    (_SET + 'systemPolicy/system_policy_logic.dart', '0x278aa5c', 'onMessageDispatch'),
    (_SET + 'utility_rate_plan/rate_plan_structure/nem_rate/nem_plan_edit/'
     'nem_plan_edit_logic.dart', '0x278e894', 'onMessageDispatch'),
    (_SET + 'utility_rate_plan/rate_plan_structure/nem_rate/nem_rate_plan/'
     'nem_rate_plan_logic.dart', '0x278ffbc', 'onMessageDispatch'),
    ('charging/ui/page/family/auto_disaster/auto_disaster_tips_logic.dart', '0x27ac7b8',
     'onMessageDispatch'),
    ('charging/ui/page/family/family_main_page_logic.dart', '0x23e1df0',
     'closure (MQTT device state model)'),
    ('charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart', '0x23ae448',
     'closure (MQTT)'),
]
MSG_RANGE = (10000, 10007)

CMP_IMM = re.compile(r'^cmp\s+([wx])\d+,\s+#(0x[0-9a-f]+|\d+)$')
CMP_REG = re.compile(r'^cmp\s+([wx])\d+,\s+([wx])17$')
R17 = re.compile(r'^r17 = (\d+)$')
STR_LIT = re.compile(r'^r\d+ = "(.*)"$')


def smi_value(width, raw):
    """Smi rule: 32-bit compare = tagged int (halve), 64-bit compare = raw."""
    return raw // 2 if width == 'w' else raw


def _compare(instrs, i):
    """Return (form, width, raw) when instrs[i] is a compare against a constant."""
    text = instrs[i].text
    m = R17.match(text)
    if m and i + 1 < len(instrs):
        n = CMP_REG.match(instrs[i + 1].text)
        if n and n.group(1) == n.group(2):
            return n.group(1) + '17', n.group(1), int(m.group(1))
        return None
    m = CMP_IMM.match(text)
    if m:
        return m.group(1) + '-imm', m.group(1), int(m.group(2), 0)
    return None


BR_COND = re.compile(r'^b\.(\w+)\s+#(0x[0-9a-f]+)')
BR_UNCOND = re.compile(r'^(b\s+#|ret\b|br\s)')
BLOCK_MAX = 80


def equal_block_strings(ins, j, stop):
    """String literals loaded on the path where the compare was equal.

    ins[j] is the conditional branch after the compare.  `b.ne T`: the equal path
    is the fall-through, which ends at the address T, at an unconditional branch,
    at `ret` or at the next compare (index `stop`).  `b.eq T`: the equal path starts
    at T and ends at the first unconditional branch, `ret` or compare.  Any other
    condition (a range split) has no single equal path: returns [].
    """
    m = BR_COND.match(ins[j].text) if j < len(ins) else None
    if not m or m.group(1) not in ('eq', 'ne'):
        return []
    target = m.group(2)
    if m.group(1) == 'ne':
        start, limit = j + 1, None
    else:
        idx = [k for k, x in enumerate(ins) if x.addr == target]
        if not idx:
            return []
        start, limit = idx[0], None
        stop = len(ins)
    out = []
    for k in range(start, min(len(ins), start + BLOCK_MAX)):
        if m.group(1) == 'ne' and (ins[k].addr == target or k >= stop):
            break
        if m.group(1) == 'eq' and k > start and _compare(ins, k):
            break
        t = ins[k].text
        if BR_UNCOND.match(t):
            break
        s = STR_LIT.match(t)
        if s and s.group(1) not in out:
            out.append(s.group(1))
    return out


def scan_function(fn, min_value, label=None, max_value=None):
    """Return the code compares of one function as row dicts (no source fields)."""
    ins = fn.instrs
    hits = [(i, _compare(ins, i)) for i in range(len(ins))]
    hits = [(i, c) for i, c in hits if c]
    rows = []
    for k, (i, (form, width, raw)) in enumerate(hits):
        value = smi_value(width, raw)
        if value < min_value or (max_value is not None and value > max_value):
            continue
        # the compare instruction itself carries the address; for `r17 = N` the
        # citation is the load of the constant, which is the first of the pair
        stop = hits[k + 1][0] if k + 1 < len(hits) else len(ins)
        strings = []
        for x in ins[i + 1:min(stop, i + 40)]:
            s = STR_LIT.match(x.text)
            if s and s.group(1) not in strings:
                strings.append(s.group(1))
        j = i + (2 if form.endswith('17') else 1)
        branch = None
        if j < len(ins):
            b = re.match(r'^b\.(\w+)\b', ins[j].text)
            branch = b.group(1) if b else None
        rows.append({
            'code': value, 'width': width, 'raw': raw, 'form': form, 'branch': branch,
            'addr': ins[i].addr, 'function': label or fn.name,
            'function_addr': fn.addr, 'odd_raw': width == 'w' and raw % 2 == 1,
            'strings': strings[:4],
            'block': equal_block_strings(ins, j, stop),
        })
    return rows


def scan_sites(asm_root, sites=None, kind='api', max_value=None):
    """Read the listed functions of the asm tree; return asm rows of this kind."""
    sites = SITES if sites is None else sites
    by_file = {}
    for rel, addr, label, minv in sites:
        by_file.setdefault(rel, {})[addr] = (label, minv)
    rows, missing = [], []
    for rel in sorted(by_file):
        path = os.path.join(asm_root, rel)
        want = dict(by_file[rel])
        if not os.path.isfile(path):
            missing += ['%s %s' % (rel, a) for a in want]
            continue
        for fn in A.iter_functions(path, rel):
            if fn.addr in want:
                label, minv = want.pop(fn.addr)
                for r in scan_function(fn, minv, label, max_value):
                    r.update({'source': 'asm', 'tag': 'asm-traced', 'file': rel,
                              'kind': kind})
                    rows.append(r)
        missing += ['%s %s' % (rel, a) for a in want]
    return rows, missing


def parse_upstream(path):
    """Parse upstream errors.py with ast: ERRORS entries and exception classes."""
    with open(path, encoding='utf-8') as fh:
        tree = ast.parse(fh.read())
    classes, table = {}, []
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            base = node.bases[0].id if node.bases and isinstance(node.bases[0], ast.Name) else None
            classes[node.name] = {'base': base, 'doc': ast.get_docstring(node) or '',
                                  'line': node.lineno}
        elif (isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name)
              and node.target.id == 'ERRORS' and isinstance(node.value, ast.Dict)):
            for k, v in zip(node.value.keys, node.value.values):
                if isinstance(k, ast.Constant) and isinstance(v, ast.Name):
                    table.append((k.value, v.id, k.lineno))
    rows = []
    for code, cls, line in table:
        info = classes.get(cls, {})
        rows.append({
            'code': code, 'source': 'upstream', 'tag': 'upstream-confirmed',
            'name': cls, 'base': info.get('base'), 'message': info.get('doc', ''),
            'line': line, 'class_line': info.get('line'),
            'file': 'api/errors.py', 'kind': 'api'})
    return rows


# Keys that label a button or a generic state next to a compare; never the message.
GENERIC_KEYS = {'failed', 'signUpGoSignIn', 'forgetPwdResend'}
LOCALE = 'en_US'
MESSAGE_TAG = 'asm-traced (proximity)'
POOL_MAP_HEAD = re.compile(r'^\[pp\+0x[0-9a-f]+\] Map<String, Map<String, String>>\(\d+\) \{$')
POOL_ENTRY = re.compile(r'^    "((?:[^"\\]|\\.)*)": "(.*)",?$')


def load_locale(pool_path, locale=LOCALE):
    """key -> text of one locale from the Blutter pool dump (read only).

    The dump prints the app's translation table as `Map<String, Map<String, String>>`
    with one `"<locale>": Map<String, String>(n) {` block per language; entries are
    `    "key": "text",`.  Returns {} when no such block is found.
    """
    out, state = {}, 0
    head = '  "%s": Map<String, String>' % locale
    with open(pool_path, encoding='utf-8', errors='replace') as fh:
        for line in fh:
            line = line.rstrip('\n')
            if state == 0:
                state = 1 if POOL_MAP_HEAD.match(line) else 0
            elif state == 1:
                state = 2 if line.startswith(head) else 1
            else:
                if line.startswith('  }'):
                    break
                m = POOL_ENTRY.match(line)
                if m:
                    out[m.group(1)] = m.group(2).replace("\\'", "'").replace('\\?', '?')
    return out


def message_for(strings, texts):
    """(keys, text of the first key) of the localization keys loaded in the equal-path block.

    A key counts when it is in the locale table and is neither a `common*` button
    label nor in GENERIC_KEYS.  Proximity, not proof: the first key may be a dialog
    title, not the body (see MESSAGE_TAG).  ([], None) when there is none.
    """
    keys = []
    for s in strings:
        if s in texts and not s.startswith('common') and s not in GENERIC_KEYS \
                and s not in keys:
            keys.append(s)
    return keys, (texts[keys[0]] if keys else None)


def build(asm_root, upstream_path, sites=None, msg_sites=None, pool=None):
    rows = parse_upstream(upstream_path)
    asm_rows, missing = scan_sites(asm_root, sites)
    texts = load_locale(pool) if pool else {}
    for r in asm_rows:
        keys, en = message_for(r['block'], texts)
        r['message_key'], r['message_en'] = (keys[0] if keys else None), en
        r['message_keys'] = keys
        if keys:
            r['message_tag'] = MESSAGE_TAG
    msg = MSG_SITES if msg_sites is None else msg_sites
    msg_rows, miss2 = scan_sites(
        asm_root, [(f, a, lb, MSG_RANGE[0]) for f, a, lb in msg], 'message-type-excluded',
        MSG_RANGE[1])
    missing += miss2
    for r in asm_rows + msg_rows:
        r.pop('block', None)
    rows += asm_rows + msg_rows + [dict(r) for r in ISSUE_ROWS]
    rows.sort(key=lambda r: (r['code'], r['source'], r.get('file', ''),
                             r.get('addr', ''), r.get('line', 0)))
    return rows, missing


def render(rows):
    doc = {'generated_by': '%s asm_root --version %s' % (TOOL, APP_VERSION),
           'app_version': APP_VERSION, 'snapshot': A.SNAPSHOT_3_24_3, 'rows': rows}
    return json.dumps(doc, indent=2, sort_keys=True, ensure_ascii=False) + '\n'


def page_gaps(repo, rows):
    """Codes in the JSON that have no table row `| <code> |` in api/errors.md."""
    page = os.path.join(repo, PAGE_REL)
    if not os.path.isfile(page):
        return []
    with open(page, encoding='utf-8') as fh:
        text = fh.read()
    have = {int(m.group(1)) for m in re.finditer(r'^\|\s*(\d+)\s*\|', text, re.M)}
    return sorted({r['code'] for r in rows if r['kind'] == 'api'} - have)


def message_gaps(repo, rows):
    """Message keys in the JSON that api/errors.md never names in backticks."""
    page = os.path.join(repo, PAGE_REL)
    if not os.path.isfile(page):
        return []
    with open(page, encoding='utf-8') as fh:
        text = fh.read()
    keys = {r['message_key'] for r in rows if r.get('message_key')}
    return sorted(k for k in keys if '`%s`' % k not in text)


def write_guarded(repo, text):
    """The only write of this tool: data/errors.json under the repo."""
    path = os.path.join(repo, OUT_REL)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(text)
    return path


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--repo', default='.')
    ap.add_argument('--asm', default=A.DEFAULT_NEW_ROOT)
    ap.add_argument('--upstream', default=os.path.join(
        os.path.dirname(A.DEFAULT_UPSTREAM), 'errors.py'))
    ap.add_argument('--pool', default=os.path.join(os.path.dirname(A.DEFAULT_NEW_ROOT.rstrip('/')), 'pp.txt'))
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args(argv)
    if not os.path.isfile(a.pool):
        print('pool dump not found (nothing written): %s' % a.pool, file=sys.stderr)
        return 2
    rows, missing = build(a.asm, a.upstream, pool=a.pool)
    if missing:
        print('sites not found (nothing written): %s' % ', '.join(missing), file=sys.stderr)
        return 2
    text = render(rows)
    path = os.path.join(a.repo, OUT_REL)
    old = open(path, encoding='utf-8').read() if os.path.isfile(path) else None
    gaps = page_gaps(a.repo, rows)
    counts = {}
    for r in rows:
        k = r['source'] if r['kind'] == 'api' else r['kind']
        counts[k] = counts.get(k, 0) + 1
    print(json.dumps({'codes': len({r['code'] for r in rows if r['kind'] == 'api'}),
                      'rows': counts},
                     sort_keys=True))
    if gaps:
        print('codes without a table row in %s: %s' % (PAGE_REL, gaps))
    kgaps = message_gaps(a.repo, rows)
    if kgaps:
        print('message keys not named in %s: %s' % (PAGE_REL, kgaps))
    if a.check:
        stale = old != text
        print('data/errors.json: %s' % ('stale or missing' if stale else 'up to date'))
        return 1 if (stale or gaps or kgaps) else 0
    print('changed: %s' % ('none' if old == text else OUT_REL))
    if old != text:
        write_guarded(a.repo, text)
    return 0


if __name__ == '__main__':
    sys.exit(main())
