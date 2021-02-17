import os
import json
import difflib
import pyttsx3
from playsound import playsound
from difflib import get_close_matches
import speech_recognition

engine = pyttsx3.init()
engine.setProperty("rate", 125)

data = json.load(open("C:\\Users\\aditya singh\\Downloads\\data.json"))
choice = "y"


def extract(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        choice = input("\nDid you mean %s ?\n\nEnter y if yes AND n if no:\n" % get_close_matches(word, data.keys())[0])

        if (choice == "y"):
            return data[get_close_matches(word, data.keys())[0]]
        else:
            print("\nSorry, unfortunatly we donn't have the meaning of the word you entered")
            engine.say("This word doesn't exist in the dictionary. Please enter correct word")
            engine.runAndWait()
            engine.stop()

while choice == "y":
    option = input("DO you want to speak(press s) or type(press t) the word: ")
    if option == "s":
        r = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as Source:
            print("Speak anything")
            audio = r.listen(Source)
            print("Recognising...")
        try:
            text = r.recognize_google(audio)
            print("you said: {}".format(text))
            to_search = text
        except:
            print("Unable to understand, please try again!")
    else:
        to_search = input("Enter the word you want to search\n").lower()

    result_str = ""
    result = extract(to_search)

    if result == None:
        choice = input("Do you want to continue searching for the meaning?(y/n)")
        if choice == "y":
            pass
        else:
            print("\nOK then have a nice day,BYE")
            engine.say("OK then have a nice day,  BYE")
            engine.runAndWait()
            engine.stop()
            exit()
    else:
        for i in range(len(result)):
            result_str += result[i]
            result_str += " "
        x = result_str.split(". ")
        for i in x:
            print("\n", i)

        engine.say(result_str)
        engine.runAndWait()
        engine.stop()

        c = input("Do you want to continue searching for the meaning?(y/n)")
        if c == "y":
            pass
        else:
            print("\nOK then have a nice day,BYE")
            engine.say("OK then, have a nice day,  BYE")
            engine.runAndWait()
            engine.stop()
            exit()
