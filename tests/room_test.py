import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("CCC_01", 5, 4.00)
    
    def test_room_has_name(self):
        self.assertEqual("CCC_01", self.room1.name)
    
    def test_room_has_capacity(self):
        self.assertEqual(5, self.room1.capacity)
    
    def test_room_has_entry_fee(self):
        self.assertEqual(4.00, self.room1.entry_fee)
