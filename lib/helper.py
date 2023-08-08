from sqlalchemy.orm import sessionmaker
from models import engine, Artist, Album, Song, Save, User

Session = sessionmaker(bind=engine)
session = Session()

songs = session.query(Song).all()

for n in songs:
    print(n.saves)

# print(dir(songs[0]))
