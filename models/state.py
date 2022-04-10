#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, String, Column
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    __table_args__ = {'extend_existing': True}
    name = Column(String(128), nullable=False)
    citiy = relationship("City", backref="state")

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
