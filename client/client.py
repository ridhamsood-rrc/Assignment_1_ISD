"""THis file contains the information of the client."""

__name__ = "Ridham Sood"
__version__ = "1.0.0"

from email_validator import EmailNotValidError, validate_email

class Client:
    """Initializes a client object."""

    def __init__(self, client_number:int, first_name:str, last_name: str,
                 email_address:str):
        """Initializes the init function.
        
        args:
            client_number: The number of the client.
            first_name: The first name of the client.
            last_name: The last name of the client.
            email_address: The email address of the client.
        
        Raises:
            Valueerror: It raises an exception if first name and last 
                        name is blank.
            Valueerror: It raises an exception if the client number is
                        not if int type.
            Valueerror: It raises an exception if email address is not
                        valid.
        
        """

        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be an int type.")
        
        if len(first_name.strip()) > 0:
            self.__first_name = first_name
        else:
            raise ValueError("First name cannot be blank.")
        
        if len(last_name.strip()) > 0:
            self.__last_name = last_name
        else:
            raise ValueError("Last name should not be blank.")
        
        if validate_email(email_address):
            self.__email_address = email_address
        else:
            raise EmailNotValidError("Email address should be in the correct format.")
        
    @property
    def client_number(self) -> int:
        return self.__client_number
    
    @property
    def first_name(self) -> str:
        return self.__first_name
    
    @property
    def last_name(self) -> str:
        return self.__last_name
    
    @property
    def email_address(self) -> str:
        return self.__email_address
    
    def __str__(self) -> str:
        return(f"{self.__last_name}, {self.__first_name} [{self.__client_number}] - {self.__email_address}")
        

