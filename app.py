from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import pyaudio
import os
import time
from datetime import datetime
import random
import webbrowser

r = sr.Recognizer()

def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="en-EN")
        except sr.UnknownValueError:
            print("Assistant: I cannot hear you, my brother")
        except sr.RequestError:
            print("Assistant: System does not work")
        return voice

def response(voice):
    if "hi" in voice or 'hello' in voice:
        speak("Hi Dr.Yusif, how are you today?")

    if "how are you" in voice or "how was your day" in voice or "what its going on" in voice:
        speak('I am fine, what about you')

    if "thank you" in voice:
       speak("nice")

    if "need help" in voice:
        speak("I can help you")

    if 'about yourself' in voice:
        speak('My name is Tony, I was created by Dr. Yusif. My name comes from the name of a cat whose name is also Tony. If you want to learn more about me, please let me know.')
        
        inquiry = record("Would you like to learn more about me?")
        
        if "yes" in inquiry:
            speak("Sure! I have an interesting story. Dr. Yusif, one day, decided to create a program that he could talk to. He envisioned a companion who could assist him with various tasks. Thus, I came into existence. It is said that Dr. Yusif is quite eccentric. He often talked to himself at home, and one day, he decided to create me to keep him company.")
            
        elif "no" in inquiry:
            speak("Okay, no problem.")
        else:
            speak("Sorry, I didn't catch that. Let me know if you'd like to learn more about me.")
    
    if 'dr.yusif' in voice:
        speak('He is greater person, and he need girlfriend :)')

    if "crush" in voice:
        speak("No, I'm like a walnut")
    
    if "what time is it" in voice or "current time" in voice:
        current_time = datetime.now().strftime("%I:%M %p")  # Time
        current_date = datetime.now().strftime("%A, %B %d, %Y")  # Date
        print(f"The current time is {current_time}.")
        print(f"Today's date is {current_date}.")
        speak(f"The current time is {current_time}. Today's date is {current_date}.")


    if 'search' in voice:
        speak("What you need to google?")
        search = record("What you need to google?")
        url = 'https://www.google.com/search?q=' + search
        webbrowser.get().open(url)
        print(search + ' what you asked')

    if 'youtube' in voice:
        speak("What you want me to search on youtube")
        search = record("What you want me to search on youtube")
        url = 'https://www.youtube.com/search?q=' + search
        webbrowser.get().open(url)
        print(search + ' what you asked')

    
def speak(String):
    tts = gTTS(text=String, lang="en", slow=False)
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

while True:
    voice = record()
    if voice != '':
        voice = voice.lower()
        print(voice)
        response(voice)
