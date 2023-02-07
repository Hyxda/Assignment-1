# Imports "random" module for dice function creation
import random

# Creates dice function
def dice():
    """
    This function uses the random integer range function between 2 -> 12,
    which represents two six-sided die. The roll result is returned after
    each roll.
    """
    roll = random.randint(2, 12)
    return roll