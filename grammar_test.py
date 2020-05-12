from nltk.parse.generate import generate
from nltk import CFG
import nltk

with open('grammar', 'r') as file:
    grammar_data = file.read()

grammar = CFG.fromstring(grammar_data)

#for sentence in generate(grammar, depth=4, n=10):
#    print(' '.join(sentence))

parser = nltk.ChartParser(grammar)

sentence = ['Pizza','Salami','mit','extra','Salami']

for tree in parser.parse(sentence):
    print(tree)
