import pyttsx3
import speech_recognition as sr
import random

engine = pyttsx3.init('sapi5')
voice_s = engine.getProperty('voices')
engine.setProperty('voice', voice_s[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def Takecommand():
    r = sr.Recognizer()

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        # Say that again will be printed in case of improper voice
        print("Say that again please...")
        speak("Please tell the name!")
        exit()
        # return "None"  # None string will be returned
    return query

if __name__ == "__main__":
    speak("Welcome to Snake, Water, Gun Game")
    speak("Iam playing game with you my name is Jarvis!")
    speak("Please tell me what's your name!")

    Name = Takecommand().lower()
    speak(f"Ok {Name} Now starting the game!")
    
    game_list = ["python","water","ak 47"]
    Jarvis_p = 0
    User_p = 0
    chances = 1

    while chances < 6:
        Jarvis = random.choice(game_list)
        game_inp = Takecommand().lower()

        if game_inp == "python" and Jarvis == "ak 47":
            Jarvis_p += 1
            speak("You loose!")
            speak("your choice is snake! My choice is gun!")
            speak(f"1 points created to me")
            print("Updated Points......")
            print(f"{Name} Points:- {User_p}".center(35))
            print(f"Jarvis Points:- {Jarvis_p}".center(35))
                
        elif game_inp == "water" and Jarvis == "python":
            Jarvis_p += 1
            speak("You loose!")
            speak("your choice is Water! My choice is snake!")
            speak(f"1 points created to me")
            print("Updated Points......")
            print(f"{Name} Points:- {User_p}".center(35))
            print(f"Jarvis Points:- {Jarvis_p}".center(35))

        elif game_inp == "ak 47" and Jarvis == "water":
            Jarvis_p += 1
            speak("You loose!")
            speak("your choice is gun! My choice is water!")
            speak(f"1 points created to me")
            print("Updated Points......")
            print(f"{Name} Points:- {User_p}".center(35))
            print(f"Jarvis Points:- {Jarvis_p}".center(35))
                
        elif Jarvis == "python" and game_inp == "ak 47":
            User_p += 1
            speak("You Won!")
            speak("your choice is gun! My choice is snake!")
            speak(f"1 points created to you")
            print("Updated Points......")
            print(f"{Name} Points:- {User_p}".center(35))
            print(f"Jarvis Points:- {Jarvis_p}".center(35))

        elif Jarvis == "water" and game_inp == "python":
            User_p += 1
            speak("You Won!")
            speak("your choice is snake! My choice is water!")
            speak(f"1 points created to you")
            print("Updated Points......")
            print(f"{Name} Points:- {User_p}".center(35))
            print(f"Jarvis Points:- {Jarvis_p}".center(35))
                
        elif Jarvis == "ak 47" and game_inp == "water":
            User_p += 1
            speak("You Won!")
            speak("your choice is water! My choice is gun!")
            speak(f"1 points created to you")
            print("Updated Points......")
            print(f"{Name} Points:- {User_p}".center(35))
            print(f"Jarvis Points:- {Jarvis_p}".center(35))
                
        elif Jarvis == game_inp:
            speak("Game is tied 0 Points credited to both")
            speak(f"your choice is {game_inp}! My choice is {Jarvis}")
            print("Updated Points......")
            print(f"{Name} Points:- {User_p}".center(35))
            print(f"Jarvis Points:- {Jarvis_p}".center(35))

        else:
            speak("Do not recognize correct inputs!")
            exit()

        print(f"{5-chances} - chances left!".rjust(35))  
        chances += 1

    speak("The result of the game is!")
    if User_p > Jarvis_p:
        print("\nCONGRADULATIONS YOU WON THE GAME!")
        speak("Congradulation! You Won the game with me!")

    elif User_p < Jarvis_p:
        print("\nOOP'S YOU LOOSE THE GAME!")
        speak("Oops's! You Loose the game with me!")

    elif User_p == Jarvis_p:
        print("\nOHH GAME IS TIED")
        speak("Oh! Game is Tied! with me")
