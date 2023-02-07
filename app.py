# Import Ninja & Mage roles
import role1
import role2

# Create Welcome function
def welcome():
    """
    This function welcomes the user to the game & provides an overview of challenges!
    """
    print(
    """
    Welcome to Ninjas & Mages! The goal of this game is to choose your fighter path
    & face three tough challenges. Begin the game by selecting your character, then roll the
    dice once you're ready to start. Your success in this game is dependant on the number you
    roll, & you must win ALL three challenges to beat the game. Lose even one challenge, and 
    you lose the game. Ready?
    """)

# Create Character Choice function
def choose_character():
    """
    This function allows the user to input "ninja" or "mage" to select which role
    they would like to play as. A while loop is used to prompt the user for their
    selection. The string of the selected roll is returned upon selection to confirm
    the user's choice. If an incorrect option is inputted, the function is called again.
    """
    character = ""
    while character.lower() != "mage" or character.lower() != "ninja":
        character = input(
            """
            Choose your path, will you be a mage or a ninja?
            \n Mage  | Mages are more skillful in magic.    | Magic = {} / Stealth = {} / Intelligence = {}
            \n Ninja | Ninjas are more skillful in stealth. | Magic = {} / Stealth = {} / Intelligence = {}
            """.format(role1.mage_magic, role1.mage_stealth, role1.mage_intelligence, role2.ninja_magic, role2.ninja_stealth, role2.ninja_intelligence))
        if character.lower() == "mage":
            print("You have selected the mage.")
            return role1.mage()
        elif character.lower() == "ninja":
            print("You have selected the ninja.")
            return role2.ninja()
        else:
            print("You have input an incorrect option, please re-try.")
            choose_character()

# Introduce user to game with welcome() function
welcome()
choose_character()