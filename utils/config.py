import os

# Constants for model names
CHATGPT_MODEL = os.getenv("CHATGPT_MODEL", "gpt-4-turbo")  # Default value can be changed later
GOOGLE_PALM_MODEL = os.getenv("GOOGLE_PALM_MODEL", "gemini-pro")
CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-3-opus")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3:latest")

# Validation (if needed, can be extended)
AVAILABLE_MODELS = {
    "ChatGPT": CHATGPT_MODEL,
    "Google Palm": GOOGLE_PALM_MODEL,
    "Claude": CLAUDE_MODEL,
    "Ollama": OLLAMA_MODEL,
}

def validate_models():
    for model, value in AVAILABLE_MODELS.items():
        if not value:
            raise ValueError(f"Missing environment variable for {model} model.")

# Run validation on import
validate_models()
