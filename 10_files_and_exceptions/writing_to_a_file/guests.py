"""
10-3. Guest: 

Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.
"""

filename = 'guests.txt'

with open(filename, 'w') as file_object:
    file_object.write(input("Hi, what is your name? ").lower())
