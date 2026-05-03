# core/llm_client.py
#
# Purpose:
# Provide a single reusable interface to the local LLM through Ollama.
#
# Design notes:
# - One shared client instance is created once for the whole run.
# - The public API is intentionally tiny: ask_llm(prompt: str) -> str.
# - Model configuration stays centralized here for easy tuning.

from typing import Final

from langchain_ollama import OllamaLLM


# Local model configuration.
_MODEL_NAME: Final[str] = "llama3.2:1b"
_TEMPERATURE: Final[float] = 0.0


# Shared client instance used by the analyzer.
_llm: OllamaLLM = OllamaLLM(model=_MODEL_NAME, temperature=_TEMPERATURE)


def ask_llm(prompt: str) -> str:
    """
    Send a prompt to the local Ollama model and return the raw response string.

    Args:
        prompt: Full prompt text prepared by the analyzer.

    Returns:
        The model response as a stripped string.
    """
    return _llm.invoke(prompt).strip()