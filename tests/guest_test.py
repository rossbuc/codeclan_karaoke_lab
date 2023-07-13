import unittest
from src.guest import Guest
from src.song import Song


class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Sam", Song("Happy Birthday", "Stevie Wonder"), 200)

    def test_guest_has_name(self):
        self.assertEqual("Sam", self.guest.name)

    def test_guest_has_name(self):
        self.assertEqual("Happy Birthday", self.guest.fav_song.name)

    def test_guest_has_money(self):
        self.assertEqual(200, self.guest.money)