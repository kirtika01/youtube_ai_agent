from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled
from youtube_transcript_api.formatters import TextFormatter
import re
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class YouTubeProcessor:
    def __init__(self):
        self.formatter = TextFormatter()

    def _extract_video_id(self, url):
        """Extract video ID from YouTube URL"""
       
        patterns = [
            r'(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([^&\?\/]+)',
            r'youtube\.com\/watch\?.*v=([^&]+)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        raise ValueError("Could not extract video ID from URL")

    def _get_transcript_with_language(self, video_id, language):
        """Get transcript for a specific language"""
        try:
            return YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
        except (NoTranscriptFound, TranscriptsDisabled):
            return None

    def process_video(self, url):
        """Get transcript from YouTube video"""
        logger.info(f"Processing video from URL: {url}")
        try:
            video_id = self._extract_video_id(url)
            
            logger.info("Attempting to get English transcript")
            transcript_list = self._get_transcript_with_language(video_id, 'en')
            
            if not transcript_list:
                logger.info("English transcript not found, trying Hindi auto-generated")
                transcript_list = self._get_transcript_with_language(video_id, 'hi')
            
            if not transcript_list:
                raise NoTranscriptFound("No transcript available in English or Hindi")

            if not isinstance(transcript_list, list) or len(transcript_list) == 0:
                raise ValueError("Received empty transcript from YouTube")

            transcript_text = self.formatter.format_transcript(transcript_list)
        
            if not transcript_text or not isinstance(transcript_text, str):
                raise ValueError("Failed to format transcript text")

            return transcript_text
            
        except Exception as e:
            logger.error(f"Error getting transcript: {str(e)}")
            raise Exception(f"Error getting transcript: {str(e)}")
