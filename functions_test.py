import unittest
from unittest.mock import patch, call
from functions import roll_dice
from functions import initialise_trail
from functions import exchange_trail_token_for_blank
from functions import initialise_player_hand
from functions import add_token_to_hand
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

  def test_initialise_trail_creates_list_with_length_six_given_five_tokens(self):
    given_tokens = 5
    expected_result = 6
    test_trail = initialise_trail(given_tokens)
    actual_result = len(test_trail)
    self.assertEqual(actual_result, expected_result)

  def test_initialise_trail_creates_list_with_length_ten_given_nine_tokens(self):
    given_tokens = 9
    expected_result = 10
    test_trail = initialise_trail(given_tokens)
    actual_result = len(test_trail)
    self.assertEqual(actual_result, expected_result)

  def test_initialise_trail_creates_list_of_increasing_integers_each_element_has_same_value_as_idx(
    self):
    given_tokens = 7
    expected_trail = [0,1,2,3,4,5,6,7]
    actual_trail = initialise_trail(given_tokens)
    self.assertEqual(actual_trail, expected_trail)

class ExchangeTrailElementWithBlankTest(unittest.TestCase):
  def test_can_exchange_single_trail_token_with_blank(self):
    trail = [0,1]
    position_to_exchange = 1
    expected_new_trail = [0, "X"]
    actual_new_trail = exchange_trail_token_for_blank(trail, position_to_exchange)
    self.assertEqual(actual_new_trail, expected_new_trail)

  def test_can_exchange_element_2_of_two_token_trail_with_blank(self):
    trail = [0,1,2]
    position_to_exchange = 2
    expected_new_trail = [0, 1, "X"]
    actual_new_trail = exchange_trail_token_for_blank(trail, position_to_exchange)
    self.assertEqual(actual_new_trail, expected_new_trail)

  def test_cannot_exchange_element_0_of_trail_list_return_trail_with_no_change(self):
    trail = [0,1,2]
    position_to_exchange = 0
    expected_new_trail = [0, 1, 2]
    actual_new_trail = exchange_trail_token_for_blank(trail, position_to_exchange)
    self.assertEqual(actual_new_trail, expected_new_trail)
    
class InitialisePlayerHandTest(unittest.TestCase):
  def test_initialise_player_hand_returns_empty_list(self):
    expected_result = []
    actual_result = initialise_player_hand()
    self.assertEqual(actual_result, expected_result)

class AddTokenToHandTest(unittest.TestCase):
  def test_add_token_to_hand_returns_list(self):
    expected_result = list
    actual_result = add_token_to_hand([], 0)
    self.assertIsInstance(actual_result, expected_result)

  def test_hand_is_empty_can_add_one_3_token(self):
    initial_hand = []
    token_being_added = 3
    expected_new_hand = [3]
    actual_new_hand = add_token_to_hand(initial_hand, token_being_added)
    self.assertEqual(actual_new_hand, expected_new_hand)

  def test_hand_is_empty_can_add_one_9_token(self):
    initial_hand = []
    token_being_added = 9
    expected_new_hand = [9]
    actual_new_hand = add_token_to_hand(initial_hand, token_being_added)
    self.assertEqual(actual_new_hand, expected_new_hand)

  def test_check_hand_is_not_empty_can_add_more(self):
    initial_hand = [3]
    token_being_added = 9
    expected_new_hand = [3,9]
    actual_new_hand = add_token_to_hand(initial_hand, token_being_added)
    self.assertEqual(actual_new_hand, expected_new_hand)


if __name__ == '__main__':
  unittest.main(verbosity = 2)
