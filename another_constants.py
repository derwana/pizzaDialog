import nltk
from nltk import CFG

SORTEN_LIST = ['Salami', 'Hawaii', 'Spinat', 'Margaritha']
BELAG_LIST = ['Salami', 'Tomate', 'Ananas', 'Schinken', 'Käse', 'Spinat', 'Oliven']
BODEN_LIST = ['dick', 'dickem', 'dicken', 'dickes', 'normal', 'normalen', 'normalem', 'normales', 'dünn', 'dünnem', 'dünnen', 'dünnes']
PRODUCT_LIST = ['Pizza', 'Pizzabrötchen', 'Calzone']

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
PRODUCT -> 'Pizza'|'Pizzabrötchen'|'Calzone'
P -> SORTE
SORTE -> 'Salami'|'Hawaii'|'Margaritha'|'Spinat'|'Margarita'|'Margherita'|'Spinatpizza'
P -> SORTE PRODUCT
P -> PRODUCT SORTE
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
B -> 'mit' BODENART
BODENART -> 'dünnem' BODEN|'dickem' BODEN
BODEN -> 'Boden'
MENUE -> 'was'|'welche'|'menue'|'Menü'
""")
PARSER = nltk.ChartParser(GRAMMAR)


MENUEGRAMMAR = CFG.fromstring("""
    S -> VEG
    S -> M
    S -> MB
    S -> O
    VEG -> 'vegetarisch'
    VEG -> 'ohne' 'Fleisch'
    M -> 'mit' MB
    M -> 'zusätzlich' MB
    M -> 'extra' MB
    M -> 'mit' M
    O -> 'ohne' OB
    O -> 'kein' OB
    MB -> MB MB
    MB -> 'Salami'|'Schinken'|'Ananas'|'Tomate'|'Peperoni'|'Käse'|'Spinat'|'Oliven'
    OB -> OB OB
    OB -> 'Salami'|'Schinken'|'Ananas'|'Tomate'|'Peperoni'|'Käse'|'Spinat'|'Oliven'
""")
MENUEPARSER = nltk.ChartParser(MENUEGRAMMAR)


BODENGRAMMAR = CFG.fromstring("""
S -> B
S -> ART
B -> 'mit' ART
ART -> 'dünnem' BODEN|'dickem' BODEN
ART -> 'dünnen' BODEN|'dicken' BODEN
ART -> 'dick'|'dünn'|'dickem'|'dicken'|'dickes'|'normal'|'normalen'|'normalem'|'normales'|'dünnem'|'dünnen'|'dünnes'
BODEN -> 'Boden'
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
    [1, 'Salami', 'Tomatensauce', 'Salami', 'Kaese'],
    [0, 'Margherita', 'Tomatensauce', 'Kaese'],
    [0, 'Spinat', 'Tomatensauce', 'Spinat' ,'Kaese'],
    [1, 'Hawaii', 'Tomatensauce', 'Schinken', 'Ananas', 'Hawaii', 'Kaese']
]