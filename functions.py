from random import randint

def roll_dice():
  die_a = randint(1, 3)
  die_b = randint(1, 3)
  roll_dice = die_a + die_b
  return roll_dice
