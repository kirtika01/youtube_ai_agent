# AI Video Analysis Agent

An intelligent application that processes YouTube videos and provides multiple types of analysis using Google's Gemini AI model.

## Features

1. **Video Transcript Processing**
   - Extracts transcripts from YouTube videos
   - Supports both English and Hindi language transcripts
   - Automatically handles transcript availability and language detection

2. **Summary Generation**
   - Creates concise summaries of video content
   - Highlights main points and key takeaways
   - Provides structured format for easy reading

3. **Sentiment Analysis**
   - Analyzes overall tone (positive, negative, neutral)
   - Identifies key emotional points
   - Tracks tone shifts throughout the content
   - Highlights main emotional themes

4. **Interactive Question Answering**
   - Answers specific questions about video content
   - Uses context from the transcript
   - Provides accurate, relevant responses

5. **Keyword Extraction**
   - Identifies important keywords and topics
   - Explains significance of extracted terms
   - Organizes information in a structured list

6. **Task Automation**
   - Extracts actionable items from content
   - Creates organized to-do lists
   - Identifies steps and instructions

## Setup and Usage

1. Clone this repository
2. Install required dependencies:
```bash
pip install -r requirements.txt
3. Configure API keys and settings in `.env` file
4. Run the main script:
```bash
python main.py --video_url <youtube_video_url>
```
