#pip install SpeechRecognition
#pip install pyaudio

import speech_recognition as sr #speech to text
import time
import pyttsx3

r = sr.Recognizer()

mic = sr.Microphone()

with mic as source:
    audio = r.listen(source)
    order = r.recognize_google(audio, language='pt-br')

print(order)

#### TEXT TO SPEECH ####
engine = pyttsx3.init()
engine.say(order)
engine.runAndWait()

print("Fim")
