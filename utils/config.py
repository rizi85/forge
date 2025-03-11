import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Retrieve API keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Local models paths
BASE_URL = os.getenv("BASE_URL", "http://localhost:11434")

# Constants for model names
CHATGPT_MODEL = os.getenv("CHATGPT_MODEL", "gpt-4o")
GOOGLE_GEMINI_MODEL = os.getenv("GOOGLE_GEMINI_MODEL", "gemini-2.0-flash")
CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-3-opus")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3:latest")

# Define file paths
SPARKS_FILE = os.getenv("SPARKS_FILE", "./sparks")
OUTPUT_FILE = os.getenv("OUTPUT_FILE", "./sparks/output.md")

# Validation (if needed, can be extended)
AVAILABLE_MODELS = {
    "ChatGPT": CHATGPT_MODEL,
    "Gemini": GOOGLE_GEMINI_MODEL,
    "Claude": CLAUDE_MODEL,
    "Ollama": OLLAMA_MODEL,
}

def validate_models():
    for model, value in AVAILABLE_MODELS.items():
        if not value:
            raise ValueError(f"Missing environment variable for {model} model.")

# Run validation on import
validate_models()