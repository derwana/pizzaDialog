import nltk
from nltk import CFG

SORTEN_LIST = ['salami', 'hawaii', 'spinat', 'margaritha', 'margarita', 'margherita']
BELAG_LIST = ['salami', 'tomate', 'ananas', 'schinken', 'käse', 'spinat', 'oliven', 'peperoni', 'peperonis', 'pepperoni']
BODEN_LIST = ['dick', 'dickem', 'dicken', 'dickes', 'normal', 'normalen', 'normalem', 'normales', 'dünn', 'dünnem', 'dünnen', 'dünnes']
PRODUCT_LIST = ['pizza', 'pizzabrötchen', 'calzone']

GRAMMAR = CFG.fromstring("""
S -> MENUE
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
S -> PRODUCT
PRODUCT -> 'pizza'|'pizzabrötchen'|'calzone'
P -> SORTE
SORTE -> 'salami'|'hawaii'|'margaritha'|'spinat'|'margarita'|'margherita'|'spinatpizza'
P -> SORTE PRODUCT
P -> PRODUCT SORTE
M -> 'mit' MBELAG
M -> 'zusätzlich' MBELAG
M -> 'extra' MBELAG
M -> 'mit' M
O -> 'ohne' OBELAG
O -> 'kein' OBELAG
MBELAG -> MBELAG MBELAG
MBELAG -> 'salami'|'schinken'|'ananas'|'tomate'|'peperoni'|'käse'|'spinat'|'oliven'|'peperonis'
OBELAG -> OBELAG OBELAG
OBELAG -> 'salami'|'schinken'|'ananas'|'tomate'|'peperoni'|'käse'|'spinat'|'oliven'|'peperonis'
B -> 'mit' BODENART
BODENART -> 'dünnem' BODEN|'dickem' BODEN
BODEN -> 'boden'
MENUE -> 'was'|'welche'|'menue'|'menü'
""")
PARSER = nltk.ChartParser(GRAMMAR)


MENUEGRAMMAR = CFG.fromstring("""
    S -> VEG
    S -> M
    S -> MB
    S -> O
    VEG -> 'vegetarisch'|'vegetarisches'
    VEG -> 'fleisch'
    M -> 'mit' MB
    M -> 'zusätzlich' MB
    M -> 'extra' MB
    M -> 'mit' M
    O -> 'ohne' OB
    O -> 'ohne' VEG
    O -> 'kein' OB
    O -> 'kein' VEG
    MB -> MB MB
    MB -> 'salami'|'schinken'|'ananas'|'tomate'|'peperoni'|'käse'|'spinat'|'oliven'|'peperonis'
    OB -> OB OB
    OB -> 'salami'|'schinken'|'ananas'|'tomate'|'peperoni'|'käse'|'spinat'|'oliven'|'peperonis'
""")
MENUEPARSER = nltk.ChartParser(MENUEGRAMMAR)


BODENGRAMMAR = CFG.fromstring("""
S -> B
S -> ART
B -> 'mit' ART
ART -> 'dünnem' BODEN|'dickem' BODEN
ART -> 'dünnen' BODEN|'dicken' BODEN
ART -> 'dick'|'dünn'|'dickem'|'dicken'|'dickes'|'normal'|'normalen'|'normalem'|'normales'|'dünnem'|'dünnen'|'dünnes'|'dicker'|'dünner'|'normaler'
BODEN -> 'boden'
""")
BODENPARSER = nltk.ChartParser(BODENGRAMMAR)


ALLESGRAMMAR = CFG.fromstring("""
S -> JA
S -> NEIN
NEIN -> 'nein'|'nö'|'nee'
JA -> 'ja'|'jo'|'jep'
""")
ALLESPARSER = nltk.ChartParser(ALLESGRAMMAR)

SORTEN = [
    # vegetarisch, Sorte, Zutaten
    [1, 'Salami', 'tomatensauce', 'salami', 'käse'],
    [0, 'Margherita', 'tomatensauce', 'käse'],
    [0, 'Spinat', 'tomatensauce', 'spinat', 'käse'],
    [1, 'Hawaii', 'tomatensauce', 'schinken', 'ananas', 'käse']
]