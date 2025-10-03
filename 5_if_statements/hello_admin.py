"""
5-8. Hello Admin: 

Make a list of five or more usernames, including the name
'admin'. Imagine you are writing code that will print a greeting to each user
after they log in to a website. Loop through the list, and print a greeting to
each user:
• If the username is 'admin', print a special greeting, such as Hello admin,
would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Eric, thank you for log-
ging in again.
"""

# usernames = ['admin', 'john', 'dave', 'maria', 'annie']

# for username in usernames:
#     if username == 'admin':
#         print("Hello admin, would you like to see a status report?")
#     else:
#         print("Hello " + username.title() + ", thank you for logging in again.")

"""
5-9. No Users: 

Add an if test to hello_admin.py to make sure the list of users is
not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct
message is printed.
"""

usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + username.title() + ", thank you for logging in again.")
else:
    print("We need to find some users!")
