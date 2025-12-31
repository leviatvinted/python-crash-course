"""
9-12. Multiple Modules: 

Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly.
"""

from admin_privileges import Admin

superadmin = Admin('john', 'doe', 57, 'finland', 'oslo')
superadmin.describe_user()
superadmin.privileges.show_privileges()
