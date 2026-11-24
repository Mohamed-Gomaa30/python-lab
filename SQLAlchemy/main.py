from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.exc import IntegrityError
from tables import User, Tasks
from base import Base


# Create Database 
engine = create_engine("sqlite:///data/tasks.db", echo=False)

# create a session to link to the engine 
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)


# queries 
try:
    session.add(User(name="Mohamed", email="mohamed.gomaa.elsafy@gmail.com"))
    session.commit()
except IntegrityError as e: 
    print(f"Error: {e}")

