"""
4-1. Pizzas: 

Think of at least three kinds of your favorite pizza. Store these
pizza names in a list, and then use a for loop to print the name of each pizza.

• Modify your for loop to print a sentence using the name of the pizza
instead of printing just the name of the pizza. For each pizza you should
have one line of output containing a simple statement like I like pepperoni
pizza.

• Add a line at the end of your program, outside the for loop, that states
how much you like pizza. The output should consist of three or more lines
about the kinds of pizza you like and then an additional sentence, such as
I really love pizza!
"""

FAV_PIZZAS = ['pepperoni', 'neapolitan', 'quattro formaggi']

# Version 1
# for pizza in FAV_PIZZAS:
#     print(pizzas.title())

for pizza in FAV_PIZZAS:
    print("I love a " + pizza.title() + " pizza!")
print("\nI really really love pizza!")


"""
4-10. Slices: 
Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:

• Print the message, The first three items in the list are:. Then use a slice to
print the first three items from that program’s list.

• Print the message, Three items from the middle of the list are:. Use a slice
to print three items from the middle of the list.

• Print the message, The last three items in the list are:. Use a slice to print
the last three items in the list.

4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
(page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
Then, do the following:

• Add a new pizza to the original list.

• Add a different pizza to the list friend_pizzas.

• Prove that you have two separate lists. Print the message, My favorite
pizzas are:, and then use a for loop to print the first list. Print the message,
My friend’s favorite pizzas are:, and then use a for loop to print the sec-
ond list. Make sure each new pizza is stored in the appropriate list.

4-12. More Loops: 
All versions of foods.py in this section have avoided using
for loops when printing to save space. Choose a version of foods.py, and
write two for loops to print each list of foods.
"""

