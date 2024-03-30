#!/usr/bin/python3
""" City Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60, collation='utf8mb4_0900_ai_ci'),
                          ForeignKey("states.id"),
                          nullable=False)
        places = relationship("Place", cascade="all, delete, delete-orphan",
                                backref="cities")
    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        """func to initialize city class"""
        super().__init__(*args, **kwargs)
