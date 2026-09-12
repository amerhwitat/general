import csv
import tempfile
import unittest
from pathlib import Path

from webcontactcrawler import Contact, extract_contacts, import_csv, import_txt, export


class WebContactCrawlerTests(unittest.TestCase):
    def test_extracts_normal_and_obfuscated_emails_and_keyword_score(self):
        html = """
        <html><title>Research Team</title><body>
        Contact research@example.org or alice [at] example [dot] com.
        </body></html>
        """
        rows = extract_contacts(html, "https://example.org/team", ["research", "team"])
        emails = {r.email for r in rows}
        self.assertEqual(emails, {"research@example.org", "alice@example.com"})
        self.assertEqual({r.score for r in rows}, {2})
        self.assertTrue(all("research" in r.keywords and "team" in r.keywords for r in rows))

    def test_txt_import_normalizes_and_deduplicates(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "emails.txt"
            p.write_text("A@EXAMPLE.ORG\ninvalid\na@example.org\n", encoding="utf-8")
            self.assertEqual(import_txt(p), ["a@example.org"])

    def test_csv_import_uses_email_column(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "emails.csv"
            with p.open("w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=["email", "name"])
                w.writeheader(); w.writerow({"email": "A@EXAMPLE.ORG", "name": "A"}); w.writerow({"email": "a@example.org", "name": "A2"})
            self.assertEqual(import_csv(p), ["a@example.org"])

    def test_exports_txt_and_csv(self):
        rows = [Contact("b@example.org", "https://example.org", "example.org"), Contact("a@example.org", "https://example.org", "example.org")]
        with tempfile.TemporaryDirectory() as d:
            txt = Path(d) / "out.txt"; csvp = Path(d) / "out.csv"
            export(rows, txt); export(rows, csvp)
            self.assertEqual(txt.read_text(encoding="utf-8").splitlines(), ["a@example.org", "b@example.org"])
            with csvp.open(encoding="utf-8", newline="") as f:
                self.assertEqual([r["email"] for r in csv.DictReader(f)], ["a@example.org", "b@example.org"])


if __name__ == "__main__":
    unittest.main()
