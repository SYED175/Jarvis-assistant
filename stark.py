import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')  #voice recognition command in windows sapi5
voices = engine.getProperty('voices')    #engine acts as a object


#setting voice
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good afternoon!")
    else:
        speak("Good Evening")
    speak("Asaalaam  alay kum Syed Ismail  ")


def takecmd():
    r = sr.Recognizer()
    with sr.Microphone as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=10)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query} \n")


    except Exception as e:
        print("Please say that again.....")
        return "None"
    return query

if __name__ == "__main__":
    wishme()