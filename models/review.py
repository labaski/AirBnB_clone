#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class wzqReview(BaseModel):
    """Represent a review.

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

    wzqplace_id = ""
    wzquser_id = ""
    wzqtext = ""
