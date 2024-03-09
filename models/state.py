#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete, delete-orphan",
                              backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """func to initialize state"""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """getting City inst for FileSt relation State and City"""

            all_cities = models.storage.all("City").values()
            related_cities = []
            for city in all_cities:
                if city.state_id == self.id:
                    related_cities.append(city)
            return related_cities
