from random import randint

def roll_dice(dice=2, sides=3):
  """Set how many movement points the player has this turn

  Gives a range of random integers from which to choose, and a number of times to choose.
  Works for any number of dice of any size, iff all dice are the same size

  Parameters
  ----------
  dice : (int)
  default value : 2
    the number of dice being rolled at a time

  sides : (int)
  default value : 3
    the 'size' of the dice being rolled - how many sides do they have.

  Returns
  -------
  dice_roll : (int)
    The result of rolling the dice.
  """
  dice_roll = 0
  for i in range(dice):
    dice_roll += randint(1, sides)
  return dice_roll

def initialise_trail(tokens):
  """Prepares the trail for this game

  Element 0 of the resulting list will not be considered as 'part of the trail', 
  the intention is to treat this differently as it will form the location of the 
  submarine and therefore care will be taken not to modify this element at any time.

  Parameters
  ----------
  tokens : (int)
    The number of tokens expected to be in the trail

  Returns
  -------
  trail : (list)
    The trail being used for this game.
    Each element is an int
    Each element has the same value as its idx
  """
  length = tokens+1
  trail = list(range(length)) 
  return trail

def exchange_trail_token_for_blank(trail, player_position):
  """Removes the token under the player from the trail and replaces with a blank

  Does not replace element 0 as this will be the position of the submarine and is not 
  considered as part of the trail.

  Parameters
  ----------
  trail : (list)
    The trail being used for this game.
    Each element is an int
    Each element has the same value as its idx

  player_position : (int)
    The location of the current player on the trail

  Returns
  -------
  trail : (list)
    The newly updated trail with one fewer regular token and a blank token in that place.
  """
  if player_position >= 1:
    trail[player_position] = "X"
  return trail

def initialise_player_hand():
  """Creates a place for the player to store tokens that are collected during the game

  Returns
  -------
  player_hand : (list)
    An empty list.
    Will have tokens from the trail added during the game.
  """
  player_hand = []
  return player_hand

def add_token_to_hand(player_hand, token_to_be_added):
  """Add a token into the player's hand

  Parameters
  ----------
  player_hand : (list)
    A list containing any/all tokens collected by the player so far this game.
    Could be empty.
    Elements are trail tokens.

  token_to_be_added : (int)
    The token being added to the player's hand

  Returns
  -------
  player_hand : (list)
    A list containing any/all tokens collected by the player so far this game.
    Newly updated with the extra token added.
    Elements are trail tokens.
  """
  player_hand.append(token_to_be_added)
  return player_hand

def move_player_along_trail(player_position, dice_roll, trail):
  """Moves the player along the trail to the new location as defined by the dice

  Parameters
  ----------
  player_position : (int)
    The idx of the trail element where the player is currently located.

  dice_roll : (int)
    The score the player achieved this turn when rolling the game dice

  trail : (list)
    The trail being used for this game.
    Each element is an int
    Each element has the same value as its idx

  Returns
  -------
  player_position : (int)
    The newly updated idx of the trail element where the player is now located.
  """
  if player_position + dice_roll >= len(trail):
    player_position = len(trail)-1
  else:
    player_position += dice_roll
  return player_position
