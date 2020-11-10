import unittest
from functions import dice_roll

# class SetupTest(unittest.TestCase):
#   def test_setup(self):
#     pass

class DiceRollTest(unittest.TestCase):
  def test_dice_roll_returns_int(self):
    expected_result = int
    actual_result = dice_roll()
    self.assertIsInstance(actual_result, expected_result)

if __name__ == '__main__':
  unittest.main(verbosity = 2)
