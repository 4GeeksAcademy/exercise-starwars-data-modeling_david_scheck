import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False)
    firstName = Column(String(255), nullable=False)
    lastName = Column(String(255), nullable=False)
    userName = Column(String(255), nullable=False)
    
    user_planet_favorites = relationship("UserPlanetFavorite", back_populates="user")
    user_character_favorites = relationship("UserCharacterFavorite", back_populates="user")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    population = Column(Integer)
    size = Column(Integer)

    user_planet_favorites = relationship("UserPlanetFavorite", back_populates="planet")

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    movies = Column(String(255))

    user_character_favorites = relationship("UserCharacterFavorite", back_populates="character")

class UserPlanetFavorite(Base):
    __tablename__ = 'user_planet_favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    
    user = relationship("User", back_populates="user_planet_favorites")
    planet = relationship("Planet", back_populates="user_planet_favorites")

class UserCharacterFavorite(Base):
    __tablename__ = 'user_character_favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    
    user = relationship("User", back_populates="user_character_favorites")
    character = relationship("Character", back_populates="user_character_favorites")

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e