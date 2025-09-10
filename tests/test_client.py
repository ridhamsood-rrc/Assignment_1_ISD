"""
Description: Unit tests for the Client class.
Author: Ridham Sood
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

__author__="Ridham Sood"
__version__ = "1.0.0"

from client.client import Client
import unittest

class TestClass(unittest.TestCase):
    """"""
    def setUp(self):

        self.client = Client(1, "Joe", "Henderson", "joehenderson9@gmail.com")

    def test_init_set_attribute_to_input_values(self):

        # Arrange & Act already

        # Assert
        self.assertEqual(1, self.client._Client__client_number)
        self.assertEqual("Joe", self.client._Client__first_name)
        self.assertEqual("Henderson", self.client._Client__last_name)
        self.assertEqual("joehenderson9@gmail.com", self.client._Client__email_address)

    def test_init_invalid_client_number_raise_exception(self):

        # Act
        with self.assertRaises(ValueError):
            client = Client("one", "Joe", "Henderson", "joehenderson9@gmail.com")

    def test_init_invalid_first_name_raise_exception(self):
        
        # Arrange & Act
        with self.assertRaises(ValueError):
            client = Client(1, "", "henderson", "joehenderson9@gmail.com")

    def test_init_invalid_last_name_raise_exception(self):

        # Arrange & Act
        with self.assertRaises(ValueError):
            client = Client(1, "Joe", "", "joehenderson9@gmail.com")

    def test_init_invalid_email_address_raise_exception(self):

        # Arrnage & Act
        with self.assertRaises(ValueError):
            client = Client(1, "Joe", "henderson", "joehenderson9")
    
    def test_accessor_return_client_number_attribute(self):

        # Arrange & Act done already

        # Assert
        self.assertEqual(1, self.client.client_number)

    def test_accessor_return_first_name_attribute(self):

        # Arrange & Act done already

        # Assert
        self.assertEqual("Joe", self.client.first_name)

    def test_accessor_return_last_name_attribute(self):

        # Arrange & Act done already

        # Assert
        self.assertEqual("Henderson", self.client.last_name)

    def test_accessor_return_email_address_attribute(self):

        # Arrange & Act done already

        # Assert
        self.assertEqual("joehenderson9@gmail.com", self.client.email_address)

    def test_str_return_valid_string(self):

        # Arrange done already
        # Act
        expected = "Henderson, Joe [1] - joehenderson9@gmail.com"

        # Assert
        self.assertEqual(expected, str(self.client))