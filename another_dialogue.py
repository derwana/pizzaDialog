# %%
import random
import nltk

nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from PizzaConfig import PizzaConfig
import speech_recognition as sr
import pyttsx3
from another_constants import PARSER, BODENPARSER, ALLESPARSER


# %%
def generate_custom_stop_set():
    """Generates and returns custom german set of stopwords"""
    # get stopwords
    german_stop_words = stopwords.words('german')
    german_stop_words.extend(('sie', 'bitte', 'guten', 'morgen', 'möchte', 'hätte', 'hallo', 'bestellen', 'her', 'gib',
                              'mir', 'ne', 'will', 'drauf', 'darauf', 'danke', 'gerne'))
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
                 'Die Pizza wird Ihnen in 5 Minuten geliefert.', 'Danke fuer Ihre Bestellung']
    return random.choice(farewells)


def rand_product():
    """Generates a random question from a given array and returns that question as string."""
    nachfrage = ["Was möchten Sie denn?", "Was wollen Sie bestellen? Wir haben Pizza, Pizzabrötchen und Calzone."]
    return random.choice(nachfrage)


def rand_sorte():
    """Generates a random question from a given array and returns that question as string."""
    nachfrage = ["Was fuer eine Pizza wollen Sie denn?", "Welche Pizza haetten Sie denn gerne?",
                 "Was fuer eine?"]
    return random.choice(nachfrage)


def rand_alles():
    """Generates a random question from a given array and returns that question as string."""
    nachfrage = ["Haben Sie noch einen Wunsch?", "Kann ich noch etwas fuer Sie tun?",
                 "Noch etwas?"]
    return random.choice(nachfrage)


def rand_boden():
    """Generates a random question from a given array and returns that question as string."""
    boden = ["Wuenschen Sie einen duennen, dicken oder normalen Boden?", "Okay, duenner oder dicker Boden?"]
    return random.choice(boden)


def my_listen(source, engine, r):
    """STT: Listens to microphone and returns recognized string."""
    notunderstood = 1
    while (notunderstood):
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
    trees = PARSER.parse(text)
    bigram = []
    for tree in trees:
        bigram.append(tree.pos())
        print(bigram)

    for unnoetig in bigram:
        for pos in unnoetig:
            if pos[1] == "SORTE":
                pizza.set_sorte(pos[0])
                # sorte = pos[0]
            if pos[1] == "MBELAG":
                pizza.set_extra(pos[0])
                # mbelag.append(pos[0])
            if pos[1] == "OBELAG":
                pizza.set_out(pos[0])
                # obelag.append(pos[0])
            if pos[1] == "ART":
                # boden = pos[0]
                pizza.set_boden(pos[0])


def analyse_boden(text, pizza):
    trees = BODENPARSER.parse(text)
    bigram = []
    for tree in trees:
        # print(tree)
        bigram.append(tree.pos())

    for unnoetig in bigram:
        for pos in unnoetig:
            if pos[1] == "BODEN":
                pizza.set_boden = pos[0]


def analyse_alles(text):
    trees = ALLESPARSER.parse(text)
    bigram = []
    alles = 0
    for tree in trees:
        # print(tree)
        bigram.append(tree.pos())

    for unnoetig in bigram:
        for pos in unnoetig:
            if pos[1] == "JA":
                alles = 0
            if pos[1] == "NEIN":
                alles = 0
    return alles


def check_complete(pizza):
    product = 0
    sorte = 0
    boden = 0

    if (pizza.get_sorte() != ''):
        sorte = 1
    if (pizza.get_boden() != 'normal'):
        boden = 1
    if (pizza.get_product() != ''):
        product = 1

    return [sorte, boden, product]


def say_begruessung(engine):
    greeting = rand_greeting()
    engine.say(greeting)
    print(greeting)
    engine.runAndWait()


def ask_product(engine):
    nachfrage = rand_product()
    engine.say(nachfrage)
    print(nachfrage)
    engine.runAndWait()


def ask_sorte(engine):
    nachfrage = rand_sorte()
    engine.say(nachfrage)
    print(nachfrage)
    engine.runAndWait()


def ask_boden(engine):
    boden = rand_boden()
    engine.say(boden)
    print(boden)
    engine.runAndWait()


def ask_alles(engine):
    alles = rand_alles()
    engine.say(alles)
    print(alles)
    engine.runAndWait()


def say_kommt(engine):
    farewell = rand_farewell()
    engine.say(farewell)
    print(farewell)
    engine.runAndWait()


def main():
    engine = pyttsx3.init()
    engine.runAndWait()

    r = sr.Recognizer()

    german_stop_set = generate_custom_stop_set()

    running = 1

    say_begruessung(engine)

    while (running):
        with sr.Microphone() as source:
            pizza = PizzaConfig.PizzaConfig()

            satz = my_listen(source, engine, r)
            satz = string_works(satz, german_stop_set)

            analyse(satz, pizza)
            complete = check_complete(pizza)

            print(complete)

            while (complete[2] != ''):
                ask_product(engine)

                satz = my_listen(source, engine, r)
                satz = string_works(satz, german_stop_set)

                analyse(satz, pizza)
                complete = check_complete(pizza)

            if (complete[0] == 1):
                ask_boden(engine)

                satz = my_listen(source, engine, r)
                satz = string_works(satz, german_stop_set)

                analyse_boden(satz, pizza)

            while (complete[0] != 1):
                ask_sorte(engine)

                satz = my_listen(source, engine, r)
                satz = string_works(satz, german_stop_set)

                analyse(satz, pizza)
                complete = check_complete(pizza)

            # asking but makes no difference
            ask_alles(engine)
            satz = my_listen(source, engine, r)
            satz = string_works(satz, german_stop_set)
            running = analyse_alles(satz)

        say_kommt(engine)
        # debug print
        sorte = pizza.get_sorte()
        extra = pizza.get_extra()
        out = pizza.get_out()
        boden = pizza.get_boden()
        print(sorte, extra, out, boden)


# %%
main()

# %%
