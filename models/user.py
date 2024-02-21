#!/usr/bin/python3
""" User Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
import models
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """class user attributes"""
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship("Place", cascade="all, delete, delete-orphan",
                               backref="user")
        reviews = relationship("Review", cascade="all, delete, delete-orphan",
                                backref="user")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''

    def __init__(self, *args, **kwargs):
        """to initialize user class"""
        super().__init__(*args, **kwargs)
