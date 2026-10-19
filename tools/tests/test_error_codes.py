"""Tests for tools/error_codes.py.

Run from the repo root:  python3 -I -m unittest discover -s tools/tests -t .
Synthetic inputs cover the Smi rule, the compare shapes, the upstream parser, the
output guard and --check; two checks read the real 3.24.3 asm and skip when the
root is missing.
"""
import io
import json
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout

TOOLS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, TOOLS)

import asmparse as A  # noqa: E402
import error_codes as E  # noqa: E402

ROOT_NEW = os.environ.get(
    'ANKER_ASM_NEW', '/Users/michaelbanda/Nextcloud/www/untitled1/ankerAPK/'
    'v3.24.3/blutter_output/asm')
UPSTREAM_ERRORS = os.environ.get(
    'ANKER_UPSTREAM_ERRORS', '/Users/michaelbanda/Nextcloud/www/untitled1/ankerAPK/'
    'anker-solix-api/api/errors.py')

FAKE_ERRORS = '''"""Errors."""


class AnkerSolixError(Exception):
    """Base."""


class RequestError(AnkerSolixError):
    """Request error."""


class ItemNotFoundError(RequestError):
    """Requested item not found error."""


ERRORS: dict[int, type[AnkerSolixError]] = {
    10003: RequestError,
    10004: ItemNotFoundError,
}
'''

# one handler function: a 64-bit register compare, a 32-bit tagged compare, a
# 32-bit immediate compare and a small compare that must be filtered out
FAKE_ASM = '''class Handler {
  _ handle(/* No info */) {
    // ** addr: 0x1000, size: 0x100
    // 0x1000: r17 = 26108
    //     0x1000: mov             x17, #0x65fc
    // 0x1004: cmp             x0, x17
    // 0x1008: b.ne            #0x1020
    // 0x100c: r1 = "errorAccountOrPassWord"
    //     0x100c: add             x1, PP, #1, lsl #12
    // 0x1010: r17 = 926
    //     0x1010: mov             x17, #0x39e
    // 0x1014: cmp             w1, w17
    // 0x1018: b.gt            #0x1030
    // 0x101c: cmp             w2, #0x322
    // 0x1020: b.ne            #0x1040
    // 0x1024: cmp             x3, #0x7
    // 0x1028: b.eq            #0x1040
  }
  _ other(/* No info */) {
    // ** addr: 0x2000, size: 0x20
    // 0x2000: r17 = 99999
    //     0x2000: mov             x17, #0x1869f
    // 0x2004: cmp             x0, x17
    // 0x2008: b.ne            #0x2020
  }
}
'''
FAKE_FILE = 'pkg/handler.dart'


def read(path):
    with open(path, encoding='utf-8') as fh:
        return fh.read()


def make_asm(tmp):
    path = os.path.join(tmp, 'asm', FAKE_FILE)
    os.makedirs(os.path.dirname(path))
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(FAKE_ASM)
    return os.path.join(tmp, 'asm')


def make_upstream(tmp):
    path = os.path.join(tmp, 'errors.py')
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(FAKE_ERRORS)
    return path


FAKE_SITES = [(FAKE_FILE, '0x1000', 'handle', 1000)]


class SmiRuleTest(unittest.TestCase):
    def test_width_decides(self):
        self.assertEqual(E.smi_value('w', 926), 463)
        self.assertEqual(E.smi_value('x', 26108), 26108)
        self.assertEqual(E.smi_value('w', 802), 401)


class ScanTest(unittest.TestCase):
    def rows(self, minv=400):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_asm(tmp)
            path = os.path.join(root, FAKE_FILE)
            fns = {f.addr: f for f in A.iter_functions(path, FAKE_FILE)}
            return E.scan_function(fns['0x1000'], minv, 'handle')

    def test_three_shapes_and_small_value_filtered(self):
        rows = self.rows()
        self.assertEqual([(r['code'], r['width'], r['raw'], r['form']) for r in rows], [
            (26108, 'x', 26108, 'x17'),
            (463, 'w', 926, 'w17'),
            (401, 'w', 802, 'w-imm')])

    def test_citation_branch_and_strings(self):
        first = self.rows()[0]
        self.assertEqual(first['addr'], '0x1000')
        self.assertEqual(first['branch'], 'ne')
        self.assertEqual(first['strings'], ['errorAccountOrPassWord'])
        self.assertEqual(self.rows()[1]['branch'], 'gt')
        self.assertFalse(any(r['odd_raw'] for r in self.rows()))

    def test_min_value_and_listing_only(self):
        self.assertEqual([r['code'] for r in self.rows(minv=26000)], [26108])
        with tempfile.TemporaryDirectory() as tmp:
            rows, missing = E.scan_sites(make_asm(tmp), FAKE_SITES)
            # `other` (0x2000) is not listed, so its 99999 never shows up
            self.assertNotIn(99999, [r['code'] for r in rows])
            self.assertEqual(missing, [])
            self.assertTrue(all(r['source'] == 'asm' and r['tag'] == 'asm-traced'
                                for r in rows))

    def test_missing_site_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            _, missing = E.scan_sites(make_asm(tmp), [(FAKE_FILE, '0x9999', 'x', 1000),
                                                       ('nope.dart', '0x1', 'y', 1000)])
            self.assertEqual(len(missing), 2)


class UpstreamTest(unittest.TestCase):
    def test_parse(self):
        with tempfile.TemporaryDirectory() as tmp:
            rows = E.parse_upstream(make_upstream(tmp))
        self.assertEqual([(r['code'], r['name'], r['base']) for r in rows],
                         [(10003, 'RequestError', 'AnkerSolixError'),
                          (10004, 'ItemNotFoundError', 'RequestError')])
        self.assertEqual(rows[1]['message'], 'Requested item not found error.')
        self.assertTrue(all(r['tag'] == 'upstream-confirmed' for r in rows))
        self.assertLess(rows[0]['line'], rows[1]['line'])


class BuildAndCliTest(unittest.TestCase):
    def run_main(self, tmp, *extra):
        out, err = io.StringIO(), io.StringIO()
        repo = os.path.join(tmp, 'repo')
        os.makedirs(repo, exist_ok=True)
        old = E.SITES
        E.SITES = FAKE_SITES
        try:
            with redirect_stdout(out), redirect_stderr(err):
                rc = E.main(['--repo', repo, '--asm', os.path.join(tmp, 'asm'),
                             '--upstream', os.path.join(tmp, 'errors.py')] + list(extra))
        finally:
            E.SITES = old
        return rc, out.getvalue(), repo

    def setup_tmp(self, tmp):
        make_asm(tmp)
        make_upstream(tmp)

    def test_issue_row_and_sort(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.setup_tmp(tmp)
            rows, missing = E.build(os.path.join(tmp, 'asm'),
                                    os.path.join(tmp, 'errors.py'), FAKE_SITES)
        self.assertEqual(missing, [])
        self.assertEqual([r['code'] for r in rows], sorted(r['code'] for r in rows))
        issue = [r for r in rows if r['source'] == 'issue']
        self.assertEqual([(r['code'], r['tag']) for r in issue], [(10004, 'device-tested')])
        self.assertIn('issues/1', issue[0]['url'])

    def test_write_is_idempotent_and_guarded(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.setup_tmp(tmp)
            rc, out, repo = self.run_main(tmp)
            self.assertEqual(rc, 0)
            self.assertIn('changed: data/errors.json', out)
            target = os.path.join(repo, 'data', 'errors.json')
            first = read(target)
            doc = json.loads(first)
            self.assertEqual(doc['app_version'], '3.24.3')
            self.assertEqual(doc['snapshot'], A.SNAPSHOT_3_24_3)
            # the only file the tool wrote
            written = [os.path.relpath(os.path.join(dp, f), repo)
                       for dp, _, fs in os.walk(repo) for f in fs]
            self.assertEqual(written, [os.path.join('data', 'errors.json')])
            rc, out, _ = self.run_main(tmp)
            self.assertEqual(rc, 0)
            self.assertIn('changed: none', out)
            self.assertEqual(read(target), first)

    def test_check_mode_writes_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.setup_tmp(tmp)
            rc, out, repo = self.run_main(tmp, '--check')
            self.assertEqual(rc, 1)
            self.assertIn('stale or missing', out)
            self.assertFalse(os.path.exists(os.path.join(repo, 'data', 'errors.json')))
            self.run_main(tmp)
            rc, out, _ = self.run_main(tmp, '--check')
            self.assertEqual(rc, 0)
            self.assertIn('up to date', out)
            with open(os.path.join(repo, 'data', 'errors.json'), 'a') as fh:
                fh.write(' ')
            rc, _, _ = self.run_main(tmp, '--check')
            self.assertEqual(rc, 1)

    def test_check_flags_code_missing_on_page(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.setup_tmp(tmp)
            _, _, repo = self.run_main(tmp)
            os.makedirs(os.path.join(repo, 'api'))
            page = os.path.join(repo, 'api', 'errors.md')
            with open(page, 'w', encoding='utf-8') as fh:
                fh.write('| code | x |\n|---|---|\n| 10003 | a |\n| 10004 | a |\n')
            self.assertEqual(self.run_main(tmp, '--check')[0], 1)  # asm codes missing
            codes = sorted({r['code'] for r in json.loads(read(
                os.path.join(repo, 'data', 'errors.json')))['rows']})
            with open(page, 'w', encoding='utf-8') as fh:
                fh.write('| code | x |\n|---|---|\n' + ''.join(
                    '| %d | a |\n' % c for c in codes))
            self.assertEqual(self.run_main(tmp, '--check')[0], 0)

    def test_unknown_site_aborts_without_writing(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.setup_tmp(tmp)
            old = E.SITES
            E.SITES = [(FAKE_FILE, '0x9999', 'x', 1000)]
            try:
                repo = os.path.join(tmp, 'repo')
                os.makedirs(repo)
                with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                    rc = E.main(['--repo', repo, '--asm', os.path.join(tmp, 'asm'),
                                 '--upstream', os.path.join(tmp, 'errors.py')])
            finally:
                E.SITES = old
            self.assertEqual(rc, 2)
            self.assertFalse(os.path.exists(os.path.join(repo, 'data')))


@unittest.skipUnless(os.path.isdir(ROOT_NEW) and os.path.isfile(UPSTREAM_ERRORS),
                     'asm root or upstream errors.py missing')
class RealDataTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows, cls.missing = E.build(ROOT_NEW, UPSTREAM_ERRORS)

    def find(self, source, code, **kw):
        return [r for r in self.rows if r['source'] == source and r['code'] == code
                and all(r.get(k) == v for k, v in kw.items())]

    def test_every_site_found(self):
        self.assertEqual(self.missing, [])

    def test_smi_halving_on_status_handler(self):
        # HttpEncryptionDecorator::handleStatusCode compares tagged ints (w): 926 -> 463
        r = self.find('asm', 463, function='handleStatusCode', addr='0x486b100')
        self.assertEqual([(x['width'], x['raw']) for x in r], [('w', 926)])
        r = self.find('asm', 461, addr='0x486b1ac')
        self.assertEqual([(x['width'], x['raw']) for x in r], [('w', 922)])

    def test_unboxed_compare_is_raw(self):
        # LoginLogic::handleLoginFail: cmp x0, x17 with r17 = 26108, raw is real
        r = self.find('asm', 26108, addr='0x3bd22b8')
        self.assertEqual([(x['width'], x['raw']) for x in r], [('x', 26108)])

    def test_upstream_and_issue_rows(self):
        self.assertEqual(self.find('upstream', 10004)[0]['name'], 'ItemNotFoundError')
        self.assertEqual(len({r['code'] for r in self.rows if r['source'] == 'upstream'}), 28)
        self.assertEqual(len(self.find('issue', 10004)), 1)


if __name__ == '__main__':
    unittest.main()
