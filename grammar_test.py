from nltk.parse.generate import generate
from nltk import CFG

with open('grammar', 'r') as file:
    grammar_data = file.read()

grammar = CFG.fromstring(grammar_data)

for sentence in generate(grammar, depth=6):
     print(' '.join(sentence))