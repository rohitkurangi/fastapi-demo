##  for models.py file use for sqlalchemy  

from sqlalchemy import Column, Integer, String, ForeignKey
from blog.database import Base
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__ = 'blogs'    ## your table name
   
    ## if your database connection ok and  when you run your project fast api migrate your fields in  your respected db
    id = Column(Integer, primary_key=True, index=True)    
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship("User", back_populates="blogs")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship('Blog', back_populates="creator")   ## foreginkey key relation if u want
