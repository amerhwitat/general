from ai_fabric import AIFabric, DISCIPLINES

def test_all_disciplines_are_available():
    assert len(DISCIPLINES) == 6
    assert set(DISCIPLINES) == {"ml", "dl", "rl", "symbolic_ai", "computer_vision", "nlp"}

def test_job_manifest():
    job = AIFabric().make_job("nlp", "tokenize", "text", framework="spacy")
    assert job.manifest()["schema"] == "CHIMERA-AI-JOB-1"
