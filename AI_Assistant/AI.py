import pyttsx3
import speech_recognition
from datetime import date, datetime

# for extensive purpose
import wikipedia
import os

def startGoogle():
    global run
    run = False
    # speak('starting google')        #dòng này có cũng được không có cũng không sao :v

    os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')  # mở google (và các file khác)

def playmusic():
    global run
    music_dir = 'D:\Music'          # thư mục để nhạc
    songs = os.listdir(music_dir)
    os.startfile(os.path.join(music_dir,songs[0]))
    run = False

def wiki(keyword):
    # speak('searching on wikipedia')
    try:
        print('**Result from wiki**')
        print(wikipedia.summary(keyword))       # search wiki
    except:
        print('Some error occurred! Try again.')
        print('')
    run = False

"""
# demo:
    startGoogle()
    playmusic()
    wiki(data) #đưa vào tham số 'data' là từ khóa cần tìm
"""

# Listen
result = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("[AI]: I'm listening...")
    result.adjust_for_ambient_noise(mic)
    audio = result.listen(mic, timeout = 3) # Only listen in 3 sec

try:
    your_order = result.recognize_google(audio)
except:
    your_order = ""

print("[you]: ", your_order)

# Think
if your_order == "":
    AI_ans = "Please try again :("
elif "fuck you" in your_order:
    AI_ans = "Fuck you too :D"
elif "google" in your_order or "Google" in your_order:
    startGoogle()
    AI_ans = "Search for yourself, fucker!!"
elif "music" in your_order:
    playmusic()
    AI_ans = "Looking for some good songs on your device!"
elif  "hi" in your_order or "hello" in your_order:
    AI_ans = "Hello there!"
elif "today" in your_order or "day" in your_order:
    today = date.today()
    AI_ans = today.strftime("Today is %B %d, %Y")
elif "time" in your_order:
    now =  datetime.now()
    AI_ans = now.strftime("The current time is %H hours %M minutes %S seconds")
else:
    AI_ans = "Something went wrong! Please try again"

print("[AI]: ", AI_ans)
# Speak
engine = pyttsx3.init()
engine.say(AI_ans)
engine.runAndWait()
