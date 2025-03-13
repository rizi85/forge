![Forge Logo](/res/forge.png)

# Forge 🔥

**Forge** is a command-line tool designed to interact with various Large Language Models (LLMs) including locally installed models via Ollama, OpenAI, Google Gemini, Anthropic*.
With Forge, you can conveniently query these models from your Linux, macOS or Windows terminal using predefined prompts called "sparks".

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Multi-LLM Support**: Seamlessly switch between different LLM providers (Local LLMs via Ollama, OpenAI, Google Gemini, Anthropic*).
- **Command-Line Friendly**: Run prompts directly from your terminal without leaving your development environment.
- **Customizable Prompts**: Easily define your own prompts and tailor them to different tasks or applications.
- **Simple Python 3 Codebase**: Built purely in Python 3 for quick installation and minimal dependency management.

---

## Project Structure

```
forge/
├── core/
│   ├── openai_client.py        # Interacts with OpenAI's API
│   ├── ollama_client.py        # Interacts with local ollama API
│   ├── google_palm_client.py   # Interacts with Google PaLM API
│   └── __init__.py
├── utils/
│   ├── config.py               # Reads and validates environment variables
│   ├── logger.py               # Basic logging utility
│   └── ...
│── sparks/
│   └──test_spark/              # Spark folder
│       └── test_sprk.md        # Spark file containing the prompt
├── forge.py                    # Main script
│── requirements.txt            # Dependency file
│── .env                        # API keys and other data
└── README.md                   # You are here!
```

---

## Requirements

- Python 3
- pip or another Python package manager

**Dependencies**:  
- Official libraries for respective LLM providers, as needed (e.g. `openai`, `google-generativeai`, `anthropic`)  
- Any other libraries used for CLI or prompt management for more info view `requiremetns.txt` file

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-org/forge.git
   cd forge
   ```

2. **(Optional) Create a virtual environment**:

   ```bash
   # Linux macOS
   
   python3 -m venv .venv
   source .venv/bin/activate

   # Windows PowerShell

   python3 -m venv .venv
   .venv\Scripts\activate
   # or
   .venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Configuration

Forge requires environment variables for each LLM provider you intend to use. Below is an example of how you might set them:

*First copy and rename file .env.example to .env on local machine and replace the value of each API key with yours*
```bash
OPENAI_API_KEY=
GEMINI_API_KEY=
ANTHROPIC_API_KEY=
```

For local models make sure to make changes in /utils/config.py by adding local API URL and Port that ollama server is running on.

```bash
# Local models paths
BASE_URL = os.getenv("BASE_URL", "http://localhost:11434")
```

For specific LLM models make changes in /utils/config.py (Check provider documentation before)
```bash
# Local models paths
# Constants for model names
CHATGPT_MODEL = os.getenv("CHATGPT_MODEL", "gpt-4o")
GOOGLE_GEMINI_MODEL = os.getenv("GOOGLE_GEMINI_MODEL", "gemini-2.0-flash")
CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-3-opus")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3:latest")
```
---

## Usage

Here is a quick overview of how to use Forge from the terminal:

1. **Specify a provider and prompt**:
   ```bash
   ./forge.py -m google -s story_teller
   ```

2. **Specify a provider, a prompt, and an input file**:
   ```bash
   ./forge.py -m ollama -s summarize_file -f rocket.txt
   ```

3. **Specify a provider, a prompt, and an input URL**:
   ```bash
   ./forge.py -m openai -s summarize_page -u https://www.bbc.com/news/articles/1.html
   ```

**Options** (example):
- "-s", "--spark", required=True, help="Spark name (folder name inside /sparks)"
- "-m", "--model", default="ollama", help="LLM model to use (default: ollama)"
- "-u", "--url", help="URL input for the Spark, if required"
- "-f", "--file", help="File input for the Spark, if required"

---

## Contributing

Contributions are welcome! Here are some ways you can help:

- **Report Bugs**: File an issue with details about what went wrong and how to reproduce it.
- **Suggest Features**: Let us know if you have ideas to make Forge more flexible, useful, or user-friendly.
- **Create Pull Requests**: If you fix a bug or implement a feature, open a pull request describing your changes.

---

## License

[MIT License](LICENSE) (replace with your own if different)

---

**Happy forging!** If you encounter any issues or have questions about getting started, open a GitHub issue or contact the maintainers.
