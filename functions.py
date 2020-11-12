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
