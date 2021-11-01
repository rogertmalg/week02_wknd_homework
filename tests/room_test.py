import unittest
import pdb
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("CCC_01", 5, 4.00)
        self.guest1 = Guest("Linda", 30, 50.00, "Wannabe")
        self.guest2 = Guest("Bob", 39, 70.00, "Last Friday night")
        self.guest3 = Guest("Tina", 13, 3.00, "Quirky turkey")
        self.song1 = Song("Wannabe", "Spice Girls")
        self.song2 = Song("I kissed a girl", "Katy Perry")
        self.song3 = Song("Last Friday night", "Katy Perry")
        
    
    def test_room_has_name(self):
        self.assertEqual("CCC_01", self.room1.name)
    
    def test_room_has_capacity(self):
        self.assertEqual(5, self.room1.capacity)
    
    def test_room_has_entry_fee(self):
        self.assertEqual(4.00, self.room1.entry_fee)

    def test_add_guest_to_room(self):
        self.room1.add_guest_to_room(self.guest1)
        self.room1.add_guest_to_room(self.guest2)
        self.assertEqual(2, len(self.room1.guests_in_room))
    
    def test_guest_can_pay(self):
        self.assertEqual(True, self.room1.check_guest_can_pay(self.guest1))

    def test_charge_guest_entry_fee_add_balance(self):
        self.room1.charge_guest_entry_fee(self.guest1)
        self.assertEqual(4.00, self.room1.room_balance)
    
    def test_charge_guest_entry_fee_lower_wallet(self):
        self.room1.charge_guest_entry_fee(self.guest1)
        self.assertEqual(46.00, self.guest1.wallet)
    
    def test_check_in_guest(self):
        self.room1.check_in_guest(self.guest2)
        self.assertEqual(4, self.room1.capacity)
    
    def test_check_in_guest_no_capacity(self):
        self.room1.capacity = 0
        self.assertEqual("Sorry, this room is full", self.room1.check_in_guest(self.guest2))

    def test_check_in_guest_cant_pay(self):
        self.room1.check_in_guest(self.guest3)
        self.assertEqual(5, self.room1.capacity)
        
    def test_check_out_guest(self):
        self.room1.guests_in_room = [self.guest1, self.guest2, self.guest3]
        self.room1.check_out_guest_by_name("Linda")
        self.assertEqual(2, len(self.room1.guests_in_room))

    def test_check_out_guest_not_in_room(self):
        self.room1.guests_in_room = [self.guest1, self.guest2]
        self.room1.check_out_guest_by_name("Ted")
        self.assertEqual(2, len(self.room1.guests_in_room))

    def test_add_song_to_play_list(self):
        self.room1.add_song_to_play_list(self.song1)
        self.room1.add_song_to_play_list(self.song2)
        self.assertEqual(2, len(self.room1.play_list))
    
    def test_remove_song_by_name(self):
        self.room1.play_list = [self.song1, self.song2, self.song3]
        self.room1.remove_song_by_name("Wannabe")
        self.assertEqual(2, len(self.room1.play_list))
        
    def test_remove_song_by_singer_name(self):
        self.room1.play_list = [self.song1, self.song2, self.song3]
        self.room1.remove_song_by_singer("Katy Perry")
        self.assertEqual(1, len(self.room1.play_list))

    
    
