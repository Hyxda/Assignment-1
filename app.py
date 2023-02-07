# Import Ninja & Mage roles
import role1
import role2

# Create Character Choice function
def choose_character():
    """
    This function allows the user to input "ninja" or "mage" to select which role
    they would like to play as. A while loop is used to prompt the user for their
    selection. The string of the selected roll is returned upon selection to confirm
    the user's choice. If an incorrect option is inputted, the function is called again.
    """
    character = ""
    while character.lower() != "mage" and character.lower() != "ninja":
        input("Choose your path, will you be a mage or a ninja? ")
        if character == "mage":
            print("You have selected the mage.")
            return role1.mage()
        elif character == "ninja":
            print("You have selected the ninja.")
            return role2.ninja()
        else:
            print("You have input an incorrect option, please re-try.")
            choose_character()

# Create Character Assign function
def character_assign():
    """
    This function initializes battle stats & sets the user's character choice 
    to character & assigns the role's respective battle attributes.
    """
    character = choose_character(role1, role2)
    health = 0
    magic = 0
    stealth = 0
    intelligence = 0

    if character == "mage":
        health += role1.mage_health
        magic += role1.mage_magic
        stealth += role1.mage_stealth
        intelligence += role1.mage_intelligence
    else:
        health += role2.ninja_health
        magic += role2.ninja_magic
        stealth += role2.ninja_stealth
        intelligence += role2.ninja_intelligence
        