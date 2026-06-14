from petri_health.models.claude_model import ClaudeModel


class ModelRouter:

    def __init__(self, model_name="claude"):
        self.model_name = model_name

        if model_name == "claude":
            self.model = ClaudeModel()
        else:
            raise ValueError(f"Unknown model: {model_name}")

    def generate(self, prompt: str) -> str:
        return self.model.generate(prompt)
