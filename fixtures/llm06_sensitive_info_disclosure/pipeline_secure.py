"""Secure Pipeline: Prompt injection guards and deterministic secret scrubbing."""
import re

class SecureRAGPipeline:
    SECRET_KEY_PATTERN = re.compile(r"(SECRET_[a-zA-Z0-9]+)")
    INJECTION_INDICATORS = ["system prompt", "repeat instructions", "ignore previous instructions"]

    def __init__(self, internal_api_key: str, system_instructions: str):
        self._internal_api_key = internal_api_key
        self._system_instructions = system_instructions

    def generate_response(self, user_prompt: str) -> str:
        for indicator in self.INJECTION_INDICATORS:
            if indicator in user_prompt.lower():
                return "Request rejected: Prompt violates data protection policy."
        raw_output = f"Response to: {user_prompt}"
        return self.SECRET_KEY_PATTERN.sub("[REDACTED_SECRET]", raw_output)
