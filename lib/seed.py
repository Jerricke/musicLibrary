from models import engine, Artist, Album, Song, Save, User
import random
from faker import Faker
from faker.providers import BaseProvider
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    Session = sessionmaker(bind=engine)
    session = Session()
    fake = Faker()

    session.query(Artist).delete()
    session.query(Album).delete()
    session.query(Song).delete()
    session.query(Save).delete()
    session.query(User).delete()

    class NewProvider(BaseProvider):
        def nationality_provider(self):
            return random.choice(
                [
                    "Afghan",
                    "Albanian",
                    "Algerian",
                    "American",
                    "Andorran",
                    "Angolan",
                    "Antiguans",
                    "Argentinean",
                    "Armenian",
                    "Australian",
                    "Austrian",
                    "Azerbaijani",
                    "Bahamian",
                    "Bahraini",
                    "Bangladeshi",
                    "Barbadian",
                    "Barbudans",
                    "Batswana",
                    "Belarusian",
                    "Belgian",
                    "Beninese",
                    "Bhutanese",
                    "Bolivian",
                    "Bosnian",
                    "Brazilian",
                    "British",
                    "Bruneian",
                    "Bulgarian",
                    "Burkinabe",
                    "Burmese",
                    "Burundian",
                    "Cambodian",
                    "Cameroonian",
                    "Canadian",
                    "Cape Verdean",
                    "Central African",
                    "Chadian",
                    "Chilean",
                    "Chinese",
                    "Colombian",
                    "Comoran",
                    "Congolese",
                    "Costa Rican",
                    "Croatian",
                    "Cuban",
                    "Cypriot",
                    "Czech",
                    "Danish",
                    "Djibouti",
                    "Dominican",
                    "Dutch",
                    "East Timorese",
                    "Ecuadorean",
                    "Egyptian",
                    "Emirian",
                    "Equatorial Guinean",
                    "Eritrean",
                    "Estonian",
                    "Ethiopian",
                    "Fijian",
                    "Filipino",
                    "Finnish",
                    "French",
                    "Gabonese",
                    "Gambian",
                    "Georgian",
                    "German",
                    "Ghanaian",
                    "Greek",
                    "Grenadian",
                    "Guatemalan",
                    "Guinea-Bissauan",
                    "Guinean",
                    "Guyanese",
                    "Haitian",
                    "Herzegovinian",
                    "Honduran",
                    "Hungarian",
                    "I-Kiribati",
                    "Icelander",
                    "Indian",
                    "Indonesian",
                    "Iranian",
                    "Iraqi",
                    "Irish",
                    "Israeli",
                    "Italian",
                    "Ivorian",
                    "Jamaican",
                    "Japanese",
                    "Jordanian",
                    "Kazakhstani",
                    "Kenyan",
                    "Kittian and Nevisian",
                    "Kuwaiti",
                    "Lebanese",
                    "Liberian",
                    "Libyan",
                    "Liechtensteiner",
                    "Lithuanian",
                    "Luxembourger",
                    "Macedonian",
                    "Malagasy",
                    "Malawian",
                    "Malaysian",
                    "Maldivian",
                    "Malian",
                    "Maltese",
                    "Marshallese",
                    "Mauritanian",
                    "Mauritian",
                    "Mexican",
                    "Micronesian",
                    "Moldovan",
                    "Monacan",
                    "Mongolian",
                    "Moroccan",
                    "Mosotho",
                    "Motswana",
                    "Mozambican",
                    "Namibian",
                    "Nauruan",
                    "Nepalese",
                    "New Zealander",
                    "Ni-Vanuatu",
                    "Nicaraguan",
                    "Nigerian",
                    "Nigerien",
                    "North Korean",
                    "Northern Irish",
                    "Norwegian",
                    "Omani",
                    "Pakistani",
                    "Palauan",
                    "Panamanian",
                    "Papua New Guinean",
                    "Paraguayan",
                    "Peruvian",
                    "Polish",
                    "Portuguese",
                    "Qatari",
                    "Romanian",
                    "Russian",
                    "Rwandan",
                    "Saint Lucian",
                    "Salvadoran",
                    "Samoan",
                    "San Marinese",
                    "Sao Tomean",
                    "Saudi",
                    "Scottish",
                    "Senegalese",
                    "Serbian",
                    "Seychellois",
                    "Sierra Leonean",
                    "Singaporean",
                    "Slovakian",
                    "Slovenian",
                    "Solomon Islander",
                    "Somali",
                    "South African",
                    "South Korean",
                    "Spanish",
                    "Sri Lankan",
                    "Sudanese",
                    "Surinamer",
                    "Swazi",
                    "Swedish",
                    "Swiss",
                    "Syrian",
                    "Taiwanese",
                    "Tajik",
                    "Tanzanian",
                    "Thai",
                    "Togolese",
                    "Tongan",
                    "Trinidadian or Tobagonian",
                    "Tunisian",
                    "Turkish",
                    "Tuvaluan",
                    "Ugandan",
                    "Ukrainian",
                    "Uruguayan",
                    "Uzbekistani",
                    "Venezuelan",
                    "Vietnamese",
                    "Welsh",
                    "Yemenite",
                    "Zambian",
                    "Zimbabwean",
                ]
            )

    fake.add_provider(NewProvider)

    artists = []
    for _ in range(10):
        artist = Artist(
            name=f"{fake.first_name()} {fake.last_name()}",
            age=f"{random.randint(12, 70)}",
            nationality=f"{fake.nationality_provider()}",
        )
        session.add(artist)
        session.commit()
        artists.append(artist)

    songs = []
    for _ in range(100):
        song = Song(
            name=f"{fake.sentence(nb_words=3)}",
            genre=f'{random.choice(["Pop","Hip hop","Rock","Rhythm and blues","Soul","Reggae","Country","Funk","Folk","Jazz","Disco","Classical","Electronic","Blues","New age","Christian","Traditional","Ska","Indian classical","Metal","Brazilian","Flamenco","Salsa","Merengue","Bachata"])}',
        )
        session.add(song)
        session.commit()
        songs.append(song)

    users = []
    for _ in range(30):
        user = User(
            name=f"{fake.first_name()} {fake.last_name()}",
            age=f"{random.randint(12, 70)}",
            nationality=f"{fake.nationality_provider()}",
        )
        session.add(user)
        session.commit()
        users.append(user)

    albums = []
    for n in artists:
        index = 0
        album_name = f"{fake.sentence(nb_words=1)}"
        for s in range(5):
            album = Album(
                name=album_name,
                artist_id=random.choice(artists).id,
                song_id=songs[index].id,
            )
            index += 1
            session.add(album)
            session.commit()
            albums.append(album)

    saves = []
    for n in users:
        for _ in range(random.randint(1, 10)):
            save = Save(song_id=random.choice(songs).id, user_id=n.id)
            session.add(save)
            session.commit()
            saves.append(save)
