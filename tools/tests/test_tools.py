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
        # truly absent from the 3.24.3 pool (no string at all): removed
        self.assertEqual(
            by_url['/smart_service/v1/app/anka/get_entry_config']['removed_in'],
            '3.24.3')
        # string still in the 3.24.3 pool, no asm load: pool-only, not removed
        self.assertNotIn('removed_in', by_url['/charging_disaster_prepared/clear'])
        self.assertEqual(
            by_url['/charging_disaster_prepared/clear']['reference'], 'pool-only')
        # set_device_feature is still used in 3.24.3 as a literal without leading
        # slash (ev_charge_command.dart), so it is not removed
        self.assertNotIn('removed_in', by_url[
            '/power_service/v1/site/set_device_feature'])

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
        self.assertIn('/smart_service/v1/app/anka/get_entry_config',
                      d['removed_endpoints'])
        self.assertNotIn('/power_service/v1/site/set_device_feature',
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
        removed = [r for r in rows
                   if r['url'] == '/smart_service/v1/app/anka/get_entry_config']
        self.assertTrue(removed and all(r.get('removed_in') for r in removed))
        pool = [r for r in rows if r['url'] == '/charging_disaster_prepared/clear']
        ppage = render_pages.render_endpoint(pool, date='2026-10-19')
        self.assertIn('string present in the object pool, no code reference found',
                      ppage)
        self.assertNotIn('Removed in', ppage)
        self.assertNotIn('absent (removed)', ppage)
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


class UrlLiteralTests(unittest.TestCase):
    """URL literals without a leading slash (synthetic, fast)."""

    def test_noslash_literals_found_and_normalised(self):
        import asmparse
        for lit in ('devicecontrol/v1/app/record_device_command',
                    'generator/v1/app/get_standby_exercise_plan',
                    'power_service/v1/app/order/get_charging_order_list',
                    'foo_bar/v2/x/y'):
            self.assertEqual(asmparse.url_literal('r16 = "%s"' % lit),
                             ('r16', '/' + lit))
        self.assertEqual(asmparse.url_literal('r0 = "/power_service/v1/x/y"'),
                         ('r0', '/power_service/v1/x/y'))

    def test_dart_package_paths_are_not_urls(self):
        import asmparse
        for lit in ('charging_platform/src/foo/bar.dart',
                    'charging_beginning/ui/page/x.dart',
                    'charging_uikit/widget/y.dart'):
            self.assertIsNone(asmparse.url_literal('r16 = "%s"' % lit))
            self.assertIsNone(asmparse.URL_PRECHECK_RE.search('= "%s"' % lit))

    def test_generic_two_segment_literal_rejected_by_inventory_filter(self):
        import asmparse
        import endpoint_inventory
        # the literal regex accepts a known prefix; the inventory filter rejects
        # a bare two-segment shape for url_provider rows (see tools/README.md)
        self.assertEqual(asmparse.url_literal('r0 = "app/foo"'), ('r0', '/app/foo'))
        self.assertFalse(endpoint_inventory.url_ok('/app/foo', 'url_provider', set()))
        self.assertTrue(endpoint_inventory.url_ok(
            '/app/rfid/get_cards', 'url_provider', set()))


@need(ROOT_NEW, ROOT_OLD)
class NoSlashInventoryTests(unittest.TestCase):
    def test_noslash_urls_in_inventory(self):
        by_url = {}
        for r in inventory_new()['rows']:
            by_url.setdefault(r['url'], []).append(r)
        for u in ('/devicecontrol/v1/app/record_device_command',
                  '/generator/v1/app/get_standby_exercise_plan',
                  '/power_service/v1/app/order/get_charging_order_list'):
            self.assertIn(u, by_url)
        self.assertFalse([u for u in by_url if u.startswith('/charging_platform')
                          or u.startswith('/charging_beginning')
                          or u.startswith('/charging_uikit')])
        self.assertFalse([u for u in by_url if u.startswith('//')])


class ServiceIndexOrphanTests(unittest.TestCase):
    def test_page_without_inventory_row_keeps_its_row(self):
        import service_index
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            os.makedirs(os.path.join(td, 'passport'))
            with open(os.path.join(td, 'passport', 'external_login.md'), 'w') as fh:
                fh.write('> Verified against: App 3.24.3 · Date: x · Confidence: '
                         'asm-traced · Owner page: this page\n\n# external_login\n\n'
                         '## Purpose\n\nA hand-written purpose.\n')
            out, _ = service_index.build({'rows': []}, td)
            txt = out[os.path.join(td, 'passport', 'README.md')]
            self.assertIn('[`/passport/external_login`](external_login.md) | '
                          'A hand-written purpose.', txt)
            self.assertIn('not in `data/endpoints.json`', txt)

    def test_skeleton_orphan_count_exclusion_and_readme_skipped(self):
        import service_index
        import tempfile
        skel = ('> Verified against: App 3.24.3 · Date: x · Confidence: string-only '
                '· Owner page: this page\n\n# t\n\n' + '<!-- TODO -->\n' * 6)
        with tempfile.TemporaryDirectory() as td:
            os.makedirs(os.path.join(td, 'passport'))
            for n, body in (('t.md', skel), ('README.md', 'not a page\n')):
                with open(os.path.join(td, 'passport', n), 'w') as fh:
                    fh.write(body)
            out, summary = service_index.build({'rows': []}, td)
            txt = out[os.path.join(td, 'passport', 'README.md')]
            self.assertIn('[`/passport/t`](t.md) | TODO | - | skeleton, not in '
                          '`data/endpoints.json`', txt)
            self.assertNotIn('README.md](README.md)', txt)
            # orphans are listed but not counted as inventory URLs
            self.assertEqual(summary, [('passport', 0, 0)])

class ServiceIndexPagesColumnTests(unittest.TestCase):
    def test_pages_column_counts_pages_on_disk_including_orphans(self):
        import service_index
        import tempfile
        page = ('> Verified against: App 3.24.3 · Date: x · Confidence: asm-traced '
                '· Owner page: this page\n\n# t\n\n## Purpose\n\nx.\n')
        rows = {'rows': [{'url': '/passport/a', 'reference': 'code'}]}
        with tempfile.TemporaryDirectory() as td:
            os.makedirs(os.path.join(td, 'passport'))
            for n in ('a.md', 'orphan.md'):
                with open(os.path.join(td, 'passport', n), 'w') as fh:
                    fh.write(page)
            out, _ = service_index.build(rows, td)
            txt = out[os.path.join(td, 'README.md')]
            self.assertIn('| `passport/` | 2 | [passport/README.md]', txt)
            self.assertIn('1 distinct URLs', txt)


PAGE_OWNER = ('> Verified against: App 3.24.3 · Date: x · Confidence: asm-traced '
              '· Owner page: this page\n\n# t\n\n## Purpose\n\nA real purpose.\n')
PAGE_SKEL = ('> Verified against: App 3.24.3 · Date: x · Confidence: string-only '
             '· Owner page: this page\n\n# t\n\n' + '<!-- TODO -->\n' * 6)


class ServiceIndexStatusAndGuardTests(unittest.TestCase):
    def _tree(self, td, pages):
        os.makedirs(os.path.join(td, 'api', 's'))
        for n, body in pages.items():
            with open(os.path.join(td, 'api', 's', n), 'w') as fh:
                fh.write(body)
        inv = {'rows': [
            {'url': '/s/own'}, {'url': '/s/skel'},
            {'url': '/s/pool', 'reference': 'pool-only'},
            {'url': '/s/gone', 'removed_in': '3.24.3'}]}
        import json
        with open(os.path.join(td, 'inv.json'), 'w') as fh:
            json.dump(inv, fh)
        return ['--endpoints', os.path.join(td, 'inv.json'), '--api', os.path.join(td, 'api')]

    def test_four_status_values_and_counts(self):
        import service_index
        import tempfile
        import json
        pages = {'own.md': PAGE_OWNER, 'skel.md': PAGE_SKEL,
                 'pool.md': PAGE_SKEL, 'gone.md': PAGE_OWNER}
        with tempfile.TemporaryDirectory() as td:
            os.makedirs(os.path.join(td, 'api', 's'))
            for n, body in pages.items():
                open(os.path.join(td, 'api', 's', n), 'w').write(body)
            inv = {'rows': [
                {'url': '/s/own'}, {'url': '/s/skel'},
                {'url': '/s/pool', 'reference': 'pool-only'},
                {'url': '/s/gone', 'removed_in': '3.24.3'}]}
            out, _ = service_index.build(inv, os.path.join(td, 'api'))
            txt = out[os.path.join(td, 'api', 's', 'README.md')]
            for url, st in (('own', 'owner'), ('skel', 'skeleton'),
                            ('pool', 'pool-only'), ('gone', 'removed')):
                row = [l for l in txt.splitlines() if '`/s/%s`' % url in l][0]
                self.assertTrue(row.rstrip().endswith('| %s |' % st), row)
            root = out[os.path.join(td, 'api', 'README.md')]
            self.assertIn('`owner` 1, `skeleton` 1, `pool-only` 1, `removed` 1', root)

    def test_refuses_service_readme_with_foreign_prose_and_no_marker(self):
        import service_index
        import tempfile
        import io
        import contextlib
        with tempfile.TemporaryDirectory() as td:
            args = self._tree(td, {'own.md': PAGE_OWNER, 'skel.md': PAGE_SKEL,
                                   'pool.md': PAGE_SKEL, 'gone.md': PAGE_OWNER})
            self.assertEqual(service_index.main(args), 0)
            readme = os.path.join(td, 'api', 's', 'README.md')
            first = open(readme).read()
            self.assertEqual(service_index.main(args), 0)  # idempotent
            self.assertEqual(open(readme).read(), first)
            with open(readme, 'a') as fh:
                fh.write('\n## Hand-written group\n\nExtra prose.\n')
            err = io.StringIO()
            with contextlib.redirect_stderr(err), contextlib.redirect_stdout(io.StringIO()):
                code = service_index.main(args)
            self.assertNotEqual(code, 0)
            self.assertIn(readme, err.getvalue())
            self.assertIn('Extra prose.', open(readme).read())
            # with the marker the tail survives and the run succeeds
            txt = open(readme).read().replace(
                '## Hand-written group', service_index.KEEP_MARKER + '\n## Hand-written group')
            open(readme, 'w').write(txt)
            self.assertEqual(service_index.main(args), 0)
            self.assertIn('Extra prose.', open(readme).read())

    def test_refusal_writes_nothing(self):
        import service_index
        import tempfile
        import io
        import contextlib
        with tempfile.TemporaryDirectory() as td:
            args = self._tree(td, {'own.md': PAGE_OWNER, 'skel.md': PAGE_SKEL,
                                   'pool.md': PAGE_SKEL, 'gone.md': PAGE_OWNER})
            readme = os.path.join(td, 'api', 's', 'README.md')
            open(readme, 'w').write('> h\n\n# s\n\nhand prose\n')
            with contextlib.redirect_stderr(io.StringIO()), contextlib.redirect_stdout(io.StringIO()):
                self.assertNotEqual(service_index.main(args), 0)
            self.assertFalse(os.path.exists(os.path.join(td, 'api', 'README.md')))

    def test_ambiguous_counts_come_from_inventory(self):
        import service_index
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            os.makedirs(os.path.join(td, 'smart_service'))
            open(os.path.join(td, 'smart_service', 'a.md'), 'w').write(PAGE_OWNER)
            inv = {'rows': [{'url': '/smart_service/v1/a'}]}
            out, _ = service_index.build(inv, td)
            txt = out[os.path.join(td, 'README.md')]
            self.assertIn('real service: 1 endpoint', txt)
            self.assertNotIn('real service: 13 endpoints', txt)


class ReadmeStatsTests(unittest.TestCase):
    def test_real_repo_numbers_come_from_data(self):
        import json
        import readme_stats
        st = readme_stats.compute(REPO)
        with open(os.path.join(REPO, 'data', 'endpoints.json')) as fh:
            urls = {r['url'] for r in json.load(fh)['rows']}
        self.assertEqual(st['urls'], len(urls))
        self.assertEqual(st['skeleton'] + st['hand_written'], st['url_pages'] + st['orphan_pages'])
        self.assertEqual(st['url_pages'], len(urls))
        with open(os.path.join(REPO, 'data', 'endpoints.json')) as fh:
            new = {r['url'] for r in json.load(fh)['rows'] if r.get('since') == '3.24.3'}
        self.assertEqual(st['new_in_3243'], len(new))
        self.assertIn('first seen in 3.24.3: %d' % len(new), readme_stats.render(st))
        self.assertEqual(st['audit_wrong'] <= st['audit_rows'], True)
        self.assertEqual(st['mqtt_pages'],
                         len([f for f in os.listdir(os.path.join(REPO, 'mqtt'))
                              if f.endswith('.md') and f != 'README.md']))

    def test_audit_rows_equal_declared_totals(self):
        import re
        import readme_stats
        st = readme_stats.compute(REPO)
        rows = wrong = 0
        d = os.path.join(REPO, 'docs', 'audit')
        for f in os.listdir(d):
            txt = open(os.path.join(d, f), encoding='utf-8').read()
            m = re.search(r'^Rows: (\d+)\.(.*)$', txt, re.M)
            if m:
                rows += int(m.group(1))
                w = re.search(r'WRONG (\d+)', m.group(2))
                wrong += int(w.group(1)) if w else 0
        self.assertEqual((st['audit_rows'], st['audit_wrong']), (rows, wrong))

    def test_block_replacement_is_idempotent(self):
        import readme_stats
        st = readme_stats.compute(REPO)
        base = 'a\n' + readme_stats.BEGIN + '\nold\n' + readme_stats.END + '\nz\n'
        once = readme_stats.replace_block(base, readme_stats.render(st))
        twice = readme_stats.replace_block(once, readme_stats.render(st))
        self.assertEqual(once, twice)
        self.assertIn('data snapshot 2026-10-19, generated by', once)
        self.assertIn('tools/readme_stats.py', once)
        self.assertNotIn('old\n', once)

    def test_committed_readme_and_structure_equal_fresh_run(self):
        import readme_stats
        st = readme_stats.compute(REPO)
        readme = open(os.path.join(REPO, 'README.md'), encoding='utf-8').read()
        self.assertEqual(readme_stats.replace_block(readme, readme_stats.render(st)), readme)
        structure = open(os.path.join(REPO, 'docs', 'STRUCTURE.md'), encoding='utf-8').read()
        self.assertEqual(readme_stats.migration_statuses(REPO, structure), structure)

    def test_cli_run_twice_is_idempotent(self):
        import readme_stats
        import shutil
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            dst = os.path.join(td, 'repo')
            shutil.copytree(REPO, dst, ignore=shutil.ignore_patterns(
                '.git', '.superpowers', 'out', '__pycache__', 'easter_eggs'))
            import io
            import contextlib
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(readme_stats.main(['--repo', dst]), 0)
            snap = {f: open(os.path.join(dst, f), encoding='utf-8').read()
                    for f in ('README.md', 'docs/STRUCTURE.md')}
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                self.assertEqual(readme_stats.main(['--repo', dst]), 0)
            self.assertIn('changed: none', buf.getvalue())
            for f, v in snap.items():
                self.assertEqual(open(os.path.join(dst, f), encoding='utf-8').read(), v)

    def test_done_rows_with_skeleton_owner_pages_are_labelled(self):
        import readme_stats
        import tempfile
        skel = PAGE_SKEL
        text = ('## Migration map\n\n| Old path | New | What | Status |\n|---|---|---|---|\n'
                '| `A.md` | `api/x/s.md` | t | pending |\n'
                '| `B.md` | `api/x/o.md` | t | pending |\n'
                '| `C.md` | `api/x/s.md`, `api/x/o.md` | t | pending |\n')
        with tempfile.TemporaryDirectory() as td:
            os.makedirs(os.path.join(td, 'api', 'x'))
            open(os.path.join(td, 'api', 'x', 's.md'), 'w').write(skel)
            open(os.path.join(td, 'api', 'x', 'o.md'), 'w').write(PAGE_OWNER)
            out = readme_stats.migration_statuses(td, text)
            st = {l.split('|')[1].strip(' `'): l.rstrip(' |').rsplit('|', 1)[1].strip()
                  for l in out.splitlines() if l.startswith('| `')}
            self.assertEqual(st, {'A.md': 'done (skeleton pages)', 'B.md': 'done',
                                  'C.md': 'done'})
            self.assertEqual(readme_stats.migration_statuses(td, out), out)

    def test_no_hand_typed_row_or_line_counts_in_structure(self):
        import re
        txt = open(os.path.join(REPO, 'docs', 'STRUCTURE.md'), encoding='utf-8').read()
        self.assertIsNone(re.search(r'\(\d+ rows', txt))
        self.assertNotIn('(2402 lines)', txt)
        self.assertNotIn('1-2402', txt)

    def test_missing_markers_raise(self):
        import readme_stats
        with self.assertRaises(ValueError):
            readme_stats.replace_block('no markers', 'x')

    def test_migration_status_derived_from_disk(self):
        import readme_stats
        import tempfile
        table = ('| Old path | New owner location(s) | What moves there | Status |\n'
                 '|---|---|---|---|\n'
                 '| `A.md` | `api/x/one.md` | t | pending |\n'
                 '| `B.md` | `api/x/one.md`, `api/x/two.md` | t | pending |\n'
                 '| `C.md` | `api/y/three.md` | t | done |\n'
                 '| `D.md` | `devices/<pn>.md` | t | pending |\n'
                 '| `E.md` | `E.md` (kept) | t | pending |\n'
                 '| `F.md` | `F.md` (rebuilt in place) and `api/x/one.md` | t | pending |\n'
                 '| `G.md` | `api/x/<endpoint>.md` | t | pending |\n'
                 '| `H.md` | `devices/<pn>.md`, `api/x/one.md` | t | pending |\n'
                 '| `I.md` | `api/x/one.md`, `api/x/` | t | pending |\n'
                 '| `J.md` | `flows/<n>.md` | t | pending |\n')
        text = '## Migration map\n\n' + table + '\n## Notes\n'
        with tempfile.TemporaryDirectory() as td:
            os.makedirs(os.path.join(td, 'api', 'x'))
            os.makedirs(os.path.join(td, 'devices'))
            os.makedirs(os.path.join(td, 'flows'))
            open(os.path.join(td, 'flows', 'README.md'), 'w').close()
            open(os.path.join(td, 'api', 'x', 'one.md'), 'w').close()
            open(os.path.join(td, 'devices', 'README.md'), 'w').close()
            open(os.path.join(td, 'devices', 'a1.md'), 'w').close()
            out = readme_stats.migration_statuses(td, text)
            st = {l.split('|')[1].strip(' `'): l.rstrip(' |').rsplit('|', 1)[1].strip()
                  for l in out.splitlines() if l.startswith('| `')}
            self.assertEqual(st, {'A.md': 'done', 'B.md': 'partial', 'C.md': 'pending',
                                  'D.md': 'partial', 'E.md': 'kept', 'F.md': 'partial',
                                  'G.md': 'done', 'H.md': 'partial', 'I.md': 'partial', 'J.md': 'pending'})
            self.assertEqual(readme_stats.migration_statuses(td, out), out)


class SyntheticToolTests(unittest.TestCase):
    """Tests on tiny synthetic trees; no Blutter output needed."""

    ASM = (
        'class A {\n'
        '  static _ f(/* No info */) {\n'
        '    // ** addr: 0x100, size: 0x10\n'
        '    // 0x104: r16 = "path"\n'
        '    // 0x108: r16 = %s\n'
        '    // 0x10c: r0 = f()\n'
        '  }\n'
        '  static _ g(/* No info */) {\n'
        '    // 0x200: r2 = 4\n'
        '  }\n'
        '}\n')

    def _tree(self, td, name, lit):
        d = os.path.join(td, name)
        os.makedirs(d)
        with open(os.path.join(d, 'x.dart'), 'w') as fh:
            fh.write(self.ASM % lit)
        return d

    def test_cmp_since_same_diff_and_branch_blind(self):
        import tempfile
        import cmp_since
        with tempfile.TemporaryDirectory() as td:
            old = self._tree(td, 'old', '"a"')
            same = self._tree(td, 'same', '"a"')
            diff = self._tree(td, 'diff', '"b"')
            r = cmp_since.compare(old + '/x.dart', same + '/x.dart')
            self.assertEqual(r['f'][0], 'same')
            self.assertEqual(r['g'][0], 'same')
            r = cmp_since.compare(old + '/x.dart', diff + '/x.dart', ['f', 'g', 'h'])
            self.assertEqual(r['f'][0], 'DIFF')
            self.assertEqual(r['f'][1], ['"path"', '"a"'])
            self.assertEqual(r['g'][0], 'same')
            self.assertEqual(r['h'][0], 'unknown')
            with self.assertRaises(FileNotFoundError):
                cmp_since.compare(old + '/nope.dart', same + '/x.dart')

    def test_keep_tail_preserved_once_and_absent_marker_unchanged(self):
        import tempfile
        import service_index
        with tempfile.TemporaryDirectory() as td:
            path = os.path.join(td, 'README.md')
            tail = service_index.KEEP_MARKER + '\n\n## Hand-written\n\ntext\n'
            with open(path, 'w') as fh:
                fh.write('old generated\n\n' + tail)
            once = service_index.keep_tail(path, 'new generated\n')
            self.assertEqual(once, 'new generated\n\n' + tail)
            with open(path, 'w') as fh:
                fh.write(once)
            twice = service_index.keep_tail(path, 'new generated\n')
            self.assertEqual(twice.count(service_index.KEEP_MARKER), 1)
            self.assertEqual(twice, once)
            with open(path, 'w') as fh:
                fh.write('no marker here\n')
            self.assertEqual(service_index.keep_tail(path, 'gen\n'), 'gen\n')
            self.assertEqual(service_index.keep_tail(os.path.join(td, 'none.md'), 'gen\n'), 'gen\n')

    def test_check_citations_address_and_key(self):
        import tempfile
        import check_citations
        with tempfile.TemporaryDirectory() as td:
            root = self._tree(td, 'asm', '"k"')
            page = os.path.join(td, 'p.md')
            with open(page, 'w') as fh:
                fh.write('Sender `x.dart @0x100` and `@0x999`.\n\n'
                         '| field | type | req | ex | source |\n|---|---|---|---|---|\n'
                         '| `k` | s | y | e | `x.dart @0x108` |\n'
                         '| `zz` | s | y | e | `x.dart @0x108` |\n')
            m, b, rows = check_citations.check_page(check_citations.Tree(root), page)
            self.assertEqual([x[2] for x in m], ['0x999'])
            self.assertEqual(rows, 2)
            self.assertEqual([x[2] for x in b], ['zz'])


class LintDocsTests(unittest.TestCase):
    HDR = ('> Verified against: App 3.24.3 · Date: 2026-10-19 · '
           'Confidence: asm-traced · Owner page: this page\n\n')
    ENDPOINT = ['Purpose', 'Upstream name', 'Method+URL', 'Encrypted?', 'Request',
                '`param_type`/`cmd`', 'Response model (link)', 'Response',
                'Example request/response', 'Errors seen', 'Callers in app',
                'Since/changed', 'Known unknowns', 'Device-tested by']

    def lint(self, files, rules=None, templates=True):
        import tempfile
        import lint_docs
        with tempfile.TemporaryDirectory() as root:
            if templates:
                body = '# Template: endpoint page\n\n' + ''.join(
                    '## %s\n\ntext\n\n' % h for h in self.ENDPOINT) + '# example\n'
                files = dict(files)
                files['docs/templates/endpoint.md'] = body
            for rel, text in files.items():
                path = os.path.join(root, rel)
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, 'w', encoding='utf-8') as fh:
                    fh.write(text)
            return lint_docs.lint_repo(root, rules)

    def rules(self, found):
        return sorted({(f.rule, f.severity) for f in found})

    def endpoint(self, extra='', sections=None):
        out = self.HDR + '# x\n\n'
        for h in sections or self.ENDPOINT:
            out += '## %s\n\n%s\n\n' % (h, extra if h == 'Request' else 'text')
        return out

    def test_clean_endpoint_page(self):
        self.assertEqual(self.lint({'api/s/x.md': self.endpoint()}), [])

    def test_header_missing_and_bad_tag(self):
        r = self.lint({'api/s/x.md': '# x\n', 'models/y.md': self.HDR.replace(
            'asm-traced', 'probably') + '# y\n'}, ['header'])
        self.assertEqual([f.path for f in r], ['api/s/x.md', 'models/y.md'])

    def test_sections_order(self):
        sec = list(self.ENDPOINT)
        sec[0], sec[1] = sec[1], sec[0]
        r = self.lint({'api/s/x.md': self.endpoint(sections=sec)}, ['sections'])
        self.assertEqual(self.rules(r), [('sections', 'error')])

    def test_uncited_int(self):
        tbl = '| a | b |\n|---|---|\n| `x` | 17 |\n| `y` | 17 @0x1234 |\n| `z` | 17 upstream-confirmed |\n| `w` | 2024-10-19, 3.24.3, a17c5, 1200W, 1 |\n'
        r = self.lint({'api/s/x.md': self.endpoint(tbl)}, ['uncited-int'])
        self.assertEqual([f.line for f in r if f.rule == 'uncited-int'],
                         [r[0].line])
        self.assertIn('| `x` |', open_line(r[0], self))

    def test_uncited_int_exempt_audit(self):
        tbl = self.HDR + '| a |\n|---|\n| 17 |\n'
        self.assertEqual(self.lint({'docs/audit/a.md': tbl}, ['uncited-int']), [])

    def test_tag_overclaim_and_traced_sequence(self):
        txt = 'This is presumably set (asm-traced).\n\nPlain step [T] inferred here.\n'
        r = self.lint({'api/s/x.md': self.endpoint(txt)},
                      ['tag-overclaim', 'inferred-as-traced-sequence'])
        self.assertEqual(self.rules(r), [('inferred-as-traced-sequence', 'error'),
                                         ('tag-overclaim', 'error')])
        ok = 'Likely (string-only). Unlikely is fine (asm-traced).\n'
        self.assertEqual(self.lint({'api/s/x.md': self.endpoint(ok)},
                                   ['tag-overclaim']), [])

    def test_todo_purpose_is_warning(self):
        sec = self.endpoint().replace('## Purpose\n\ntext', '## Purpose\n\n<!-- TODO -->')
        r = self.lint({'api/svc/x.md': sec}, ['todo-purpose'])
        self.assertEqual(self.rules(r), [('todo-purpose', 'warning')])

    def test_links(self):
        txt = ('[ok](y.md) [bad](nope.md) [anc](y.md#hello-world) [badanc](y.md#zzz) '
               '`[code](nope2.md)` [self](#request) [web](https://x.y/z)\n')
        r = self.lint({'api/s/x.md': self.endpoint(txt),
                       'api/s/y.md': self.HDR + '# Hello World\n'}, ['links'])
        self.assertEqual(len(r), 2)
        self.assertTrue(all(f.rule == 'links' for f in r))

    def test_length(self):
        big = self.HDR + '# x\n' + 'line\n' * 160
        huge = self.HDR + '# x\n' + 'line\n' * 610
        toc = self.HDR + '# x\n\n## Contents\n' + 'line\n' * 160
        r = self.lint({'reference/a.md': big, 'reference/b.md': huge,
                       'reference/c.md': toc}, ['length'])
        self.assertEqual(sorted((f.path, f.severity) for f in r),
                         [('reference/a.md', 'warning'), ('reference/b.md', 'error')])

    def test_dup_payload(self):
        blk = '```json\n{"a": 1,\n "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb": 2}\n```\n'
        flat = '```json\n{"a":1,"bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb":2}\n```\n'
        r = self.lint({'reference/a.md': self.HDR + blk, 'reference/b.md': self.HDR + flat,
                       'docs/templates/t.md': blk}, ['dup-payload'])
        self.assertEqual(sorted(f.path for f in r), ['reference/a.md', 'reference/b.md'])
        self.assertEqual({f.rule for f in r}, {'dup-payload'})

    def test_secret(self):
        h = 'a' * 32
        r = self.lint({'reference/a.md': self.HDR + h + '\n',
                       'docs/audit/a.md': self.HDR + h + '\n',
                       'reference/b.md': self.HDR + 'a' * 31 + '\n'}, ['secret'])
        self.assertEqual([f.path for f in r], ['reference/a.md'])

    def test_owner_cmd(self):
        txt = 'x "cmd": 17 and cmd = 18 and cmd 19 and `cmd` 20\n'
        r = self.lint({'reference/a.md': self.HDR + txt,
                       'api/param_types.md': self.HDR + txt}, ['owner-cmd'])
        self.assertEqual({f.path for f in r}, {'reference/a.md'})
        self.assertEqual(self.lint({'reference/a.md': self.HDR + 'the `cmd` value, see x\n'}, ['owner-cmd']), [])

    def test_slug_and_legacy_skip(self):
        import lint_docs
        self.assertEqual(lint_docs.slug('`param_type`/`cmd` (x)'), 'param_typecmd-x')
        legacy = '| `old.md` | `new.md` | x | pending |\n'
        mig = '## Migration map\n\n| Old path | New | What | Status |\n|---|---|---|---|\n' + legacy
        r = self.lint({'docs/STRUCTURE.md': self.HDR + mig, 'old.md': '# old\n'}, ['header'])
        self.assertEqual(r, [])

    def test_legacy_page_is_link_checked(self):
        legacy = '| `old.md` | `new.md` | x | pending |\n'
        mig = '## Migration map\n\n| Old path | New | What | Status |\n|---|---|---|---|\n' + legacy
        files = {'docs/STRUCTURE.md': self.HDR + mig, 'old.md': '# old\n[bad](nope.md) [ok](new.md)\n',
                 'new.md': '# new\n'}
        r = self.lint(files, ['links'])
        self.assertEqual([(f.path, f.rule) for f in r], [('old.md', 'links')])
        self.assertEqual(self.lint(files, ['header']), [])


class LintDocsRound1Tests(LintDocsTests):
    """Exemptions and CLI of lint_docs; inherits the helpers (its own tests run again, cheap)."""

    def ui(self, rows, pre='', hdr=None):
        body = (hdr or self.HDR) + '# x\n\n' + pre + '| k | v |\n|---|---|\n' + rows
        return self.lint({'reference/a.md': body}, ['uncited-int'])

    def test_year_regex_only_real_dates(self):
        self.assertEqual(len(self.ui('| max | 2000 |\n')), 1)
        self.assertEqual(len(self.ui('| max | 2048 |\n')), 1)
        self.assertEqual(len(self.ui('| Date: 2026-10-19 | x |\n')), 0)

    def test_year_not_exempt_with_unit(self):
        r = self.ui('| max | 2000 W |\n')
        self.assertEqual(len(r), 1)

    def test_tag_section_exemption_only_untagged(self):
        for tag, n in (('untagged by design', 0), ('string-only', 1),
                       ('upstream-confirmed', 1), ('device-tested', 1)):
            self.assertEqual(len(self.ui('| a | 17 |\n', pre='Tag: %s\n\n' % tag)), n, tag)

    def test_untagged_sections_by_heading(self):
        body = self.HDR + '# x\n\n## Known unknowns\n\n| a | b |\n|--|--|\n| 1 | 17 |\n'
        self.assertEqual(self.lint({'reference/a.md': body}, ['uncited-int']), [])

    def test_tally_columns(self):
        ok = '| name | calls |\n|---|---|\n| `x` | 17 |\n'
        bad = '| name | calls |\n|---|---|\n| 17 | 3 |\n'
        ids = '| param_type | other |\n|---|---|\n| 17 | text |\n'
        notcount = '| name | value |\n|---|---|\n| `x` | 17 |\n'
        for tbl, n in ((ok, 0), (bad, 1), (ids, 0), (notcount, 1)):
            self.assertEqual(len(self.lint({'reference/a.md': self.HDR + tbl}, ['uncited-int'])), n, tbl)

    def test_step_and_count_noun(self):
        self.assertEqual(len(self.ui('| see step 10 | 38 sends |\n')), 0)
        self.assertEqual(len(self.ui('| 38 cloud sends | x |\n')), 1)

    def test_header_variants(self):
        import lint_docs as L
        base = '> Verified against: App 3.24.3 · Date: 2026-10-19 · '
        good = [base + 'Confidence: asm-traced · Page type: audit table · Owner page: this page',
                base + 'Confidence: string-only (note) · Owner page: x · Page type: feature',
                base + 'Page type: guidance (no API facts) · Owner page: this page']
        bad = [base + 'Confidence: guess · Owner page: x', base + 'Owner page: x',
               base + 'Confidence: asm-traced', base + 'Confidence: asm-traced · Owner page: x · Extra: y']
        for g in good:
            self.assertTrue(L.valid_header(g), g)
        for b in bad:
            self.assertFalse(L.valid_header(b), b)

    def test_scope_limit(self):
        ok = 'The element is not traced (asm-traced elsewhere). Also (analogy, not traced) asm-traced.\n'
        self.assertEqual(self.lint({'reference/a.md': self.HDR + ok}, ['tag-overclaim']), [])
        sec = self.HDR + '## S\n\nTag: asm-traced\n\nthis is likely.\n'
        self.assertEqual(len(self.lint({'reference/a.md': sec}, ['tag-overclaim'])), 1)

    def test_dup_payload_exemptions(self):
        env = '```json\n{"code": 0, "msg": "success", "data": {}}\n```\n'
        shape = '```json\n{"vehicle_id": "<vehicle id>", "other_key_padding": 1}\n```\n'
        ex = lambda blk: self.endpoint().replace(
            '## Example request/response\n\ntext', '## Example request/response\n\n' + blk)
        r = self.lint({'api/s/a.md': ex(env), 'api/s/b.md': ex(env)}, ['dup-payload'])
        self.assertEqual(r, [])
        r = self.lint({'api/s/a.md': ex(shape), 'api/s/b.md': ex(shape)}, ['dup-payload'])
        self.assertEqual(r, [])
        r = self.lint({'api/s/a.md': ex(shape), 'reference/b.md': self.HDR + shape}, ['dup-payload'])
        self.assertEqual(len(r), 2)

    def test_secret_keyword_adjacent(self):
        h = 'a' * 64
        self.assertEqual(self.lint({'reference/a.md': self.HDR + 'XAPK sha256 %s\n' % h}, ['secret']), [])
        far = self.HDR + 'sha256 is mentioned here ' + 'x' * 80 + ' %s\n' % h
        self.assertEqual(len(self.lint({'reference/a.md': far}, ['secret'])), 1)
        self.assertEqual(len(self.lint({'reference/a.md': self.HDR + 'sha256 %s\n' % ('a' * 50)}, ['secret'])), 1)

    def test_owner_cmd_exemptions(self):
        txt = 'x "cmd": 17\n'
        r = self.lint({'METHODOLOGY.md': self.HDR + txt + 'y cmd 5 <!-- lint: owner-cmd example -->\n',
                       'docs/plan.md': '# plan\n' + txt}, ['owner-cmd'])
        self.assertEqual([(f.path, f.line) for f in r], [('METHODOLOGY.md', 3)])

    def test_page_type_header_is_fact_page(self):
        feat = self.HDR.replace('Confidence: asm-traced', 'Page type: feature') + '| a | 17 |\n'
        self.assertEqual(len(self.lint({'reference/a.md': feat}, ['uncited-int'])), 1)
        guide = self.HDR.replace('Confidence: asm-traced', 'Page type: guidance (no API facts)') + '| a | 17 |\n'
        self.assertEqual(self.lint({'reference/a.md': guide}, ['uncited-int']), [])

    def test_audit_length_warning(self):
        big = self.HDR + 'line\n' * 610
        r = self.lint({'docs/audit/a.md': big}, ['length'])
        self.assertEqual([(f.rule, f.severity) for f in r], [('length', 'warning')])

    def test_strict_hedge_on_cited_rows(self):
        import lint_docs
        row = '| `k` | presumably x | `f.dart @0x1234` |\n'
        body = self.endpoint('| a | b | c |\n|---|---|---|\n' + row)
        self.assertEqual(self.lint({'api/s/x.md': body}, ['tag-overclaim']), [])
        import tempfile
        with tempfile.TemporaryDirectory() as root:
            os.makedirs(os.path.join(root, 'api/s'))
            with open(os.path.join(root, 'api/s/x.md'), 'w') as fh:
                fh.write(body)
            r = lint_docs.lint_repo(root, ['tag-overclaim'], strict=True)
        self.assertEqual([(f.rule, f.severity) for f in r], [('tag-overclaim', 'warning')])

    def run_main(self, args, files):
        import contextlib
        import io
        import tempfile
        import lint_docs
        with tempfile.TemporaryDirectory() as root:
            for rel, text in files.items():
                path = os.path.join(root, rel)
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, 'w', encoding='utf-8') as fh:
                    fh.write(text)
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                code = lint_docs.main(['--root', root] + args)
        return code, out.getvalue()

    def test_cli(self):
        import json
        files = {'reference/a.md': '# no header\n', 'reference/b.md': self.HDR + '# b\n\n## Purpose\n\n<!-- TODO -->\n'}
        code, out = self.run_main(['--summary'], files)
        self.assertEqual(code, 1)
        self.assertIn('header', out)
        self.assertRegex(out, r'TOTAL\s+errors\s+1')
        code, out = self.run_main(['--json', '--rule', 'header'], files)
        data = json.loads(out)
        self.assertEqual([d['path'] for d in data], ['reference/a.md'])
        code, out = self.run_main(['--rule', 'links'], files)
        self.assertEqual(code, 0)
        code, out = self.run_main(['--warn-only'], files)
        self.assertEqual(code, 0)
        self.assertNotIn('ERROR', out)
        code, out = self.run_main(['--rule', 'nope'], files)
        self.assertEqual(code, 2)
        code, out = self.run_main(['--strict', '--summary'], files)
        self.assertEqual(code, 1)


def open_line(finding, case):
    return finding.text


if __name__ == '__main__':
    unittest.main()
