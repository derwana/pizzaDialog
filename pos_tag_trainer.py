# training after this blogpost:
# https://datascience.blog.wzb.eu/2016/07/13/accurate-part-of-speech-tagging-of-german-texts-with-nltk/
# use downloaded corpus from:
# https://www.ims.uni-stuttgart.de/documents/ressourcen/korpora/tiger-corpus/download/tigercorpus-2.2.conll09.tar.gz

import nltk
import random
from ClassifierBasedGermanTagger.ClassifierBasedGermanTagger import GermanTagger
import pickle

corpus_dir = '/home/cw/Documents/UNI/14_Semester/GST/aufgabe4/nltk-nenv/nltk_data/corpora/'
corpus_name = 'tiger_release_aug07.corrected.16012013.conll09'

## load tiger corpus from uni stuttgart from given directories
corp = nltk.corpus.ConllCorpusReader(corpus_dir, corpus_name,
                                   ['ignore', 'words', 'ignore', 'ignore', 'pos'],
                                   encoding='utf-8')

tagged_sents = list(corp.tagged_sents())
random.shuffle(tagged_sents)

## set a split size: use 90% for training, 10% for testing
split_perc = 0.1
split_size = int(len(tagged_sents) * split_perc)
train_sents, test_sents = tagged_sents[split_size:], tagged_sents[:split_size]

## train tagger
tagger = GermanTagger(train=train_sents)

## test tagger accuracy
accuracy = tagger.evaluate(test_sents)
print (accuracy)

## saving and loading the tagger
# saving
with open('nltk_german_classifier_data.pickle', 'wb') as f:
    pickle.dump(tagger, f, protocol=3)

# loading
with open('nltk_german_classifier_data.pickle', 'rb') as f:
    tagger = pickle.load(f)