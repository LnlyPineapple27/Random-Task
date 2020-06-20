import speech_recognition

result = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("[AI]: I'm listening....")
    audio = result.listen(mic)
try:
    your_order = result.recognize_google(audio)
except:
    your_order == ""

print(your_order)
