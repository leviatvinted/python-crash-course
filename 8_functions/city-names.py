"""
8-6. City Names: 

Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:

"Santiago, Chile"

Call your function with at least three city-country pairs, and print the value
that’s returned.
"""

# Version 1
# def city_country(city, country):
#     print('"' + city.title() + ", " + country.title() + '"')

# city_country('santiago', 'chile')
# city_country('berlin', 'germany')
# city_country('madrid', 'spain')

#Version 2
def city_country(city, country):
    formatted_location = ('"' + city.title() + ', ' + country.title() + '"')
    return formatted_location

location = city_country('santiago', 'chile')
print(location)

location = city_country('berlin', 'germany')
print(location)

location = city_country('madrid', 'spain')
print(location)

