from sqlalchemy import (
    ForeignKey,
    create_engine,
    Column,
    String,
    Integer,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///musicLibrary.db")

Base = declarative_base()


class Artist(Base):
    __tablename__ = "artists"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    songs = relationship("Song", secondary="publishes", backref="artists")

    def __repr__(self):
        return f"\n \
            <id: {self.id}>, \n \
            <name: {self.name}>"


class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    genre = Column(String())
    # artists = relationship("Artist", secondary="publishes", backref="publishes")
    users = relationship("User", secondary="saves", backref="songs")

    def __repr__(self):
        return f"\n \
            <name: {self.name}>, \n \
            <genre: {self.genre}>"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    age = Column(Integer())
    nationality = Column(String())

    def __repr__(self):
        return f"\n \
            <id: {self.id}>, \n \
            <name: {self.name}>, \n \
            <age: {self.age}>, \n \
            <nationality: {self.nationality}>"


class Publish(Base):
    __tablename__ = "publishes"

    id = Column(Integer(), primary_key=True)
    artist_id = Column(Integer(), ForeignKey("artists.id"))
    song_id = Column(Integer(), ForeignKey("songs.id"))

    def __repr__(self):
        return f"\n \
            <id: {self.id}>, \n \
            <name: {self.name}>, \n \
            <artist_id: {self.artist_id}>,\n \
            <song_id: {self.song_id}>"


class Save(Base):
    __tablename__ = "saves"

    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey("users.id"))
    song_id = Column(Integer(), ForeignKey("songs.id"))

    def __repr__(self):
        return f"\n \
            <id: {self.id}>, \n \
            <user_id: {self.user_id}>, \n \
            <song_id: {self.song_id}>"
