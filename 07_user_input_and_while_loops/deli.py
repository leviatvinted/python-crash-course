"""
7-8. Deli: 

Make a list called sandwich_orders and fill it with the names of vari-
ous sandwiches. Then make an empty list called finished_sandwiches. Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list
of finished sandwiches. After all the sandwiches have been made, print a
message listing each sandwich that was made.

7-9. No Pastrami: 

Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches.
"""

sandwich_orders = [
    'cheese sandwich', 'pastrami sandwich', 'chicken sandwich', 
    'pastrami sandwich', 'beef sandwich', 'pastrami sandwich'
    ]
finished_sandwiches = []

print("Our apologies, the deli has ran out of pastram. \n")

while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print("I made your " + sandwich + "\n")
    finished_sandwiches.append(sandwich)

print("=== Sanwiches made ===")
for sandwich in finished_sandwiches:
    print("- " + sandwich.title())
