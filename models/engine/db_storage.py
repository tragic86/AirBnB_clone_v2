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

from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from sqlalchemy import scoped_session

class DBStorage():
    '''
        Database Engine
    '''
    self.__engine = None
    self.__session = None

    def __init__(self):
    '''
        initializes the engine
    '''
        user = os.getenv('HBNB_MYSQL_USER')
        pw = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
        user, pw, host, db, pool_pre_ping=True))
        Base.metadata.create_all(self.__engine)
    
        session_factory = sessionmaker(bind=self.__engine)
        Session = scoped_session(session_factory)
        sesh = Session()
