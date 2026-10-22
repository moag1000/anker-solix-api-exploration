"""Tests for the package keys and the noise filter of tools/model_fields.py.

Run from the repo root:  python3 -I -m unittest discover -s tools/tests -t .
Synthetic rows only; the committed data/models.json is checked by test_schema_check.
"""
import json
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from unittest import mock

TOOLS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(TOOLS)
sys.path.insert(0, TOOLS)

import model_fields as M  # noqa: E402

F = [{'json_key': 'k'}]


def row(cls, path, fields=F):
    return {'class': cls, 'dart_file': path, 'fields': list(fields)}


class TestKeys(unittest.TestCase):
    def test_package_is_first_segment(self):
        self.assertEqual(M.package_of('charging/model/power.dart'), 'charging')
        self.assertEqual(M.package_of('top.dart'), '')

    def test_unique_class_gets_package_key(self):
        rows = M.assign_keys([row('A', 'p/a.dart')])
        self.assertEqual(rows[0]['key'], 'p::A')
        self.assertEqual(rows[0]['class'], 'A')

    def test_same_name_other_package(self):
        rows = M.assign_keys([row('A', 'p/a.dart'), row('A', 'q/a.dart')])
        self.assertEqual({r['key'] for r in rows}, {'p::A', 'q::A'})

    def test_same_package_extends_to_directory(self):
        rows = M.assign_keys([row('A', 'p/model/a.dart'), row('A', 'p/bean/a.dart')])
        self.assertEqual({r['key'] for r in rows}, {'p/model::A', 'p/bean::A'})

    def test_same_directory_falls_back_to_file(self):
        rows = M.assign_keys([row('A', 'p/m/a.dart'), row('A', 'p/m/b.dart')])
        self.assertEqual({r['key'] for r in rows}, {'p/m/a::A', 'p/m/b::A'})

    def test_non_colliding_rows_keep_short_key(self):
        rows = M.assign_keys([row('A', 'p/model/a.dart'), row('A', 'p/bean/a.dart'),
                              row('B', 'p/model/b.dart')])
        by = {r['dart_file']: r['key'] for r in rows}
        self.assertEqual(by['p/model/b.dart'], 'p::B')

    def test_keys_unique_and_sorted(self):
        rows = M.assign_keys([row('B', 'p/b.dart'), row('A', 'q/a.dart'),
                              row('A', 'p/a.dart')])
        keys = [r['key'] for r in rows]
        self.assertEqual(keys, sorted(keys))
        self.assertEqual(len(keys), len(set(keys)))


class TestNoise(unittest.TestCase):
    def test_fieldless_app_class_is_not_noise(self):
        self.assertFalse(M.is_noise(row('A', 'p/a.dart', fields=[])))

    def test_sentry_is_noise_even_with_fields(self):
        self.assertTrue(M.is_noise(row('SentryGeo', 'sentry/src/protocol/sentry_geo.dart')))

    def test_sentry_substring_in_other_package_is_not_noise(self):
        self.assertFalse(M.is_noise(row('SentryLike', 'charging/sentry_like.dart')))

    def test_regular_class_is_kept(self):
        self.assertFalse(M.is_noise(row('A', 'p/a.dart')))

    def test_filter_default_and_include(self):
        rows = [row('A', 'p/a.dart'), row('B', 'p/b.dart', fields=[]),
                row('C', 'sentry/c.dart')]
        self.assertEqual([r['class'] for r in M.filter_noise(rows, False)], ['A', 'B'])
        self.assertEqual(len(M.filter_noise(rows, True)), 3)


class TestMain(unittest.TestCase):
    def _run(self, extra):
        built = {'rows': [row('A', 'p/a.dart'), row('A', 'q/a.dart'),
                          row('E', 'p/e.dart', fields=[]), row('S', 'sentry/s.dart')]}
        out = os.path.join(tempfile.mkdtemp(), 'models.json')
        with mock.patch.object(M, 'build_models', return_value=built), \
                mock.patch.object(M.A, 'check_root'), \
                redirect_stdout(StringIO()), redirect_stderr(StringIO()):
            self.assertEqual(M.main(['ROOT', '--version', '3.24.3', '--out', out] + extra), 0)
        with open(out, encoding='utf-8') as fh:
            return json.load(fh)['rows']

    def test_default_drops_sentry_only(self):
        rows = self._run([])
        self.assertEqual([r['key'] for r in rows], ['p::A', 'p::E', 'q::A'])

    def test_include_noise_keeps_all_with_keys(self):
        rows = self._run(['--include-noise'])
        self.assertEqual(len(rows), 4)
        self.assertTrue(all('key' in r and 'class' in r for r in rows))


if __name__ == '__main__':
    unittest.main()
