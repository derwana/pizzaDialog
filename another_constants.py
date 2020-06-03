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

PARSER = nltk.ChartParser(GRAMMAR)

# sortengrammar = CFG.fromstring("""
# S -> SORTE
# S -> SORTE 'Pizza'
# S -> 'Pizza' SORTE
# SORTE -> 'Salami'|'Hawaii'|'Margaritha'|'Spinat'
# """)

# sortenparser = nltk.ChartParser(sortengrammar)

BODENGRAMMAR = CFG.fromstring("""
S -> BODEN
B -> 'mit' ART
ART -> 'dünnem' BODEN|'dickem' BODEN
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