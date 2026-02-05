# src/formatting.py

from datetime import timedelta

def format_timestamp(seconds: float) -> str:
    return str(timedelta(seconds=int(seconds)))

def format_segment(speaker: str, start: float, text: str) -> str:
    timestamp = format_timestamp(start)
    return f"{speaker}: ({timestamp})\n    - {text.strip()}"


