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
        self.room.check_in_guest(self.guest)
        self.room.check_out_guest(self.guest)
        self.assertEqual(False, self.guest in self.room.guests_in_room)

    def test_song_added_to_playlist(self):
        song = Song("Last Dance", "Donna Summer")
        self.room.add_song_to_playlist(song)
        self.assertEqual(True, song in self.room.playlist)

    def test_guest_refused_if_room_at_capacity(self):
        self.room_1 = Room("The Candi Suite", 1, 30, [])
        self.guest_1 = Guest("Dan", Song("Relight My Fire", "Dan Hartman"), 50)
        self.guest_2 = Guest("Terry", Song("Relight My Fire", "Dan Hartman"), 50)
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_in_guest(self.guest_2)
        self.assertEqual(False, self.guest_2 in self.room_1.guests_in_room)
       
    def test_refusal_message(self):
        self.room.capacity = 0
        self.room.check_in_guest(self.guest)
        self.assertEqual("Sorry! This room is at capacity", self.room.check_in_guest(self.guest))

    def test_guest_paid_entry(self):
        self.room.charge_guest_entry(self.guest)
        self.assertEqual(20, self.room.till)