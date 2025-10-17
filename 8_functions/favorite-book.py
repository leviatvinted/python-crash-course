"""
8-2. Favorite Book: 

Write a function called favorite_book() that accepts one
parameter, title. The function should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to
include a book title as an argument in the function call.
"""

def favorite_book(fname, title):
    """Simple message showing the persons favorite book"""
    print(fname.title() + "'s favorite book is " + title)

fname = input("Hi, what is your name? ")
title = input("What is the title of your favorite book? ")

favorite_book(fname, title)
