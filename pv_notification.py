import os
import json
import difflib
import random
from tkinter import *
import pyttsx3
from playsound import playsound
from difflib import get_close_matches
from plyer import notification
import random
import requests
import datetime
import time

l=[]

while True:
    data=json.load(open("C:\\Users\\aditya singh\\Downloads\\data.json"))
    res = random.choice(list((data.items())))
    first_word=list(res[0])
    word_string=''.join(first_word)

    if len(word_string)>5:
        pass

    else:
        res = random.choice(list((data.items())))
        first_word=list(res[0])
        word_string=''.join(first_word)
    get_word=data.get(word_string)
    str_getword=''.join(get_word)

    if str_getword!="ISO 639-6 entity":
        pass

    else:
        res = random.choice(list((data.items())))
        first_word=list(res[0])
        word_string=''.join(first_word)

        if len(word_string)>5:
            pass

        else:
            res = random.choice(list((data.items())))
            first_word=list(res[0])
            word_string=''.join(first_word)
        get_word=data.get(word_string)
        str_getword=''.join(get_word)
    l.append(word_string)
    print(l)

    if len(l)<8:
        pass

    else:
        l=l[::-1]
        l.pop()
        l=l[::-1]
        print(l)

    notification.notify(title="The power Vocabe of the day on {}".format(datetime.date.today()),
                        message="the power word for the day is: {}\nMeaning: {}".format(word_string,str_getword),
                        app_icon='C:\\Users\\aditya singh\\Downloads\\icon3.ico',
                        timeout = 8)

    time.sleep(8)
