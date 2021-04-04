import fitz
from gtts import gTTS
import os
from textblob import TextBlob
from playsound import playsound

filedirac = str(input("enter file directory: "))
os.chdir(filedirac)
filename = str(input("enter file name: "))
with fitz.open(filename) as doc:
    text = ""
    for page in doc:
        text += page.getText()

language = TextBlob(text).detect_language()
ooku = gTTS(text=text, lang=language, slow=False)
ooku.save("reading.mp3")
playsound("reading.mp3")