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
"""

WANT_TO_VISIT = ['taj mahal', 'machu picchu', 'pyramids of giza', 'angkor wat', 
                 'grand canyon', 'leaning tower of pisa', 
                 'the great wall of china'
                 ]

print("The first threee items in the list are:")
print(WANT_TO_VISIT[:3])

print("\nThree items from the middle of the list are:")
print(WANT_TO_VISIT[2:5])

print("\nThe last three items in the list are:")
print(WANT_TO_VISIT[4:])
