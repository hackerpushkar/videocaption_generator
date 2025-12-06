from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def overlay_subtitles(video_path, segments, output_path):
    video = VideoFileClip(video_path)
    clips = []

    for seg in segments:
        txt = TextClip(
            seg["text"],
            fontsize=32,
            color="white",
            stroke_color="black",
            stroke_width=2
        )
        txt = txt.set_start(seg["start"]).set_duration(seg["end"] - seg["start"])
        # txt = txt.set_position(("center", "bottom"))
        txt.set_position(lambda t: ('center', video.h*0.8))
        clips.append(txt)

    final = CompositeVideoClip([video] + clips)
    final.write_videofile(output_path)


# for more details checkout this blog because i learn about this module from this 
# https://codewithtj.blogspot.com/2025/03/how-to-add-text-and-captions-to-your.html
