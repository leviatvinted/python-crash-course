"""
9-7. Admin: 

An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.
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

class Admin(User):
    def __init__(self, first_name, last_name, age, location_country,
                 location_city):
        super().__init__(first_name, last_name, age, location_country,
                         location_city)
        self.privileges = ['can add post', 'can delete post', 'can ban user',
                           'can unban user', 'can add group',
                            'can delete group']
    
    def show_privileges(self):
        print("\nAdmins have the following privileges")
        for privilege in self.privileges:
            print("\t- " + privilege)

admin_1 = Admin('dave', 'smith', 38, 'united states', 'los angeles')
admin_1.describe_user()
admin_1.show_privileges()
