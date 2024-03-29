#!/usr/bin/python3
"""Module to store data in db"""
from os import getenv
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """to deal with Mysql db """
    __engine = None
    __session = None

    def __init__(self):
        """to initialize db engine and create session"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST', 'localhost')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            user, pwd, host, db), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Return a dict of all obj in storage depending on cls"""
        elemnts = {}
        all_classes = (User, State, City, Amenity, Place, Review)
        if cls:
            my_query = self.__session.query(cls).all()
            for elem in my_query:
                elem_key = '{}.{}'.format(elem.__class__.__name__, elem.id)
                elemnts[elem_key] = elem
        else:
            for one_cls in all_classes:
                my_query = self.__session.query(one_cls).all()
                for elem in my_query:
                    elem_key = '{}.{}'.format(elem.__class__.__name__, elem.id)
                    elemnts[elem_key] = elem
        return elemnts

    def new(self, obj):
        """to add new object to storage"""
        self.__session.add(obj)
        return self

    def save(self):
        """to save and commit changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """to delete an object"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """to reloads data from db"""
        Base.metadata.create_all(self.__engine)
        factory_ses = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory_ses)
        self.__session = Session()

    def close(self):
        """to remove private session"""
        self.__session.close()
