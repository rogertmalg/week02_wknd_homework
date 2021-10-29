import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Linda", 30, 50.00)
        self.guest2 = Guest("Bob", 39, 70.00)

    def test_guest_has_name(self):
        self.assertEqual("Linda", self.guest1.name)
        self.assertEqual("Bob", self.guest2.name)
    
    def test_guest_has_age(self):
        self.assertEqual(30, self.guest1.age)
        self.assertEqual(39, self.guest2.age)
    