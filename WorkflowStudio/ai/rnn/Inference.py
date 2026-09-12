from .SequenceModel import SequenceModel
class InferenceService:
    def __init__(self, model=None): self.model=model or SequenceModel()
    def anomaly(self, sequence): return self.model.score(sequence).__dict__
    def forecast(self, sequence, horizon): return {"predictions":self.model.forecast(sequence,horizon),"model_version":"reference-1"}
    def recommend_change(self, context):
        return {"action":"review","requires_approval":True,"reason":"AI recommendations are advisory","context":context}
