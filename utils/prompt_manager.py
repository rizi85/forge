import os

class PromptManager:
    """
    Manages reading and writing prompts from/to files.
    """
    @staticmethod
    def read_prompt(file_path: str) -> str:
        """
        Reads the content of a prompt file.
        :param file_path: Path to the file containing the prompt.
        :return: The content of the file as a string.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Prompt file not found: {file_path}")
        
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read().strip()

    @staticmethod
    def write_response(file_path: str, response: str):
        """
        Writes a model response to a file.
        :param file_path: Path to the file where response will be saved.
        :param response: The response text to be saved.
        """
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(response)
