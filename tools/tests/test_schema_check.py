"""Tests for tools/schema_check.py.

Run from the repo root:  python3 -I -m unittest discover -s tools/tests -t .
Synthetic documents cover the envelope, row types, unknown fields, bool-vs-int,
cross-file consistency and --check; one test validates the committed data/.
"""
import copy
import io
import json
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout

TOOLS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(TOOLS)
sys.path.insert(0, TOOLS)

import schema_check as S  # noqa: E402

ENV = {'generated_by': 'tools/x.py', 'app_version': '3.24.3', 'snapshot': 'ab' * 16}


def doc(rows, **over):
    d = dict(ENV, rows=rows)
    d.update(over)
    return d


EP_ROW = {
    'addr': '0x1', 'callers': ['a'], 'class': 'C', 'cmd': None, 'cmd_addr': None,
    'cmd_note': None, 'cmd_raw': None, 'dart_file': 'a/b.dart', 'encrypted': True,
    'encryption_note': None, 'envelope': [], 'function': 'f', 'http_callees': [],
    'param_data_is_json': False, 'param_type': None, 'param_type_source': None,
    'params': [], 'role': 'url_provider', 'service': 's', 'since': '3.24.3',
    'upstream_key': None, 'url': '/s/v1/x', 'url_addr': '0x2',
}
MODEL_FIELD = {'dart_type': 'int?', 'json_key': 'k', 'key_addr': '0x3',
               'nullable': True, 'since': '3.24.3'}
MODEL_ROW = {'key': 'a::C', 'class': 'C', 'dart_file': 'a/c.dart', 'fields': [MODEL_FIELD],
             'from_json_addr': '0x4', 'removed_keys': [], 'since': '3.24.3'}
ERR_ROW = {'code': 10004, 'source': 'issue', 'tag': 'device-tested'}


class TestCheckDoc(unittest.TestCase):
    def test_valid_endpoints(self):
        self.assertEqual(S.check_doc('endpoints', doc([EP_ROW])), [])

    def test_valid_models_and_errors(self):
        self.assertEqual(S.check_doc('models', doc([MODEL_ROW])), [])
        self.assertEqual(S.check_doc('errors', doc([ERR_ROW])), [])

    def test_missing_top_level_key(self):
        d = doc([EP_ROW])
        del d['snapshot']
        v = S.check_doc('endpoints', d)
        self.assertEqual(len(v), 1)
        self.assertIn('snapshot', v[0])

    def test_unknown_top_level_key(self):
        v = S.check_doc('endpoints', doc([EP_ROW], extra=1))
        self.assertTrue(any('extra' in x for x in v))

    def test_rows_not_a_list(self):
        v = S.check_doc('endpoints', doc({}))
        self.assertTrue(any('rows' in x for x in v))

    def test_missing_required_row_field(self):
        r = copy.deepcopy(EP_ROW)
        del r['url']
        v = S.check_doc('endpoints', doc([r]))
        self.assertEqual(len(v), 1)
        self.assertIn('rows[0]', v[0])
        self.assertIn('url', v[0])

    def test_unknown_row_field(self):
        r = dict(EP_ROW, brand_new=1)
        v = S.check_doc('endpoints', doc([r]))
        self.assertTrue(any('brand_new' in x for x in v))

    def test_wrong_type(self):
        r = dict(EP_ROW, encrypted='yes')
        v = S.check_doc('endpoints', doc([r]))
        self.assertTrue(any('encrypted' in x and 'bool' in x for x in v))

    def test_bool_is_not_int(self):
        r = dict(ERR_ROW, code=True)
        self.assertTrue(S.check_doc('errors', doc([r])))

    def test_optional_sender_fields(self):
        r = dict(EP_ROW, sender='f', sender_file='a.dart', sender_kind='self',
                 sender_via=[], sender_via_files=[], sender_wrapper='w',
                 sender_also=['x'], sender_via_also=[['a']], resolution='unresolved')
        self.assertEqual(S.check_doc('endpoints', doc([r])), [])
        bad = dict(EP_ROW, sender_via=[1])
        self.assertTrue(S.check_doc('endpoints', doc([bad])))

    def test_nested_model_field(self):
        r = copy.deepcopy(MODEL_ROW)
        r['fields'][0]['nullable'] = 'maybe'
        v = S.check_doc('models', doc([r]))
        self.assertTrue(any('fields[0]' in x and 'nullable' in x for x in v))
        r = copy.deepcopy(MODEL_ROW)
        del r['fields'][0]['json_key']
        self.assertTrue(S.check_doc('models', doc([r])))

    def test_duplicate_model_key(self):
        v = S.check_doc('models', doc([MODEL_ROW, dict(MODEL_ROW)]))
        self.assertTrue(any('duplicate' in x for x in v))

    def test_model_key_must_embed_class(self):
        r = dict(MODEL_ROW, key='a::Other')
        self.assertTrue(any('key' in x for x in S.check_doc('models', doc([r]))))

    def test_unknown_file(self):
        with self.assertRaises(KeyError):
            S.check_doc('nope', doc([]))


class TestRepo(unittest.TestCase):
    def _repo(self, **docs):
        tmp = tempfile.mkdtemp()
        os.makedirs(os.path.join(tmp, 'data'))
        base = {'endpoints': [EP_ROW], 'models': [MODEL_ROW],
                'param_types': None, 'errors': [ERR_ROW]}
        base.update(docs)
        for n, rows in base.items():
            if rows is None:
                continue
            d = rows if isinstance(rows, dict) else doc(rows)
            with open(os.path.join(tmp, 'data', n + '.json'), 'w') as fh:
                json.dump(d, fh)
        return tmp

    def test_missing_file_is_violation(self):
        v = S.check_repo(self._repo())
        self.assertTrue(any('param_types.json' in x and 'missing' in x for x in v))

    def test_invalid_json(self):
        tmp = self._repo()
        with open(os.path.join(tmp, 'data', 'errors.json'), 'w') as fh:
            fh.write('{')
        self.assertTrue(any('errors.json' in x and 'JSON' in x for x in S.check_repo(tmp)))

    def test_cross_file_version_mismatch(self):
        tmp = self._repo(errors=doc([ERR_ROW], app_version='3.18.0'))
        self.assertTrue(any('app_version' in x for x in S.check_repo(tmp)))

    def test_cross_file_snapshot_mismatch(self):
        tmp = self._repo(errors=doc([ERR_ROW], snapshot='cd' * 16))
        self.assertTrue(any('snapshot' in x for x in S.check_repo(tmp)))


class TestMain(unittest.TestCase):
    def _run(self, argv):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            rc = S.main(argv)
        return rc, out.getvalue() + err.getvalue()

    def test_check_exit_codes_and_no_writes(self):
        tmp = tempfile.mkdtemp()
        os.makedirs(os.path.join(tmp, 'data'))
        before = sorted(os.listdir(tmp))
        rc, text = self._run(['--repo', tmp, '--check'])
        self.assertEqual(rc, 1)
        self.assertIn('missing', text)
        self.assertEqual(sorted(os.listdir(tmp)), before)
        self.assertEqual(os.listdir(os.path.join(tmp, 'data')), [])

    def test_without_check_reports_but_exits_zero(self):
        tmp = tempfile.mkdtemp()
        os.makedirs(os.path.join(tmp, 'data'))
        rc, text = self._run(['--repo', tmp])
        self.assertEqual(rc, 0)
        self.assertIn('violation', text)


class TestCommittedData(unittest.TestCase):
    def test_committed_data_is_clean(self):
        self.assertEqual(S.check_repo(REPO), [])


if __name__ == '__main__':
    unittest.main()
