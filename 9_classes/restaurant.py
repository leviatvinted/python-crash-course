"""
9-1. Restaurant: 

Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indi-
cating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attri-
butes individually, and then call both methods.

9-2. Three Restaurants: 

Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
"""


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print("\nThe name of the restaurant is '" + self.restaurant_name.title() 
              + "'.")
        print(self.cuisine_type.title() + " is the type of cuisine they serve.")

    def open_restaurant(self):
        print("\n" + self.restaurant_name.title() + " is now open!")

new_restaurant = Restaurant('fries with guys', 'deep fried')
print("Adding new restaurant: " + new_restaurant.restaurant_name.title() + ".")
print("Adding type of cuisine: " + new_restaurant.cuisine_type.title() + ".")

new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()

new_restaurant_1 = Restaurant('my thai', 'thai')
new_restaurant_2 = Restaurant('chinese from overseas', 'chinese')
new_restaurant_3 = Restaurant('doodle your noodle', 'noodles')

new_restaurant_1.describe_restaurant()
new_restaurant_2.describe_restaurant()
new_restaurant_3.describe_restaurant()
