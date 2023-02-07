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

# Creates main battle function with battle logistics
def battle():
    """
    This function uses the dice function to determine the user's roll number (2 -> 12),
    depending on the rolled number, the user wins or loses the challenge, battle
    attributes are increased or decreased respectively. Win is preset to True, as losses
    are counted. True or False values are returned depending on win/loss. If win is found
    to be False, the game ends, otherwise if the challenge is won, the game proceeds to
    the next challenge. User must win 3/3 challenges to beat the game.
    """
    win = True
    while win == True:
        roll = roll()
        if roll <= 3:
            health -= 1
            magic -= 1
            print("You rolled {}. Critical Loss! Health lowered to {}. Game Over.".format(roll, health))
            return False
        elif roll <= 7:
            health -= 1
            print("You rolled {}. Loss! Health lowered to {}. Game Over.".format(roll, health))
            return False
        elif roll <= 10:
            health += 1
            print("You rolled {}. Health increased to {}. Moving to next challenge!".format(roll, health))
            return True
        else:
            health += 1
            print("You rolled {}. Health increased to {}. Moving to next challenge!".format(roll, health))
            return True