"""
10-13. Verify User: 

The final listing for remember_me.py assumes either that the
user has already entered their username or that the program is running for the
first time. We should modify it in case the current user is not the person who
last used the program.
    Before printing a welcome back message in greet_user(), ask the user if
this is the correct username. If it’s not, call get_new_username() to get the correct
username.
"""

import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    print("We'll remember you when you come back, " + username + "!")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        username_check = input("Hi, " + username + 
                            ", is this your name? (Y/N) ")
        if username_check == 'Y':
            print("Welcome back, " + username + "!")
        else:
            print("Ow, let's correct this!")
            username = get_new_username()
    else:
        username = get_new_username()

greet_user()
