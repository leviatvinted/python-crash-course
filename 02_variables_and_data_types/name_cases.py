# First name variables
FNAME_1 = "jan"
FNAME_2 = "    koos    "

# Quotes by famouse people
FAMOUS_PERSON = "guido van rossum"
FAMOUS_QUOTE = "Python was created to be fun to use, and it has stayed that way throughout its evolution."
MESSAGE = "\n" + FAMOUS_PERSON.title() + " once said: " + '"' + FAMOUS_QUOTE + '"'

print("Hi " + FNAME_1.title() + ", would you like to learn some Python today?")

print(
    "\nHi " + FNAME_1.title() + 
    ", this is your name in lowercase: " + FNAME_1.lower() +
    ", in uppercase: " + FNAME_1.upper() + 
    ", and in titlecase: " + FNAME_1.title() + "."
)

# Variations in printing messages with and without a stored variable
print('\nLinus Torvalds once said: "Talk is cheap. Show me the code"')
print(MESSAGE)

# Strips whitespace from the first name
print("\nOriginal entry: " + FNAME_2)
print("\tlstrip: " + FNAME_2.lstrip())
print("\trstrip: " + FNAME_2.rstrip())
print("\tstrip: " + FNAME_2.strip())
