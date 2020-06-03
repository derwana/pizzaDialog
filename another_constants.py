import nltk
from nltk import CFG

GRAMMAR = CFG.fromstring("""
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
S -> N
N -> 'Pizza'
P -> SORTE
P -> SORTE 'Pizza'
P -> 'Pizza' SORTE
SORTE -> 'Salami'|'Hawaii'|'Margaritha'|'Spinat'|'Margarita'|'Margherita'
M -> 'mit' MBELAG
M -> 'zusätzlich' MBELAG
M -> 'extra' MBELAG
M -> 'mit' M
O -> 'ohne' OBELAG
O -> 'kein' OBELAG
MBELAG -> MBELAG MBELAG
MBELAG -> 'Salami'|'Schinken'|'Ananas'|'Tomate'|'Peperoni'|'Käse'|'Spinat'|'Oliven'
OBELAG -> OBELAG OBELAG
OBELAG -> 'Salami'|'Schinken'|'Ananas'|'Tomate'|'Peperoni'|'Käse'|'Spinat'|'Oliven'
B -> 'mit' ART
ART -> 'dünnem' BODEN|'dickem' BODEN
BODEN -> 'Boden'
""")

PARSER = nltk.ChartParser(GRAMMAR)


BODENGRAMMAR = CFG.fromstring("""
S -> B
S -> ART
B -> 'mit' ART
ART -> 'dünnem' BODEN|'dickem' BODEN
ART -> 'dünnen' BODEN|'dicken' BODEN
ART -> 'dick'|'dünn'
BODEN -> 'Boden'
""")

BODENPARSER = nltk.ChartParser(BODENGRAMMAR)

ALLESGRAMMAR = CFG.fromstring("""
S -> JA
S -> NEIN
NEIN -> 'nein'
JA -> 'ja'
""")

ALLESPARSER = nltk.ChartParser(ALLESGRAMMAR)