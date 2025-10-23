"""
9-11. Imported Admin: 

Start with your work from Exercise 9-8 (page 178).
Store the classes User, Privileges, and Admin in one module. Create a sepa-
rate file, make an Admin instance, and call show_privileges() to show that
everything is working correctly.
"""

from admin_module import Admin

superadmin = Admin('john', 'doe', 57, 'finland', 'oslo')
superadmin.describe_user()
superadmin.privileges.show_privileges()
