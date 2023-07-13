import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Young Hearts Run Free", "Candi Staton")

    def test_song_has_name(self):
        self.assertEqual("Young Hearts Run Free", self.song.name)

    def test_song_has_artist(self):
        self.assertEqual("Candi Staton", self.song.artist)