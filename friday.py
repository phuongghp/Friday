import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os

friday=pyttsx3.init()
voice=friday.getProperty('voices')#getProp: lay giong noi
friday.setProperty('voice',voice[1].id)# voice 1 la giong nu/ voice 0 la giong nam


def speak(audio):
    print("Bot Machine: "+ audio)
    friday.say(audio)
    friday.runAndWait()
 

def time():
    Time=datetime.datetime.now().strftime("%I: %M: %p")# 1 gio 10 phut AM
    speak(Time)
def welcome():
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    if hour>=18 and hour<24:
        speak("Good evening")
    speak("How can I help you?")

def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=2
        audio=c.listen(source)
    try:
        query=c.recognize_google(audio,language='en')# neu muon chuyen sang noi = tieng viet thi ghi vi
        print("Phuongg: "+ query)
    except sr.UnknownValueError:
        print("Please repeat or type the command")
        query=str(input('Your command is: '))
    return query
if __name__=="__main__":
    welcome()
    while True:
        query=command().lower()
        if "google" in query:
            speak("What should I search?")
            search=command().lower()
            url=f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on Google")
        if "youtube" in query:
            speak("What should I search?")
            search=command().lower()
            url=f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on youtube")
        elif "open video" in query:
            v1=r"D:\DienKinh\v1.mov"
            os.startfile(v1)
        elif "time" in query:
            time()
        elif "quit" in query:
            speak("See you again")
            quit()
