import os
from openai import OpenAI

class TextGenerator:
    def __init__(self, api_key=None):
        # Use API key from parameter or fallback to environment
        self.client = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))

        # Load client-specific greeting from .env
        self.system_prompt = os.getenv(
            "GREETING_MESSAGE",
            "You are a helpful virtual receptionist."
        )

    def generate_response(self, conversation_history):
        # Prepend system prompt to conversation
        messages = [{"role": "system", "content": self.system_prompt}] + conversation_history

        # Call GPT-4
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=messages
        )

        return response.choices[0].message.content
