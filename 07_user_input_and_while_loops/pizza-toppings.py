"""
7-4. Pizza Toppings: 

Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.
"""

prompt = "\n" + "What topping would you like to add to your pizza?"
prompt += "\n" + "(Enter 'make pizza' when you're ready.) "

while True:
    pizza_topping = input(prompt)

    if pizza_topping == 'make pizza':
        break
    else:
        print("Adding " + pizza_topping + " to your Pizza.")
