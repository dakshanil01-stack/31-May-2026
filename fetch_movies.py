import requests
import json
import os

# API Key github secrets se ayegi
API_KEY = os.environ.get("TMDB_API_KEY")
URL = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=hi-IN&page=1"

response = requests.get(URL)
if response.status_code == 200:
    data = response.json()
    movies = []
    for item in data['results']:
        movies.append({
            "title": item['title'],
            "poster": f"https://image.tmdb.org/t/p/w500{item['poster_path']}",
            "year": item['release_date'][:4]
        })
    with open("movies.json", "w", encoding="utf-8") as f:
        json.dump(movies, f, ensure_ascii=False, indent=4)
