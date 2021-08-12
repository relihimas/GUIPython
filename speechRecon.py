#pip install SpeechRecognition
#pip install pyaudio

import speech_recognition as sr #speech to text
import time
import pyttsx3
from reportlab.pdfgen import canvas

r = sr.Recognizer()

mic = sr.Microphone()

with mic as source:
    audio = r.listen(source)
    order = r.recognize_google(audio, language='pt-br')

print(order)

def generatePDF(texto):
    try:
        nome_pdf = "Teste"
        pdf = canvas.Canvas(f'{nome_pdf}.pdf')
        x = 720
        pdf.setTitle(nome_pdf)
        pdf.drawString(247, x, texto)
        pdf.setFont('Helvetica-Oblique',14)
        pdf.save()
        print("PDF gerado com sucesso")
    except:
        print("Erro ao gerar o pdf")

generatePDF(order)




#### TEXT TO SPEECH ####
engine = pyttsx3.init()
engine.say(order)
engine.runAndWait()

print("Fim")
