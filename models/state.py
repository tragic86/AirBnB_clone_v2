#!/usr/bin/python3
'''
    Implementation of the State class
'''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
import models

class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    places = relationship("City", cascade="all, delete-orphan", backref="state")

    @property
    def cities(self):
        """getter"""
        getit = models.storage.all("City")
        for i in getit:
            if i.state_id == self.id:
                return i
