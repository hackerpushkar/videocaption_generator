# Auto Subtitle Generator

Automates subtitle creation for any video: extracts audio, transcribes speech using Whisper, builds subtitle files, and overlays captions on the video.

---

## Features

- Converts any video to audio  
- Transcribes speech to text (English or Hindi)  
- Outputs subtitles in JSON and SRT formats  
- Burns subtitles into the video  
- Configurable caption position (center, bottom, top)

---

## Project Structure

```
auto-subtitles/
├── extract_audio.py
├── transcribe.py
├── srt_builder.py
├── overlay.py
├── main.py
├── requirements.txt
├── input/
│   └── video.mp4
└── output/
    ├── audio.wav
    ├── subtitles.srt
    └── final_video.mp4
```

---

## Requirements

### Python dependencies

Listed in `requirements.txt`:

```
moviepy
ffmpeg-python
torch
openai-whisper
```

Install using:

```
pip install -r requirements.txt
```

---

## System Dependencies

### FFmpeg (required)

Verify:

```
ffmpeg -version
```

If missing, download from:  
https://www.gyan.dev/ffmpeg/builds/

Add `<ffmpeg>/bin` to PATH.

---

### ImageMagick 6.x (required for subtitle rendering)

MoviePy TextClip uses ImageMagick **convert.exe**.

Download from:  
https://download.imagemagick.org/archive/binaries/

Choose any file named:

```
ImageMagick-6.x.x-Q16-HDRI-x64-dll.exe
```

Verify:

```
convert -version
```

It must show ImageMagick 6.x output.

---

## How It Works

1. Audio extracted from video  
2. Whisper transcribes audio  
3. JSON + SRT generated  
4. Subtitles burned into video  

---

## Output

After running:

```
python main.py
```

You get:

- `output/audio.wav`
- `output/subtitles.srt`
- `output/final_video.mp4`

---

## Subtitle Position Options

Choose inside overlay script:

- `("center", "center")` → center  
- `("center", "bottom")` → bottom  
- `("center", "top")` → top  

---

## License

MIT License.
