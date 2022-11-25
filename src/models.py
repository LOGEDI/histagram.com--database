import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email= Column(String(250),nullable=False)
    password = Column(String(250),nullable=False)
    followers_id = Column(Integer,ForeignKey('followers.id'))
    #user_id = Column(Integer,ForeignKey('user.id'))

class Followers(Base):
    __tablename__ = 'followers'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_following_id = Column(Integer, ForeignKey('user.id'))
    user_followed_id = Column(Integer, ForeignKey('user.id'))
    #username = Column(String(250))
    #password = Column(String(250), nullable=False)

    #user_id = Column(Integer,ForeignKey('user.id'))
    #email = Column(String(250),ForeignKey('email.id'))
   
   #followers_id = Column(Integer,ForeignKey('followers.id'))
    #person_id = Column(Integer, ForeignKey('person.id'))
    #person = relationship(Person)
class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, primary_key=True) 
    author_id = Column(String(250))
    follower_id =Column(String(250))
    user_id = Column(Integer,ForeignKey('user.id'))
   # followers_id = Column(Integer,ForeignKey('followers.id'))
    

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, primary_key=True) 
    author_id = Column (String(250))
    follower_id =Column(String(250))
    user_id = Column(Integer,ForeignKey('user.id'))
    comment_id = Column(Integer,ForeignKey(' comment.id'))
    #followers_id = Column(Integer,ForeignKey('followers.id'))
   # video = Column(String(250))
    #image = Column(String(250))
    #music = Column (String(250))
    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
