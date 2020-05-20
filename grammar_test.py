from nltk.parse.generate import generate, demo_grammar
from nltk import CFG
import nltk


grammar = CFG.fromstring("""
S -> P M O B
S -> P O M B
S -> P B M O
S -> P B O M
S -> P B O
S -> P O B
S -> P M B
S -> P B M
S -> P O M
S -> P M O
S -> P O
S -> P B
S -> P M
S -> P
P -> SORTE 'Pizza'
P -> 'Pizza' SORTE
SORTE -> 'Salami'|'Hawaii'|'Margaritha'|'Spinat'
M -> 'mit' MBELAG
M -> 'zusätzlich' MBELAG
M -> 'extra' MBELAG
M -> 'mit' M
O -> 'ohne' OBELAG
MBELAG -> MBELAG MBELAG
MBELAG -> 'Salami'|'Schinken'|'Ananas'|'Tomate'|'Peperoni'|'Käse'|'Spinat'|'Oliven'
OBELAG -> OBELAG OBELAG
OBELAG -> 'Salami'|'Schinken'|'Ananas'|'Tomate'|'Peperoni'|'Käse'|'Spinat'|'Oliven'
B -> 'mit' ART
ART -> 'dünnem' BODEN|'dickem' BODEN
BODEN -> 'Boden'
""")


parser = nltk.ChartParser(grammar)


sentence = ['Pizza', 'Salami', 'mit', 'extra', 'Käse', 'Salami', 'ohne', 'Oliven', 'mit', 'dünnem', 'Boden']
trees = parser.parse(sentence)
bigram = []
for tree in trees:
    print(tree)
    bigram.append(tree.pos())


bigram


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
