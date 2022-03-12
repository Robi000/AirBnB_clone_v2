#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ this is the aminity class"""
    
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", overlaps="amenities", secondary="place_amenity",
                                   viewonly=False)

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)
