"""
9-6. Ice Cream Stand: 

An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.
"""


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print("\nThe name of the restaurant is '" + self.restaurant_name.title() 
              + "'.")
        print(self.cuisine_type.title() + " is the type of cuisine they serve.")

    def open_restaurant(self):
        print("\n" + self.restaurant_name.title() + " is now open!")

    def read_number_served(self):
        print(self.restaurant_name.title() + " has served " + 
              str(self.number_served) + " people today.")

    def set_number_served(self, serving):
        self.number_served = serving

    def increment_number_served(self, served):
        if served >= self.number_served:
            self.number_served += served
        else:
            print("You can't rollback the customers served for today.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'strawberry', 'chocolate']
    
    def list_flavors(self):
        print("\nThe following flavors are available:")
        for flavor in self.flavors:
            print("\t- " + flavor.title())

icecreamstand1 = IceCreamStand("ice ice baby", "ice cream")
icecreamstand1.describe_restaurant()
icecreamstand1.list_flavors()
