"""
This file is used to test the app.
"""

from django.test import SimpleTestCase
from app.calc import add, subtract, multiply

class CalcTestCase(SimpleTestCase):
    def test_add(self):
        self.assertEqual(add(3,8), 11)
        self.assertEqual(add(3,3), 6)
        self.assertEqual(add(-3,-3), -6)
        
    def test_subtract(self):
        self.assertEqual(subtract(5,11), 6)
        
    def test_multiply(self):
        res = multiply(5,3)
        self.assertEqual(res, 15)
    