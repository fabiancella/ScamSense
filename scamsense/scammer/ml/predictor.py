import joblib
import os

# Load the trained model from the 'ml' folder
MODEL_PATH = os.path.join(os.path.dirname(__file__), "scam_detector.pkl")

# Check if model exists
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"❌ Model file not found at {MODEL_PATH}. Train the model first!")

model = joblib.load(MODEL_PATH)

def detect_scam(message):
    """Predict if a message is a Scam or Legitimate, with confidence percentage."""
    prediction = model.predict([message])[0]
    confidence = model.predict_proba([message])[0]

    # Get probability of "Scam" class
    scam_index = list(model.classes_).index("Scam")  # Find the index of "Scam" in the model classes
    scam_probability = confidence[scam_index] * 100  # Convert to percentage

    return {"classification": prediction, "confidence": round(scam_probability, 2)}
