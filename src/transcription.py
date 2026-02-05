# src/transcription.py

import whisper
from pathlib import Path
from typing import List

from .formatting import format_segment

class WhisperTranscriber:
    def __init__(self, model_size: str):
        print(f"Loading Whisper model: {model_size}")
        self.model = whisper.load_model(model_size)

    def transcribe(self, audio_path: Path) -> List[str]:
        print("Transcribing audio...")
        result = self.model.transcribe(str(audio_path), verbose=False)

        transcript = []
        speaker = "Person A"

        for segment in result["segments"]:
            entry = format_segment(
                speaker=speaker,
                start=segment["start"],
                text=segment["text"]
            )
            transcript.append(entry)
            speaker = "Person B" if speaker == "Person A" else "Person A"

        return transcript



