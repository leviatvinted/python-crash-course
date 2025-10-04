"""
7-2. Restaurant Seating: 

Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message say-
ing they’ll have to wait for a table. Otherwise, report that their table is ready.
"""

print("Welcome to Pizza Joe's \n")
party_size = int(input("How many people are you with? "))

if party_size >= 8:
    print("\n" + "You will have to wait for a table.")

else:
    print("\n" + "Your table is ready.")
