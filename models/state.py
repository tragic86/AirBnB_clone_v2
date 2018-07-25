#!/usr/bin/python3
'''
    Define the class State.
'''

from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    '''
        Define the class State that inherits from BaseModel and Base
    '''
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
