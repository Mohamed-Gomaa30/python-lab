from base import Base
from sqlalchemy import Integer,String, ForeignKey, Column 
from sqlalchemy.orm import relationship


class User(Base): 
    __tablename__ = "users"

    # what is this table? 
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String, unique=True ,nullable=True)
    
    tasks = relationship('Tasks', back_populates='user', cascade="all, delete-orphan")


class Tasks(Base): 
    __tablename__ = "tasks"

    id = Column(Integer, primary_key= True)
    title = Column(String(50), nullable=True)
    description = Column(String(200))
    user_id = Column(Integer, ForeignKey("users.id"))
    
    user = relationship('User', back_populates='tasks')



