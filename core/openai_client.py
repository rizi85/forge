from openai import OpenAI
from utils.config import CHATGPT_MODEL
from utils.config import OPENAI_API_KEY

class OpenAIClient:
    def __init__(self):
        self.api_key = OPENAI_API_KEY
        self.model = CHATGPT_MODEL
        
        if not self.api_key:
            raise ValueError("OpenAI API key is missing in configuration.")
        
        self.client = OpenAI()
        self.client.api_key = self.api_key
    
    def connect(self, prompt: str, prompt_source: str = None) -> str:

        try:
            #Buid prompt based on user input
            #Sends a request to OpenAI's model - prompt only
            if not prompt_source:
                prompt = prompt
            #Sends a request to OpenAI's model - prompt and source
            else:
                prompt = prompt + "\n\n" + prompt_source

            #Send request to OpenAI model
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                stream=True
            )

            #Get model response
            response_text = ""
            for chunk in response:
                if chunk.choices:
                    delta_content = chunk.choices[0].delta.content
                    if delta_content:
                        response_text += delta_content
            
            return response_text.strip() if response_text else "Unexpected response format from OpenAI API."
        except Exception as e:
            return f"Connection error: {e}"
    
    def test_connection(self) -> str:
        """
        Tests if OpenAI API is reachable and if the model is available.
        :return: Success message or an error message.
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "system", "content": "Ping"}]
            )
            if response and response.choices:
                return f"Successfully connected to OpenAI model: {self.model}"
            return f"Model '{self.model}' is not responding as expected."
        except Exception as e:
            return f"Failed to connect to OpenAI API: {e}"
    
    def set_model(self, model_name):
        """Update the model used for generating responses."""
        self.model = model_name
