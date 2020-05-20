from nltk import CFG
import nltk
from constants import *


grammar = CFG.fromstring(GRAMMAR)
parser = nltk.ChartParser(grammar)


sentence = ['Pizza', 'Salami', 'mit', 'extra', 'Käse', 'Salami', 'ohne', 'Oliven', 'mit', 'dünnem', 'Boden']

trees = parser.parse(sentence)
bigram = []
for tree in trees:
    print(tree)
    bigram.append(tree.pos())


sorte = ""
mbelag = []
obelag = []
boden = ""

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



print(sorte)
print(mbelag)
print(obelag)
print(boden)
