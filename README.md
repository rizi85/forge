![Forge Logo](forge.png)

# Forge 🔥

**Forge** is a command-line tool designed to interact with various Large Language Models (LLMs) including OpenAI, Anthropic, and Google PaLM. With Forge, you can conveniently query these models from your Linux or macOS terminal using predefined prompts called "sparks".

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Multi-LLM Support**: Seamlessly switch between different LLM providers (OpenAI, Anthropic, Google PaLM).
- **Command-Line Friendly**: Run prompts directly from your terminal without leaving your development environment.
- **Customizable Prompts**: Easily define your own prompts and tailor them to different tasks or applications.
- **Simple Python 3 Codebase**: Built purely in Python 3 for quick installation and minimal dependency management.

---

## Project Structure

```
forge/
├── core/
│   ├── openai_client.py        # Interacts with OpenAI's API
│   ├── anthropic_client.py     # Interacts with Anthropic's API
│   ├── google_palm_client.py   # Interacts with Google PaLM API
│   └── __init__.py
├── cli/
│   ├── forge_cli.py            # Main CLI entry point
│   └── prompts/                # Collection of predefined prompt templates
│       ├── coding_prompts.json
│       ├── summarization_prompts.json
│       └── ...
├── utils/
│   ├── config.py               # Reads and validates environment variables
│   ├── logger.py               # Basic logging utility
│   └── ...
├── tests/
│   ├── test_openai_client.py
│   ├── test_anthropic_client.py
│   └── test_google_palm_client.py
├── setup.py                    # Package setup script
└── README.md                   # You are here!
```

- **`core/`**: Houses clients for each LLM provider's API.
- **`cli/forge_cli.py`**: Main executable for command-line interactions.
- **`cli/prompts/`**: Directory for storing or referencing predefined prompt templates.
- **`utils/`**: Helper scripts, e.g. configuration or logging.
- **`tests/`**: Contains unit tests for all major functionalities.
- **`setup.py`**: Standard Python package setup script.

---

## Requirements

- Python 3.8+ (recommended)
- pip or another Python package manager

**Dependencies**:  
- `requests` or your preferred library for HTTP requests  
- Official libraries for respective LLM providers, as needed (e.g. `openai`, `google-generativeai`, `anthropic`)  
- Any other libraries used for CLI or prompt management

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-org/forge.git
   cd forge
   ```

2. **(Optional) Create a virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   Or if you have a `setup.py`:
   ```bash
   pip install .
   ```

---

## Configuration

Forge requires environment variables for each LLM provider you intend to use. Below is an example of how you might set them:

```bash
# OpenAI
export OPENAI_API_KEY="sk-..."

# Anthropic
export ANTHROPIC_API_KEY="api_..."

# Google PaLM
export GOOGLE_PALM_API_KEY="..."

# Optionally, for specifying your default LLM provider:
export FORGE_DEFAULT_PROVIDER="openai"  # or "anthropic", "google"
```

You can place these in your shell startup file (`.bashrc`, `.zshrc`) or manage them via a tool like `direnv`.

---

## Usage

Hereâ€™s a quick overview of how to use Forge from the terminal:

1. **Run the CLI**:
   ```bash
   python forge/cli/forge_cli.py --help
   ```

2. **Specify a provider and prompt**:
   ```bash
   python forge/cli/forge_cli.py        --provider openai        --prompt "Write a short poem about the sunrise."
   ```

3. **Use a predefined prompt**:
   ```bash
   python forge/cli/forge_cli.py        --provider anthropic        --template summarization_prompts.json        --context "A long piece of text to summarize"
   ```

**Options** (example):
- `--provider`: Which LLM API to call.  
- `--prompt`: A direct prompt string.  
- `--template`: Name of a predefined prompt or template file.  
- `--context`: Additional text to feed into a template.  

---

## Examples

1. **Interactive Shell** (if available):
   ```bash
   python forge/cli/forge_cli.py --interactive
   ```
   Type your questions or commands directly, and get responses in real-time.

2. **Code Generation**:
   ```bash
   python forge/cli/forge_cli.py        --provider openai        --prompt "Generate a Python function to parse JSON data."
   ```

3. **Batch Processing** (pseudo-code):
   ```bash
   python your_script_that_calls_forge.py
   ```
   Where `your_script_that_calls_forge.py` automates multiple queries to the Forge library.

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
