"""
10-8. Cats and Dogs: 

Make two files, cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file. Write
a program that tries to read these files and print the contents of the file to the
screen. Wrap your code in a try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing. Move one of the files to a dif-
ferent location on your system, and make sure the code in the except block
executes properly.

10-9. Silent Cats and Dogs: 

Modify your except block in Exercise 10-8 to fail silently if either file is 
missing.
"""

filenames = ['dolphins.txt', 'cats.txt', 'dogs.txt', 'bears.txt']

for filename in filenames:
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # Uncomment print and comment pass if you want to give an error message
        # print("Sorry, the file: " + filename + " could not be found.\n")
        pass
    else:
        print("Reading: " + filename + "\n")
        print(contents)
