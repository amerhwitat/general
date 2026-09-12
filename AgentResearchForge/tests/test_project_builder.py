import unittest
from AgentResearchForge.project_builder.generator import ProjectGenerator

class TestBuilder(unittest.TestCase):
    def test_generates_without_execution(self):
        m = ProjectGenerator().render(ProjectGenerator().plan('build a small agent', 'python'))
        self.assertIn('main.py', m.files)
        self.assertFalse(m.execute_after_review)
    def test_rejects_unknown_language(self):
        with self.assertRaises(ValueError): ProjectGenerator().plan('x', 'unknown')

if __name__ == '__main__': unittest.main()
