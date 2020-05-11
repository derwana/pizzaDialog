import nltk
import pickle

# read screen input
string_input = input("your input please: ")

## analyse input
# tokenize string
string_tokenised = nltk.word_tokenize(string_input)
# count words
print("You typed", len(string_tokenised), "words.")

# loading tagger
with open('nltk_german_classifier_data.pickle', 'rb') as f:
    tagger = pickle.load(f)

# tag the tokenized words
string_tagged = tagger.tag(string_tokenised)
print (string_tagged)