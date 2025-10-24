"""
10-4. Guest Book: 

Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file.
"""

filename = 'guest_book.txt'
prompt = "\nHi, what is your name?"
prompt += "\n(Enter 'q' to exit.) "

with open(filename, 'a') as file_object:

    while True:
        guest_input = input(prompt)

        if guest_input == 'q':
            break
        else:
            file_object.write(guest_input.lower() + "\n")
            print("Greetings, " + guest_input.title() + "!")
