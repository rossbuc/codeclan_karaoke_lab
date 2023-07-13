from src.room import Room
from src.song import Song
from src.guest import Guest
import unittest


class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Gary", Song("Let The Music Play", "Barry White"), 80)
        self.room = Room("Houston Room", 50, 20, [Song("How Will I Know", "Whitney Houston"), Song("Million Dollar Bill", "Whitney Houston"), Song("I Wanna Dance With Somebody", "Whitney Houston")])

    def test_room_has_name(self):
        self.assertEqual("Houston Room", self.room.name)

    def test_room_has_capacity(self):
        self.assertEqual(50, self.room.capacity)

    def  test_room_has_entry_fee(self):
        self.assertEqual(20, self.room.entry_fee)

    def test_room_has_songs(self):
        self.assertEqual(list, type(self.room.playlist))

    def test_guest_checked_in(self):
        self.room.check_in_guest(self.guest)
        self.assertEqual("Gary", self.room.guests_in_room[0].name)

    def test_guest_checked_out(self):
        self.room.check_out_guest(self.guest)
        self.assertEqual(False, self.guest in self.room.guests_in_room)