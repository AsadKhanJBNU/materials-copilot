import os
from google import genai


class LLMInterface:
    def __init__(self):
        api_key = os.environ.get("GEMINI_API_KEY", "").strip()

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY environment variable is not set. "
                "Set it before running the app (e.g. export GEMINI_API_KEY=your_key)."
            )

        self.client = genai.Client(api_key=api_key)
        self.model_name = "models/gemini-2.5-flash"

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
            config={
                "temperature": 0.2,
                "top_p": 0.9,
                "max_output_tokens": 4096
            }
        )

        return response.text