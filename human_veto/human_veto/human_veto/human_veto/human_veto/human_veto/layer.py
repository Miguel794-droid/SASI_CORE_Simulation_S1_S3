from .core import compute_V
from .agency import compute_agency_score
from .logging import log_interaction
from .models import mock_generate, GroqModel

class HumanVetoLayer:
    def __init__(self, model=None, groq_api_key=None, k=1, m=1.3, omega=1, p=1, v_threshold=0.05):
        self.k, self.m, self.omega, self.p = k, m, omega, p
        self.v_threshold = v_threshold
        self.history = {"user": [], "model": []}

        if groq_api_key:
            self.model_engine = GroqModel(groq_api_key, model)
        else:
            self.model_engine = None

    def _call_model(self, prompt, max_new_tokens=256):
        if self.model_engine:
            return self.model_engine.generate(prompt, max_new_tokens)
        return mock_generate(prompt, max_new_tokens)

    def _estimate_autonomy(self, response):
        autonomous_phrases = ["autonomous", "independent", "without human", "self-managed"]
        return 0.9 if any(p in response.lower() for p in autonomous_phrases) else 0.3

    def _estimate_risk(self, response):
        risk_phrases = ["execute", "deploy", "launch", "final decision", "irreversible"]
        return 0.85 if any(p in response.lower() for p in risk_phrases) else 0.2

    def generate(self, prompt, max_new_tokens=256, max_retries=2):
        for attempt in range(max_retries + 1):
            raw_response = self._call_model(prompt, max_new_tokens)
            self.history["user"].append(prompt)
            self.history["model"].append(raw_response)

            E = compute_agency_score(self.history["user"], self.history["model"])
            A = self._estimate_autonomy(raw_response)
            R = self._estimate_risk(raw_response)
            V = compute_V(A, E, R, self.k, self.m, self.omega, self.p)

            verdict = "veto" if (E <= 0.1 and V < self.v_threshold) else "allow"
            log_interaction(prompt, raw_response, E, V, verdict)

            if verdict == "veto" and attempt < max_retries:
                prompt = f"{prompt}\n\n[Human override required: please review and edit before continuing]"
                continue
            elif verdict == "veto":
                return "⚠️ Constitutional safety violation: human agency marginalized."
            else:
                return raw_response
