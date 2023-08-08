from sqlalchemy import (
    ForeignKey,
    create_engine,
    Column,
    String,
    Integer,
    Float,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///musicLibrary.db")

Base = declarative_base()


class Artist(Base):
    __tablename__ = "artists"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    age = Column(Integer())
    nationality = Column(String())

    def __repr__(self):
        return f"\n \
            <id: {self.id} \n \
            <name: {self.name} \n \
            <age: {self.age} \n \
            <nationality: {self.nationality} "


class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    genre = Column(String())

    def __repr__(self):
        return f"\n \
            <id: {self.id} \n \
            <name: {self.name} \n \
            <genre: {self.genre}"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    age = Column(Integer())
    nationality = Column(String())

    def __repr__(self):
        return f"\n \
            <id: {self.id} \n \
            <name: {self.name} \n \
            <age: {self.age} \n \
            <nationality: {self.nationality} "


class Album(Base):
    __tablename__ = "albums"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    artist_id = Column(Integer(), ForeignKey("artists.id"))
    artist = relationship("Artist", backref="albums")
    song_id = Column(Integer(), ForeignKey("songs.id"))
    song = relationship("Song", backref="albums")

    def __repr__(self):
        return f"\n \
            <id: {self.id} \n \
            <name: {self.name} \n \
            <artist_id: {self.artist_id} \n \
            <song_id: {self.song_id}"


class Save(Base):
    __tablename__ = "saves"

    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey("users.id"))
    user = relationship("User", backref="saves")
    song_id = Column(Integer(), ForeignKey("songs.id"))
    song = relationship("Song", backref="saves")

    def __repr__(self):
        return f"\n \
            <id: {self.id} \n \
            <user_id: {self.user_id} \n \
            <song_id: {self.song_id}"
