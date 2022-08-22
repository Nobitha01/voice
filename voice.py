from setuptools import Command
import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
# import flask

engine =pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
recognizer=sr.Recognizer()

def cmd():
    with sr.Microphone() as sourse:
        print('Cleaning background noises..Please wait')
        recognizer.adjust_for_ambient_noise(sourse,duration=0.5)
        print('Ask me anything..')
        recordedaudio=recognizer.listen(sourse)

    
    try:
        text=recognizer.recognize_google(recordedaudio,language='en_US')
        text=text.lower()
        print('Your message:',format(text))

    except Exception as ex:
        print(ex)

    if 'chrome' in Command:
        a='Opening chrome..'
        engine.say(a)
        engine.runAndWait()
        programName = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([programName])
    if 'time' in Command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say(time)
        engine.runAndWait()
    if 'play' in Command:
        a='opening youtube..'
        engine.say(a)
        engine.runAndWait()
        pywhatkit.playonyt(text)
    if 'youtube' in Command:
        b='opening youtube'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('www.youtube.com')
while True:
    cmd()
