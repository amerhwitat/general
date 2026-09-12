import unittest

from rnn_llm_engine import RNNLLMEngine


class RNNEngineTests(unittest.TestCase):
    def test_state_changes_and_memory_is_bounded(self):
        engine = RNNLLMEngine(hidden_size=8, max_memory=2)
        first = engine.step("deploy pipeline")
        second = engine.step("incident failed")
        self.assertNotEqual(first, second)
        engine.step("third event")
        self.assertEqual(len(engine.state.memory), 2)

    def test_workflow_advisory_is_explainable(self):
        engine = RNNLLMEngine(hidden_size=8)
        result = engine.suggest_workflow_action(["production incident", "service outage"])
        self.assertEqual(result["action"], "review_incident_cluster_and_recent_deployments")
        self.assertIn("signals", result)
        self.assertGreaterEqual(result["confidence"], 0.45)


if __name__ == "__main__":
    unittest.main()
