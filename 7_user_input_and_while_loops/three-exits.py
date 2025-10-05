"""
7-6. Three Exits: 

Write different versions of either Exercise 7-4 or Exercise 7-5
that do each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value.
"""

print("=== TICKETING MACHINE === \n")

loops = 0

while loops < 5:
    loops += 1
    age_input = input("\n" + "Enter your age to check ticket price (or type "
    "'buy' to buy the ticket): ")
    
    if age_input.lower() == 'buy':
        break

    age = int(age_input)
    
    if age < 3:
        price = 0
    elif age < 12:
        price = 10
    else:
        price = 15

    print("The cost of your ticket is $" + str(price) + ". \n")
    print("You check " + str(5 - loops) + " more times.")

print("\n" + "Thank you for your visit!")
