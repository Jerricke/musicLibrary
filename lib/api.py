import requests

url = "https://theaudiodb.p.rapidapi.com/track-top10.php"

querystring = {"s": "taylor swift"}

headers = {
    "X-RapidAPI-Key": "e47623508emsh383f932cc8b3ca9p1c0b5djsn6ca516bc61c0",
    "X-RapidAPI-Host": "theaudiodb.p.rapidapi.com",
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
