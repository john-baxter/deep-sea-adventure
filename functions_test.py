import unittest
from unittest import mock
from unittest.mock import patch, call
from functions import dice_roll

# class SetupTest(unittest.TestCase):
#   def test_setup(self):
#     pass

class DiceRollTest(unittest.TestCase):
  def test_dice_roll_returns_int(self):
    expected_result = int
    actual_result = dice_roll()
    self.assertIsInstance(actual_result, expected_result)

  def test_dice_roll_returns_a_number_between_two_and_six_inc(self):
    expected_results = [2,3,4,5,6]
    actual_result = dice_roll()
    self.assertIn(actual_result, expected_results)

  @patch('random.randint')
  def test_dice_roll_calls_random_int_generator(self, mock_random_int):
    manager = mock.Mock()
    manager.attach_mock(mock_random_int, 'mock_random_int')

    dice_roll()

    # expected_mock_calls = [mock.call.mock_random_int()]
    # self.assertEqual(manager.mock_calls, expected_mock_calls)
    
    mock_random_int.assert_called_once()
    # self.assertEqual(mock_random_int.call_count, 1)
    

if __name__ == '__main__':
  unittest.main(verbosity = 2)
