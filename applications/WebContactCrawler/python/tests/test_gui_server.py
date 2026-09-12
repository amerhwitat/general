import tempfile
import unittest
from pathlib import Path

from gui_server import _safe_url, _job_snapshot

class GuiServerTests(unittest.TestCase):
    def test_safe_url_allows_http_and_https(self):
        self.assertEqual(_safe_url('https://example.org/path'), 'https://example.org/path')
        self.assertEqual(_safe_url('http://example.org'), 'http://example.org')

    def test_safe_url_rejects_credentials_and_other_schemes(self):
        with self.assertRaises(ValueError): _safe_url('ftp://example.org')
        with self.assertRaises(ValueError): _safe_url('https://user:pass@example.org')

    def test_job_snapshot_reads_last_progress_event(self):
        with tempfile.TemporaryDirectory() as d:
            event = Path(d) / 'job.events.jsonl'
            event.write_text('{"event":"page","pages":2,"emails":3}\n', encoding='utf-8')
            job = {'id':'abc','state':'running','created':1.0,'output':'x.csv','events':str(event)}
            snap = _job_snapshot(job)
            self.assertEqual(snap['progress']['pages'], 2)
            self.assertEqual(snap['progress']['emails'], 3)

if __name__ == '__main__': unittest.main()
