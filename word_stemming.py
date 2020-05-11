# https://www.nltk.org/api/nltk.stem.html#module-nltk.stem.cistem
# stemming return only the word stemm for further processing

from nltk.stem.cistem import Cistem

stemmer = Cistem(True)
s1 = "Speicherbehältern"

print("('" + stemmer.segment(s1)[0] + "', '" + stemmer.segment(s1)[1] + "')")
# >>> ('speicherbehäl', 'tern')

# TODO: die Frage ist ob es das braucht