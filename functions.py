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
    the 'size' of the dice being rolled - how many sides does it have.

  Returns
  -------
  dice_roll : (int)
    The result of rolling the dice.
  """
  dice_roll = 0
  for i in range(dice):
    dice_roll += randint(1, sides)
  return dice_roll

def initialise_trail(length):
  return [None for i in range(length)]
