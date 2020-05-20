import random
import nltk
from nltk import CFG
from nltk.corpus import stopwords
from PizzaConfig import PizzaConfig
from constants import *


def rand_greeting():
    """Generates a random greeting from two given array and returns that greeting as string."""
    greetings = ['Guten Morgen', 'Hallo']
    question = [', was kann ich für Sie tun?', '!']
    return random.choice(greetings) + random.choice(question)


def rand_farewell():
    """Generates a random farewell from a given array and returns that farewell as string."""
    farewells = ['Ihre Pizza wird in 5 Minuten geliefert!', 'Gut, kommt.',
                 'Die Pizza wird Ihnen in 5 Minuten geliefert.']
    return random.choice(farewells)


def generate_custom_stop_set():
    """Generates and returns custom german set of stopwords"""
    # get stopwords
    german_stop_words = stopwords.words('german')
    # make it a set to be faster
    german_stop_set = set(german_stop_words)
    # remove some needed stopwords from set
    needed_words = ['mit', 'ohne', 'kein', 'extra', 'nicht']
    german_stop_set = [word for word in german_stop_set if word not in needed_words]
    # add some stopwords
    german_stop_set.append('bitte')

    return german_stop_set


def string_tokenize(string_input):
    """Tokenizes the string_input argument. Returns a list of tokens."""
    return nltk.word_tokenize(string_input)


def cut_stopwords(string_input, stop_set):
    """Cuts given stopwords in stop_set argument from string_input argument. Returns a list words."""
    return [word for word in string_input if word not in stop_set]


def string_works(string_input, stop_set):
    """Wrapper for string_tokenize(string_input) and cut_stopwords(string_input, stop_set). Returns a list."""
    string_tokenized = string_tokenize(string_input)
    tokenized_output = cut_stopwords(string_tokenized, stop_set)
    return tokenized_output


def parse_sentence(parser, sentence):
    """parses given sentence with given parser into a tree and return its bigram"""
    trees = parser.parse(sentence)
    bigram = []

    for tree in trees:
        # print(tree)
        bigram.append(tree.pos())

    return bigram


def parse_bigram(bigram, pizza):
    """parses given bigram and sets variables of given pizza object accordingly"""
    for unnoetig in bigram:
        for pos in unnoetig:
            if pos[1] == "SORTE":
                pizza.set_sorte(pos[0])
            if pos[1] == "MBELAG":
                pizza.set_extra(pos[0])
            if pos[1] == "OBELAG":
                pizza.set_out(pos[0])
            if pos[1] == "ART":
                pizza.set_boden(pos[0])


def process_information(stop_set, parser, string_input, pizza):
    """wrapper for string_works(), parse_sentence() and parse_bigram()"""
    # tokenize and cutting stopwords from input-string
    string_input = string_works(string_input, stop_set)

    # parse the input-string into a bigram
    bigram = parse_sentence(parser, string_input)

    # parse the bigram and set variables in pizza
    parse_bigram(bigram, pizza)


def reask_sorte(stop_set, parser, pizza):
    """checks if pizza.sorte is set, reasks and processes a new input to set it"""
    if not pizza.check_sorte():
        print('keine Sorte gewählt, wie kann ich Ihnen helfen')

        string_input = 'eine Salami Pizza bitte'

        process_information(stop_set, parser, string_input, pizza)

        # maybe do a recursion for rechecking with:
        # reask_sorte(stop_set, parser, pizza)

#def reask_extras(stop_set, parser, pizza):
#    if not pizza.check_extra() or not pizza.check_out():
#        print('haben Sie Extra-Wünsche?')
#
#        string_input = 'ja'
#
#        if string_input in NEGATION:
#            print('keine Extras gewählt')
#        else:
#            print('Welche Extra-Wünsche haben Sie?')
#            string_input = 'extra Käse und Salami'
#            process_information(stop_set, parser, string_input, pizza)


def main():
    # load grammar and its parser
    grammar = CFG.fromstring(GRAMMAR)
    parser = nltk.ChartParser(grammar)

    # list of all created pizzas
    pizzaList = []

    # generate stop set
    german_stop_set = generate_custom_stop_set()

    # random greeting
    print(rand_greeting())

    # while
    while True:
        # create a new pizza
        pizza = PizzaConfig.PizzaConfig()

        # first input (stt)
        #string_input = 'Pizza Salami mit extra Käse und Salami, ohne Oliven, aber mit dünnem Boden'
        string_input = 'eine Pizza bitte'

        # doing string works, parsing and value-assignments for pizza
        process_information(german_stop_set, parser, string_input, pizza)

        # check if pizza.sorte is set
        reask_sorte(german_stop_set, parser, pizza)

        # check if extras
        #reask_extras(german_stop_set, parser, pizza)

        # add created pizza to list
        pizzaList.append(pizza)

        # ask "noch etwas" (second pizza)
        if True:
            break

    # random bye
    print(rand_farewell())

    # print order
    for pizza in pizzaList:
        print(pizza.get_sorte(), pizza.get_boden(), pizza.get_extra(), pizza.get_out())

# run Main Function
main()
