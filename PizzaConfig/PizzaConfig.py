import another_constants


class PizzaConfig:

    # init
    def __init__(self):
        self.boden = 'normal'
        self.extra = []
        self.out = []
        self.sorte = ''
        self.product = ''

    # set methods
    def set_boden(self, boden):
        """set class-member-variable 'boden' by checking against allowed inputs in constants"""
        if boden in another_constants.BODEN_LIST:
            self.boden = boden

    def set_extra(self, belag):
        """set class-member-variable 'extra' by checking against allowed inputs in constants"""
        if belag in another_constants.BELAG_LIST:
            self.extra.append(belag)

    def set_out(self, belag):
        """set class-member-variable 'out' by checking against allowed inputs in constants"""
        if belag in another_constants.BELAG_LIST:
            self.out.append(belag)

    def set_sorte(self, sorte):
        """set class-member-variable 'sorte' by checking against allowed inputs in constants"""
        if sorte in another_constants.SORTEN_LIST:
            self.sorte = sorte

    def set_product(self, product):
        """set class-member-variable 'sorte' by checking against allowed inputs in constants"""
        if product in another_constants.PRODUCT_LIST:
            self.product = product

    # get methods
    def get_boden(self):
        """returns class-member-variable 'boden'"""
        return self.boden

    def get_extra(self):
        """returns class-member-variable 'extra'"""
        return self.extra

    def get_out(self):
        """returns class-member-variable 'out'"""
        return self.out

    def get_sorte(self):
        """returns class-member-variable 'sorte'"""
        return self.sorte

    def get_product(self):
        """returns class-member-variable 'product'"""
        return self.product

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

    def check_out(self):
        if self.get_out():
            return True
        else:
            return False

    def check_sorte(self):
        if self.get_sorte():
            return True
        else:
            return False
