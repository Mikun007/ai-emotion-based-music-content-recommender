from config import CLIENT_ID
from config import CLIENT_SECRET

import requests
import base64

def get_access_token():
    url = "https://accounts.spotify.com/api/token"

    auth_str = f"{CLIENT_ID}:{CLIENT_SECRET}"
    b64_auth = base64.b64encode(auth_str.encode()).decode()

    headers = {
        "Authorization": f"Basic {b64_auth}"
    }

    data = {
        "grant_type": "client_credentials"
    }

    res = requests.post(url, headers=headers, data=data)

    print("TOKEN RESPONSE:", res.json())

    return res.json().get("access_token")


def get_spotify_music(query):
    try:
        token = get_access_token()

        if not token:
            return []

        headers = {
            "Authorization": f"Bearer {token}"
        }

        params = {
            "q": query,
            "type": "track",
            "limit": 5
        }

        response = requests.get(
            "https://api.spotify.com/v1/search",
            headers=headers,
            params=params,
            timeout=5
        )

        print("STATUS:", response.status_code)

        # 🔥 KEY FIX
        if response.status_code != 200:
            print("Spotify error:", response.text)
            return []

        # 🔥 SAFE JSON PARSE
        try:
            data = response.json()
        except Exception:
            print("Invalid JSON:", response.text)
            return []

        songs = []

        for item in data.get("tracks", {}).get("items", []):
            songs.append({
                "title": item["name"],
                "artist": item["artists"][0]["name"],
                "url": item["external_urls"]["spotify"],
                "thumbnail": item["album"]["images"][0]["url"]
            })

        return songs

    except Exception as e:
        print("Spotify Exception:", e)
        return []
