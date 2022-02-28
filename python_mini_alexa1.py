import pywhatkit
import datetime
import sys
import wikipedia
import pyjokes
import webbrowser
import time
from datetime import date
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty("voices",voices[0].id)
engine.setProperty("rate",150)

def engine_talk(text):
    engine.say(text)
    engine.runAndWait()


def mini_alexa():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        engine_talk("start speaking.")
        print("Listening..")
        audio = r.listen(source)
        engine_talk(audio)
        
    try:
        command =r.recognize_google(audio,language="en-in")
        command = command.lower()
        
        if 'alexa' in command:
            command = command.replace('alexa','')
            print(command)
        else:
            print(command)
            
        
        if 'hello' in command:
            engine_talk("hello how can i help you.")
            
        elif 'who are you' in command:
            engine_talk("i am a mini alexa your assistant. how can i help you.")
            
        elif 'you can do' in command:
            engine_talk("i can tell you date, time , i can tell you jokes , play songs on youtube ,search on google ,wikipedia . i can open different websites like instagram ,youtube ,stack over flow ,wikipedia")
        
        elif 'what can you do' in command:
            engine_talk("i can tell you date, time , i can tell you jokes , play songs on youtube ,search on google ,wikipedia . i can open different websites like instagram ,youtube ,stack over flow ,wikipedia")
        
        elif 'date and time' in command:
            today =date.today()
            time = datetime.datetime.now().strftime('%T:%M %p')
            d2 = today.strftime("%8 %d, %Y")
            engine_talk('today is'+d2)
            engine_talk('and current time is'+time)
            
        elif 'time and date' in command:
            today =date.today()
            time = datetime.datetime.now().strftime('%T:%M %p')
            d2 = today.strftime("%8 %d, %Y")
            engine_talk('and current time is'+time)
            engine_talk('today is'+d2)
            
        elif 'today\'s time' in command:
            today =date.today()
#             time = datetime.datetime.now().strftime('%T:%M %p')
            engine_talk('current time is',today.strftime("%I"),today.strftime("%M"),today.strftime("%p"))
            
        elif 'date' in command:
            today =date.today()
#             d2 = today.strftime("%8 %d, %Y")
            engine_talk('today is:',today.strftime("%A"),today.strftime("%d"),tofay.strftime("%B"))
            
        elif 'joke' in command:
            joke = pyjokes.get_joke(language="en", category="neutral")
            engine_talk(joke)
        
        elif 'play song' in command:
            song = command.replace('play song','')
            engine_talk('playing '+song)
            pywhatkit.playonyt(song)
            
        elif 'who is' in command:
            name = command.replace('who is','')
            info = wikipedia.summary(name,sentences=5)
            engine_talk(info)
            
        elif 'what is' in command:
            thing = command.replace('what is','')
            info = wikipedia.summary(thing,sentences=5)
            engine_talk(info)
            
        elif 'wikipedia' in command:
            name = command.replace('wikipedia','')
            info = wikipedia.summary(name,sentences=5)
            engine_talk(info)
            
        elif 'search' in command:
            query = command.replace('search','')
            query ="https://www.google.com/search?q=" + query
            webbrowser.open(query)
            
        elif 'instagram' in command:
            webbrowser.open('https://www.instagram.com/')
            
        elif 'youtube' in command:
            webbrowser.open('https://www.youtube.com/')
            
        elif 'facebook' in command:
            webbrowser.open('https://www.facebook.com/')
        
        elif 'linkedin' in command:
            webbrowser.open('https://in.linkedin.com/')
                

        elif 'github' in command:
            webbrowser.open('https://github.com/')
            
        elif 'stack overflow' in command:
            webbrowser.open('https://stackoverflow.com/')
            
        elif 'my location' in command:
            webbrowser.get().open('https://www.google.com/search?q=where+i+am')
            engine_talk("you must somewhere here")
                            
        elif 'locate' in command:
            loc = command.replace('locate','')
            if 'on map' in loc:
                loc = loc.replace('on map','')
            else:
                loc = "https://www.google.com/maps/place/" + loc +'/&amp;'
                webbrowser.get().open(loc)
            engine_talk('here is that location')
            
        elif 'on map' in command:
            loc = command.replace('on map','')
            loc = "https://www.google.com/maps/place/" + loc +'/&amp;'
            webbrowser.get().open(loc)
            engine_talk('here is that location')
            
        elif 'find' in command:
            name = command.replace('find','')
            if 'on map' in name:
                loc = name.replace('on map','')
                loc = "https://www.google.com/maps/place/" + loc +'/&amp;'
                webbrowser.get().open(loc)
            info = wikipedia.summery(name,sentences=5 )
            engine_talk(info)
                
        elif 'exit' in command:
            engine_talk('Thank you.')
            sys.exit()
            
        elif 'thank you' in command:
            engine_talk('thank you')
            sys.exit()
            
        else:
            query ="https://www.google.com/search?q=" + command
            webbrowser.open(query)
            engine_talk('here is what i found on internet')

    except Exception as e:
        print(e)
        
                                     
def main():
    
    # ----------Application name :python_mini_alexa----------   

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty("voices")
#   print(voices[1])

    engine.setProperty("voices",voices[0].id)
    engine.setProperty("rate",150)

    
    print("Hello i am mini alexa how can i help you..")
    engine_talk("Hello i am mini alexa how can i help you..")
    while (True):
        mini_alexa()
        time.sleep(4)
    

if __name__ =="__main__":
    main()