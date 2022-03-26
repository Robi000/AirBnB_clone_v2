#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, String, Column
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    __table_args__ = {'extend_existing': True}
    name = Column(String(128), nullable=False)
    citiy = relationship("City", backref="state")

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)
