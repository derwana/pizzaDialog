# %%
import random
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from PizzaConfig import PizzaConfig
import speech_recognition as sr
import pyttsx3
from another_constants import PARSER, BODENPARSER, ALLESPARSER, MENUEPARSER, SORTEN


# %%
def generate_custom_stop_set():
    """Generates and returns custom german set of stopwords"""
    # get stopwords
    german_stop_words = stopwords.words('german')
    german_stop_words.extend(('sie', 'bitte', 'guten', 'morgen', 'möchte', 'hätte', 'hallo', 'bestellen', 'her', 'gib',
                              'mir', 'ne', 'will', 'drauf', 'darauf', 'danke', 'gerne', 'können', 'zeigen', 'nehmen',
                              'sehen', 'nehme', 'tag', 'lieber'))
    # make it a set to be faster
    german_stop_set = set(german_stop_words)
    # remove some needed stopwords from set
    needed_words = ['mit', 'ohne', 'kein', 'extra', 'nicht', 'oder']
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
    nachfrage = ["Was moechten Sie denn?", "Was wollen Sie bestellen? Wir haben Pizza, Pizzabroetchen und Calzone."]
    return random.choice(nachfrage)


def rand_sorte():
    """Generates a random question from a given array and returns that question as string."""
    nachfrage = ["Was fuer eine Sorte wollen Sie denn?", "Welche Sorte haetten Sie denn gerne?",
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
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    recognized = ""
    try:
        recognized = r.recognize_google(audio, language="de-de")
    except:
        engine.say("Entschuldigung, das habe ich nicht verstanden. Bitte wiederholen Sie, was Sie gesagt haben.")
        engine.runAndWait()
        recognized = my_listen(source, engine, r)
    print(recognized)
    return recognized


def string_works(string_input, stop_set):
    """Convert string to lower case, tokenize words, remove words from stop-set, return list of words"""
    string_input = string_input.lower()
    string_tokenized = nltk.word_tokenize(string_input)
    tokenized_output = [word for word in string_tokenized if word not in stop_set]
    return tokenized_output


def analyse(text, pizza, engine, source, r, german_stop_set):
    """Parse text and add features to pizza-object, if relevant information is given.
    Open menu-dialogue if asked for."""
    trees = PARSER.parse(text)
    bigram = []
    for tree in trees:
        bigram.append(tree.pos())
        print(bigram)

    for unnoetig in bigram:
        for pos in unnoetig:
            if pos[1] == "PRODUCT":
                pizza.set_product(pos[0])
            if pos[1] == "SORTE":
                pizza.set_sorte(pos[0])
            if pos[1] == "MBELAG":
                pizza.set_extra(pos[0])
            if pos[1] == "OBELAG":
                pizza.set_out(pos[0])
            if pos[1] == "BODENART":
                pizza.set_boden(pos[0])
            if pos[1] == "MENUE":
                menue_dialog(engine, source, r, german_stop_set)
            if pos[1] == "ODER":
                op1 = ""
                op2 = ""
                for pos1 in unnoetig:
                    if pos1[1] == "PRODUCT1":
                        op1 = pos1[0]
                    if pos1[1] == "PRODUCT2":
                        op2 = pos1[0]
                engine.say("Moechten Sie lieber " + op1 + " oder " + op2 + "?")
                engine.runAndWait()
                print("Moechten Sie lieber " + op1 + " oder " + op2 + "?")
                satz = my_listen(source, engine, r)
                satz = string_works(satz, german_stop_set)
                analyse(satz, pizza, engine, source, r, german_stop_set)



def analyse_boden(text, pizza):
    """Parse text and add Boden-feature to pizza-object, if relevant information is given."""
    trees = BODENPARSER.parse(text)
    bigram = []
    for tree in trees:
        bigram.append(tree.pos())

    for unnoetig in bigram:
        for pos in unnoetig:
            if pos[1] == "BODEN":
                pizza.set_boden = pos[0]


def analyse_alles(text, pizza):
    """Parse text and return 0 if customer is satisfied, 1 if customer wants to add anything to order."""
    trees = ALLESPARSER.parse(text)
    bigram = []
    alles = 0
    for tree in trees:
        bigram.append(tree.pos())

    for unnoetig in bigram:
        for pos in unnoetig:
            if pos[1] == "JA":
                alles = 0
            if pos[1] == "NEIN":
                alles = 0
            if pos[1] == "MB":
                pizza.set_extra(pos[0])
                alles = 1
            if pos[1] == "OB":
                pizza.set_out(pos[0])
                alles = 1
            
    return alles


def analyse_menue(text):
    """Parse text and return relevant menu-options"""
    trees = MENUEPARSER.parse(text)
    bigram = []
    for tree in trees:
        bigram.append(tree.pos())

    menue = []

    for unnoetig in bigram:
        for pos in unnoetig:
            if pos[1] == "VEG":
                # show veggie menue
                for sorte in SORTEN:
                    if sorte[0] == 0:
                        menue.append(sorte[1])
            if pos[1] == "MB":
                # show menue with topping
                for sorte in SORTEN:
                    if pos[0] in sorte:
                        menue.append(sorte[1])
            if pos[1] == "OB":
                # show menue without topping
                for sorte in SORTEN:
                    if pos[0] not in sorte:
                        menue.append(sorte[1])
            if pos[1] == "NEIN":
                for sorte in SORTEN:
                    menue.append(sorte)
        return menue


def check_complete(pizza):
    """returns an Array of Boolean Values according to set Variables in given PizzaConfig Object"""
    product = False
    sorte = False
    boden = False

    if (pizza.get_sorte() != ''):
        sorte = True
    if (pizza.get_boden() != 'normal'):
        boden = True
    if (pizza.get_product() != ''):
        product = True

    return [sorte, boden, product]


def menue_dialog(engine, source, r, german_stop_set):
    """Ask for preferences for menu, call analyse_menue(), give relevant options from return value"""
    engine.say("Haben Sie besondere Vorlieben?")
    engine.runAndWait()
    print("Haben Sie besondere Vorlieben?")
    satz = my_listen(source, engine, r)
    satz = string_works(satz, german_stop_set)
    menue = analyse_menue(satz)
    separator = ", "
    try:
        menue = separator.join(menue)
    except:
        engine.say("So etwas haben wir leider nicht. Versuchen Sie es mit etwas anderem.")
        engine.runAndWait()
        menue_dialog(engine, source, r, german_stop_set)
    
    engine.say("Da haben wir " + menue + ".")
    engine.runAndWait()
    print("Da haben wir " + menue + ".")


def say_begruessung(engine):
    """Say greeting from randomised greetings"""
    greeting = rand_greeting()
    engine.say(greeting)
    print(greeting)
    engine.runAndWait()


def ask_product(engine):
    """Ask for product - randomised question"""
    nachfrage = rand_product()
    engine.say(nachfrage)
    print(nachfrage)
    engine.runAndWait()


def ask_sorte(engine):
    """Ask for type - randomised question"""
    nachfrage = rand_sorte()
    engine.say(nachfrage)
    print(nachfrage)
    engine.runAndWait()


def ask_boden(engine):
    """Ask for base - randomised question"""
    boden = rand_boden()
    engine.say(boden)
    print(boden)
    engine.runAndWait()


def ask_alles(engine):
    """Ask if customer is done - randomised question"""
    alles = rand_alles()
    engine.say(alles)
    print(alles)
    engine.runAndWait()


def say_kommt(engine):
    """Say farewell from randomised farewells"""
    farewell = rand_farewell()
    engine.say(farewell)
    print(farewell)
    engine.runAndWait()


def main():
    # initialise text-to-speech-engine
    engine = pyttsx3.init()
    engine.runAndWait()

    # initialise speech-recognition
    r = sr.Recognizer()

    german_stop_set = generate_custom_stop_set()

    running = 1

    say_begruessung(engine)

    while (running):
        with sr.Microphone() as source:
            # initialise pizza object
            pizza = PizzaConfig.PizzaConfig()

            # listen for initial order
            satz = my_listen(source, engine, r)
            satz = string_works(satz, german_stop_set)

            # analyse order
            analyse(satz, pizza, engine, source, r, german_stop_set)
            complete = check_complete(pizza)

            # debug print
            print(complete)

            # check if product is set and if not ask for it
            while (complete[2] == False):
                ask_product(engine)

                satz = my_listen(source, engine, r)
                satz = string_works(satz, german_stop_set)

                analyse(satz, pizza, engine, source, r, german_stop_set)
                complete = check_complete(pizza)

            # if type and product were given, ask for base 
            if (complete[0] == True and pizza.get_product() == 'Pizza'):
                ask_boden(engine)

                satz = my_listen(source, engine, r)
                satz = string_works(satz, german_stop_set)

                analyse_boden(satz, pizza)

            # check if type is set and if not ask for it
            while (complete[0] == False):
                ask_sorte(engine)

                satz = my_listen(source, engine, r)
                satz = string_works(satz, german_stop_set)

                analyse(satz, pizza, engine, source, r, german_stop_set)
                complete = check_complete(pizza)

            # does the customer want to add anything? yes -> change and reask, no -> go on
            running = 1
            while(running):
                ask_alles(engine)
                satz = my_listen(source, engine, r)
                satz = string_works(satz, german_stop_set)
                running = analyse_alles(satz, pizza)

        say_kommt(engine)
        # debug print
        product = pizza.get_product()
        sorte = pizza.get_sorte()
        extra = pizza.get_extra()
        out = pizza.get_out()
        boden = pizza.get_boden()
        print(product, sorte, extra, out, boden)


# %%
main()

# %%
