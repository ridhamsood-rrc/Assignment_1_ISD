"""
Description: Unit tests for the BankAccount class.
Author: Ridham Sood
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""

__author__ = "Ridham Sood"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount
import unittest
from unittest.mock import patch

class TestClass(unittest.TestCase):

    def setUp(self):

        self.bank_account = BankAccount(20021, 123, 2131.123)
    
    def test_init_attributes_set_to_input_values(self):
        # Arrange and Act
        bank_account = BankAccount(20021, 123, 1123.123)

        # Assert
        self.assertEqual(20021, bank_account._BankAccount__account_number)
        self.assertEqual(123, bank_account._BankAccount__client_number)
        self.assertEqual(1123.123, bank_account._BankAccount__balance)

    def test_init_invalid_account_number_raise_exception(self):
        # Arrange & Act
        with self.assertRaises(ValueError):
            bank_account = BankAccount("Ridham", 123, 1231.122)

    def test_init_invalid_client_number_raise_exception(self):
        # Arrange & Act
        with self.assertRaises(ValueError):
            bank_account = BankAccount(20021, "Joe", 1231.122)

    def test_init_non_numeric_balance_set_to_zero(self):
        # Arrange & Act
        bank_account = BankAccount(20021, 123, "Ridham")

        # Assert
        self.assertEqual(bank_account.balance, 0.0)

    def test_getter_returns_account_number_attribute(self):

        # Arrange & Act done already

        # Assert
        self.assertEqual(20021, self.bank_account.account_number)

    def test_getter_returns_client_number_attribute(self):

        # Arrange & Act done already
        
        # Assert
        self.assertEqual(123, self.bank_account.client_number)

    def test_getter_returns_balance_attribute(self):

        # Arrange & Act done already

        # assert 
        self.assertEqual(2131.123, self.bank_account.balance)

    def test_update_balance_when_positive_value_is_received(self):

        # Arrange done already
        # Act
        actual = BankAccount.update_balance(self.bank_account, 31)

        self.assertIsNone(actual)

        self.assertEqual(2162.123, self.bank_account.balance)

    def test_update_balance_when_negative_value_is_received(self):

        # Arrange done already
        # Act
        actual = BankAccount.update_balance(self.bank_account, -21)

        self.assertIsNone(actual)

        self.assertEqual(2110.123, self.bank_account.balance)

    def test_update_balance_when_amount_received_is_non_numeric_balance_remain_unchanged(self):

        # Arrange done already
        # Act
        actual = BankAccount.update_balance(self.bank_account, "Ridham")

        self.assertIsNone(actual)

        # Assert
        self.assertEqual(2131.123, self.bank_account.balance)

    def test_deposit_when_valid_amount_is_provided(self):
        # Arrange done already
        # Act
        
        actual = BankAccount.deposit(self.bank_account, 21)

        self.assertIsNone(actual)

        self.assertEqual(self.bank_account.balance, 2152.123)

    def test_deposit_when_negative_amount_is_provided_raises_exception(self):
        # Arrange
        # Act
        with self.assertRaises(ValueError):
            actual = BankAccount.deposit(self.bank_account, -21)
    
    def test_withdraw_when_valid_amount_is_provided(self):
        # Arrange done already
        # Act
        
        actual = BankAccount.withdraw(self.bank_account, 21)

        self.assertIsNone(actual)
        # Assert
        self.assertEqual(self.bank_account.balance, 2110.123)

    def test_withdraw_when_negative_amount_is_provided_raises_exception(self):
        # Arrange
        # Act
        with self.assertRaises(ValueError):
            actual = BankAccount.withdraw(self.bank_account, -21)

    def test_withdraw_when_amount_exceeds_balance_raises_exception(self):
        # Arrange
        # Act
        with self.assertRaises(ValueError):
            actual = BankAccount.withdraw(self.bank_account, 3221)

    def test_str_return_expected_format(self):

        # Arrange done already
        expected = f"Account number: 20021 Balance: $2,131.12"

        self.assertEqual(expected, str(self.bank_account))