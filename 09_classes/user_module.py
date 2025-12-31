"""
9-12. Multiple Modules: 

Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly.
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
        
