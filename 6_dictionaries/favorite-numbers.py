"""
6-2. Favorite Numbers: 

Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program.
"""

favorite_numbers = {
    'john': 7,
    'jane': 9,
    'james': 18,
    'mary': 1,
    'patricia': 4,
    }

# Long notation
print("Long notitation example \n")
print("John's favorite number is " + str(favorite_numbers['john']))
print("Jane's favorite number is " + str(favorite_numbers['jane']))
print("James' favorite number is " + str(favorite_numbers['james']))
print("Mary's favorite number is " + str(favorite_numbers['mary']))
print("Patricia's favorite number is " + str(favorite_numbers['patricia']))

# Short notation
print("\n" +  "Short notitation example \n")
for name, number in favorite_numbers.items():
    print(name.title() + "'s favorite number is: " + str(number))

"""
6-6. Polling: 

Use the code in favorite_languages.py (page 104).
• Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.
"""

take_poll = ['david', 'mary', 'michael', 'sarah', 'john']

print("\n" +  "Have you taken the poll? \n")
for participant in take_poll:
    if participant in favorite_numbers:
        print("Hi " + participant.title() + ", you have already taken the poll, thank you.")
    else:
        print("Hi " + participant.title() + ", We invite you take the poll.")

"""
6-10. Favorite Numbers: 

Modify your program from Exercise 6-2 (page 102) so
each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers.
"""

favorite_numbers_updated = {
    'john': [7, 99, 33],
    'jane': [9, 60],
    'james': [18, 999],
    'mary': [1],
    'patricia': [1, 2, 4, 8, 16, 32, 64, 128],
    }

for name, numbers in favorite_numbers_updated.items():
    print("\n" + name.title() + " favorite numbers are:")
    for number in numbers:
        print("\t" + str(number))
