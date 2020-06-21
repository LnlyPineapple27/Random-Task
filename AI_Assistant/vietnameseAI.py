# Input
import speech_recognition
from gtts import gTTS
import os

robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("[AI]: listening...")
    audio = robot_ear.listen(mic)

robot_brain = "I don't know wtf you r talking 'bout! Have a nice day :)"

try:
    your_order = robot_ear.recognize_google(audio, Language = 'vi-VN')
    print("[You]: ", your_order)
    if "Xin chào" in your_order or "chào" in your_order:
        robot_brain = "Chào em! Anh đứng đây từ chiều :)"
except:
    print("[You]: ", robot_brain)



# Output
tts = gTTS(text = robot_brain, lang = 'vi')
tts.save("pcvoice.mp3")
os.system("start pcvoice.mp3")
