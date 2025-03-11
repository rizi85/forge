#!/usr/bin/env python3

import argparse
import os
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

def main():
    #Handles argument parsing and orchestrates LLM query process.
    parser = argparse.ArgumentParser(description="Forge CLI for querying different LLMs with Sparks.")
    parser.add_argument("-s", "--spark", required=True, help="Spark name (folder name inside /sparks)")
    parser.add_argument("-m", "--model", default="ollama", help="LLM model to use (default: ollama)")
    parser.add_argument("-u", "--url", help="URL input for the Spark, if required")
    parser.add_argument("-f", "--file", help="File input for the Spark, if required")
    
    args = parser.parse_args()

    # Read the prompt from the Spark file
    prompt = PromptManager.read_prompt_from_spark_file(args.spark)

    # Check if the Spark requires an URL
    if args.url:
        prompt_url = PromptManager.read_url(args.url)

    # Check if the Spark requires a file
    if args.file:
        prompt_file = PromptManager.read_local_file(args.file)

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
        
        # Print LLM response
        print(response)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()