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

import cv2
import numpy as np

# Load the pre-trained Haar Cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def predict_emotion(img):
    # 1. Convert to grayscale for detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 2. Detect faces (returns x, y, w, h for each face)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    
    # 3. Process the first detected face (if any)
    for (x, y, w, h) in faces:
        # Crop the face region from the grayscale image
        roi_gray = gray[y:y+h, x:x+w]
        
        # 4. Existing preprocessing on the cropped face
        resized = cv2.resize(roi_gray, (48, 48))
        normalized = resized / 255.0
        reshaped = np.reshape(normalized, (1, 48, 48, 1))

        # 5. Predict emotion
        prediction = model.predict(reshaped)
        return emotion_labels[np.argmax(prediction)]
    
    return "No Face Detected"
