#Modules require
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)    #0 is David voice, 1 is Zira voice
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)       # Wish
    if hour>=0 and hour<12:
        speak('Good Morning sir!')
    elif hour>=12 and hour<18:
        speak('Good afternoon sir!')
    else:
        speak('Good evening sir!')

    speak("I am Jarvis sir, how may I help you? ")

def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold= 1
        audio = r.listen(source)

    try:
        print('Recognizing.....')
        query= r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)

        speak("Sir, please say that again.... ")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('tejasgidde2000@gmail.com ','prakash1')
    server.sendmail('tejasgidde2000@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    wishme()
    while True:
        query =takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia, please wait.....')
            query= query.replace('wikipedia',"")
            results = wikipedia.summary(query, sentences=1)
            speak("Sir, According to wikipedia")
            speak(results)



        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")
        elif 'gmail' in query:
            webbrowser.open("gmail.com")

        elif 'play music' in query:
            music_dir = 'E:\\Music\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"sir,the time is{strTime}")

        elif 'open teams ' in query:
            path = "C:\\Users\\tejas\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Teams"
            os.startfile(path)


        elif 'email to prakash'in query:
            try:
                speak("What should I say????")
                content = takecommand()
                to ="mahalakshmiinduction@gmail.com"
                sendEmail(to, content)
                speak("Email has sent, sir")
            except Exception as e:
                print (e)
                speak("sorry sir, I am not able to send this email")

        elif 'thankyou  jarvis'in query:
            speak("Its my duty sir")





