#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base, Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Table
from os import getenv

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id', onupdate='CASCADE',
                                        ondelete='CASCADE'),
                             primary_key=True),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id', onupdate='CASCADE',
                                        ondelete='CASCADE'),
                             primary_key=True))


class Place(BaseModel, Base):
    __tablename__ = "places"

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)

    """ A place to stay """
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer(), nullable=False, default=0)
    number_bathrooms = Column(Integer(), nullable=False, default=0)
    max_guest = Column(Integer(), nullable=False, default=0)
    price_by_night = Column(Integer(), nullable=False, default=0)
    latitude = Column(Float(), nullable=True)
    longitude = Column(Float(), nullable=True)
    amenity_ids = []
    from models.review import Review
    reviews = relationship("Review", backref="place")

    amenities = relationship("Amenity", overlaps="amenities", secondary="place_amenity",
                             viewonly=False)
    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            import models
            review_list = []
            from models.review import Review
            listofall = models.storage.all(Review)
            for review in listofall.values():
                if review.place_id == self.id:
                    review_list.append(review)

            return review_list

        @property
        def amenities(self):
            import models
            amenity_list = []
            from models.amenity import Amenity
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id == self.id:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            from models.amenity import Amenity
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
