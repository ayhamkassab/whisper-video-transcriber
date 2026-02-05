# Whisper Video Transcriber

A simple Python code for automatic transcription of video interviews using **OpenAI Whisper**

This tool:
- Extracts audio from `.mp4` video files
- Transcribes speech using OpenAI Whisper
- Outputstimestamped interview-style transcripts



Installation

git clone https://github.com/ayhamkassab/whisper-video-transcriber

cd whisper-video-transcriber



Install dependencies

pip install -r requirements.txt


Install FFmpeg

sudo apt install ffmpeg



Place .mp4 files into: data/videos/

Run python src/main.py


Transcripts will be saved to: data/transcripts/





