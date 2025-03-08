from pytube import YouTube
import re


from youtube_transcript_api import YouTubeTranscriptApi

def transcribe_youtube(video_url):
    """Extracts transcript from a YouTube video using YouTube's subtitles (if available)."""
    video_id = video_url.split("v=")[-1].split("&")[0]  # Extract video ID
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = " ".join([entry["text"] for entry in transcript])
        return transcript_text[:5000]
    except Exception as e:
        return f"Error: {e}"




#print(transcribe_youtube("https://www.youtube.com/watch?v=y2BaTt1fxJU&list=PLhhyoLH6IjfxeoooqP9rhU3HJIAVAJ3Vz&index=27"))