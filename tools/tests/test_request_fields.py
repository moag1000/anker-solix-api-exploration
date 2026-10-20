"""Request-field extractor tests (fixture excerpt of getMessage @0x297c340 plus one
synthetic function, see tools/tests/fixtures/request_builder_excerpt.dart).

Run from the repo root:  python3 -I -m unittest discover -s tools/tests -t .
"""
import json
import os
import shutil
import sys
import tempfile
import unittest

TOOLS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, TOOLS)
import asmparse as A  # noqa: E402
import request_fields as R  # noqa: E402

FIX = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures',
                   'request_builder_excerpt.dart')
REL = 'charging/http/http_request_repository_impl.dart'


def analysed(addr):
    for fn in A.iter_functions(FIX, REL):
        if fn.addr == addr:
            info = R.analyse_function(fn)
            return info, {f['key']: f for f in R.fields_of(info)}
    raise AssertionError(addr)


class RequestFieldsTest(unittest.TestCase):
    def test_extracts_keys_and_const_smi(self):
        _, f = analysed('0x297c340')
        self.assertEqual(list(f), ['last_time', 'device_sns', 'limit',
                                   'message_type', 'last_msg_id'])
        lim = f['limit']
        self.assertEqual((lim['value_kind'], lim['raw'], lim['value'], lim['width']),
                         ('const_smi', 20, 10, 'w'))
        self.assertEqual(lim['addr'], '0x297c430')
        self.assertIn('stur w16, [x2, #0x23]', lim['evidence'])
        self.assertTrue(lim['required'])

    def test_param_value_kind(self):
        _, f = analysed('0x297c340')
        for k in ('last_time', 'device_sns', 'message_type', 'last_msg_id'):
            self.assertEqual(f[k]['value_kind'], 'param', k)
        self.assertEqual(f['message_type']['raw'], 'fp+0x20')

    def test_method_post_detected(self):
        info, _ = analysed('0x297c340')
        self.assertEqual(info['method'], 'Method.post')
        self.assertEqual(info['method_addr'], '0x297c51c')
        info2, _ = analysed('0x1000')
        self.assertIsNone(info2['method'])

    def test_bool_int64_and_guard(self):
        _, f = analysed('0x1000')
        self.assertEqual((f['flag']['value_kind'], f['flag']['value']), ('const_bool', True))
        self.assertEqual((f['big']['value_kind'], f['big']['value'], f['big']['width']),
                         ('const_int64', 12345, 'x'))
        self.assertTrue(f['flag']['required'])
        self.assertFalse(f['opt']['required'])
        self.assertEqual(f['opt']['guard_addr'], '0x1058')

    def test_lsl_param_never_const(self):
        _, f = analysed('0x2000')
        self.assertEqual(list(f), ['type'])
        self.assertEqual((f['type']['value_kind'], f['type']['raw']), ('param', 'fp-0x28'))
        self.assertIsNone(f['type']['value'])

    def test_spilled_array_literal(self):
        info, _ = analysed('0x2000')
        self.assertEqual([a['kind'] for a in info['maps']], ['map'])

    def test_body_from_direct_caller(self):
        root = tempfile.mkdtemp()
        try:
            dst = os.path.join(root, REL)
            os.makedirs(os.path.dirname(dst))
            shutil.copy(FIX, dst)
            ep = {'rows': [{'url': '/power_service/v1/synth/no_map', 'service': 'power_service',
                            'addr': '0x3000', 'class': 'HttpRequestControllerImpl',
                            'function': 'synthNoMap', 'dart_file': REL, 'role': 'sender',
                            'callers': [REL + '::synthCaller']}]}
            r = R.run(root, ep, {'rows': []}, 'power_service')[0]
            self.assertEqual(len(r['fields']), 1)
            f = r['fields'][0]
            self.assertEqual((f['key'], f['value_kind'], f['value'], f['source']),
                             ('type_id', 'const_smi', 1, 'caller'))
            self.assertEqual(f['caller'], 'HttpRequestControllerImpl::synthCaller @0x4000')
            ep['rows'][0]['callers'] = []
            r = R.run(root, ep, {'rows': []}, 'power_service')[0]
            self.assertEqual(r['fields'], [])
            self.assertIn('no map literal', r['note'])
        finally:
            shutil.rmtree(root)

    def test_response_class_and_key_from_closure(self):
        root = tempfile.mkdtemp()
        try:
            dst = os.path.join(root, REL)
            os.makedirs(os.path.dirname(dst))
            shutil.copy(FIX, dst)
            ep = {'rows': [{'url': '/power_service/v1/get_message', 'service': 'power_service',
                            'addr': '0x297c340', 'class': 'HttpRequestControllerImpl',
                            'function': 'getMessage', 'dart_file': REL, 'role': 'sender',
                            'callers': []}]}
            mod = {'rows': [{'key': 'charging::MsgHttpModel', 'class': 'MsgHttpModel',
                             'dart_file': 'charging/models/m.dart'}]}
            recs = R.run(root, ep, mod, 'power_service')
            self.assertEqual(len(recs), 1)
            r = recs[0]
            self.assertEqual(r['response_class'], 'MsgHttpModel')
            self.assertEqual(r['response_key'], 'charging::MsgHttpModel')
            self.assertEqual(r['method'], 'Method.post')
            self.assertEqual(R.stats(recs)['urls_with_classified_field'], 1)
            # two packages with the same class and none in the caller's directory
            mod['rows'].append({'key': 'other::MsgHttpModel', 'class': 'MsgHttpModel',
                                'dart_file': 'other/m.dart'})
            r = R.run(root, ep, mod, 'power_service')[0]
            self.assertIsNone(r['response_key'])
            self.assertEqual(r['response_candidates'],
                             ['charging::MsgHttpModel', 'other::MsgHttpModel'])
        finally:
            shutil.rmtree(root)

    def test_check_fails_on_unknown_model_key(self):
        d = tempfile.mkdtemp()
        try:
            out = os.path.join(d, 'out.json')
            mp = os.path.join(d, 'models.json')
            with open(mp, 'w') as fh:
                json.dump({'rows': [{'key': 'a::A', 'class': 'A', 'dart_file': 'a.dart'}]}, fh)
            with open(out, 'w') as fh:
                json.dump({'rows': [{'url': '/x', 'response_key': 'a::A'}]}, fh)
            self.assertEqual(R.main(['--check', '--out', out, '--models', mp]), 0)
            with open(out, 'w') as fh:
                json.dump({'rows': [{'url': '/x', 'response_key': 'a::A'},
                                    {'url': '/y', 'response_key': 'b::Gone'}]}, fh)
            self.assertEqual(R.main(['--check', '--out', out, '--models', mp]), 1)
            self.assertEqual(R.find_unknown_model_keys(
                [{'response_key': None}, {'response_key': 'b::Gone'}], {'a::A'}),
                ['b::Gone'])
        finally:
            shutil.rmtree(d)


if __name__ == '__main__':
    unittest.main()
