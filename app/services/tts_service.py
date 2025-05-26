from gtts import gTTS
import os

def generate_audio(text: str) -> str:
    """Generate audio from text using Google Text-to-Speech."""
    output_path = "outputs/audio.mp3"
    os.makedirs("outputs", exist_ok=True)
    
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save(output_path)
    
    return output_path
