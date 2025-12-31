'''
3-1. Names: 
Store the names of a few of your friends in a list called names. Print
each person's name by accessing each element in the list, one at a time.

3-2. Greetings: 
Start with the list you used in Exercise 3-1, but instead of just
printing each person's name, print a message to them. The text of each mes-
sage should be the same, but each message should be personalized with the
person's name.
'''

FRIENDS = ['john', 'jane', 'dustin']
MESSAGE_0 = "Hi " + FRIENDS[0].title() + ", how are you today?"
MESSAGE_1 = "Hi " + FRIENDS[1].title() + ", how are you today?"
MESSAGE_2 = "Hi " + FRIENDS[2].title() + ", how are you today?"

print(MESSAGE_0)
print(MESSAGE_1)
print(MESSAGE_2)
