import pyaudio
import json
from vosk import Model, KaldiRecognizer

def listening():
    while 1:
        data = stream.read(
            4_000,
            exception_on_overflow=False,
            )
        
        if data and recognizer_ua.AcceptWaveform(data):
            answer = json.loads(recognizer_ua.Result())
            text = answer.get('text')
            if text:
                yield text
        if data and recognizer_en.AcceptWaveform(data):
            answer = json.loads(recognizer_en.Result())
            text = answer.get('text')
            if text:
                yield text

six_trhousands = 16*10**3

recognizer_en = KaldiRecognizer(
    Model('vosk-model-small-en-us-0.15'),
    six_trhousands,
)

recognizer_ua = KaldiRecognizer(
    Model('vosk-model-small-uk-v3-nano'),
    six_trhousands,
)

words = pyaudio.PyAudio()
stream = words.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=six_trhousands,
    input=True,
    frames_per_buffer=8192,
)

stream.start_stream()
for text in listening():
    print(f'User: {text}')
    if "слава україні" in text:
        print("Героям слава")
    if "батько наш" in text:
        print("Бандера")
    if "україна" in text:
        print("мати")
    if "stop" in text:
        print("ok")
        break
    if "доброго ранку" in text:
        print("Доброго ранку, чим будешь снідати?")
    if "доброго дня" in text:
        print("Доброго дня, чим будешь обідати?")
    if "доброго вечора" in text:
        print("Доброго вечора, чим будешь вечеряти?")
    
    if "good morning" in text:
        print("Good morning, what will you have for breakfast?")
    if "good afternoon" in text:
        print("Good afternoon, what will you have for lunch?")
    if "good evening" in text:
        print("Good evening, what will you have for dinner?")
    
