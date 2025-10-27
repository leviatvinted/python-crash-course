"""
10-10. Common Words: 

Visit Project Gutenberg (http://gutenberg.org/ )
and find a few texts you’d like to analyze. Download the text files for these
works, or copy the raw text from your browser into a text file on your
computer.
    You can use the count() method to find out how many times a word or
phrase appears in a string. For example, the following code counts the number
of times 'row' appears in a string:

>>> line = "Row, row, row your boat"
>>> line.count('row')
2
>>> line.lower().count('row')
3

    Notice that converting the string to lowercase using lower() catches
all appearances of the word you’re looking for, regardless of how it’s
formatted.
    Write a program that reads the files you found at Project Guten
"""

filenames = ['iliad.txt', 'odyssey.txt', 'miserables.txt', 'mobydick.txt']
word_to_count = input("Check how often a word appears. Input word: ").lower().strip()

for filename in filenames:
    try:
        with open(filename) as f_obj:
            contents = f_obj.read().lower()
    except FileNotFoundError:
        print("Sorry, the file: " + filename + " could not be found.\n")
    else:
        count_words = contents.count(word_to_count)
        print("The word '" + word_to_count + "' appears " + str(count_words) +
            " times in the file " + filename)
