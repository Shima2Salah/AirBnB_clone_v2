#!/usr/bin/python3
""" Review Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """class review attributes"""
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'reviews'
        place_id = Column(String(60, collation='latin1_swedish_ci'),
                          ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60, collation='latin1_swedish_ci'),
                         ForeignKey("users.id"), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """func to initialize Reviews"""
        super().__init__(*args, **kwargs)
