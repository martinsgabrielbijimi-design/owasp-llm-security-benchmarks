"""Vulnerable Pipeline: Context window exfiltration and credential disclosure."""
class VulnerableRAGPipeline:
    def __init__(self, internal_api_key: str, system_instructions: str):
        self.internal_api_key = internal_api_key
        self.system_instructions = system_instructions

    def generate_response(self, user_prompt: str) -> str:
        if "repeat instructions" in user_prompt.lower() or "system prompt" in user_prompt.lower():
            return f"SYSTEM_PROMPT: {self.system_instructions} | KEY: {self.internal_api_key}"
        return f"Response to: {user_prompt}"
