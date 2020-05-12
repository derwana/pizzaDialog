def constant(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)

class _Const(object):
    @constant
    def SORTEN_LIST(self):
        list = ['Salami', 'Hawaii', 'Spinat', 'Margaritha']
        return list

    @constant
    def BELAG_LIST(self):
        list = ['Salami', 'Tomate', 'Ananas', 'Schinken', 'Käse', 'Spinat']
        return list

    @constant
    def BODEN_LIST(self):
        list = ['dick', 'normal', 'dünn']
        return list


class PizzaConfig():
    # set constants
    CONST = _Const()

    # init
    def __init__(self, name):
        self.sorte = ''
        self.boden = 'normal'
        self.extra = [] # ['Salami', True]

    # set methods
    def set_extra(self, belag, status):
        if belag in self.CONST.BELAG_LIST():
            self.extra.append([belag, status])

    def set_sorte(self, sorte):
        if sorte in self.CONST.SORTEN_LIST():
            self.sorte = sorte

    def set_boden(self, boden):
        if boden in self.CONST.BODEN_LIST():
            self.boden = boden

    # get methods
    def get_extra(self):
        return self.extra

    def get_sorte(self):
        return self.sorte

    def get_boden(self):
        return self.boden