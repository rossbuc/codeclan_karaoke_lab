import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room


class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Sam", Song("Happy Birthday", "Stevie Wonder"), 200)
        self.guest_2 = Guest("Sandy", Song("How Will I Know", "Whitney Houston"), 200)
        self.room = Room("Houston Room", 50, 20, [Song("How Will I Know", "Whitney Houston"), Song("Million Dollar Bill", "Whitney Houston"), Song("I Wanna Dance With Somebody", "Whitney Houston")])

    def test_guest_has_name(self):
        self.assertEqual("Sam", self.guest.name)

    def test_guest_has_name(self):
        self.assertEqual("Happy Birthday", self.guest.fav_song.name)

    def test_guest_has_money(self):
        self.assertEqual(200, self.guest.money)

    def test_guest_can_pay_entry(self):
        self.guest.pay_entry(20)
        self.assertEqual(180, self.guest.money)

    def test_wooh_if_fav_song_in_playlist(self):
        self.assertEqual("Wooh! They have my favourite song", self.guest_2.fav_song_in_playlist(self.room))

    def test_no_wooh_if_no_fav_song_in_playlist(self):
        self.assertEqual(None, self.guest.fav_song_in_playlist(self.room))