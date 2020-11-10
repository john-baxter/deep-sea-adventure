from random import randint

def roll_dice(dice=2, sides=3):
  dice_roll = 0
  for i in range(dice):
    dice_roll += randint(1, sides)
  return dice_roll
