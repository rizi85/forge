#!/usr/bin/env python3

import argparse
import os
from utils.prompt_manager import PromptManager
from core.ollama_client import OllamaClient
from core.openai_client import OpenAIClient
#from core.gemini_client import GeminiClient
#from core.anthropic_client import AnthropicClient
from utils.config import SPARKS_FILE, OUTPUT_FILE

def get_llm_client(model_name):
    #Returns the appropriate LLM client based on user input.
    clients = {
        "ollama": OllamaClient,
        "openai": OpenAIClient
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
    
    # Validate spark path
    spark_path = os.path.join(SPARKS_FILE, args.spark, f"{args.spark}.md")
    if not os.path.isfile(spark_path):
        print(f"Error: No such spark '{spark_path}' found.")
        return
    
    # Read the prompt file from the Spark folder
    spark_file = os.path.join(SPARKS_FILE, args.spark, f"{args.spark}.md")
    if not os.path.isfile(spark_file):
        print(f"Error: Spark not found in {args.spark}")
        return
    
    prompt = PromptManager.read_prompt(spark_file)
    
    # Append optional inputs if provided
    if args.url:
        prompt += f"\nURL: {args.url}"
    if args.file:
        if os.path.isfile(args.file):
            with open(args.file, "r", encoding="utf-8") as file:
                file_content = file.read()
            prompt += f"\nFile Content:\n{file_content}"
        else:
            print(f"Error: File '{args.file}' not found.")
            return
    
    # Initialize and use the selected LLM client
    try:
        llm_client = get_llm_client(args.model)
        response = llm_client.connect(prompt)
        
        # Print and save response
        print(response)
        PromptManager.write_response(OUTPUT_FILE, response)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()