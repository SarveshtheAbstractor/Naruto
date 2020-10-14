import pyttsx3
import speech_recognition   as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<16:
        speak("Good AfterNoon")
    elif hour>=16 and hour<19:
        speak("Good Evening")
    else:
        speak("Good Night") 
    speak("I am Naruto. I will become Hokage one day for sure")
        
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ",query)
    except Exception as e:
        print(e)
        print("Can You Say that Again?, Please..")
        return "None"
    return query

    


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to wikipedia ")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.register('firefox',
                                None,
                                webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe")) #path should be the user's where the browser is located.
            webbrowser.get('firefox').open('youtube.com')

        elif 'open google' in query:
            webbrowser.register('firefox',
                                None,
                                webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe")) #path should be the user's where the browser is located.
            webbrowser.get('firefox').open('google.com')
        elif 'open stackoverflow' in query:
            webbrowser.register('firefox',
                                None,
                                webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe")) #path should be the user's where the browser is located.
            webbrowser.get('firefox').open('stackoverflow.com')
        elif 'play music' in query:
            music_dir =    'D:\\MUSIC\\Jarvis'  #path should be the user's where the music is located.
            songs = os.listdir(music_dir)
            n = random.randint(0,len(songs)-1)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[n]))

        elif 'time' in query:
            strTime =   datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is: {strTime}")


        elif 'open code' in query:
            codePath = "C:\\Users\\{Your PC Username}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" #path should be the user's where the VScode is located.
            os.startfile(codePath)
        #elif 'email to receiver' in query:
           # try:
               # speak("What Should I say?")
                #content = takeCommand()
                #to = "Receivers Email"
                #sendEmail(to,content)
                #speak("Email Has been Sent")

           # except Exception as e:
                #print(e)
                #speak("Sorry friend I cannot Send this Email due to some Reasons")
                
            
            

        
