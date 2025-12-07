# main.py
from extract_audio import extract_audio
from transcribe import transcribe_audio
from srt_builder import build_srt
from overlay import overlay_subtitles

video_path = "input/video.mp4"
audio_path = "output/audio.wav"
srt_path = "output/subtitles.srt"
final_video_path = "output/final_video.mp4"

extract_audio(video_path, audio_path)
segments = transcribe_audio(audio_path)
build_srt(segments, srt_path)
overlay_subtitles(video_path, segments, final_video_path)
