"""This file contains the information of the bank account."""

__author__ = "Ridham Sood"
__version__ = "1.0.0"

class BankAccount:
    """Initializes the bank account object"""

    def __init__(self, account_number:int, client_number:int, balance:float):
        """ Initializes the init method.
        
        args:  
            account_number(int): The account number of the account holder.
            client_number(int): The client number of the account holder.
            balance(float): The balance of the account holder.
        
        """

        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("Account number must be an int type.")
        
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be an int type.")
        
        try:
            self.__balance = float(balance)
        except (ValueError, TypeError):
            self.__balance = 0.0

    @property
    def account_number(self) -> int:
        """This helps to access the account number anywhere.

        Return:
            int: The account number attribute.
        
        """
        return self.__account_number
    
    @property
    def client_number(self) -> int:
        """This helps to access the client number anywhere.
        
        Return:
            int: The client number attribute.
        """
        return self.__client_number
    
    @property
    def balance(self) -> float:
        """This helps to access the balance anywhere.
        
        Return:
            float: The balance of the account holder.
        """
        return self.__balance
    
    def update_balance(self, amount: int) -> None:
        """Updates the balance of the account holder.
        
        args:
            amount(int): The amount which will be deposited or withdraw.
        
        """

        try:
            updated_balance = float(amount)
            self.__balance += amount
        except ValueError:
            updated_balance = self.__balance
      

    def deposit(self, amount:int) -> None:
        """The amount deposited to the account.
        
        args:
            amount(int): The amount which is deposited.

        Raises:
            ValueError: Raises when amount is not numeric.
            ValueError: Raises when amount is negative.
        """

        try:
            valid_amount = int(amount)
        except ValueError:
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        
        if valid_amount >= 0:
                self.update_balance(valid_amount)
        else:
            raise ValueError(f"Deposit amount: ${amount:,.2f} must be positive.")

        
    def withdraw(self, amount:int) -> None:
        """The withdraw method to calculate the balance.
        
        args:
            amount(int): The amount which is withdrew by the account holder.

        Raises:
            ValueError: Raises when the amount is not numeric.
            ValueError: Raises when the amount is more than the current balance.
            ValueError: Raises when the amount is negative.
        
        """

        try:
            valid_amount = int(amount)
        except ValueError:
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")
        
        if valid_amount >= 0:
            if valid_amount <= self.__balance:
                real_amount = valid_amount * -1
                self.update_balance(real_amount)
            else:
                raise ValueError(f"Withdraw amount: ${amount:,.2f} must not exceed the current balance: ${self.__balance}")
        else:
            raise ValueError(f"Withdraw amount: ${amount:,.2f} must be positive.")
        

    def __str__(self) -> str:
        """The str method to display the final content.
        
        Return:
            str: The final statement displayed to the account holder.
        """

        return(f"Account number: {self.__account_number} Balance: ${self.__balance:,.2f}")
