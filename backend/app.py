from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import cv2
import numpy as np

from utils.emotion import predict_emotion
from utils.youtube_api import get_youtube_music
from utils.spotify_api import get_spotify_music

app = Flask(__name__, static_folder="../frontend/dist", static_url_path="/")
CORS(app, origins=["https://ai-emotion-based-music-content-reco.vercel.app"])

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
    try:
        if "image" not in request.files:
            return jsonify({"error": "No image uploaded"}), 400

        file = request.files["image"]

        img = cv2.imdecode(
            np.frombuffer(file.read(), np.uint8),
            cv2.IMREAD_COLOR
        )

        if img is None:
            return jsonify({"error": "Invalid image"}), 400

        emotion = predict_emotion(img)
        query = emotion_to_query.get(emotion, "trending songs")

        youtube_songs = get_youtube_music(query)

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

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500

import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))