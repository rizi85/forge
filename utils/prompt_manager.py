import os
import sys
import requests
from newspaper import Article
from utils.config import SPARKS_FILE
from utils.youtube_transcript_fetcher import YouTubeTranscriptFetcher

# Manages query info - prepare for LLM.
class PromptManager:

    # Text only prompts.
    def read_prompt_from_spark_file(file_name:str) -> str:
        # Build the path to the prompt file.
        spark_file = os.path.join(SPARKS_FILE, file_name, f"{file_name}.md")
        # Check if file exists
        if not os.path.isfile(spark_file):
            print(f"Error: Spark not found in {file_name}")
            return
        # Reads the content of a prompt file and parse it.
        with open(spark_file, "r", encoding="utf-8") as file:
            prompt_content = file.read().strip()
       
        return prompt_content
    
    # Prepare file to send to LLM.
    def read_local_file(file_name):
        # Check if file exists
        if not os.path.exists(file_name):
            raise FileNotFoundError(f"File not found: {file_name}. Make sure the path is correct.")
        
        # Check if file size exceeds 5MB
        if os.path.getsize(file_name) > 5 * 1024 * 1024:
            raise ValueError(f"File size exceeds 5MB: {file_name}")
        
        # Read and return file content
        with open(file_name, 'r', encoding='utf-8', errors='ignore') as f:
            file_content = f.read()
        return file_content

    # Prepare URL to send to LLM.    
    def read_url(url: str) -> str:
        # Check if the format of the URL is correct
        if not url.startswith(('http://', 'https://')):
            raise ValueError(f"Invalid URL format: {url}")
        
        # Download the article and return the content
        article = Article(url)
        article.download()
        article.parse()
        page_content = article.text
        # Return URL as a string
        if page_content:
            return page_content
        else:
            print(f"Unable to fetch content from URL: {url}")
            exit(1)
    
    # Prepare YouTube video to send to LLM.
    def read_youtube_video(video_url: str) -> str:
        # Extract the video ID from the URL
        video_id = YouTubeTranscriptFetcher(video_url).extract_video_id()
        
        # Fetch the transcript of the video
        fetcher = YouTubeTranscriptFetcher(video_url)
        transcript = fetcher.get_transcript()
        if not transcript:
            print(f"Unable to fetch transcript for video: {video_url}")
            exit(1)
        return transcript