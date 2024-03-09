#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                    Column('place_id', String(60),
                           ForeignKey("places.id"), primary_key=True,
                           nullable=False),
                    Column('amenity_id', String(60),
                           ForeignKey("amenities.id"),
                           primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """class place attributes"""
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", cascade="all, delete, delete-orphan",
                               backref="place")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 backref="place_amenities",
                                 viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        """func to initialize Place"""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """getting reviw inst for FileSt relation Place and Review"""
            stor_review = models.storage.all("Review").values()
            All_review = []
            for one_review in stor_review:
                if one_review.place_id == self.id:
                    All_review.append(one_review)
            return All_review

        @property
        def amenities(self):
            """getting Amenity inst for FileSt relation"""
            stor_amenity = models.storage.all("Amenity").values()
            All_amenity = []
            for one_amenity in stor_amenity:
                if one_amenity.place_id == self.id:
                    All_amenity.append(one_amenity)
            return All_amenity
