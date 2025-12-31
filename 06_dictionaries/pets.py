"""
6-8. Pets: 

Make several dictionaries, where the name of each dictionary is the
name of a pet. In each dictionary, include the kind of animal and the owner’s
name. Store these dictionaries in a list called pets. Next, loop through your list
and as you do print everything you know about each pet.
"""

pets = {
    'fluffy':{
        'owner': 'john', 'animal': 'dog', 'age': 7, 'main charateristic': 'good boy'
    },
    'bella':{
        'owner': 'annie', 'animal': 'cat', 'age': 3, 'main charateristic': 'meanie'
    },
    'thumper':{
        'owner': 'james', 'animal': 'rabbit', 'age': 5, 'main charateristic': 'jumpy'
    },
    'bubbles':{
        'owner': 'dave', 'animal': 'fish', 'age': 1, 'main charateristic': 'floaty'
    },
    'squeaky':{
        'owner': 'robert', 'animal': 'hamster', 'age': 12, 'main charateristic': 'noisy'
    },   
}

for pet, pet_info in pets.items():
    print("\nPet name: " + pet.title())
    print("\tOwner: " + pet_info['owner'].title())
    print("\tAnimal: " + pet_info['animal'].title())
    print("\tAge: " + str(pet_info['age']))
    print("\tMain charateristic: " + pet_info['main charateristic'].title())
