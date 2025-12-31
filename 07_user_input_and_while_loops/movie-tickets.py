"""
7-5. Movie Tickets: 

A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.
"""

# Version 1
# age = 0

# while age == 0:
#     age = int(input("Welcome to the movie theater. How old are you? "))
#     # age += 1
#     if age < 3:
#         print("Your ticket is free!")
#     elif age <12:
#         print("Your ticket will be $10.")
#     else:
#         print("Your ticket will be $15.")

# Version 2

print("=== TICKETING MACHINE === \n")
while True:
    age_input = input("\n" + "Enter your age to check ticket price: ")
    age = int(age_input)

    if age < 3:
        price = 0
    elif age < 12:
        price = 10
    else:
        price = 15

    print("The cost of your ticket is $" + str(price) + ".")
