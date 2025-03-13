from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

class YouTubeTranscriptFetcher:
    def __init__(self, video_url):
        self.video_url = video_url
        self.video_id = self.extract_video_id()

    def extract_video_id(self):
        # Extracts the video ID from the given YouTube URL.
        parsed_url = urlparse(self.video_url)
        if parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
            return parse_qs(parsed_url.query).get("v", [None])[0]
        elif parsed_url.hostname in ["youtu.be"]:
            return parsed_url.path.lstrip("/")
        return None

    def get_transcript(self, languages=['en']):
        # Fetches the transcript of the video in the given language(s).
        if not self.video_id:
            raise ValueError("Invalid YouTube URL provided.")
        
        try:
            transcript = YouTubeTranscriptApi.get_transcript(self.video_id, languages=languages)
            return " ".join([entry["text"] for entry in transcript])
        except Exception as e:
            return f"Error fetching transcript: {str(e)}"

"""Example usage
if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    fetcher = YouTubeTranscriptFetcher(video_url)
    transcript = fetcher.get_transcript()
    print(transcript)
"""