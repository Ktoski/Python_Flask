from sqlalchemy.orm import sessionmaker
from tabledef import *


Session = sessionmaker(bind = engine)
session = Session()

user = User("Toyota", "1996")
session.add(user)

session.commit()