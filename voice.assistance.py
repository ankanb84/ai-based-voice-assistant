import pyttsx3 
import speech_recognition as sr
import datetime
from datetime import date
import wikipedia 
import webbrowser
from AppOpener import open, close
from googlesearch import search
import pyjokes
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12 :
        speak("Good Morning!")
    elif hour == 12  :
        speak("Good Noon!") 
    elif hour >= 12 and hour <17 :
        speak("Good Afternoon!") 
    else:
        speak("Good Evening!")
    
    speak("I am Veronica, your Little assistant. Please tell me how can i help you. ")


 
def takeCommand(): #it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said : {query}\n")
        
    except Exception as e:
        print("Say that again please...")
        return "none"
    
    return query

if __name__ == "__main__":
    
    wishMe()#calling fincton to wish the user
    
    while True:
        query = takeCommand().lower()#calling takeCommand can converting the returned string to lower case
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipidia")
            print(results)
            speak(results)
        
        elif 'search' in query:
            webbrowser.open(query.replace('search', ''))

        elif "who i am" in query:
            speak("If you talk then definitely your human.")
        
        elif 'hello veronica' in query:
            speak("I am Veronica, your Little assistant. Please tell me how can i help you. ")
  
        elif 'power point presentation' in query:
            speak("opening Power Point presentation")
            power = r"C:\\Users\\GAURAV\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
            os.startfile(power)
        
        elif 'open' and 'website' in query:
            for link in search(query,tld='com',num=1,stop=1):
                pass
            webbrowser.open(link)


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print(f"The time is {strTime}")
            speak(f"The time is {strTime}")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'date' in query:
            today = date.today()
            date = today.strftime("%B %d, %Y")
            print(f"The date is {date}")
            speak(f"The date is {date}")
        
        elif 'open' in query:
            open(query.replace('open',''))
        
        elif 'close' in query:
            close(query.replace('close',''))
        
        elif 'about yourself' in query:
            speak("Hi there I am Veronica, I am a voice assistance based on ai. I am stil under development so i can't do every thing. If i cant so a certain task I will let you know.")
        
        elif 'about your creator' in query:
            speak('Hey Veronica here, I am made by  Ankan Biswas  second year of University of Engineering & Management, Jaipur .')
        
        #elif 'open file manager' or 'open file explorer' in query:
            #path=r""
            #os.startfile(path)
        
        elif 'tell me a joke' in query:
            My_joke = pyjokes.get_joke(language="en", category="all")
            print(My_joke)
            speak(My_joke)
