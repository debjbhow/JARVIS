import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyjokes
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print('voices[0].id')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12:
        speak("Good Morning, Sir!")

    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon, Sir!")

    else:
        speak("Good Evening, Sir!")
    
    speak("I am Jarvis!, Please tell me how may I help you, Sir")

#def sendEmail (to, content):
    #server = smtplib.SMTP('smtp.gmail.com', 587)
    #server.ehlo()
    #server.starttls()
    #server.login("debjitbhowmik807@gmail.com", "###")
    #server.sendmail("debjitbhowmik1998@gmail.com", to, content)
    #server.close()

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said:  {query}\n")

    except Exception as e:
       # print(e)

        print("Sorry. Please, Say that again, Sir....")
        return "None"

    return query

if __name__ == "__main__":
    speak("Debjit is a great programmer")
    wishme()
    while True:
        query = takeCommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia......")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences= 2)
            speak("Sir, According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open instagram' in query:
            webbrowser.get('chrome').open("instagram.com")

        elif 'open facebook' in query:
            webbrowser.get('chrome').open("facebook.com") 
        
        elif 'open gaana' in query:
            webbrowser.get('chrome').open("gaana.com") 
        
        elif 'open whatsapp web' in query:
            webbrowser.get('chrome').open("web.whatsapp.com") 
        
        elif 'open flipkart' in query:
            webbrowser.get('chrome').open("flipkart.com") 
       
        elif 'open amazon' in query:
            webbrowser.get('chrome').open("amazon.in") 
        
        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir!!,The time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Debjit-pc\\AppData\\Local\\Programs\\Microsoft VS Code 2\\Code.exe"
            os.startfile(codePath)
            
         elif "who made you" in query or "who created you" in query:  
            speak("I have been created by Debjit Bhowmik") 
              
        elif 'joke' in query: 
            speak(pyjokes.get_joke())

        elif 'shutdown system' in query: 
                speak("Hold On a Sec ! Your system is on its way to shut down") 
                subprocess.call('shutdown / p /f') 

        #elif 'email to Debjit' is query:
            #try:
                #speak("What should I say"):
                #content = takeCommand()
                #to = "debjitbhowmik807@gmail.com"
                #sendEmail(to, content)
                #speak("Email has been sent")

            #except Exception as e:
                #print(e)
                #speak("Sorry! My friend Debjit, I am not able to send this e-mail")

