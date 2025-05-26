# PromptToVideo

A web application that converts text prompts into animated videos using Manim and Google's Gemini AI.

## Features

- Text-to-video generation using Manim animations
- Powered by Google's Gemini AI for code generation
- Optional text-to-speech voiceover
- Modern web interface with real-time status updates
- Video preview and playback

## Prerequisites

- Python 3.8+
- Manim (with required dependencies)
- Google Gemini API key

## Installation

1. Clone the repository:
```bash
https://github.com/sachin62025/PromptToVideo.git
cd PromptToVideo
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your Gemini API key in `app/services/llm_service.py`
 - You need to give your Gemini API key
## Usage

1. Start the server:
```bash
uvicorn app.main:app --reload
```

2. Open your browser and navigate to `http://127.0.0.1:8000/`

3. Enter your prompt describing the animation you want to create

4. Click "Generate Video" and wait for the process to complete

## Project Structure

```
PromptToVideo/
├── app/
│   ├── main.py
│   ├── services/
│   │   ├── llm_service.py
│   │   ├── manim_service.py
│   │   ├── tts_service.py
│   │   └── merge_service.py
│   └── routes/
|             |── video.py
|
├── manim_scenes/
├── static/
│   ├── css/
│   └── js/
├── templates/
└── outputs/
```

## How It Works

1. User submits a text prompt through the web interface
2. The prompt is sent to Gemini AI to generate Manim code
3. The generated code is executed to create a video
4. Optional text-to-speech is generated for voiceover
5. Video and audio are merged into the final output
6. The result is displayed in the web interface

## License

MIT License
