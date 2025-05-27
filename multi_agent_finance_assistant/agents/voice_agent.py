import whisper
import pyttsx3

model = whisper.load_model("base")
tts = pyttsx3.init()

def speech_to_text(audio_path):
    result = model.transcribe(audio_path)
    return result['text']

def text_to_speech(text):
    tts.say(text)
    tts.runAndWait()
