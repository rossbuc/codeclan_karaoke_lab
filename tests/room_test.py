from src.room import Room
from src.song import Song
import unittest


class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room("Houston Room", 50, 20, [Song("How Will I Know", "Whitney Houston"), Song("Million Dollar Bill", "Whitney Houston"), Song("I Wanna Dance With Somebody", "Whitney Houston")])

    def test_room_has_name(self):
        self.assertEqual("Houston Room", self.room.name)

    def test_room_has_capacity(self):
        self.assertEqual(50, self.room.capacity)

    def  test_room_has_entry_fee(self):
        self.assertEqual(20, self.room.entry_fee)

    def test_room_has_songs(self):
        self.assertEqual(list, type(self.room.playlist))