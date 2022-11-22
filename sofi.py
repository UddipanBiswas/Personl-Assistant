from datetime import datetime
from distutils.cmd import Command
from re import A
import speech_recognition as sr
import pyttsx3 as tts
import pywhatkit
import datetime
import wikipedia
import pyjokes

engine = tts.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

talk("hello, i am Sofi, what can i do for you?")
listener = sr.Recognizer()
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source, phrase_time_limit=5)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'sophie' in command or 'sofi' in command:
                command = command.replace("sophie ", "").replace("sofi ", "")
                talk(command)
            else:
                print(command)
                return False
    except:
        pass
    return command

def run_sophie():
    command = take_command()
    
    if not command:
        return

    if 'play' in command:
        song = command.replace('play ', "" )
        talk("playing " + song)
        pywhatkit.playonyt(song)

    

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("current time is " + time)
    
    elif 'joke' in command:
        talk(pyjokes.get_joke())

    

    elif 'date' in command:
        talk('I would go anywhere you take me')

    elif 'do you love me' in command:
        talk('Sorry i am in a relationship with wifi')

    elif 'how are you' in command:
        talk('i am good until the wifi is connected')

    elif 'who are you' in command:
        talk('i am sophie, i am your personal assistant')  


    elif  'stop' in command:
        talk('hope i was helpfull')
        exit()

    elif 'you are the best' in command:
        talk("don't make me blush, we are the best")   



    
    elif 'wikipedia' or 'what is' in command:
        term = command.replace('wikipedia ', "")
        info = wikipedia.summary(term, 2)
        talk(info)
      
   

    else:
        talk("I couldn't understand you, please repeat the command")

while True:
    run_sophie()