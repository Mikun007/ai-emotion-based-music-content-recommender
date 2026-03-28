import requests
from config import YOUTUBE_API_KEY

def get_youtube_music(query):
    url = "https://www.googleapis.com/youtube/v3/search"

    params = {
        "part": "snippet",
        "q": query,
        "key": YOUTUBE_API_KEY,
        "maxResults": 6,
        "type": "video"
    }

    response = requests.get(url, params=params)
    data = response.json()

    results = []
    for item in data["items"]:
        video_id = item["id"]["videoId"]
        snippet = item["snippet"]

        results.append({
            "title": snippet["title"],
            "url": f"https://www.youtube.com/watch?v={video_id}",
            "thumbnail": snippet["thumbnails"]["medium"]["url"],
            "channel": snippet["channelTitle"]
        })

    return results