from logging import exception
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    speak("Hello ma'am!")
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 15:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis. How may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        speak("Sorry! I did not understand. Please say that again.")
        print("Sorry! I did not understand. Please say that again.\n")
        return "None"

    return query

if __name__ == "__main__":
    start = takeCommand().lower()
    if 'jarvis' in start:
        wishMe()
        flag = True
        while flag == True:
            query = takeCommand().lower()

            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=1)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"Time: {strTime}")
                speak(f"Ma'am, The time is {strTime}")
            
            elif "date" in query:
                strDate = datetime.datetime.now().strftime("%d%m%Y")
                months = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
                print(strDate)
                speak(f"today's date is {months[(int(strDate[:2]))]} {strDate[2:4]} {strDate[4:]}")

            elif 'search' in query or 'what is' in query:
                webbrowser.open(f"https://www.google.com/search?q={query}&rlz=1C1RLNS_enIN973IN973&sxsrf=ALiCzsaCNlbRllUgWsk_jitXE3vy25mzgA%3A1665244874925&ei=yp5BY__9N8yI4-EPlq2-8A4&ved=0ahUKEwj_iu_JgNH6AhVMxDgGHZaWD-4Q4dUDCA4&uact=5&oq=bye&gs_lcp=Cgdnd3Mtd2l6EAMyCgguELEDENQCEEMyCgguELEDENQCEEMyCgguELEDENQCEEMyCgguELEDENQCEEMyBAgAEEMyBAguEEMyBwgAELEDEEMyBwgAELEDEEMyBQgAEIAEMgcIABCxAxBDOgoIABBHENYEELADOg0IABBHENYEELADEMkDOgcIABCwAxBDOg0IABDkAhDWBBCwAxgBOgwILhDIAxCwAxBDGAI6DwguENQCEMgDELADEEMYAjoHCCMQ6gIQJzoECCMQJzoECC4QJzoFCAAQkQI6CAguEIAEELEDOgsIABCABBCxAxCDAUoECEEYAEoECEYYAVCrEVirHGD9ImgCcAF4BYAB0wWIAZoSkgELMC4xLjQuNS0xLjGYAQCgAQGwAQrIARPAAQHaAQYIARABGAnaAQYIAhABGAg&sclient=gws-wiz")
            
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
            
            elif  'open mail' in query:
                webbrowser.open("gmail.com")
            
            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open code' in query:
                path = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(path)

            elif 'goodbye' in query:
                speak("Goodbye ma'am. Have a good day.")
                print("Bye Bye")
                flag = False

