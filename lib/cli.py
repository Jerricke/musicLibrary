from sqlalchemy.orm import sessionmaker
from sqlalchemy import delete
from models import engine, Artist, Publish, Song, Save, User

import inquirer
from pyfiglet import Figlet
import time

Session = sessionmaker(bind=engine)
session = Session()


class menuDirectory:
    def artists(self, notUsed=None):
        q = session.query(Artist).order_by(Artist.name).all()
        artistOptions = ["<<MAIN MENU>>", "<<ADD ARTIST>>"]
        for n in q:
            artistOptions.append(n.name)
        action = inquirer.list_input("Select Artist", choices=artistOptions)
        artistDict = {
            "<<MAIN MENU>>": self.menuSelect,
            "<<ADD ARTIST>>": self.addArtist,
        }
        artistDict.get(action, self.artistInfo)(action)

    def artistInfo(self, action):
        q = session.query(Artist).filter(Artist.name == action).first()
        print(
            f" \n \
                    Artist's Name: {action}"
        )
        print("=" * 100)  # Underscore
        if len(q.songs) > 0:
            for n in q.songs:
                print(
                    f" \n \
                    Song name: {n.name} \n \
                    Song genre: {n.genre} \n"
                )
                print("_" * 100)  # Underscore
        else:
            print("This artist does not have any songs :( \n")
            action2 = inquirer.list_input(
                "Would you like to add a song?", choices=["Yes", "No"]
            )
            actDict = {"Yes": self.addSong, "No": self.passer}
            actDict.get(action2)(action)
        deleteP = inquirer.list_input("Nav", choices=["Back", "Delete Artist"])
        deleteDict = {"Delete Artist": self.deleteArtist, "Back": self.artists}
        deleteDict.get(deleteP)(action)

    def songs(self):
        q = session.query(Song).order_by(Song.name).all()
        songOptions = ["<<MAIN MENU>>", "<<ADD SONG>>", "<<DELETE SONG>>"]
        for n in q:
            songOptions.append(n.name)
        action = inquirer.list_input("All songs", choices=songOptions)
        songDict = {
            "<<MAIN MENU>>": self.menuSelect,
            "<<ADD SONG>>": self.addSong,
            "<<DELETE SONG>>": self.deleteSong,
        }
        songDict.get(action, self.songInfo)(action)

    def deleteSong(self, notUsed=None):
        q = session.query(Song).order_by(Song.name).all()
        songOptions = []
        for n in q:
            songOptions.append(n.name)
        action = inquirer.list_input("All songs", choices=songOptions)

        q1 = session.query(Song).filter_by(name=action).first()
        session.delete(q1)
        session.commit()

        self.songs()

        print("* Song Deleted * \n")

    def deleteArtist(self, action):
        q1 = session.query(Artist).filter_by(name=action).first()

        for n in q1.songs:
            session.delete(n)
        session.delete(q1)
        session.commit()
        print("* Artist Deleted * \n")
        self.artists()

    def songInfo(self, action):
        q = session.query(Song).filter(Song.name == action).first()
        # print(q)
        if q.artists:
            art = q.artists[0].name
        else:
            art = "No Artist"
        print(
            f" \n \
            Song name: {q.name} \n \
            Song genre: {q.genre} \n \
            Song artist: {art}"
        )
        print("_" * 100)  # Underscore
        input("Hit enter to return to song menu")
        self.songs()

    def users(self, notUsed=None):
        q = session.query(User).order_by(User.name).all()
        userOptions = ["<<MAIN MENU>>", "<<ADD USER>>"]
        for n in q:
            userOptions.append(n.name)
        action = inquirer.list_input("All users", choices=userOptions)
        userDict = {
            "<<MAIN MENU>>": self.menuSelect,
            "<<ADD USER>>": self.addUser,
        }
        userDict.get(action, self.userNav)(action)

    def userNav(self, action):
        q = session.query(User).filter(User.name == action).first()
        print(
            f" \n \
                    User's name: {q.name} \n \
                    User's age: {q.age} \n \
                    User's Nationality: {q.nationality}"
        )
        print("=" * 100)  # Underscore

        action2 = inquirer.list_input(
            "Select",
            choices=["Back", "Saved Songs", "Save New Song", "Delete Saved Song"],
        )
        userDict = {
            "Saved Songs": self.userInfo,
            "Save New Song": self.saveNewSong,
            "Delete Saved Song": self.deleteSavedSong,
            "Back": self.users,
        }

        userDict.get(action2)(action)
        pass

    def userInfo(self, action):
        q = session.query(User).filter(User.name == action).first()
        if len(q.songs) > 0:
            for n in q.songs:
                print(
                    f" \n \
                    Song name: {n.name} \n \
                    Song genre: {n.genre} \n \
                    Song artist: {n.artists[0].name}"
                )
                print("_" * 100)  # Underscore
            input("Hit enter to return to user menu")
        else:
            print("This user does not have any songs saved :( \n")
            input("Hit enter to return to user menu")
        self.userNav(action)

    def saveNewSong(self, action):
        q = session.query(Song).order_by(Song.name).all()
        options = []
        for n in q:
            options.append(n.name)
        songPicked = inquirer.list_input("All songs", choices=options)

        q1 = session.query(User).filter(User.name == action).first()
        q2 = session.query(Song).filter(Song.name == songPicked).first()
        saveSong = Save(song_id=q2.id, user_id=q1.id)

        session.add(saveSong)
        session.commit()

        self.userNav(action)

    def deleteSavedSong(self, action):
        q = session.query(User).filter_by(name=action).first()

        deleteOpt = []
        for n in q.songs:
            deleteOpt.append(n.name)
        deleteP = inquirer.list_input("Select Song To Delete", choices=deleteOpt)

        print(deleteP)
        q1 = session.query(Song).filter_by(name=deleteP).first()
        print(q1)
        q2 = session.query(Save).filter_by(user_id=q.id, song_id=q1.id).first()
        print(q2)
        session.delete(q2)
        session.commit()
        print("* Song Deleted * \n")
        self.userNav(action)

    def addArtist(self, notUsed=None):
        newName = str(input("Please input an artist name: "))
        if isinstance(newName, str) and len(newName) > 0:
            newArtist = Artist(name=newName.lower())
            session.add(newArtist)
            session.commit()
        else:
            print("Error: Please input a string of greater than one character!")
        print("* added Artist * \n")
        self.artists()

    def addUser(self, notUsed=None):
        newName = str(input("Please input new user's name: "))
        newAge = int(input("Please input new user's age: "))
        newNat = str(input("Please input new user's nationality: "))
        if len(newName) > 0 and newAge > 0 and len(newNat) > 0:
            newUser = User(name=newName.title(), age=newAge, nationality=newNat.title())
            session.add(newUser)
            session.commit()
        else:
            print(
                "Error: Please input valid name(string), age(integer), nationality(string)!"
            )
        print("* added new user * \n")
        self.users()

    def addSong(self, notUsed=None):
        newName = str(input("Please input new song name: "))
        newGenre = str(input("Please input the new song's genre: "))

        q = session.query(Artist).order_by(Artist.name).all()
        options = []
        for n in q:
            options.append(n.name)
        qArtist = inquirer.list_input("Select Artist", choices=options)

        if len(newName) > 0 and len(newGenre) > 0:
            newSong = Song(name=newName.title(), genre=newGenre)
            session.add(newSong)
            session.commit()

        q1 = session.query(Song).filter(Song.name == newName.title()).first()
        q2 = session.query(Artist).filter(Artist.name == qArtist).first()
        newPublish = Publish(artist_id=q2.id, song_id=q1.id)
        session.add(newPublish)
        session.commit()

        print("* added Song * \n")
        self.songs()

    def menuSelect(self, notUsed=None):
        action = inquirer.list_input(
            "Main Menu", choices=["Artists", "Songs", "Users", "Exit"]
        )
        menuDict = {
            "Artists": self.artists,
            "Songs": self.songs,
            "Users": self.users,
        }
        menuDict.get(action, self.exit)()

    def exit(self):
        print(f.renderText("Thank you for using Poorman's Spotify"))

    def passer(self, notUsed=None):
        pass


if __name__ == "__main__":
    f = Figlet(font="big")
    print(f.renderText("Poorman's Spotify"))
    time.sleep(1)
    print(f.renderText("Loading"))
    for _ in range(6):
        f = Figlet(font="small")
        print(f.renderText("."))
        time.sleep(0.35)

    menu = menuDirectory()
    menu.menuSelect()
