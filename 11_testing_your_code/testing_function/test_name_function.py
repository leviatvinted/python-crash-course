import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'John Doe' work?"""
        formatted_name = get_formatted_name('john', 'doe')
        self.assertEqual(formatted_name, 'John Doe')

    def test_first_last_middle_name(self):
        """Do names like 'John Quidam Doe work?'"""
        formatted_name = get_formatted_name('john', 'doe', 'quidam')
        self.assertEqual(formatted_name, 'John Quidam Doe')

unittest.main()
