"""Tests for tools/unknowns_triage.py.

Run from the repo root:
  python3 -I -m unittest discover -s tools/tests -t . -p 'test_unknowns_triage.py'
Synthetic pages only; nothing reads the asm.
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

import unknowns_triage as U  # noqa: E402

PAGE = '''> header

# Page

- not a known unknown (before the section)

## Purpose

- also not one

## Known unknowns

Tag: untagged by design.

- Whether the server accepts a free value.
- Which firmware versions accept the key.
  continuation line of the bullet.

```
## Not a heading
- inside a fence
```

- The polarity of the device flag that guards block 5 `@0x1234`.

## Other

- bullet in the next section
'''


def write(root, rel, text):
    p = os.path.join(root, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(text)


class TriageTests(unittest.TestCase):
    def test_extracts_bullets_under_known_unknowns_only(self):
        with tempfile.TemporaryDirectory() as d:
            write(d, 'api/x.md', PAGE)
            write(d, 'docs/archive/old.md', '## Known unknowns\n\n- archived\n')
            write(d, 'docs/superpowers/p.md', '## Known unknowns\n\n- plan\n')
            write(d, '.superpowers/s.md', '## Known unknowns\n\n- scratch\n')
            rows = U.collect(d)
        self.assertEqual([(r['page'], r['line']) for r in rows],
                         [('api/x.md', 15), ('api/x.md', 16), ('api/x.md', 24)])
        self.assertIn('continuation line', rows[1]['text'])

    def test_command_level_and_on_this_page_headings(self):
        page = ('## Commands\n\n### Cmd\n\n#### Known unknowns\n\n- one\n\n'
                '#### Device-tested by\n\n- not me\n\n#### Known unknowns\n\n- two\n\n'
                '## Known unknowns on this page\n\n- three\n\n## Known unknowns\n\nNone.\n')
        with tempfile.TemporaryDirectory() as d:
            write(d, 'ble/x.md', page)
            rows = U.collect(d)
        self.assertEqual([r['text'] for r in rows], ['one', 'two', 'three'])

    def test_classifies_server_words(self):
        c = U.classify
        self.assertEqual(c('Whether the server accepts a value')[0], 'server')
        self.assertEqual(c('Which firmware versions accept the key')[0], 'device')
        self.assertEqual(
            c('The polarity of the device flag that guards block 5')[0], 'asm')
        self.assertEqual(c('Meaning of key `foo`'), ('unclear', 'no-rule'))
        self.assertEqual(c('The server flag at @0x1234')[0], 'server')  # first rule wins

    def test_counts_per_class_in_markdown(self):
        with tempfile.TemporaryDirectory() as d:
            write(d, 'api/x.md', PAGE)
            rows = U.collect(d)
        md = U.render(rows, '2026-10-20')
        table = [ln for ln in md.split('## Summary')[1].split('##')[0].splitlines()
                 if ln.startswith('| ') and 'class' not in ln and '---' not in ln]
        self.assertEqual([ln.split('|')[1].strip() for ln in table],
                         ['asm', 'server', 'device', 'unclear', 'total'])
        counts = [int(ln.split('|')[2]) for ln in table]
        self.assertEqual(counts, [1, 1, 1, 0, 3])
        self.assertEqual(sum(counts[:4]), counts[4])

    def test_override_applies_and_reports_stale_keys(self):
        with tempfile.TemporaryDirectory() as d:
            write(d, 'api/x.md', PAGE)
            rows = U.collect(d)
            ov = {'api/x.md:15': {'class': 'device', 'note': 'n'},
                  'api/gone.md:1': {'class': 'asm', 'note': ''}}
            stale = U.apply_overrides(rows, ov)
        self.assertEqual(rows[0]['class'], 'device')
        self.assertEqual(rows[0]['heuristic_class'], 'server')
        self.assertEqual(rows[0]['hint'], 'override')
        self.assertEqual(stale, ['api/gone.md:1'])

    def test_bad_override_class_exits_2(self):
        with tempfile.TemporaryDirectory() as d:
            write(d, 'api/x.md', PAGE)
            with open(os.path.join(d, 'ov.json'), 'w') as f:
                json.dump({'api/x.md:15': {'class': 'bogus'}}, f)
            err = io.StringIO()
            with redirect_stderr(err), redirect_stdout(io.StringIO()):
                rc = U.main([d, '--override', os.path.join(d, 'ov.json'),
                             '--out', os.path.join(d, 'o.md')])
        self.assertEqual(rc, 2)

    def test_cell_escapes_pipes_and_flattens_links(self):
        self.assertEqual(U.cell('a | b [t](../x.md#y) c'), 'a \\| b t c')
        self.assertTrue(U.cell('x' * 400).endswith('…'))
        self.assertLessEqual(len(U.cell('x' * 400)), 160)


if __name__ == '__main__':
    unittest.main()
