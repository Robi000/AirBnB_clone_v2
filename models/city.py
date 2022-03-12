#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.place import Place


class City(BaseModel, Base):
    """ this is city model for the user base model """
    from models.base_model import Base, String, Column, ForeignKey
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    cities = relationship('Place', backref="cities")

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)
