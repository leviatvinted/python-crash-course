"""
10-11. Favorite Number: 

Write a program that prompts for the user’s favorite
number. Use json.dump() to store this number in a file. Write a separate pro-
gram that reads in this value and prints the message, “I know your favorite
number! It’s _____."

10-12. Favorite Number Remembered: 

Combine the two programs from
Exercise 10-11 into one file. If the number is already stored, report the favorite
number to the user. If not, prompt for the user’s favorite number and store it in a
file. Run the program twice to see that it works.
"""

import json

def get_stored_number():
    """Get stored favorite number if available."""
    filename = 'fav_number.json'
    try:
        with open(filename) as f_obj:
            fav_num = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return fav_num

def get_favorite_number():
    """Prompt for a favorite number if nothing is stored"""
    while True:
        try:
            fav_num_input = input("What is your favorite number? ")
            fav_num = int(fav_num_input)
            filename = 'fav_number.json'
            with open(filename, 'w') as f_obj:
                json.dump(fav_num, f_obj)

            return fav_num
        except ValueError:
            print("Please input a numerical value.\n")

def return_favorite_number():
    """Returns favorite number to the user"""
    fav_num = get_stored_number()
    if fav_num:
        print("I know your favorite number! It's " + str(fav_num))
    else:
        fav_num = get_favorite_number()
        print("Your favorite number " + str(fav_num) + " is stored!")

return_favorite_number()
