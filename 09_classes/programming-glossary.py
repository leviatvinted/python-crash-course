"""
9-13. OrderedDict Rewrite: 

Start with Exercise 6-4 (page 108), where you
used a standard dictionary to represent a glossary. Rewrite the program using
the OrderedDict class and make sure the order of the output matches the order
in which key-value pairs were added to the dictionary.
"""

from collections import OrderedDict

glossary = OrderedDict()

glossary['print'] = "Outputs the string representations of given objects to " \
"console."
glossary['if'] = "Starts a conditional block; executes its suite when the " \
"condition is truthy"
glossary['elif'] = "Adds another condition to an if chain; checked only if " \
"previous conditions were false."
glossary['else'] = "Runs when prior if/elif conditions are false; with " \
"loops, runs only if the loop didn't break; with try, runs if no exception occurred."
glossary['list'] = "Mutable ordered sequence. Supports indexing and " \
"slicing; methods like append, extend, insert, remove, pop; literal form []."


print("Programming Glossary")
for entry, meaning in glossary.items():
    print("\n" + entry.title())
    print(meaning)
