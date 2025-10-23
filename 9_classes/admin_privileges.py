"""
9-12. Multiple Modules: 

Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly.
"""

from user_module import User

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
