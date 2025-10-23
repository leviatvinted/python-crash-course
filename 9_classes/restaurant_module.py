"""
9-10. Imported Restaurant: 

Using your latest Restaurant class, store it in a mod-
ule. Make a separate file that imports Restaurant. Make a Restaurant instance,
and call one of Restaurant’s methods to show that the import statement is work-
ing properly.
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
