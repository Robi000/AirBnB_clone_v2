#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    user = relationship('Place', backref='user')
    reviews = relationship("Review", backref="user")

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)
