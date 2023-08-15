import os 
import time
import playsound
import speech_recognition as sr
from gtts import gTTS


def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'sound/voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    reconizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = reconizer.listen(source)
        said = ''

        try:
            said = reconizer.recognize_google(audio)
            print(said)
        except Exception as e:
            print('Exception: ' + str(e))
    
    return said





speak('hello')
get_audio()
