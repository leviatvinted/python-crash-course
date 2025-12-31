"""
6-1. Person: 

Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary.
"""

person = {'first_name': 'john', 'last_name': 'doe', 'age': 30, 
            'city': 'new york'}

print(str(person) + "\n")
print(person['first_name'].title())
print(person['last_name'].title())
print(person['age'])
print(person['city'].title())

"""
6-7. People: 

Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person.
"""

# Version 1
person_1 = {'first_name': 'john', 'last_name': 'doe', 'age': 30, 
            'city': 'new york'}
person_2 = {'first_name': 'sarah', 'last_name': 'stone', 'age': 28, 
            'city': 'austin'},
person_3 = {'first_name': 'michelle', 'last_name': 'jones', 'age': 21, 
            'city': 'los angeles'}

people = [person_1, person_2, person_3]

print("\n" + "Notation version 1 \n")
for person in people:
    print(people)

# Version 2
people2 = {
    'jdoe': {
        'first_name': 'john', 'last_name': 'doe', 'age': 30, 'city': 'new york'
        },
    'sstone': {
        'first_name': 'sarah', 'last_name': 'stone', 'age': 28, 'city': 'austin'
        },
    'mjones': {
        'first_name': 'michelle', 'last_name': 'jones', 'age': 21, 'city': 'los angeles'
        }
    }

print("\n" + "Notation version 2 \n")
for person, personal_info in people2.items():
    print(
        personal_info['first_name'].title() + " " +
        personal_info['last_name'].title() + " is " + 
        str(personal_info['age']) + " years old and lives in " + 
        personal_info['city'].title() + "."
        )
