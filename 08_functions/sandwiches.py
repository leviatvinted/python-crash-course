"""
8-12. Sandwiches: 

Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sand-
wich that is being ordered. Call the function three times, using a different num-
ber of arguments each time.
"""

def make_sandwich(*ingredients):
    print("\nMaking a sandwhich with the following ingredients:")
    for ingredient in ingredients:
        print("\t- " + ingredient)

make_sandwich('ham', 'cheese')
make_sandwich('salmon', 'cream cheese', 'lettuce')
make_sandwich('pepperoni', 'cheese', 'green peppers')
