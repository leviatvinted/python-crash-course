"""
9-5. Login Attempts: 

    Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. Write
another method called reset_login_attempts() that resets the value of login_
attempts to 0.
    Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
"""

class User():
    def __init__(self, first_name, last_name, age, location_country,
                 location_city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location_country = location_country
        self.location_city = location_city
        self.login_attempts = 0
    
    def describe_user(self):
        print("\nUser: " + self.first_name.title() + " " + 
              self.last_name.title())
        print("Age: " + str(self.age))
        print("Location: " + self.location_city.title() + ", " +
              self.location_country.title())

    def greet_user(self):
        print("\nHi " + self.first_name.title() + ", how are you?")
        print("How is the weather today in " + self.location_city.title() + "?")

    def increment_login_attempts(self):
        print("\nTrying to login...")
        self.login_attempts += 1

    def reset_login_attempts(self):
        print("\nLogin successful. Reseting login attempts..")
        self.login_attempts = 0

    def read_login_attempts(self):
        print("Login(s) attempted: " + str(self.login_attempts))

user_1 = User('john', 'doe', 25, 'spain', 'madrid')
user_2 = User('jane', 'doe', 30, 'italy', 'milan')
user_3 = User('james', 'jones', 27, 'ireland', 'dublin')

user_1.increment_login_attempts()
user_1.read_login_attempts()
user_1.increment_login_attempts()
user_1.read_login_attempts()
user_1.increment_login_attempts()
user_1.read_login_attempts()

user_1.reset_login_attempts()
user_1.read_login_attempts()
