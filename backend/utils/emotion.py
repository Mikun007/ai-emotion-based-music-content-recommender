import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model("model/best_emotion_model.keras")

emotion_labels = ["angry", "disgust", "fear", "happy", "sad", "surprise", "neutral"]

def predict_emotion(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (48, 48))
    normalized = resized / 255.0
    reshaped = np.reshape(normalized, (1, 48, 48, 1))

    prediction = model.predict(reshaped)
    return emotion_labels[np.argmax(prediction)]