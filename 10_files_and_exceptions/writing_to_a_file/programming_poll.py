"""
10-5. Programming Poll: 

Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.
"""

filename = 'programming_poll.txt'

polling_active = True

with open(filename, 'a') as file_object:

    while polling_active:
        reason = input("Why do you like programming? (enter 'q' to close) ")

        if reason == 'q':
            polling_active = False
        else: 
            file_object.write(reason + "\n")

print("\n=== Reasons why people program ====")
with open(filename) as file_object:
    for reason in file_object:
        print(reason.rstrip())
