'''
3-8. Seeing the World:
Think of at least five places in the world you'd like to
visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don't worry about printing the list neatly,
just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the
actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse alphabetical order without chang-
ing the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse() to change the order of your list. Print the list to show that its
order has changed.
• Use reverse() to change the order of your list again. Print the list to show
it's back to its original order.
• Use sort() to change your list so it's stored in alphabetical order. Print the
list to show that its order has been changed.
• Use sort() to change your list so it's stored in reverse alphabetical order.
Print the list to show that its order has changed.
'''


WANT_TO_VISIT = ['taj mahal', 'machu picchu', 'pyramids of giza', 'angkor wat', 'grand canyon']

print("The original list:")
print(WANT_TO_VISIT)

print("\nTemporarily sorting the list in alphabetical order...")
print(sorted(WANT_TO_VISIT))

print("\nThe original list remains:")
print(WANT_TO_VISIT)

print("\nTemporarily sorting the list in reverse alphabetical order...")
print(sorted(WANT_TO_VISIT, reverse = True))

print("\nThe original list still remains:")
print(WANT_TO_VISIT)

print("\nReversing the list...")
WANT_TO_VISIT.reverse()
print(WANT_TO_VISIT)

print("\nReversing back to original...")
WANT_TO_VISIT.reverse()
print(WANT_TO_VISIT)

print("\nPerminantly sorting list in alphabetical order...")
WANT_TO_VISIT.sort()
print(WANT_TO_VISIT)

print("\nPerminantly sorting list in revers alphabetical order...")
WANT_TO_VISIT.sort(reverse = True)
print(WANT_TO_VISIT)
