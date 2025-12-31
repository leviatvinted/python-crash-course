"""
8-3. T-Shirt: 

Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.

8-4. Large Shirts: 

Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.
"""

def make_tshirt(tshirt_size, tshirt_message):
    print("You've selected t-shirt size " + tshirt_size.upper() + ".")
    print('The message on the t-shirt: "' + tshirt_message + '".\n')

make_tshirt('m', 'I <3 Vilnius')
make_tshirt(tshirt_size="l", tshirt_message="I have no idea what I'm doing")

def make_shirt(shirt_size='l', shirt_message='I love Python'):
    print("You've selected t-shirt size " + shirt_size.upper() + ".")
    print('The message on the t-shirt: "' + shirt_message + '".\n')

make_shirt()
make_shirt(shirt_size='m')
