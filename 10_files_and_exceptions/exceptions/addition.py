"""
10-6. Addition: 

One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int, you’ll get a TypeError. Write a program that prompts for
two numbers. Add them together and print the result. Catch the TypeError if
either input value is not a number, and print a friendly error message. Test your
program by entering two numbers and then by entering some text instead of a
number.

10-7. Addition Calculator: 

Wrap your code from Exercise 10-6 in a while loop
so the user can continue entering numbers even if they make a mistake and
enter text instead of a number.

"""

def get_number_input(prompt_message):
    """Number request that doesn't stop on failed input"""
    while True:
        try:
            user_input = input(prompt_message)
            number = int(user_input)
        except TypeError:
            print("Please make sure to enter a number.\n")
        except ValueError:
            print("Please make sure to enter a number.\n")
        else:
            return number


def addition():
    """Adding two numbers together"""
    print("Let's add two numbers together!\n")
    num_1 = get_number_input("Input the first number: ")
    num_2 = get_number_input("Input the second number: ")
    
    total = int(num_1) + int(num_2)
    
    print("\nThe total of " + str(num_1) + " and " + str(num_2) + " is: " +
        str(total) + "\n")
    
addition()
