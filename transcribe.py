import whisper
import json

def transcribe_audio(audio_path):
    model = whisper.load_model("base")

    result = model.transcribe(
        audio_path,
        language="en",
        task="transcribe"
    )

    out = []
    for seg in result["segments"]:
        out.append({
            "start": seg["start"],
            "end": seg["end"],
            "text": seg["text"].strip()
        })

    with open("transcribe.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=4, ensure_ascii=False)

    return out


if __name__ == "__main__":
    transcribe_audio("audio.wav")
