from google import genai
from utils.config import GEMINI_API_KEY
from utils.config import GOOGLE_GEMINI_MODEL

# Define the Google Gemini model to use
class GooglePalmClient:
    def __init__(self):
        self.api_key = GEMINI_API_KEY
        self.model = GOOGLE_GEMINI_MODEL

        if not self.api_key:
            raise ValueError("Google Gemini key is missing in configuration.")

        # Configure the Google PaLM client
        client = genai.Client(api_key=self.api_key)
        # We’ll store the library reference in self.client to stay consistent with the OpenAIClient pattern
        self.client = client

    def connect(self, prompt: str, file_content: str = None, page_content: str = None) -> str:

        try:

            #Buid prompt based on user input
            #Sends a request to OpenAI's model - prompt only
            if not file_content and not page_content:
                prompt = prompt
            #Sends a request to OpenAI's model - prompt and file
            elif file_content:
                prompt = prompt + "\n\n" + file_content
            #Sends a request to OpenAI's model - prompt and URL
            elif page_content:
                prompt = prompt + "\n\n" + page_content

            # PaLM's chat interface typically accepts a single list of conversation strings
            # We'll replicate the structure (user prompt only). 
            response = self.client.models.generate_content(
                model=self.model, 
                contents=prompt
            )

            # The response object may contain response candidates; we use .last for the final text
            return response.text
        except Exception as e:
            return f"Connection error: {e}"

    def test_connection(self) -> str:
        """
        Tests if the PaLM API is reachable and if the model is available.
        :return: Success message or an error message.
        """
        try:
            # Send a basic request to see if the model responds
            response = self.client.chat(
                model=self.model,
                messages=["Ping"]
            )
            if response and hasattr(response, "last"):
                return f"Successfully connected to Google PaLM model: {self.model}"
            return f"Model '{self.model}' did not respond as expected."
        except Exception as e:
            return f"Failed to connect to Google PaLM API: {e}"

    def set_model(self, model_name: str):
        #Update the model used for generating responses.
        self.model = model_name
