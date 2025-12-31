"""
6-11. Cities: 

Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the infor-
mation you have stored about it.
"""

cities = {
    'tokyo': {
        'country': 'japan',
        'population': '14 million',
        'fact': 'Japan is an archipelago consisting of over 6,800 islands.'
    },
    'london': {
        'country': 'united kingdom',
        'population': '9 million',
        'fact': 'The national animal of Scotland, which is part of the UK, is '
        'the unicorn.'
    },
    'mexico city': {
        'country': 'mexico',
        'population': '9 million',
        'fact': "The Great Pyramid of Cholula in Mexico is the world's largest "
        "pyramid by volume, even bigger than the Great Pyramid of Giza in Egypt."
    }
}

for city, city_info in cities.items():
    print("\n" + "City: " + city.title())
    print("\tCountry: " + city_info['country'].title())
    print("\tPopulation: " + city_info['population'])
    print("\tFact: " + city_info['fact'])
