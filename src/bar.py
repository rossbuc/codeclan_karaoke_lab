class Bar:

    def __init__(self, drinks_list):
        self.drinks_list = drinks_list
        self.tab = []
        self.till = 0

    def sell_drink(self, order):
        for drink in self.drinks_list:
            if drink == order:
                self.tab.append((drink, self.drinks_list[drink]))
                self.till += self.drinks_list[drink]