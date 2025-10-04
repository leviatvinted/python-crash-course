"""
7-1. Rental Car:

Write a program that asks the user what kind of rental car they
would like. Print a message about that car, such as “Let me see if I can find you
a Subaru.
”
"""
name = input("Hi, what is your name? ").lower()

print("Hello, " + name.title() + "!")

car = input("\n" + "What kind of rental car are you looking for? ").lower()

print("Let me see if I can find you a " + car.title() + ".")
