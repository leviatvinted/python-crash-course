"""
9-3. Users: 

Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.
"""

class User():
    def __init__(self, first_name, last_name, age, location_country,
                 location_city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location_country = location_country
        self.location_city = location_city
    
    def describe_user(self):
        print("\nUser: " + self.first_name.title() + " " + 
              self.last_name.title())
        print("Age: " + str(self.age))
        print("Location: " + self.location_city.title() + ", " +
              self.location_country.title())

    def greet_user(self):
        print("\nHi " + self.first_name.title() + ", how are you?")
        print("How is the weather today in " + self.location_city.title() + "?")

user_1 = User('john', 'doe', 25, 'spain', 'madrid')
user_2 = User('jane', 'doe', 30, 'italy', 'milan')
user_3 = User('james', 'jones', 27, 'ireland', 'dublin')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()
