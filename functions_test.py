import unittest
# from unittest import mock
from unittest.mock import patch, call
from functions import roll_dice

# class SetupTest(unittest.TestCase):
#   def test_setup(self):
#     pass

class DiceRollTest(unittest.TestCase):
  def test_roll_dice_returns_int(self):
    expected_result = int
    actual_result = roll_dice()
    self.assertIsInstance(actual_result, expected_result)

  def test_roll_dice_returns_a_number_between_two_and_six_inc(self):
    expected_results = [2,3,4,5,6]
    actual_result = roll_dice()
    self.assertIn(actual_result, expected_results)

  @patch('functions.randint', side_effect = [2, 3])
  def test_roll_dice_calls_random_int_generator(self, mock_random_int):
    roll_dice()

    expected_mock_calls = [
      call(1, 3),
      call(1, 3),
      ]

    self.assertEqual(mock_random_int.mock_calls, expected_mock_calls)
    self.assertEqual(mock_random_int.call_count, 2)

if __name__ == '__main__':
  unittest.main(verbosity = 2)
