# src/audio.py

from moviepy import VideoFileClip
from pathlib import Path

def extract_audio(video_path: Path, audio_path: Path) -> None:
    """Extract audio from a video file."""
    video = VideoFileClip(str(video_path))
    video.audio.write_audiofile(
        str(audio_path),
        codec="pcm_s16le",
        logger=None
    )
    video.close()



