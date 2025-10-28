"""
11-3. Employee: 

Write a class called Employee. The __init__() method should
take in a first name, a last name, and an annual salary, and store each of these
as attributes. Write a method called give_raise() that adds $5000 to the
annual salary by default but also accepts a different raise amount.
    Write a test case for Employee. Write two test methods, test_give_
default_raise() and test_give_custom_raise(). Use the setUp() method so
you don’t have to create a new employee instance in each test method. Run
your test case, and make sure both tests pass.
"""

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee."""

    def setUp(self):
        """"Create an employee for use in all test methods."""
        self.f_name = 'John'
        self.l_name = 'Doe'
        self.salary = 70000

        self.my_employee = Employee(self.f_name, self.l_name, self.salary)
    
    def test_give_default_raise(self):
        """Test that gives a default raise."""
        self.my_employee.give_raise()
        
        expcted_salary = self.salary + 5000
        self.assertEqual(self.my_employee.salary, expcted_salary)
        
    def test_give_custom_raise(self):
        """Test that gives a custom raise."""
        custom_raise_amount = 8000
        
        self.my_employee.give_raise(custom_raise_amount)
        
        expcted_salary = self.salary + custom_raise_amount
        self.assertEqual(self.my_employee.salary, expcted_salary)

unittest.main()
