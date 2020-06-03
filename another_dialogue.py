#%%
import random
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk import CFG
from nltk.corpus import stopwords
from PizzaConfig import *
from PizzaConfig import PizzaConfig

import speech_recognition as sr
from gtts import gTTS
import pyttsx3
from pyttsx3 import drivers
from another_constants import *

#%%
def generate_custom_stop_set():
    """Generates and returns custom german set of stopwords"""
    # get stopwords
    german_stop_words = stopwords.words('german')
    german_stop_words.extend(('guten', 'morgen', 'möchte', 'hätte', 'hallo', 'bestellen', 'her', 'gib', 'mir', 'ne', 'will', 'drauf', 'darauf', 'danke', 'gerne'))
    # make it a set to be faster
    german_stop_set = set(german_stop_words)
    # remove some needed stopwords from set
    needed_words = ['mit', 'ohne', 'kein', 'extra', 'nicht']
    german_stop_set = [word for word in german_stop_set if word not in needed_words]

    return german_stop_set

def rand_greeting():
    """Generates a random greeting from two given array and returns that greeting as string."""
    greetings = ['Guten Morgen', 'Hallo']
    question = [', was kann ich fuer Sie tun?', '!']
    return random.choice(greetings) + random.choice(question)

def rand_farewell():
    """Generates a random farewell from a given array and returns that farewell as string."""
    farewells = ['Ihre Pizza wird in 5 Minuten geliefert!', 'Gut, kommt.',
                 'Die Pizza wird Ihnen in 5 Minuten geliefert.']
    return random.choice(farewells)

def rand_nachfrage():
    """Generates a random question from a given array and returns that question as string."""
    nachfrage = ["Was fuer eine Pizza wollen Sie denn?", "Welche Pizza haetten Sie denn gerne?",
                 "Was fuer eine?"]
    return random.choice(nachfrage)

def rand_alles():
    """Generates a random question from a given array and returns that question as string."""
    nachfrage = ["Ist das alles?", "Kann ich noch etwas für Sie tun?",
                 "Haben Sie noch einen Wunsch?", "Noch etwas?"]
    return random.choice(nachfrage)

def my_listen(source, engine, r):
    """STT: Listens to microphone and returns recognized string."""
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

def string_tokenize(string_input):
    """Tokenizes the string_input argument. Returns a list of tokens."""
    return nltk.word_tokenize(string_input)

def cut_stopwords(string_input, stop_set):
    """Cuts given stopwords in stop_set argument from string_input argument. Returns a list words."""
    return [word for word in string_input if word not in stop_set]

def string_works(string_input, stop_set):
    """Wrapper for string_tokenize(string_input) and cut_stopwords(string_input, stop_set). Returns a list."""
    string_input.lower()
    string_tokenized = string_tokenize(string_input)
    tokenized_output = cut_stopwords(string_tokenized, stop_set)
    return tokenized_output

def analyse(text, pizza):
    #sentence = text.split()
    
    # sorte = ""
    # mbelag = []
    # obelag = []
    # boden = ""

    trees = PARSER.parse(text)
    bigram = []
    for tree in trees:
        #print(tree)
        bigram.append(tree.pos())
        print(bigram)
    
    for unnoetig in bigram:
        for pos in unnoetig:
            if pos[1] == "SORTE":
                print("Ich bin hier.")
                pizza.set_sorte(pizza, pos[0])
                #sorte = pos[0]
            if pos[1] == "MBELAG":
                pizza.set_extra(pizza, pos[0])
                #mbelag.append(pos[0])
            if pos[1] == "OBELAG":
                pizza.set_out(pizza, pos[0])
                #obelag.append(pos[0])
            if pos[1] == "ART":
                # boden = pos[0]
                pizza.set_boden(pizza, pos[0])
            #if pos[1] == "N":
                #return ["",[],[],""]
    #pizza = [sorte, mbelag, obelag, boden]
    #return pizza

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
   
    trees = ALLESPARSER.parse(text)
    bigram = []
    alles = 0
    for tree in trees:
        #print(tree)
        bigram.append(tree.pos())
        
    for unnoetig in bigram:
        for pos in unnoetig:
            if pos[1] == "JA":
                alles = 0
            if pos[1] == "NEIN":
                alles = 0
    return alles

def say_begruessung(engine):
    engine.say(rand_greeting())
    engine.runAndWait()
    
def complete(pizza):
    s = 0
    m = 0
    o = 0
    #b = 0

    if(pizza.get_sorte() != ''):
        s = 1
    if(pizza.get_extra() != []):
        m = 1
    if(pizza.get_out != []):
        o = 1

    # if(pizza[0] != ""):
    #     s = 1
    # if(pizza[1] != []):
    #     m = 1
    # if(pizza[2] != []):
    #     o = 1
    # if(pizza[3] != ""):
    #     b = 1
    complete = [s, m, o]
    return complete

def ask_sorte(engine):
    engine.say(rand_nachfrage())
    engine.runAndWait()
    
def ask_boden(engine):
    engine.say("Wuenschen Sie einen duennen oder dicken Boden?")
    engine.runAndWait()
    
def ask_alles(engine):
    engine.say(rand_alles())
    engine.runAndWait()
    
def say_kommt(engine):
    engine.say(rand_farewell())
    engine.runAndWait()

def main():
    engine = pyttsx3.init()
    engine.runAndWait()

    r = sr.Recognizer()


    #pizza = []

    pizzaList = []
    german_stop_set = generate_custom_stop_set()

    running = 1

    say_begruessung(engine)

    while(running):
        with sr.Microphone() as source:
            pizza = PizzaConfig.PizzaConfig()

            satz = my_listen(source, engine, r)
            satz = string_works(satz, german_stop_set)
            analyse(satz, pizza)
            komplett = complete(pizza)
            print(pizza)
            print(komplett)
            
            while(komplett[0] != 1):
                ask_sorte(engine)
                satz = my_listen(source, engine, r)
                satz = string_works(satz, german_stop_set)
                #sorte = analyse(satz)
                analyse(satz, pizza)
                #pizza = sorte
                komplett = complete(pizza)
                
            # while(komplett[3] != 1):
            #     ask_boden(engine)
            #     satz = my_listen(source, engine, r)
            #     boden = analyse_boden(satz)
            #     pizza[3] = boden
            #     komplett = complete(pizza)
                
            ask_alles(engine)
            satz = my_listen(source, engine, r)
            satz = string_works(satz, german_stop_set)
            running = analyse_alles(satz)
            
        if(analyse_alles(satz)):
            say_kommt(engine)
    
#%%
main()

# %%
