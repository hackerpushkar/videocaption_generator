# src/srt_builder.py
def build_srt(segments, srt_path):
    def fmt(t):
        ms = int((t - int(t)) * 1000)
        h = int(t // 3600)
        m = int((t % 3600) // 60)
        s = int(t % 60)
        return f"{h:02}:{m:02}:{s:02},{ms:03}"

    with open(srt_path, "w", encoding="utf-8") as f:
        for i, seg in enumerate(segments, start=1):
            start = fmt(seg["start"])
            end = fmt(seg["end"])
            f.write(f"{i}\n{start} --> {end}\n{seg['text']}\n\n")
