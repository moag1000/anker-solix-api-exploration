"""Spot checks for the extraction tools.

Run from the repo root:  python3 -I -m unittest discover -s tools/tests -t .
The tests read the real Blutter asm trees; they skip when a root is missing.
"""
import os
import sys
import unittest

TOOLS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, TOOLS)

ROOT_NEW = os.environ.get(
    'ANKER_ASM_NEW', '/Users/michaelbanda/Nextcloud/www/untitled1/ankerAPK/'
    'v3.24.3/blutter_output/asm')
ROOT_OLD = os.environ.get(
    'ANKER_ASM_OLD', '/Users/michaelbanda/Nextcloud/www/untitled1/ankerAPK/'
    'blutter_output/asm')
UPSTREAM = os.environ.get(
    'ANKER_UPSTREAM', '/Users/michaelbanda/Nextcloud/www/untitled1/ankerAPK/'
    'anker-solix-api/api/apitypes.py')
REPO = os.path.dirname(TOOLS)

HTTP_FILE = os.path.join(ROOT_NEW, 'charging/http/http_request_repository_impl.dart')
LOGIC_FILE = os.path.join(
    ROOT_NEW, 'charging/ui/page/device/main/sitation_energy_system/'
    'station_home_settings/station_power_limit/station_power_limit_logic.dart')


def need(*roots):
    missing = [r for r in roots if not os.path.isdir(r)]
    return unittest.skipIf(bool(missing), 'asm root missing: %s' % missing)


_cache = {}


def cached(key, fn):
    if key not in _cache:
        _cache[key] = fn()
    return _cache[key]


def inventory_new():
    import endpoint_inventory
    return cached('inv_new', lambda: endpoint_inventory.build_inventory(
        ROOT_NEW, '3.24.3', old_root=ROOT_OLD, upstream=UPSTREAM))


def models_new():
    import model_fields
    return cached('models_new', lambda: model_fields.build_models(
        ROOT_NEW, '3.24.3', old_root=ROOT_OLD))


@need(ROOT_NEW)
class SmiTests(unittest.TestCase):
    def test_cmd_246_is_32bit_store_halved(self):
        import smi
        r = smi.smi_at(HTTP_FILE, '0x43558c4')
        self.assertEqual((r['raw'], r['store'], r['width'], r['value']),
                         (246, 'stur', 'w', 123))

    def test_100_is_64bit_store_raw(self):
        import smi
        r = smi.smi_at(LOGIC_FILE, '0x43550b8')
        self.assertEqual((r['raw'], r['store'], r['width'], r['value']),
                         (100, 'stur', 'x', 100))


@need(ROOT_NEW, ROOT_OLD)
class InventoryTests(unittest.TestCase):
    def test_set_site_device_power_limit_row(self):
        rows = inventory_new()['rows']
        hit = [r for r in rows if r['function'] == 'setSiteDevicePowerLimit'
               and r['url'] == '/power_service/v1/site/set_site_device_param']
        self.assertEqual(len(hit), 1)
        r = hit[0]
        self.assertEqual(r['param_type'], '19')
        self.assertEqual(r['cmd'], 123)
        self.assertEqual(r['cmd_raw'], 246)
        self.assertTrue(r['encrypted'])
        for p in ('display_type', 'power_limit.limit', 'power_limit.limit_real'):
            self.assertIn(p, r['params'])
        self.assertTrue(any('_setOutputPowerLimit' in c for c in r['callers']))

    def test_row_fields_and_since(self):
        rows = inventory_new()['rows']
        need_keys = {'url', 'service', 'function', 'dart_file', 'params',
                     'param_type', 'cmd', 'cmd_raw', 'encrypted', 'callers',
                     'since', 'upstream_key'}
        for r in rows:
            self.assertTrue(need_keys <= set(r), r['url'])
        by_url = {r['url']: r for r in rows}
        self.assertEqual(
            by_url['/power_service/v1/site/get_power_limit']['since'], '≤3.18.0')
        # present in both versions (see DiffTests), so not removed
        self.assertNotIn('removed_in', by_url[
            '/power_service/v1/app/get_device_last_exercise_log'])
        self.assertEqual(
            by_url['/power_service/v1/site/set_device_feature']['removed_in'],
            '3.24.3')

    def test_upstream_key(self):
        rows = inventory_new()['rows']
        keys = {r['upstream_key'] for r in rows
                if r['url'] == '/power_service/v1/site/set_site_device_param'}
        self.assertEqual(keys, {'set_device_parm'})


@need(ROOT_NEW, ROOT_OLD)
class ModelTests(unittest.TestCase):
    def test_station_power_limit_model(self):
        rows = models_new()['rows']
        hit = [r for r in rows if r['class'] == 'StationPowerLimitModel']
        self.assertEqual(len(hit), 1)
        keys = [f['json_key'] for f in hit[0]['fields']]
        self.assertEqual(len(keys), 13)
        for k in ('ac_input_power', 'unlock_default_power_type',
                  'unlock_pop_content', 'unlock_pop_image'):
            self.assertIn(k, keys)
        since = {f['json_key']: f['since'] for f in hit[0]['fields']}
        self.assertEqual(since['unlock_pop_image'], '3.24.3')
        self.assertEqual(since['site_id'], '≤3.18.0')
        types = {f['json_key']: f['dart_type'] for f in hit[0]['fields']}
        self.assertEqual(types['site_id'], 'String?')
        self.assertEqual(types['ac_input_power'], 'int?')


@need(ROOT_NEW, ROOT_OLD)
class ParamTypeTests(unittest.TestCase):
    def test_param_types_present(self):
        import param_types
        res = cached('pt', lambda: param_types.build_param_types(
            ROOT_NEW, '3.24.3', upstream=UPSTREAM))
        got = {r['param_type'] for r in res['rows']}
        for p in ('6', '18', '19', '20', '26'):
            self.assertIn(p, got)
        r19 = [r for r in res['rows'] if r['param_type'] == '19'][0]
        self.assertEqual(r19['cmd'], 123)
        self.assertEqual(r19['param_type_source'], 'literal')
        self.assertIn('traced', {r['param_type_source'] for r in res['rows']})
        for r in res['rows']:
            if r['param_type_source'] == 'traced':
                self.assertTrue(r['traced_from'])
            self.assertTrue(set(r['function_sources'].values())
                            <= {'literal', 'traced', 'variable'})
        self.assertEqual(
            [r for r in res['rows'] if r['param_type'] == 'variable'][0]
            ['param_type_source'], 'variable')
        self.assertIn('setSiteDevicePowerLimit', r19['set_function'])
        by = {r['param_type']: r for r in res['rows']}
        # zero-register sender: cmd 0, no GET cmd
        self.assertEqual((by['24']['cmd_set'], by['24']['cmd'], by['24']['cmd_get']), (0, 0, None))
        # type 32: SET sends 0 (setGridPowerAsync), GET _fetchPowerLimits sends 123
        self.assertEqual((by['32']['cmd_set'], by['32']['cmd_get']), (0, 123))
        self.assertEqual(by['32']['cmd'], by['32']['cmd_set'])
        self.assertEqual((by['19']['cmd_set'], by['19']['cmd_get']), (123, None))


@need(ROOT_NEW, ROOT_OLD)
class NonFactoryModelTests(unittest.TestCase):
    def test_heat_pump_param_present(self):
        classes = {r['class'] for r in models_new()['rows']}
        for c in ('HeatPumpParam', 'Params', 'SocSettingParam', 'FeedGridSettingParam'):
            self.assertIn(c, classes)


@need(ROOT_NEW, ROOT_OLD)
class DiffTests(unittest.TestCase):
    def test_diff(self):
        import diff_versions
        d = cached('diff', lambda: diff_versions.compute_diff(
            ROOT_OLD, ROOT_NEW, '3.18.0', '3.24.3', UPSTREAM))
        added = [u for u in d['added_endpoints']
                 if u.startswith('/charging_hes_installer_svc/')]
        # The brief expected 19, which counts the string fragment
        # "charging_hes_installer_svc/v2/ota/" (a prefix of ".../v2/ota/batch/
        # check_update") that exists in the string table but is not an
        # endpoint.  The asm shows 18 real endpoints; all 18 are new in 3.24.3.
        self.assertEqual(len(added), 18)
        self.assertIn('/charging_hes_installer_svc/v2/ota/batch/check_update', added)
        # The brief expected get_device_last_exercise_log to be removed.  The
        # string is present in BOTH trees (a7320_requet_api.dart), so it is
        # neither added nor removed.  A URL that really disappeared:
        gone = '/power_service/v1/app/get_device_last_exercise_log'
        self.assertNotIn(gone, d['removed_endpoints'])
        self.assertNotIn(gone, d['added_endpoints'])
        self.assertIn('/power_service/v1/site/set_device_feature',
                      d['removed_endpoints'])
        md = diff_versions.render_markdown(d, '3.18.0', '3.24.3')
        for h in ('## Added endpoints', '## Removed endpoints',
                  '## Changed params', '## Added models', '## Removed models',
                  '## Changed fields'):
            self.assertIn(h, md)


@need(ROOT_NEW, ROOT_OLD)
class RenderTests(unittest.TestCase):
    def test_render_set_site_device_param(self):
        import render_pages
        inv = inventory_new()
        page = render_pages.render_endpoint(
            [r for r in inv['rows'] if r['url'] ==
             '/power_service/v1/site/set_site_device_param'],
            date='2026-10-19')
        self.assertTrue(page.startswith(
            '> Verified against: App 3.24.3 · Date: 2026-10-19'))
        self.assertIn('Confidence: string-only', page.splitlines()[0])
        self.assertIn('# set_site_device_param', page)
        self.assertIn('power_limit.limit_real', page)
        self.assertIn('http_request_repository_impl.dart @0x4355750', page)
        self.assertIn('<!-- TODO -->', page)
        self.assertEqual(render_pages.endpoint_path(
            '/power_service/v1/site/set_site_device_param'),
            'api/power_service/site/set_site_device_param.md')

    def test_variable_param_type_labelled_unverified(self):
        import render_pages
        rows = [r for r in inventory_new()['rows']
                if r['param_type_source'] == 'variable'
                and r['url'] == '/power_service/v1/site/set_site_device_param']
        self.assertTrue(rows)
        page = render_pages.render_endpoint(rows[:1], date='2026-10-19')
        self.assertIn('traced by heuristic', page)
        self.assertIn('verify', page)

    def test_removed_url_gets_page_with_note_and_one_page_per_url(self):
        import render_pages
        rows = inventory_new()['rows']
        removed = [r for r in rows if r['url'] == '/charging_disaster_prepared/clear']
        self.assertTrue(removed and all(r.get('removed_in') for r in removed))
        page = render_pages.render_endpoint(removed, date='2026-10-19')
        lines = page.splitlines()
        self.assertIn('Confidence: string-only', lines[0])
        self.assertEqual(lines[2], 'Removed in 3.24.3 \u2014 present in 3.18.0 only')
        self.assertIn('absent (removed)', page)
        # several senders of one URL share one page that lists all of them
        many = [r for r in rows if r['url'] == '/power_service/v1/site/get_site_device_param']
        self.assertGreater(len(many), 1)
        page = render_pages.render_endpoint(many, date='2026-10-19')
        self.assertEqual(page.count('# get_site_device_param'), 1)
        for r in many:
            if r['role'] == 'sender':
                self.assertIn('`%s` @%s' % (r['function'], r['addr']), page)
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            n_ep, _ = render_pages.render_all(
                {'rows': rows}, {'rows': []}, td, '2026-10-19')
        self.assertEqual(n_ep, len({r['url'] for r in rows}))

    def test_path_scheme_keeps_non_v1_versions(self):
        import render_pages
        ep = render_pages.endpoint_path
        self.assertEqual(ep('/power_service/v2/device/energy_options'),
                         'api/power_service/v2/device/energy_options.md')
        self.assertEqual(
            ep('/charging_hes_installer_svc/v2/app/third/platform/list'),
            'api/charging_hes_installer_svc/v2/app/third/platform/list.md')
        self.assertEqual(ep('/v2/anka/history/get_msg'),
                         'api/v2/anka/history/get_msg.md')
        self.assertEqual(ep('/power_service/v1/site/get_power_limit'),
                         'api/power_service/site/get_power_limit.md')
        urls = {r['url'] for r in inventory_new()['rows']}
        paths = [ep(u) for u in urls]
        self.assertEqual(len(paths), len(set(paths)))

    def test_noise_keys_filtered_from_request_table(self):
        import render_pages
        for k in ('fixedPrice:', 'a.value.isEmpty:', ' salePrice'):
            self.assertTrue(render_pages.is_noise_key(k), k)
        for k in ('url', 'method', 'useWebsocket', 'isAIotEnv'):
            self.assertTrue(render_pages.is_noise_key(k, envelope=True), k)
            self.assertFalse(render_pages.is_noise_key(k), k)
        base = dict(
            addr='0x1', callers=[], cmd=None, dart_file='x/y.dart', encrypted=True,
            encryption_note=None, envelope=['url', 'useWebsocket'], function='f',
            http_callees=['A::b'], param_data_is_json=False, param_type=None,
            params=['site_id', 'method', 'url', 'fixedPrice:'], role='sender',
            since='3.24.3', url='/s/v1/a/b', url_addr='0x2')
        page = render_pages.render_endpoint([base], date='2026-10-19')
        for k in ('site_id', 'method', 'url'):
            self.assertIn('| `%s` |' % k, page)
        self.assertNotIn('fixedPrice:', page)
        env_only = dict(base, params=[], envelope=['url', 'method', 'foo'])
        page = render_pages.render_endpoint([env_only], date='2026-10-19')
        self.assertIn('| `foo` |', page)
        self.assertNotIn('| `url` |', page)
        self.assertNotIn('| `method` |', page)

    def test_param_data_outer_keys_are_envelope(self):
        import render_pages
        row = dict(
            addr='0x1', callers=[], cmd=None, dart_file='x/y.dart', encrypted=True,
            encryption_note=None,
            envelope=['site_id', 'param_type', 'cmd', 'param_data', 'url'],
            function='f', http_callees=['A::b'], param_data_is_json=True,
            param_type=None, params=['display_type', 'power_limit.limit'],
            role='sender', since='3.24.3', url='/s/v1/a/b', url_addr='0x2')
        page = render_pages.render_endpoint([row], date='2026-10-19')
        outer = [l for l in page.splitlines() if 'outer keys:' in l]
        self.assertEqual(len(outer), 1)
        for k in ('site_id', 'param_type', 'cmd', 'param_data'):
            self.assertIn('`%s`' % k, outer[0])
        self.assertNotIn('`url`', outer[0])
        self.assertNotIn('display_type', outer[0])
        self.assertIn('| `display_type` |', page)
        self.assertIn('| `power_limit.limit` |', page)
        self.assertNotIn('| `site_id` |', page)

    def test_service_index_idempotent(self):
        import service_index, tempfile, shutil
        inv = inventory_new()
        with tempfile.TemporaryDirectory() as td:
            api = os.path.join(td, 'api')
            shutil.copytree(os.path.join(REPO, 'api'), api)
            first, _ = service_index.build(inv, api)
            for path, text in first.items():
                with open(path, 'w', encoding='utf-8') as fh:
                    fh.write(text)
            second, _ = service_index.build(inv, api)
            self.assertEqual(first, second)


SYNTH = """// lib: , url: package:x/y.dart

class A extends Object {

  _ send(/* No info */) {
    // ** addr: 0x100, size: 0x10
    // 0x101: r2 = 8
    //     0x101: mov             x2, #8
    // 0x102: r0 = AllocateArray()
    //     0x102: bl              #0x1  ; AllocateArrayStub
    // 0x103: r16 = "cmd"
    //     0x103: ldr             x16, [PP, #1]  ; [pp+1] "cmd"
    // 0x104: StoreField: r0->field_f = r16
    //     0x104: stur            w16, [x0, #0xf]
    // 0x105: r16 = 246
    //     0x105: mov             x16, #0xf6
    // 0x106: StoreField: r0->field_13 = r16
    //     0x106: %s
    // 0x107: r0 = Map._fromLiteral()
    //     0x107: bl              #0x2  ; [dart:core] Map::Map._fromLiteral
  }
}
"""


class SynthTests(unittest.TestCase):
    def _req(self, store):
        import tempfile
        import asmparse
        import endpoint_inventory
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, 'y.dart')
            with open(p, 'w') as fh:
                fh.write(SYNTH % store)
            fn = next(asmparse.iter_functions(p, 'y.dart'))
            return endpoint_inventory.extract_request(fn)

    def test_known_width_goes_through_smi(self):
        r = self._req('stur            w16, [x0, #0x13]')
        self.assertEqual((r['cmd'], r['cmd_raw']), (123, 246))
        self.assertIsNone(r['cmd_note'])

    def test_zero_register_store_is_cmd_zero(self):
        r = self._req_zr()
        self.assertEqual((r['cmd'], r['cmd_raw']), (0, 0))
        self.assertIsNone(r['cmd_note'])

    def _req_zr(self):
        import tempfile
        import asmparse
        import endpoint_inventory
        src = SYNTH.replace('r16 = 246', 'r16 = 7').replace(
            '    //     0x105: mov             x16, #0xf6\n', '    //     0x105: mov             x16, #7\n')
        src = src.replace('// 0x106: StoreField: r0->field_13 = r16',
                          '// 0x106: StoreField: r0->field_13 = rZR') % 'stur            wzr, [x0, #0x13]'
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, 'y.dart')
            with open(p, 'w') as fh:
                fh.write(src)
            fn = next(asmparse.iter_functions(p, 'y.dart'))
            return endpoint_inventory.extract_request(fn)

    def test_unknown_width_gives_null_cmd(self):
        r = self._req('str             x1, [x0, #0x13]')
        self.assertIsNone(r['cmd'])
        self.assertEqual(r['cmd_raw'], 246)
        self.assertEqual(r['cmd_note'], 'store width not found')


class OutputGuardTests(unittest.TestCase):
    def test_guard(self):
        import render_pages
        for bad in ('.', 'api', 'models', 'tools/outside', '..',
                    'tools/out/../..'):
            self.assertFalse(render_pages.out_allowed(
                os.path.join(REPO, bad), REPO), bad)
        for good in ('tools/out/x', 'tools/out'):
            self.assertTrue(render_pages.out_allowed(
                os.path.join(REPO, good), REPO), good)

    def test_cli_refuses(self):
        import render_pages

        def boom(*a, **k):
            raise AssertionError('must not render')

        saved = (render_pages.render_all, render_pages._write)
        render_pages.render_all = render_pages._write = boom
        try:
            self.assertEqual(render_pages.main(['--out', REPO]), 2)
            self.assertEqual(
                render_pages.main(['--out', os.path.join(REPO, 'api')]), 2)
            self.assertEqual(
                render_pages.main(['--out', os.path.join(REPO, 'models')]), 2)
        finally:
            render_pages.render_all, render_pages._write = saved


if __name__ == '__main__':
    unittest.main()
