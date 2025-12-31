"""
4-2. Animals: 

Think of at least three different animals that have a common char-
acteristic. Store the names of these animals in a list, and then use a for loop to
print out the name of each animal.

• Modify your program to print a statement about each animal, such as
A dog would make a great pet.

• Add a line at the end of your program stating what these animals have in
common. You could print a sentence such as Any of these animals would
make a great pet!
"""

ANIMALS = ['cassowary', 'crocodile', 'turtle']

print("The following animals have a common characteristic:")
for animal in ANIMALS:
    print("\t" + animal.title())

print("\nFun facts:")
print("\tThe " + ANIMALS[0].title() +  "'s casque (the helmet-like growth on",
        "its head) is thought to help it push through dense rainforest",
        "undergrowth, amplify sounds, or even regulate its body temperature."
       )
print("\t" + ANIMALS[1].title() + "s have the strongest bite of any living", 
        "animal, capable of exerting over 3,700 pounds per square inch (psi)", 
        "of pressure!"
      )
print("\tSome Sea " + ANIMALS[2].title() + "s can hold their breath for ",
        "several hours, slowing their heart rate to conserve oxygen."
      )

print("\nTheir evolutionary lines extend back millions of years, with",
        "ancestors coexisting with dinosaurs."
        )
