#!/usr/bin/python3
'''
    DB Storage
'''
from models.base_model import BaseModel, Base
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from sqlalchemy import scoped_session

class DBStorage:
    '''
        Database Engine
    '''
    __engine = None
    __session = None

    def __init__(self):
        '''
        initializes the engine
        '''
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user = os.getenv('HBNB_MYSQL_USER')
            pw = os.getenv('HBNB_MYSQL_PWD')
            host = os.getenv('HBNB_MYSQL_HOST')
            db = os.getenv('HBNB_MYSQL_DB')
            env = os.getenv('HBNB_ENV')),
                                      pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
    
        session_factory = sessionmaker(self.__engine)
        self.__session = session_factory()

    def all(self, cls=None):
        """ Returns objects in dictionary format
            depending on the class name, if given.
            Otherwise, returns all objects in database
        """
        list_obj = {}
        if cls:
            for obj in self.__session.query(cls).all()
            key = str(obj.__class__.__name__) + "." + str(obj.id)
            list_obj[key] = obj

        else:
            others = [User, State, City, Amenity, Place, Review]
            for name in others:
                for name in self.__session.query(others).all():
                    key = str(name.__class__.__name__) + "." + str(name.id)
                    list_obj[key] = name
        return newkey

    def new(self, obj):
        """add to session"""
        self.__session.add(obj)


    def save(self):
        """save session"""
        self.__session.commit()

    def delete(self, obj=None):
        """remove obj from session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reload session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, 
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)
