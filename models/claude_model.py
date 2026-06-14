from anthropic import Anthropic
import os


class ClaudeModel:

    def __init__(self):
        self.client = Anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )

    def generate(self, prompt: str) -> str:

        response = self.client.messages.create(
            model="claude-3-5-sonnet-latest",
            max_tokens=800,
            temperature=0,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.content[0].text
