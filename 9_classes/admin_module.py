"""
9-11. Imported Admin:

Start with your work from Exercise 9-8 (page 178).
Store the classes User, Privileges, and Admin in one module. Create a sepa-
rate file, make an Admin instance, and call show_privileges() to show that
everything is working correctly.
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

class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user',
                           'can unban user', 'can add group',
                            'can delete group']
        
    def show_privileges(self):
        print("\nAdmins have the following privileges")
        for privilege in self.privileges:
            print("\t- " + privilege)

class Admin(User):
    def __init__(self, first_name, last_name, age, location_country,
                 location_city):
        super().__init__(first_name, last_name, age, location_country,
                         location_city)
        self.privileges = Privileges()
