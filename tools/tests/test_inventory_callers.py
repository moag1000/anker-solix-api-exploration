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

ROOT_NEW = os.environ.get(
    'ANKER_ASM_NEW', '/Users/michaelbanda/Nextcloud/www/untitled1/ankerAPK/'
    'v3.24.3/blutter_output/asm')

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

    def test_two_level_chain(self):
        rows = [r for r in self.inv['rows']
                if r['url'] == '/power_service/v1/site/set_site_device_param'
                and r['function'] == 'getSetElectricityUsagePolicyUrl']
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['sender_via'], [
            'ElectricityUsageHelper::setManualSetTOUDetail @0x31b8da8',
            'TOUEditPreviewLogic::savePlan @0x31de7dc'])
        self.assertEqual(rows[0]['sender'], rows[0]['sender_via'][-1])

    def test_unresolved_stays_a_provider(self):
        r = self.row(self._timezone_url(), 'getDeviceTimezone')
        self.assertEqual(r['role'], 'url_provider')
        self.assertEqual(r['resolution'], 'unresolved')
        self.assertNotIn('sender', r)

    def _timezone_url(self):
        return [x['url'] for x in self.inv['rows']
                if x['function'] == 'getDeviceTimezone'][0]


class RenderNote(unittest.TestCase):
    def test_note_cites_file_before_address(self):
        import render_pages
        note = render_pages._sender_note({
            'sender': 'C2::run @0x2200', 'sender_file': 'ui/c2.dart',
            'sender_via': ['C1::run @0x2100', 'C2::run @0x2200'],
            'sender_via_files': ['ui/c1.dart', 'ui/c2.dart']})
        self.assertIn('`ui/c1.dart @0x2100`', note)
        self.assertIn('`ui/c2.dart @0x2200`', note)

    def test_note_for_gap_and_unresolved(self):
        import render_pages
        self.assertIn('UNCONFIRMED',
                      render_pages._sender_note({'resolution': 'mixin-gap'}))
        self.assertIn('3 caller levels',
                      render_pages._sender_note({'resolution': 'unresolved'}))
        self.assertEqual(render_pages._sender_note({}), '')
