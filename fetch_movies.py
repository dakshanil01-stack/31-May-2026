import requests
import json
import os

API_KEY = os.environ.get("TMDB_API_KEY")
# Maine URL change kiya hai taaki 'popular' movies mile
BASE_URL = "https://api.themoviedb.org/3/movie/popular" 

def fetch_latest_movies():
    if not API_KEY:
        print("Error: API KEY nahi mili!")
        return

    response = requests.get(f"{BASE_URL}?api_key={API_KEY}&language=hi-IN&page=1")
    
    # Check karo ki response sahi hai ya nahi
    if response.status_code == 200:
        data = response.json()
        print(f"Data mil gaya! {len(data['results'])} movies mili.")
        
        movies_list = []
        for movie in data['results']:
            movies_list.append({
                "title": movie.get('title', 'N/A'),
                "poster": f"https://image.tmdb.org/t/p/w500{movie.get('poster_path', '')}",
                "year": movie.get('release_date', '0000')[:4],
                "rating": movie.get('vote_average', 0)
            })
        
        with open("movies.json", "w", encoding="utf-8") as f:
            json.dump(movies_list, f, ensure_ascii=False, indent=4)
        print("movies.json update ho gayi.")
    else:
        print(f"Error: API ne error diya - {response.status_code}")

if __name__ == "__main__":
    fetch_latest_movies()
