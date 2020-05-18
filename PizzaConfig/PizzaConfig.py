import constants


class PizzaConfig:

    # init
    def __init__(self):
        self.boden = 'normal'
        self.extra = []  # ['Salami', True]
        self.sorte = ''

    # set methods
    def set_boden(self, boden):
        if boden in constants.BODEN_LIST:
            self.boden = boden

    def set_extra(self, belag, status):
        if belag in constants.BELAG_LIST:
            self.extra.append([belag, status])

    def set_sorte(self, sorte):
        if sorte in constants.SORTEN_LIST:
            self.sorte = sorte

    # get methods
    def get_boden(self):
        return self.boden

    def get_extra(self):
        return self.extra

    def get_sorte(self):
        return self.sorte

    # check methods
    def check_boden(self):
        if self.get_boden():
            return True
        else:
            return False

    def check_extra(self):
        if self.get_extra():
            return True
        else:
            return False

    def check_sorte(self):
        if self.get_sorte():
            return True
        else:
            return False
