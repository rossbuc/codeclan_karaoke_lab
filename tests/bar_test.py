import unittest
from src.bar import Bar
from src.guest import Guest
from src.song  import Song


class  TestBar(unittest.TestCase):

    def setUp(self):
        self.bar = Bar({"Beer": 4, "Glass of Wine": 4, "Bottle of wine": 20, "Spirit Mixer": 3})
        self.guest = Guest("Gary", Song("Let The Music Play", "Barry White"), 80)

    def test_bar_has_drinks_list(self):
        self.assertEqual(dict, type(self.bar.drinks_list))

    def test_bar_till_starts_at_zero(self):
        self.assertEqual([], self.bar.tab)

    def test_drink_goes_onto_tab(self):
        self.bar.sell_drink(self.guest, "Beer")
        self.assertEqual([("Beer", 4)], self.bar.tab)

    def test_money_goes_into_till(self):
        self.bar.sell_drink(self.guest, "Beer")
        self.assertEqual(4, self.bar.till)

    def test_money_taken_from_guest(self):
        self.bar.sell_drink(self.guest, "Beer")
        self.assertEqual(76, self.guest.money)