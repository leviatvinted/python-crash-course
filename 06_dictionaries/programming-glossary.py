"""
6-3. Glossary: 

A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
• Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output.

6-4. Glossary 2: 

Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 102) by replacing your series of print
statements with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your
glossary. When you run your program again, these new words and meanings
should automatically be included in the output.
"""

glossary = {
    'print': "Outputs the string representations of given objects to stdout "
    "(console). Supports sep, end, file, flush keyword args.",
    'if': "Starts a conditional block; executes its suite when the condition "
    "is truthy.",
    'elif': "Adds another condition to an if chain; checked only if previous "
    "conditions were false.",
    'else': "Runs when prior if/elif conditions are false; with loops, runs "
    "only if the loop didn't break; with try, runs if no exception occurred.",
    'list': "Mutable ordered sequence. Supports indexing and slicing; methods "
    "like append, extend, insert, remove, pop; literal form [].",
    'tuple': "Immutable ordered sequence. Hashable if its elements are; good "
    "for fixed records and dict keys; literal () or comma-separated values.",
    'dict': "Mutable mapping of key->value pairs; keys must be hashable. "
    "Literal {'k': v}; empty dict is {}.",
    'set': "Unordered collection of unique hashable elements; supports "
    "union/intersection/difference. Literal {1,2}; empty set via set().",
    'int': "Arbitrary-precision integer number type.",
    'float': "Double-precision floating-point number (IEEE 754).",
    'str': "Immutable sequence of Unicode characters; many methods for text "
    "processing.",
    }

print("Programming Glossary")
for entry, meaning in glossary.items():
    print("\n" + entry.title())
    print(meaning)
