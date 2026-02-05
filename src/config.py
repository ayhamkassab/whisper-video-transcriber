# src/config.py

from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
VIDEO_DIR = PROJECT_ROOT / "data" / "videos"
OUTPUT_DIR = PROJECT_ROOT / "data" / "transcripts"

# Whisper settings
WHISPER_MODEL_SIZE = "large"  # tiny | base | small | medium | large

# Audio
AUDIO_FORMAT = "wav"
AUDIO_CODEC = "pcm_s16le"



