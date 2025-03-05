from utils.prompt_manager import PromptManager
from core.ollama_client import OllamaClient
from utils.config import SPARKS_FILE, OUTPUT_FILE

def main():
    """
    Orchestrates reading a prompt, sending it to Ollama, and saving the response.
    """
    try:
        # Read the prompt
        prompt = PromptManager.read_prompt(SPARKS_FILE)
        
        # Initialize Ollama client
        ollama_client = OllamaClient()
        
        # Send the prompt to the model
        response = ollama_client.connect(prompt)
        
        # Print and save response
        print("\nModel Response:\n", response)
        PromptManager.write_response(OUTPUT_FILE, response)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()