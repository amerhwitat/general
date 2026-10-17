"""Contract checks for the reference WorkflowStudio Python API."""
from pathlib import Path
import ast
import unittest

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "services" / "python" / "main.py"


class WorkflowStudioApiContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SOURCE.read_text(encoding="utf-8")
        cls.tree = ast.parse(cls.source)

    def test_api_source_parses(self):
        self.assertIsNotNone(self.tree)

    def test_cors_is_explicitly_allowlisted(self):
        self.assertIn("CORSMiddleware", self.source)
        self.assertIn("WORKFLOW_STUDIO_CORS_ORIGINS", self.source)
        self.assertIn("allow_origins=CORS_ORIGINS", self.source)
        self.assertIn("allow_credentials=False", self.source)
        self.assertIn('"GET", "POST", "OPTIONS"', self.source)

    def test_reference_endpoints_remain_present(self):
        for route in (
            "/health",
            "/api/projects",
            "/api/work-items",
            "/api/ai/sequence-score",
        ):
            with self.subTest(route=route):
                self.assertIn(route, self.source)


if __name__ == "__main__":
    unittest.main()
