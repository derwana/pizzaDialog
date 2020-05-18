import random
import nltk
from nltk.corpus import stopwords


def rand_greeting():
    """Generates a random greeting from two given array and returns that greeting as string."""
    greetings = ['Guten Morgen', 'Hallo']
    question = [', was kann ich für Sie tun?', '!']
    return (random.choice(greetings) + random.choice(question))


def rand_farewell():
    """Generates a random farewell from a given array and returns that farewell as string."""
    farewells = ['Ihre Pizza wird in 5 Minuten geliefert!', 'Gut, kommt.', 'Die Pizza wird Ihnen in 5 Minuten geliefert.']
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


def main():
    pizzaList = []

    # generate stop set
    german_stop_set = generate_custom_stop_set()

    # random greeting
    print(rand_greeting())

    # do-while
    while(True):
        # first input (stt)
        string_input = 'das ist ein Test'

        # tokenize and cutting stopwords
        string_works(string_input, german_stop_set)

        # analysing input (add to list of PizzaConfig - create and fill class)

        # check if sorte
        # ask belag
        # ask boden

        # ask "noch etwas" (second pizza)

    # random bye
    print(rand_farewell())

# run Main Function
main()