"""
4-13. Buffet: 

A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.

• Use a for loop to print each food the restaurant offers.

• Try to modify one of the items, and make sure that Python rejects the
change.

• The restaurant changes its menu, replacing two of the items with different
foods. Add a block of code that rewrites the tuple, and then use a for
loop to print each of the items on the revised menu.
"""

BUFFET_OPTIONS = ('french fries', 'salad', 'chicken', 'spare-ribs',
                  'ice-cream'
                  )

print("The buffet options are:")
for choice in BUFFET_OPTIONS:
    print(choice.title())

# Try to modify one of the items, and make sure that Python rejects the change.
# Commented this section to continue the exercise
# print("\nThe restaurant has changed from French Fries to Belgian Fries")
# BUFFET_OPTIONS[0] = 'belgian fries'

BUFFET_OPTIONS = ('belgian fries', 'salad', 'duck', 'spare-ribs',
                  'ice-cream'
                  )
print("\nThe restaurant has revised their menu.")
print("\nThe new buffet options are:")
for choice in BUFFET_OPTIONS:
    print(choice.title())
