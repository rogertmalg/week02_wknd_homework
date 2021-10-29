import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Wannabe", "Spice Girls")
        self.song2 = Song("I kissed a girl", "Katy Perry")

    def test_song_has_name(self):
        self.assertEqual("Wannabe", self.song1.name)    
        self.assertEqual("I kissed a girl", self.song2.name)

    def test_song_has_singer(self):
        self.assertEqual("Spice Girls", self.song1.singer)    
        self.assertEqual("Katy Perry", self.song2.singer)    