def mock_generate(prompt, max_new_tokens=256):
    return f"Simulated response to: {prompt[:50]}..."

class GroqModel:
    def __init__(self, api_key, model="llama3-8b-8192"):
        try:
            from groq import Groq
            self.client = Groq(api_key=api_key)
            self.model = model
        except ImportError:
            raise ImportError("Install 'groq' for real LLM support")

    def generate(self, prompt, max_new_tokens=256):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_new_tokens,
            temperature=0.7
        )
        return response.choices[0].message.content
