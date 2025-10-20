"""
8-9. Magicians: 

Make a list of magician’s names. Pass the list to a function
called show_magicians(), which prints the name of each magician in the list.

8-10. Great Magicians: 

Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the list of magicians by add-
ing the phrase the Great to each magician’s name. Call show_magicians() to
see that the list has actually been modified.
"""

# Version 1 (8-9 + 8-10)

# def show_magicians(magicians):
#     for magician in magicians:
#         print(magician.title())

# def make_great(magicians, great_magicians):
#     while magicians:
#         great_magician = magicians.pop()
#         great_magicians.append("the great " + great_magician)
      
# def show_great_magicians(great_magicians):
#     for great_magician in great_magicians:
#         print(great_magician.title())

# magicians = ['houdini', 'mystifying zandero', 'harry potter']
# great_magicians = []

# show_magicians()
# make_great(magicians, great_magicians)
# show_great_magicians(great_magicians)

# Version 2 (8-9 + 8-10)

# def show_magicians(magicians):
#     for magician in magicians:
#         print("\t" + magician.title())

# def make_great(magicians):
#     great_magicians = ["the great " + magician for magician in magicians]

#     magicians.clear()
#     magicians.extend(great_magicians)

# magicians = ['houdini', 'mystifying zandero', 'harry potter']

# print("Magicians:")
# show_magicians(magicians)

# print ("\nMaking the magicians great...")
# make_great(magicians)

# print("\nGreat Magicians:")
# show_magicians(magicians)

"""
8-11. Unchanged Magicians: 

Start with your work from Exercise 8-10. Call the
function make_great() with a copy of the list of magicians’ names. Because the
original list will be unchanged, return the new list and store it in a separate list.
Call show_magicians() with each list to show that you have one list of the origi-
nal names and one list with the Great added to each magician’s name.
"""

# Version 3 (8-11)

def show_magicians(magicians):
    for magician in magicians:
        print("\t" + magician.title())

def make_great(magicians, great_magicians):
    while magicians:
        great_magician = magicians.pop()
        great_magicians.append("the great " + great_magician)


magicians = ['houdini', 'mystifying zandero', 'harry potter']
great_magicians = []

print ("\nMaking the magicians great...\n")
make_great(magicians[:], great_magicians)

print("Magicians:")
show_magicians(magicians)

print("\nGreat Magicians:")
show_magicians(great_magicians)
