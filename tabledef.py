from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///tutorial.db', echo = True)
Base = declarative_base()
 
########################################################################
class User(Base):
    """"""
    __tablename__ = "users"
 
    id = Column(Integer, primary_key = True)
    username = Column(String)
    password = Column(String)
 
    #----------------------------------------------------------------------
    def __init__(self, username, password):
        """"""
        self.username = username
        self.password = password

class Car(Base):
    """"""
    __tablename__ = "cars"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    year = Column(String)

    def __init__(self, name, year):
        """"""
        self.name = name
        self.year = year

# create tables
Base.metadata.create_all(engine)