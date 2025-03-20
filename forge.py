#!/usr/bin/env python3

import argparse
import sys
from utils.prompt_manager import PromptManager
from core.ollama_client import OllamaClient
from core.openai_client import OpenAIClient
from core.google_client import GooglePalmClient
#from core.anthropic_client import AnthropicClient
from utils.config import SPARKS_FILE, OUTPUT_FILE

def get_llm_client(model_name):
    #Returns the appropriate LLM client based on user input.
    clients = {
        "ollama": OllamaClient,
        "openai": OpenAIClient,
        "google": GooglePalmClient
    }
    
    if model_name not in clients:
        raise ValueError(f"Invalid model: {model_name}. Choose from: {', '.join(clients.keys())}")
    
    return clients[model_name]()

def print_logo():
    logo = """
░▒█▀▀▀░▄▀▀▄░█▀▀▄░█▀▀▀░█▀▀
░▒█▀▀░░█░░█░█▄▄▀░█░▀▄░█▀▀
░▒█░░░░░▀▀░░▀░▀▀░▀▀▀▀░▀▀▀
Forge v0.1.0-alpha
    """
    print(logo)

class CustomArgumentParser(argparse.ArgumentParser):
    def print_help(self):
        print_logo()
        super().print_help()

def main():

    #Handles argument parsing and orchestrates LLM query process.
    parser = CustomArgumentParser(
        description="Forge CLI for querying different LLMs with Sparks.",
        epilog="Example usage: ./forge.py -s my_spark -m openai -u https://example.com -f input.txt",
        add_help=True  # Ensures the help option is automatically included
    )
    parser.add_argument("-s", "--spark", required=True, help="Spark name (folder name inside /sparks)")
    parser.add_argument("-m", "--model", default="ollama", help="LLM model to use (default: ollama)")
    parser.add_argument("-u", "--url", help="URL input for the Spark, if required")
    parser.add_argument("-f", "--file", help="File input for the Spark, if required")
    parser.add_argument("-v", "--video", help="YouTube video URL for the Spark, if required")
    parser.add_argument("-i", "--input", help="Optional input text for the Spark. Reads from stdin if omitted.")
    
    args = parser.parse_args()

    # Read the prompt from the Spark file
    prompt = PromptManager.read_prompt_from_spark_file(args.spark)

    # Check if the Spark requires an URL
    if args.url:
        prompt_url = PromptManager.read_url(args.url)

    # Check if the Spark requires a file
    if args.file:
        prompt_file = PromptManager.read_local_file(args.file)

    # Check if the Spark requires a YouTube video
    if args.video:
        prompt_video = PromptManager.read_youtube_video(args.video)

    # Check if the Spark requires an input
    if args.input:
        prompt_input = PromptManager.read_input_text(args.input)
    else:
    # Read from stdin if no input is provided    
        try:
            if not sys.stdin.isatty():  # Works for Linux/macOS and most Windows cases
                prompt_input = sys.stdin.read().strip()
            else:
                prompt_input = None
        except Exception as e:
            print(f"Error reading stdin: {e}", file=sys.stderr)
            sys.exit(1)

    # Initialize and use the selected LLM client
    try:
        llm_client = get_llm_client(args.model)

        # Query LLM with a prompt
        response = llm_client.connect(prompt)

        # Query LLM with a prompt and file
        if args.file:
            response = llm_client.connect(prompt, prompt_file)

        # Query LLM with a prompt and URL
        if args.url:
            response = llm_client.connect(prompt, prompt_url)
        
        # Query LLM with a prompt and YouTube video
        if args.video:
            response = llm_client.connect(prompt, prompt_video)
        
        # Query LLM with a prompt and input text
        if args.input or not sys.stdin.isatty():
            response = llm_client.connect(prompt, prompt_input)

        # Print LLM response
        print(response)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()