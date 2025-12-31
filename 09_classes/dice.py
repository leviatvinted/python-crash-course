"""
9-14. Dice: 

The module random contains functions that generate random num-
bers in a variety of ways. The function randint() returns an integer in the
range you provide. The following code returns a number between 1 and 6:
from random import randint

x = randint(1, 6)

    Make a class Die with one attribute called sides, which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll
it 10 times.
    Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""

from random import randint

class Die():
    def __init__(self, sides = 6):
        self.sides = sides

    def describe_die(self):
        print("\nThe die has " + str(self.sides) + " sides.")

    def roll_die(self):
        die = randint(1, int(self.sides))
        print("Rolling the die... You've rolled: " + str(die))

my_die = Die()

my_die.describe_die()
for x in range(6):
    my_die.roll_die()

big_die = Die(10)

big_die.describe_die()
for x in range(10):
    big_die.roll_die()

bigger_die = Die(20)

bigger_die.describe_die()
for x in range(10):
    bigger_die.roll_die()
