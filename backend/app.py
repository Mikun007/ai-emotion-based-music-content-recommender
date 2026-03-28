from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS, cross_origin
import cv2
import numpy as np
import os

from utils.emotion import predict_emotion
from utils.youtube_api import get_youtube_music
from utils.spotify_api import get_spotify_music

app = Flask(__name__, static_folder="dist", static_url_path="")
CORS(app)

@app.route("/")
@cross_origin()
def home():
    return send_from_directory(app.static_folder, "index.html")

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
@cross_origin()
def detect():
    try:
        if "image" not in request.files:
            return jsonify({"error": "No image uploaded"}), 400

        file = request.files["image"]
        img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
        print("Image shape:", img.shape if img is not None else None)
        if img is None:
            return jsonify({"error": "Invalid image"}), 400

        try:
            emotion = predict_emotion(img)
        except Exception as e:
            print("Emotion prediction failed:", e)
            emotion = "neutral"
        query = emotion_to_query.get(emotion, "trending songs")

        # YouTube always tries
        try:
            youtube_songs = get_youtube_music(query)
        except Exception as e:
            print("YouTube error:", e)
            youtube_songs = []
        print("Received request:", request.files.keys())
        # Spotify protected
        # try:
        #     spotify_songs = get_spotify_music(query)
        # except Exception as e:
        #     print("Spotify error:", e)
        #     spotify_songs = []

        return jsonify({
            "emotion": emotion,
            "songs": youtube_songs,
            # "spotify": spotify_songs
        })

    except Exception as e:
        print("Backend error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)