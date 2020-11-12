import unittest
from unittest.mock import patch, call
from functions import roll_dice
from functions import initialise_trail
# from functions import 

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

class InitialiseTrailTest(unittest.TestCase):
  def test_initialise_trail_creates_a_list(self):
    expected_result = list
    actual_result = initialise_trail(0)
    self.assertIsInstance(actual_result, expected_result)

  def test_initialise_trail_creates_list_with_given_length_of_five_elements(self):
    given_length = 5
    expected_result = 5
    test_trail = initialise_trail(given_length)
    actual_result = len(test_trail)
    self.assertEqual(actual_result, expected_result)

  def test_initialise_trail_creates_list_with_given_length_of_nine_elements(self):
    given_length = 9
    expected_result = 9
    test_trail = initialise_trail(given_length)
    actual_result = len(test_trail)
    self.assertEqual(actual_result, expected_result)

  def test_initialise_trail_creates_list_of_increasing_integers_each_element_has_same_value_as_idx(
    self):
    given_length = 7
    expected_trail = [0,1,2,3,4,5,6]
    actual_trail = initialise_trail(given_length)

    self.assertEqual(actual_trail, expected_trail)



if __name__ == '__main__':
  unittest.main(verbosity = 2)
