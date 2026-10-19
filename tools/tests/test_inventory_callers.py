"""Caller resolution for url_provider rows (Task 3.1c).

Run from the repo root:  python3 -I -m unittest discover -s tools/tests -t .
Synthetic asm fixtures cover the walk; one test reads the real asm and skips
when the root is missing.
"""
import os
import shutil
import sys
import tempfile
import unittest

TOOLS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, TOOLS)

# Default sibling checkouts live next to the repo root (override with the ANKER_* env vars).
_SIBLINGS = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
ROOT_NEW = os.environ.get(
    'ANKER_ASM_NEW', os.path.join(_SIBLINGS, 'v3.24.3/blutter_output/asm'))

URL = '/power_service/v1/app/fixture/get_thing'


def fn_text(name, addr, body, static=False):
    """One asm function. body: list of ('lit', text) | ('call', sym, lib)."""
    out = ['  %s_ %s(/* No info */) {' % ('static ' if static else '', name),
           '    // ** addr: %s, size: 0x40' % addr]
    a = int(addr, 16)
    for item in body:
        a += 4
        h = '0x%x' % a
        if item[0] == 'lit':
            out.append('    // %s: r0 = "%s"' % (h, item[1]))
            out.append('    //     %s: ldr x0, [PP, #0x10]' % h)
        elif item[0] == 'field':
            out.append('    // %s: r2 = %s' % (h, item[1].split('.')[-1]))
            out.append('    //     %s: add x2, PP, #0x66, lsl #12  ; [pp+0x667b0] '
                       'Field <%s>: static late (offset: 0xae0)' % (h, item[1]))
        else:
            lib = item[2] if len(item) > 2 else 'package:fix/a.dart'
            out.append('    // %s: r0 = %s()' % (h, item[1].split('::')[-1]))
            out.append('    //     %s: bl #0x999  ; [%s] %s' % (h, lib, item[1]))
    out.append('  }')
    return '\n'.join(out)


def write_class(root, rel, cls, funcs, abstract=False):
    p = os.path.join(root, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as fh:
        fh.write('// lib: , url: package:fix/%s\n\n// class id: 1, size: 0x8\n'
                 'class :: {\n}\n\n// class id: 2, size: 0x8\n%sclass %s extends Object {\n\n'
                 % (rel, 'abstract ' if abstract else '', cls))
        fh.write('\n'.join(funcs) + '\n}\n')


class CallerResolution(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.root, True)

    def inv_row(self, fn='getUrl'):
        import endpoint_inventory
        inv = endpoint_inventory.build_inventory(self.root, '3.24.3')
        rows = [r for r in inv['rows'] if r['url'] == URL and r['function'] == fn]
        self.assertEqual(len(rows), 1, rows)
        return rows[0]

    def chain(self, depth, sender_last=True):
        """Provider P0 <- C1 <- ... <- C<depth>; the last one sends."""
        write_class(self.root, 'api/p.dart', 'Prov', [
            fn_text('getUrl', '0x1000', [('lit', URL)])])
        for i in range(1, depth + 1):
            callee = 'Prov::getUrl' if i == 1 else 'C%d::run' % (i - 1)
            body = [('call', callee)]
            if i == depth and sender_last:
                body.append(('call', 'HttpRequestControllerImpl::requestHttp'))
            write_class(self.root, 'ui/c%d.dart' % i, 'C%d' % i, [
                fn_text('run', '0x%x' % (0x2000 + i * 0x100), body)])

    def test_resolves_in_one_level(self):
        self.chain(1)
        r = self.inv_row()
        self.assertEqual(r['role'], 'url_provider')
        self.assertEqual(r['sender'], 'C1::run @0x2100')
        self.assertEqual(r['sender_via'], ['C1::run @0x2100'])
        self.assertNotIn('resolution', r)

    def test_resolves_in_three_levels(self):
        self.chain(3)
        r = self.inv_row()
        self.assertEqual(r['sender'], 'C3::run @0x2300')
        self.assertEqual(r['sender_via'], ['C1::run @0x2100', 'C2::run @0x2200',
                                           'C3::run @0x2300'])
        self.assertEqual(r['sender_via_files'],
                         ['ui/c1.dart', 'ui/c2.dart', 'ui/c3.dart'])
        self.assertEqual(r['sender_file'], 'ui/c3.dart')

    def test_stops_at_three_levels(self):
        self.chain(4)
        r = self.inv_row()
        self.assertEqual(r['resolution'], 'unresolved')
        self.assertNotIn('sender', r)
        self.assertNotIn('sender_via', r)

    def test_no_callers_is_unresolved(self):
        self.chain(0)
        self.assertEqual(self.inv_row()['resolution'], 'unresolved')

    def test_mixin_gap(self):
        # Prov::getUrl is called only through a deduplicated mixin application
        # whose body is absent from the dump
        write_class(self.root, 'api/p.dart', 'ProvExt', [
            fn_text('getUrl', '0x1000', [('lit', URL)])], abstract=True)
        write_class(self.root, 'ui/c.dart', 'Ui', [fn_text('go', '0x2000', [
            ('call', '_MixinApplication7&Base&ProvExt::getUrl',
             'dart:mixin_deduplication')])])
        r = self.inv_row()
        self.assertEqual(r['resolution'], 'mixin-gap')
        self.assertNotIn('sender', r)

    def test_sdk_handle_in_same_function(self):
        write_class(self.root, 'api/p.dart', 'Cmd', [fn_text('getUrl', '0x1000', [
            ('lit', URL), ('call', 'AKIoTKitManagerImpl::handle')])], abstract=True)
        r = self.inv_row()
        self.assertEqual(r['role'], 'url_provider')
        self.assertEqual(r['sender'], 'Cmd::getUrl @0x1000')
        self.assertEqual(r['sender_via'], [])

    def test_static_late_url_field_load_counts_as_caller(self):
        write_class(self.root, 'api/p.dart', 'Api', [fn_text('getUrl', '0x1000', [
            ('lit', URL)])], abstract=True)
        write_class(self.root, 'ui/c.dart', 'Ui', [fn_text('go', '0x2000', [
            ('field', 'Api.getUrl'),
            ('call', 'HttpRequestControllerImpl::requestHttp')])])
        r = self.inv_row()
        self.assertEqual(r['sender'], 'Ui::go @0x2000')

    def test_send_before_the_url_load_is_not_the_sender(self):
        write_class(self.root, 'api/p.dart', 'Prov', [
            fn_text('getUrl', '0x1000', [('lit', URL)])])
        write_class(self.root, 'ui/c1.dart', 'C1', [fn_text('run', '0x2100', [
            ('call', 'HttpRequestControllerImpl::requestHttp'),
            ('call', 'Prov::getUrl')])])
        self.assertEqual(self.inv_row()['resolution'], 'unresolved')

    def test_callee_after_url_load_sends(self):
        write_class(self.root, 'api/p.dart', 'Prov', [
            fn_text('getUrl', '0x1000', [('lit', URL)])])
        write_class(self.root, 'ui/c1.dart', 'C1', [fn_text('run', '0x2100', [
            ('call', 'Prov::getUrl'), ('call', 'Svc::post')])])
        write_class(self.root, 'ui/svc.dart', 'Svc', [fn_text('post', '0x2200', [
            ('call', 'HttpRequestControllerImpl::encryptionRequestHttp')])])
        r = self.inv_row()
        self.assertEqual(r['sender'], 'Svc::post @0x2200')
        self.assertEqual(r['sender_kind'], 'callee')
        self.assertEqual(r['sender_via'], ['C1::run @0x2100'])
        self.assertEqual(r['sender_wrapper'],
                         'HttpRequestControllerImpl::encryptionRequestHttp')

    def test_callee_with_another_url_literal_is_not_taken(self):
        write_class(self.root, 'api/p.dart', 'Prov', [
            fn_text('getUrl', '0x1000', [('lit', URL)])])
        write_class(self.root, 'ui/c1.dart', 'C1', [fn_text('run', '0x2100', [
            ('call', 'Prov::getUrl'), ('call', 'Svc::post')])])
        write_class(self.root, 'ui/svc.dart', 'Svc', [fn_text('post', '0x2200', [
            ('lit', '/power_service/v1/app/other/endpoint'),
            ('call', 'HttpRequestControllerImpl::encryptionRequestHttp')])])
        self.assertEqual(self.inv_row()['resolution'], 'unresolved')

    def test_http_helper_wrapper_is_the_sender(self):
        write_class(self.root, 'fix/http/http_helper.dart', 'HttpHelper', [
            fn_text('getData', '0x3000', [
                ('call', 'HttpRequestControllerImpl::encryptionRequestHttp')])])
        write_class(self.root, 'api/p.dart', 'Prov', [
            fn_text('getUrl', '0x1000', [('lit', URL)])])
        write_class(self.root, 'ui/c1.dart', 'C1', [fn_text('run', '0x2100', [
            ('call', 'Prov::getUrl'),
            ('call', 'HttpHelper::getData', 'package:fix/http/http_helper.dart')])])
        r = self.inv_row()
        self.assertEqual(r['sender'], 'HttpHelper::getData @0x3000')
        self.assertEqual(r['sender_kind'], 'wrapper')
        self.assertEqual(r['sender_wrapper'], 'HttpHelper::getData')
        self.assertEqual(r['sender_via'], ['C1::run @0x2100'])

    def test_literal_in_generic_http_manager_is_a_path_check(self):
        write_class(self.root, 'fix/util/http_manager.dart', 'HttpRequestManager', [
            fn_text('requestHttp', '0x1000', [
                ('lit', URL)])])
        r = self.inv_row('requestHttp')
        self.assertEqual(r['resolution'], 'generic-path-check')
        self.assertNotIn('sender', r)

    def test_mixin_gap_real_excerpt(self):
        # call site copied from custom_mode_usage_scenario_logic.dart
        # @0x2886c44 (3.24.3); the mixin method has no body in the dump
        write_class(self.root, 'api/p.dart', 'AE100ApiExt', [
            fn_text('setUserParamsAsync', '0x1000', [('lit', URL)])], abstract=True)
        p = os.path.join(self.root, 'ui/c.dart')
        os.makedirs(os.path.dirname(p))
        with open(p, 'w') as fh:
            fh.write(
                'class Ui extends Object {\n\n  _ go(/* No info */) {\n'
                '    // ** addr: 0x2000, size: 0x40\n'
                '    // 0x2886c44: r0 = setUserParamsAsync()\n'
                '    //     0x2886c44: bl              #0x2886c64  ; '
                '[dart:mixin_deduplication] _MixinApplication707&BaseBleController'
                '&CommonLocation&AE100ApiExt::setUserParamsAsync\n  }\n}\n')
        self.assertEqual(self.inv_row('setUserParamsAsync')['resolution'],
                         'mixin-gap')

    def test_mixin_gap_without_deduplication_library(self):
        write_class(self.root, 'api/p.dart', 'FooMixin', [
            fn_text('getUrl', '0x1000', [('lit', URL)])], abstract=True)
        write_class(self.root, 'ui/c.dart', 'Ui', [fn_text('go', '0x2000', [
            ('call', '_MixinApplication9&Base&FooMixin::getUrl',
             'package:fix/ui/c.dart')])])
        self.assertEqual(self.inv_row()['resolution'], 'mixin-gap')

    def test_abstract_class_name_is_kept(self):
        write_class(self.root, 'api/p.dart', 'Cmd', [fn_text('getUrl', '0x1000', [
            ('lit', URL)])], abstract=True)
        write_class(self.root, 'ui/c.dart', 'Ui', [fn_text('go', '0x2000', [
            ('call', 'Cmd::getUrl'),
            ('call', 'HttpRequestControllerImpl::requestHttp')])])
        r = self.inv_row()
        self.assertEqual(r['class'], 'Cmd')
        self.assertEqual(r['sender'], 'Ui::go @0x2000')


@unittest.skipIf(not os.path.isdir(ROOT_NEW), 'asm root missing')
class RealAsm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import endpoint_inventory
        cls.inv = endpoint_inventory.build_inventory(ROOT_NEW, '3.24.3')

    def row(self, url, fn):
        rows = [r for r in self.inv['rows']
                if r['url'] == url and r['function'] == fn]
        self.assertEqual(len(rows), 1)
        return rows[0]

    def test_user_site_param_is_already_a_sender_not_a_provider(self):
        # the brief expected a url_provider here; the literal sits in
        # HttpRequestControllerImpl.setUserParams, which calls
        # encryptionRequestHttp itself (setUserParamsAsync, a deduplicated mixin
        # method, only calls it).  No caller walk, no new fields.
        r = self.row('/power_service/v1/set_user_site_param', 'setUserParams')
        self.assertEqual(r['role'], 'sender')
        self.assertNotIn('sender', r)
        self.assertNotIn('resolution', r)

    def test_command_map_function_sends_itself(self):
        r = self.row('/power_service/v1/app/user/set_user_params', 'setUserParams')
        self.assertEqual(r['role'], 'url_provider')
        self.assertEqual(r['sender'], 'AKIotEVChargeCommand::setUserParams @0x405be14')
        self.assertEqual(r['sender_via'], [])

    def test_standby_exercise_plan_closure_sends_itself(self):
        r = self.row('/generator/v1/app/get_standby_exercise_plan',
                     '<anonymous closure>@0x35e1f50')
        self.assertEqual(r['sender_via'], [])
        self.assertIn('@0x35e1f50', r['sender'])

    def test_save_time_of_use_sender_is_the_http_helper(self):
        rows = [r for r in self.inv['rows']
                if r['url'] == '/charging_hes_dynamic_price_svc/save_time_of_use'
                and r['role'] == 'url_provider']
        self.assertEqual(len(rows), 1)
        r = rows[0]
        self.assertEqual(r['sender'], 'HttpHelper::getDataFromService @0x27bda38')
        self.assertEqual(r['sender_kind'], 'wrapper')
        chains = [r['sender_via']] + r.get('sender_via_also', [])
        flat = [x for c in chains for x in c]
        self.assertIn('ElectricityPricePlanApiHelper::changeToTouPlan @0x31a9fdc',
                      flat)
        self.assertFalse([x for x in flat if '@0x41a68ac' in x], flat)

    def test_tou_detail_sender_is_set_site_tou_detail(self):
        for url in ('/power_service/v1/site/set_site_device_param',
                    '/power_service/v1/app/device/set_device_home_load'):
            rows = [r for r in self.inv['rows'] if r['url'] == url
                    and r['function'] == 'getSetElectricityUsagePolicyUrl']
            self.assertEqual(len(rows), 1)
            r = rows[0]
            self.assertEqual(r['sender'],
                             'ElectricityUsageHelper::setSiteTOUDetail @0x31b90a0')
            self.assertEqual(r['sender_kind'], 'callee')
            self.assertEqual(r['sender_via'],
                             ['ElectricityUsageHelper::setManualSetTOUDetail @0x31b8da8'])
            self.assertNotIn('@0x31de7dc', ' '.join(r['sender_via']))

    def test_faqs_literal_is_a_path_check(self):
        rows = [r for r in self.inv['rows'] if r['url'] == '/app/help/faqs'
                and r['role'] == 'url_provider']
        self.assertEqual(len(rows), 2)
        for r in rows:
            self.assertEqual(r['resolution'], 'generic-path-check')
            self.assertNotIn('sender', r)

    def test_formerly_unresolved_same_function_senders_resolve(self):
        want = {'0x22d7594', '0x22ba090', '0x24a40fc', '0x27e20b4', '0x29b0b28',
                '0x29b0c8c', '0x2d90620', '0x31211e0', '0x3313658'}
        got = {}
        for r in self.inv['rows']:
            if r['role'] == 'url_provider' and r['addr'] in want:
                got.setdefault(r['addr'], []).append(r)
        self.assertEqual(set(got), want)
        for addr, rs in got.items():
            for r in rs:
                if addr == '0x3313658':
                    # the upload runs in SmallChargingHttpMixin.uploadStream, a
                    # deduplicated mixin method whose body is not in the dump
                    self.assertEqual(r['resolution'], 'mixin-gap')
                else:
                    self.assertIn('sender', r, (addr, r['url']))

    def test_unresolved_stays_a_provider(self):
        rows = [r for r in self.inv['rows'] if r['function'] == 'isAlexaAuthUrl']
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['role'], 'url_provider')
        self.assertEqual(rows[0]['resolution'], 'unresolved')
        self.assertNotIn('sender', rows[0])


class RenderNote(unittest.TestCase):
    ROW = {'dart_file': 'api/p.dart', 'url_addr': '0x1004'}

    def note(self, **kw):
        import render_pages
        return render_pages._sender_note(dict(self.ROW, **kw))

    def test_note_cites_file_before_address(self):
        note = self.note(
            sender='C2::run @0x2200', sender_file='ui/c2.dart', sender_kind='self',
            sender_via=['C1::run @0x2100', 'C2::run @0x2200'],
            sender_via_files=['ui/c1.dart', 'ui/c2.dart'])
        self.assertIn('`ui/c1.dart @0x2100`', note)
        self.assertIn('`ui/c2.dart @0x2200`', note)

    def test_note_names_the_literal_and_carries_the_caveat(self):
        import render_pages
        for kind, via in (('self', []), ('wrapper', ['C1::run @0x2100']),
                          ('callee', ['C1::run @0x2100'])):
            note = self.note(sender='S::go @0x3000', sender_file='x/s.dart',
                             sender_kind=kind, sender_wrapper='W::w',
                             sender_via=via, sender_via_files=['ui/c1.dart'] * len(via))
            self.assertIn('`api/p.dart @0x1004`', note)
            self.assertIn(render_pages.CAVEAT, note)
        self.assertIn('it may send other URLs too', render_pages.CAVEAT)

    def test_note_for_gap_unresolved_and_path_check(self):
        self.assertIn('UNCONFIRMED', self.note(resolution='mixin-gap'))
        self.assertIn('3 caller levels', self.note(resolution='unresolved'))
        self.assertIn('path check', self.note(resolution='generic-path-check'))
        self.assertEqual(self.note(), '')
