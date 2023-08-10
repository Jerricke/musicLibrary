from models import engine, Artist, Publish, Song, Save, User
import random
from faker import Faker
from faker.providers import BaseProvider
from sqlalchemy.orm import sessionmaker
import requests
import math as m


if __name__ == "__main__":
    Session = sessionmaker(bind=engine)
    session = Session()
    fake = Faker()

    session.query(Artist).delete()
    session.query(Publish).delete()
    session.query(Song).delete()
    session.query(Save).delete()
    session.query(User).delete()

    url = "https://theaudiodb.p.rapidapi.com/track-top10.php"
    headers = {
        "X-RapidAPI-Key": "e47623508emsh383f932cc8b3ca9p1c0b5djsn6ca516bc61c0",
        "X-RapidAPI-Host": "theaudiodb.p.rapidapi.com",
    }

    # querystring = {"s": "taylor swift"}

    # response = requests.get(url, headers=headers, params=querystring)

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

    artistToFetch = [
        "taylor swift",
        "coldplay",
        "the weeknd",
        "adele",
        "bruno mars",
    ]

    artists = []
    for a in artistToFetch:
        artist = Artist(name=a)
        session.add(artist)
        session.commit()
        artists.append(artist)

    responses = []
    songs = []
    publishes = []
    for idx, a in enumerate(artistToFetch):
        response = requests.get(url, headers=headers, params={"s": f"{a}"})
        responses.append(response.json()["track"])
        res = response.json()["track"]

        newSongs = []
        for s in res:
            song = Song(
                name=s.get("strTrack"),
                genre=s.get("strGenre"),
            )
            session.add(song)
            session.commit()
            songs.append(song)
            newSongs.append(song)

        for s in newSongs:
            publish = Publish(
                artist_id=artists[idx].id,
                song_id=s.id,
            )
            session.add(publish)
            session.commit()
            publishes.append(publish)

    users = []
    for _ in range(20):
        user = User(
            name=f"{fake.first_name()} {fake.last_name()}",
            age=f"{random.randint(12, 70)}",
            nationality=f"{fake.nationality_provider()}",
        )
        session.add(user)
        session.commit()
        users.append(user)

    saves = []
    for n in users:
        for _ in range(random.randint(1, 10)):
            save = Save(song_id=random.choice(songs).id, user_id=n.id)
            session.add(save)
            session.commit()
            saves.append(save)
