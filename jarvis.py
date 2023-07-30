import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S") 
    speak("The current time is " +Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)    
    speak("The current date is {0}/{1}/{2}" .format(month, date, year))

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\Shivam\\OneDrive\\Pictures\\Screenshots\\ss.png") 

def cpu():
    usage = str(psutil.cpu_percent())
    battery = psutil.sensor_battery()
    speak('CPU is at ' +usage)
    speak('Battery is at ' + battery.percent)

def jokes():
    speak(pyjokes.get_joke())

def wishme():
    hour = datetime.datetime.now().hour
    if hour > 6 and hour<12:
        speak ("Good Morning Sir! Welcome back")
    elif hour >=12 and hour<18:
        speak ("Good Afternoon Sir! Welcome back")
    elif hour >= 18 and hour<24:
        speak ("Good Evening Sir! Welcome back")
    else:
        speak ("Good Night Sir! Welcome back")
    time()
    date()
    speak("JARVIS at your service. Please tell me how can I help you?")    
    takeCommand()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing ...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Failed to recognize. Say that again please.")
        return "None"
    return query        

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if 'time' in query:
            time()
        
        elif 'date' in query:
            date()
        
        elif 'wikipedia' in query:
            speak('Searching ...')
            query = query.replace("Wikipedia", "")
            result = wikipedia.summary(query, sentence=2)
            print(result)
            speak(result)
        
        elif 'search in chrome' in query:
            speak('What should I search')
            chromepath = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'    
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')   
        
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        
        elif 'logout' in query:
            os.system("shutdown -l")    
        
        elif 'screenshot' in query:
            screenshot()
            speak('Done!')
        
        elif 'cpu' in query:
            cpu()    

        elif 'joke' in query:
            jokes()    
        
        elif 'offline' in query:
            quit()    