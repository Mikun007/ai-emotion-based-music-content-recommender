import cv2
import numpy as np
from tensorflow.keras.models import load_model
from huggingface_hub import hf_hub_download

model_path = hf_hub_download(
    repo_id="Budhadev/best-emotion-model",
    filename="best_emotion_model.keras"
)

model = load_model(model_path)

emotion_labels = ["angry", "disgust", "fear", "happy", "sad", "surprise", "neutral"]

def predict_emotion(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (48, 48))
    normalized = resized / 255.0
    reshaped = np.reshape(normalized, (1, 48, 48, 1))

    prediction = model.predict(reshaped)
    return emotion_labels[np.argmax(prediction)]