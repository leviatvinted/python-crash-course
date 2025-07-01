'''
3-10. Every Function:
Think of something you could store in a list. For example,
you could make a list of mountains, rivers, countries, cities, languages, or any-
thing else you'd like. Write a program that creates a list containing these items
and then uses each function introduced in this chapter at least once.
'''

MY_POKEDEX = []
HELD_POKEMON = []
STORED_POKEMON = []
BILLS_PC = []

MY_ITEMS = ['pokédex',]
RIVAL_POKEMON = []
STARTER_POKEMON = ['bulbasaur', 'charmander', 'squirtle']

print("You awaken in your bedroom in Pallet Town...")
print("\nGood to see you! How is your Pokédex coming? Here, let me take a look!")
print("\tPokémon seen: " + str(len(MY_POKEDEX)))
POKEMON_CAUGHT = len(HELD_POKEMON) + len(STORED_POKEMON)
print("\tPokémon caught: " + str(POKEMON_CAUGHT))
print("\nYou still have lots to do. Look for Pokémon in grassy areas!")

print("\nYou leave your house and attempt to walk into the grass...")
print("\nA wild professor Oak appears:")
print(
    '"Hey! Wait!' " Don't go out! It's" ' unsafe! Wild Pokémon live in tall grass!"', 
    '\n"You need your own Pokémon for your protection. I know! Here, come with me!"'
)

print("\nYou follow professor Oak into his lab and are presented with:")
print(
    STARTER_POKEMON[0].upper() + ", " + 
    STARTER_POKEMON[1].upper() + ", and " + 
    STARTER_POKEMON[2].upper()
)

MY_CHOICE = STARTER_POKEMON.pop(1)
HELD_POKEMON.append(MY_CHOICE)
POKEMON_CAUGHT = len(HELD_POKEMON) + len(STORED_POKEMON)
MY_POKEDEX.append(MY_CHOICE)
print("\nYou obviously choose " + MY_CHOICE.upper() + "!")

RIVAL_CHOICE = STARTER_POKEMON.pop(1)
RIVAL_POKEMON.append(RIVAL_CHOICE)
print("\nYour rival surprisingly chooses " + RIVAL_CHOICE.upper() + "!")

print("\nYour rival challenges you to a battle!")
print("\nMany, many, many.... Tail whips later... You win the fight!")
MY_POKEDEX.append(RIVAL_CHOICE)

MY_ITEMS.append('pokè ball')
POKEBALLS = +5
print(
    "\nProfessor Oak gives you " + 
    str(POKEBALLS) + "s " + 
    MY_ITEMS[1].upper() + "."
)

print("\nGood to see you! How is your Pokédex coming? Here, let me take a look!")
print("\tPokémon seen: " + str(len(MY_POKEDEX)))
print("\tPokémon caught: " + str(POKEMON_CAUGHT))

print("\nYou continue your journey and decide to take route 1 to Veridian City.")
MY_ITEMS.append('potion')
POTIONS = +1
print("\nYou find " + str(POTIONS), MY_ITEMS[2] + " on the ground!")

WILD_POKEMON = 'ratata'
MY_POKEDEX.append(WILD_POKEMON)
print("\nWild " + WILD_POKEMON.upper() + " appeared!")

POKEBALLS = -1
HELD_POKEMON.append(WILD_POKEMON)
print("\nYou throw a " + MY_ITEMS[1].upper() + " at " + WILD_POKEMON.upper())
print("Wiggle...")
print("Wiggle...")
print("Wiggle...")
print("CLICK!")
print("\nAll right! " + WILD_POKEMON.upper() + " was caught!")
print(WILD_POKEMON.upper() + " data was added to the " + MY_ITEMS[0].upper() + "!")

print("\nGood to see you! How is your Pokédex coming? Here, let me take a look!")
print("\tPokémon seen: " + str(len(MY_POKEDEX)))
POKEMON_CAUGHT = len(HELD_POKEMON) + len(STORED_POKEMON)
print("\tPokémon caught: " + str(POKEMON_CAUGHT))

print("\nYou continue your journey...")

WILD_POKEMON = 'pidgey'
MY_POKEDEX.append(WILD_POKEMON)
print("\nWild " + WILD_POKEMON.upper() + " appeared!")

POKEBALLS = -1
HELD_POKEMON.append(WILD_POKEMON)
print("\nYou throw a " + MY_ITEMS[1].upper() + " at " + WILD_POKEMON.upper())
print("Wiggle...")
print("Wiggle...")
print("Wiggle...")
print("CLICK!")
print("\nAll right! " + WILD_POKEMON.upper() + " was caught!")
print(WILD_POKEMON.upper() + " data was added to the " + MY_ITEMS[0].upper() + "!")

print("\nGood to see you! How is your Pokédex coming? Here, let me take a look!")
print("\tPokémon seen: " + str(len(MY_POKEDEX)))
POKEMON_CAUGHT = len(HELD_POKEMON) + len(STORED_POKEMON)
print("\tPokémon caught: " + str(POKEMON_CAUGHT))

print("\nYou finally arive in Veridian City.")
print("\nYou walk into the local Pokémon Center.")
print("\nYou decide to store Pokémon in BILL's PC")
print("\nYou currently hold the following Pokémon:")
print(sorted(HELD_POKEMON))

print("\nDeposit POKÉMON")
print("\nWhich POKÉMON do you want to put away?")
print(HELD_POKEMON)

del HELD_POKEMON[1]
BILLS_PC.insert(0, 'ratata')

print("\nRATATA has been deposited in BOX 1")

print("\nDeposit POKÉMON")
print("\nWhich POKÉMON do you want to put away?")
print(HELD_POKEMON)

HELD_POKEMON.remove('pidgey')
BILLS_PC.insert(0, 'pidgey')

print("\nGood to see you! How is your Pokédex coming? Here, let me take a look!")
print("\tPokémon seen: " + str(len(MY_POKEDEX)))
POKEMON_CAUGHT = len(HELD_POKEMON) + len(STORED_POKEMON) + len(BILLS_PC)
print("\tPokémon caught: " + str(POKEMON_CAUGHT))

print("\nPOKÉMON in POKÉDEX")
print(MY_POKEDEX)

print("\nSort POKÉMON in alphabetical order")
MY_POKEDEX.sort()
print(MY_POKEDEX)

print("\nSort POKÉMON in reverse alphabetical order")
MY_POKEDEX.sort(reverse=True)
print(MY_POKEDEX)

print("\nSort POKÉMON in alphabetical order")
MY_POKEDEX.sort()
print(MY_POKEDEX)

print("\nSort POKÉMON in reverse alphabetical order")
MY_POKEDEX.reverse()
print(MY_POKEDEX)
