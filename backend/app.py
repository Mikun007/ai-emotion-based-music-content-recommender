from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np

from utils.emotion import predict_emotion
from utils.youtube_api import get_youtube_music
from utils.spotify_api import get_spotify_music

app = Flask(__name__)
CORS(app)

emotion_to_query = {
    "happy": "happy songs",
    "sad": "sad songs",
    "angry": "calm music",
    "surprise": "party songs",
    "neutral": "trending songs",
    "fear": "motivational music",
    "disgust": "chill songs"
}

@app.route("/detect", methods=["POST"])
def detect():
    file = request.files["image"]
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)

    emotion = predict_emotion(img)
    query = emotion_to_query[emotion]

    youtube_songs = get_youtube_music(query)

    # 🔥 Protect Spotify call
    try:
        spotify_songs = get_spotify_music(query)
    except Exception as e:
        print("Spotify crashed:", e)
        spotify_songs = []
    return jsonify({
        "emotion": emotion,
        "songs": youtube_songs,
        "spotify": spotify_songs
    })

if __name__ == "__main__":
    app.run(debug=True)