"""
5-3. Alien Colors #1: 

Imagine an alien was just shot down in a game. Create a
variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
• Write an if statement to test whether the alien’s color is green. If it is, print
a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that
fails. (The version that fails will have no output.)

"""

# alien_color = 'green'

# if alien_color == 'green':
#     print("The alien is " + alien_color + " You earned 5 points.")

# if alien_color != 'green':
#     print("The alien is " + alien_color + " You earned no points.")

# if alien_color == 'yellow':
#     print("The alien is " + alien_color + " You earned 5 points.")

# if alien_color != 'yellow':
#     print("The alien is " + alien_color + " You earned no points.")


"""
5-4. Alien Colors #2: 

Choose a color for an alien as you did in Exercise 5-3, and
write an if-else chain.
• If the alien’s color is green, print a statement that the player just earned
5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned
10 points.
• Write one version of this program that runs the if block and another that
runs the else block.

5-5. Alien Colors #3: 

Turn your if-else chain from Exercise 5-4 into an if-elif-
else chain.
• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed
for the appropriate color alien.
"""

# Example running the if block
alien_color = 'green'

if alien_color == 'green':
    print("The alien is " + alien_color + " You earned 5 points.")

else:
    print("The alien is " + alien_color + " You earned 10 points.")

# Example running the else block
alien_color = 'yellow'

if alien_color == 'green':
    print("The alien is " + alien_color + " You earned 5 points.")

else:
    print("The alien is " + alien_color + " You earned 10 points.")


# Example running the if block
alien_color = 'green'

if alien_color == 'green':
    print("The alien is " + alien_color + " You earned 5 points.")

elif alien_color == 'yellow':
    print("The alien is " + alien_color + " You earned 10 points.")

else:
    print("The alien is " + alien_color + " You earned 15 points.")

# Example running the elif block
alien_color = 'yellow'

if alien_color == 'green':
    print("The alien is " + alien_color + " You earned 5 points.")

elif alien_color == 'yellow':
    print("The alien is " + alien_color + " You earned 10 points.")

else:
    print("The alien is " + alien_color + " You earned 15 points.")

# Example running the else block
alien_color = 'red'

if alien_color == 'green':
    print("The alien is " + alien_color + " You earned 5 points.")

elif alien_color == 'yellow':
    print("The alien is " + alien_color + " You earned 10 points.")

else:
    print("The alien is " + alien_color + " You earned 15 points.")
