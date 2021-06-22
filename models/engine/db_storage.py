#!/usr/bin/python3
""" """
import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State

user = os.getenv('HBNB_MYSQL_USER')
password = os.getenv('HBNB_MYSQL_PWD')
host = os.getenv('HBNB_MYSQL_HOST')
database = os.getenv('HBNB_MYSQL_DB')


class DBStorage():
    """new engine DBStorage"""
    __engine = None
    __session = None
    classname = {"User": User, "Place": Place, "State": State,
                 "City": City, "Amenity": Amenity, "Review": Review}

    def __init__(self):
        """Initiation"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host,
                                              database), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """query on the current database session for all objects"""
        new_dict = {}
        if not cls:
            for values in self.classname.values():
                for objs in self.__session.query(values):
                    new_dict[(objs.__class__.__name__ + '.' + objs.id)] = objs
        else:
            for objs in self.__session.query(cls):
                new_dict[(objs.__class__.__name__ + '.' + objs.id)] = objs
        return new_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database, create current database session
        """
        Base.metadata.create_all(self.__engine)
        new_sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(new_sess)
        self.__session = Session()

    def close(self):
        """
        Connections are returned to their connection
        pool and any transactional state is rolled back
        """
        if self.__session:
            self.__session.close()
