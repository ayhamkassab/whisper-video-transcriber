# src/main.py

import os
from pathlib import Path

from config import VIDEO_DIR, OUTPUT_DIR, WHISPER_MODEL_SIZE
from audio import extract_audio
from transcription import WhisperTranscriber

def process_video(video_path: Path, transcriber: WhisperTranscriber):
    print(f"\nProcessing video: {video_path.name}")

    audio_path = video_path.with_suffix(".wav")
    extract_audio(video_path, audio_path)

    transcript = transcriber.transcribe(audio_path)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_file = OUTPUT_DIR / f"{video_path.stem}_transcript.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n\n".join(transcript))

    audio_path.unlink()
    print(f"Saved transcript → {output_file.name}")

def main():
    if not VIDEO_DIR.exists():
        raise FileNotFoundError(f"Video directory not found: {VIDEO_DIR}")

    transcriber = WhisperTranscriber(WHISPER_MODEL_SIZE)

    for file in os.listdir(VIDEO_DIR):
        if file.endswith(".mp4"):
            process_video(VIDEO_DIR / file, transcriber)

if __name__ == "__main__":
    main()



