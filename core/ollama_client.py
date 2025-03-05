import requests
from utils.config import OLLAMA_MODEL

class OllamaClient:
    """
    A client for connecting to locally installed Ollama models.
    """
    
    def __init__(self, base_url="http://localhost:11434"):
        self.base_url = base_url
        self.model = OLLAMA_MODEL

    def connect(self, prompt: str):
        """
        Sends a request to the locally running Ollama model.
        :param prompt: The input text to send to the model.
        :return: The model's response or an error message.
        """
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
        }

        try:
            response = requests.post(url, json=payload, timeout=10)
            response.raise_for_status()
            return response.json().get("response", "No response received.")
        except requests.exceptions.RequestException as e:
            return f"Connection error: {e}"

    def test_connection(self):
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

# Example usage (for testing)
if __name__ == "__main__":
    client = OllamaClient()
    print(client.test_connection())
