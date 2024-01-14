#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class wzqUser(BaseModel):
    """Represent a User.

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    wzqemail = ""
    wzqpassword = ""
    wzqfirst_name = ""
    wzqlast_name = ""
