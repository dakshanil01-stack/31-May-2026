import requests
import json
import os

# Render ke environment variable se API Key lega
API_KEY = os.environ.get("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3/movie/now_playing"

def fetch_latest_movies():
    # TMDB se data mangwao
    response = requests.get(f"{BASE_URL}?api_key={API_KEY}&language=hi-IN&page=1")
    data = response.json()
    
    movies_list = []
    for movie in data['results']:
        movies_list.append({
            "title": movie['title'],
            "poster": f"https://image.tmdb.org/t/p/w500{movie['poster_path']}",
            "year": movie['release_date'][:4],
            "rating": movie['vote_average']
        })
    
    # Data ko JSON file mein save karo
    with open("movies.json", "w", encoding="utf-8") as f:
        json.dump(movies_list, f, ensure_ascii=False, indent=4)
    print("Movies updated successfully!")

if __name__ == "__main__":
    fetch_latest_movies()
