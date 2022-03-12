#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base, Column, String, ForeignKey


class Review(BaseModel, Base):
    __tablename__ = "reviews"
    """ Review classto store review information """
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)

