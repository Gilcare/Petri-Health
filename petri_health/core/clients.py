import os
from anthropic import Anthropic


def get_claude_client():

    api_key = os.getenv("ANTHROPIC_API_KEY")

    if not api_key:
        raise ValueError("Missing ANTHROPIC_API_KEY")

    return Anthropic(api_key=api_key)
