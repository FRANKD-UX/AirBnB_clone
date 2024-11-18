#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review."""
    place_id = ""  # Will store the Place.id
    user_id = ""   # Will store the User.id
    text = ""
