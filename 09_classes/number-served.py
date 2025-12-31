"""
9-4. Number Served: 

Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
    Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
    Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any num-
ber you like that could represent how many customers were served in, say, a
day of business.
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

new_restaurant = Restaurant('fries with guys', 'deep fried')
new_restaurant.describe_restaurant()

new_restaurant.read_number_served()

new_restaurant.set_number_served(50)
new_restaurant.read_number_served()

new_restaurant.increment_number_served(100)
new_restaurant.read_number_served()
