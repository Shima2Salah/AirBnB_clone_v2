#!/usr/bin/python3
"""class for all amenities data"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import models
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel, Base):
    """ The Amenity class, contains name """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """func to initialize amenity class"""
        super().__init__(*args, **kwargs)
