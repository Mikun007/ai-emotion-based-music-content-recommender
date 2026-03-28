from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
import os

from utils.emotion import predict_emotion
from utils.youtube_api import get_youtube_music
from utils.spotify_api import get_spotify_music

# Initialize Flask
app = Flask(__name__)
# Only allow frontend URL for CORS
CORS(app, origins=["https://ai-emotion-based-music-content-reco.vercel.app"])

# Simple root route
@app.route("/")
def home():
    return "Backend running 🚀"

# Map emotions to search queries
emotion_to_query = {
    "happy": "happy songs",
    "sad": "sad songs",
    "angry": "calm music",
    "surprise": "party songs",
    "neutral": "trending songs",
    "fear": "motivational music",
    "disgust": "chill songs"
}

# Main detect route
@app.route("/detect", methods=["POST"])
def detect():
    try:
        # Check if image is sent
        if "image" not in request.files:
            return jsonify({"error": "No image uploaded"}), 400

        file = request.files["image"]

        # Decode image
        img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
        if img is None:
            return jsonify({"error": "Invalid image"}), 400

        # Predict emotion
        emotion = predict_emotion(img)
        query = emotion_to_query.get(emotion, "trending songs")

        # Get YouTube songs
        try:
            youtube_songs = get_youtube_music(query)
        except Exception as e:
            print("YouTube API error:", e)
            youtube_songs = []

        # # Get Spotify songs (if fails, just return empty list)
        # try:
        #     spotify_songs = get_spotify_music(query)
        # except Exception as e:
        #     print("Spotify API error:", e)
        #     spotify_songs = []

        # Always return YouTube songs even if Spotify fails
        return jsonify({
            "emotion": emotion,
            "songs": youtube_songs,
            # "spotify": spotify_songs
        })

    except Exception as e:
        print("Backend error:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))