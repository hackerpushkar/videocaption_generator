from moviepy.editor import VideoFileClip

def extract_audio(video_path, audio_path):
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_path)

