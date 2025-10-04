"""
7-3. Multiples of Ten: 

Ask the user for a number, and then report whether the
number is a multiple of 10 or not.
"""

number = int(input("Please provide a number: "))

if number % 10 == 0:
    print("\n" + "Your number is a multiple of 10.")
else:
    print("\n" + "Your number is not a multiple of 10.")
