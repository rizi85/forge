import requests
import json
from utils.config import OLLAMA_MODEL
from utils.config import BASE_URL

class OllamaClient:
    #A client for connecting to locally installed Ollama models.
   
    def __init__(self):
        self.base_url = BASE_URL
        self.model = OLLAMA_MODEL

    def connect(self, prompt: str, prompt_source: str = None) -> str:
        #Buid prompt based on user input
        #Sends a request to OpenAI's model - prompt only
        if not prompt_source:
            prompt = prompt
        #Sends a request to OpenAI's model - prompt and source
        else:
            prompt = prompt + "\n\n" + prompt_source

        #Send request to Ollama model
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": True  # Handle streamed responses correctly
        }

        try:
            response = requests.post(url, json=payload, timeout=10, stream=True)
            response.raise_for_status()
            
            response_text = ""
            for line in response.iter_lines():
                if line:
                    try:
                        json_data = line.decode("utf-8")
                        parsed_data = json.loads(json_data)  # Use json.loads instead of requests.utils.json
                        response_text += parsed_data.get("response", "") + ""
                    except (json.JSONDecodeError, ValueError):
                        continue
            
            return response_text.strip() if response_text else "Unexpected response format from Ollama API."
        except requests.exceptions.RequestException as e:
            return f"Connection error: {e}"

    def test_connection(self) -> str:
        """
        Tests if the Ollama API is reachable and if the model is available.
        :return: Success message or an error message.
        """
        url = f"{self.base_url}/api/tags"

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            models = response.json().get("models", [])
            if any(m["name"] == self.model for m in models):
                return f"Successfully connected to Ollama model: {self.model}"
            return f"Model '{self.model}' not found in locally installed models."
        except requests.exceptions.RequestException as e:
            return f"Failed to connect to Ollama API: {e}"
