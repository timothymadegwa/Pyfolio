import unittest
from rolling_dice import roll_the_dice

class TestRollingDice(unittest.TestCase):
    def test_roll_the_dice(self):
        self.assertRaises(TypeError,roll_the_dice,1)
        self.assertRaises(TypeError,roll_the_dice,1.0)
        self.assertRaises(TypeError,roll_the_dice,True)
    