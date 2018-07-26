#!/usr/bin/python3
'''
    Define the class City.
'''
from models.base_model import BaseModel


class City(BaseModel):
    '''
        Define the class City that inherits from BaseModel.
    '''
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey(states.id), nullable=False)
    name = Column(String(128), nullable=False)
