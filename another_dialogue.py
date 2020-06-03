import random
import nltk
from nltk import CFG
from nltk.corpus import stopwords
from PizzaConfig import PizzaConfig

import speech_recognition as sr
from gtts import gTTS
import pyttsx3
from pyttsx3 import drivers
from another_constants import *


def rand_greeting():
    """Generates a random greeting from two given array and returns that greeting as string."""
    greetings = ['Guten Morgen', 'Hallo']
    question = [', was kann ich für Sie tun?', '!']
    return random.choice(greetings) + random.choice(question)

def my_listen(source):
    notunderstood = 1
    while(notunderstood):
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        test = ""
        try:
            test = r.recognize_google(audio, language="de-de")
        except:
            engine.say("Entschuldigung, das habe ich nicht verstanden. Bitte wiederholen Sie, was Sie gesagt haben.")
            engine.runAndWait()
        notunderstood = 0
        print(test)
        return test

def analyse(text):
    sentence = text.split()
    
    sorte = ""
    mbelag = []
    obelag = []
    boden = ""

    trees = PARSER.parse(sentence)
    bigram = []
    for tree in trees:
        #print(tree)
        bigram.append(tree.pos())
    
    for unnoetig in bigram:
        for pos in unnoetig:
            if pos[1] == "SORTE":
                sorte = pos[0]
            if pos[1] == "MBELAG":
                mbelag.append(pos[0])
            if pos[1] == "OBELAG":
                obelag.append(pos[0])
            if pos[1] == "ART":
                boden = pos[0]
            if pos[1] == "N":
                return ["",[],[],""]
    pizza = [sorte, mbelag, obelag, boden]
    return pizza

def analyse_boden(text):
    sentence = text.split()
   
    trees = BODENPARSER.parse(sentence)
    bigram = []
    boden = ""
    for tree in trees:
        #print(tree)
        bigram.append(tree.pos())
        
    for unnoetig in bigram:
        for pos in unnoetig:
            if pos[1] == "BODEN":
                boden = pos[0]
    return boden

def analyse_alles(text):
    sentence = text.split()
   
    trees = ALLESPARSER.parse(sentence)
    bigram = []
    alles = 0
    for tree in trees:
        #print(tree)
        bigram.append(tree.pos())
        
    for unnoetig in bigram:
        for pos in unnoetig:
            if pos[1] == "JA":
                alles = 1
            if pos[1] == "NEIN":
                alles = 0
    return alles


def say_begruessung():
    engine.say(rand_greeting())
    engine.runAndWait()
    
def complete(pizza):
    s = 0
    m = 0
    o = 0
    b = 0
    if(pizza[0] != ""):
        s = 1
    if(pizza[1] != []):
        m = 1
    if(pizza[2] != []):
        o = 1
    if(pizza[3] != ""):
        b = 1
    complete = [s, m, o, b]
    return complete

def ask_sorte():
    engine.say("Was fuer eine Pizza wollen Sie denn?")
    engine.runAndWait()
    
def ask_boden():
    engine.say("Wuenschen Sie einen duennen oder dicken Boden?")
    engine.runAndWait()
    
def ask_alles():
    engine.say("War das alles fuer Sie?")
    engine.runAndWait()
    
def say_kommt():
    engine.say("Alles klar, kommt sofort.")
    engine.runAndWait()



import speech_recognition as sr
from gtts import gTTS
import pyttsx3
from pyttsx3 import drivers
from another_constants import *

engine = pyttsx3.init()
engine.runAndWait()

r = sr.Recognizer()

# sorte = ""
# mbelag = []
# obelag = []
# boden = ""

pizza = []


with sr.Microphone() as source:
    say_begruessung()
    satz = my_listen(source)
    pizza = analyse(satz)
    complete = complete(pizza)
    print(pizza)
    print(complete)
    
    while(complete[0] != 1):
        ask_sorte()
        satz = my_listen(source)
        sorte = analyse(satz)
        pizza = sorte
        complete = complete(pizza)
        
    while(complete[3] != 1):
        ask_boden()
        satz = my_listen(source)
        boden = analyse_boden(satz)
        pizza[3] = boden
        complete = complete(pizza)
        
    ask_alles()
    satz = my_listen(source)
    
    if(analyse_alles(satz)):
        say_kommt()
    