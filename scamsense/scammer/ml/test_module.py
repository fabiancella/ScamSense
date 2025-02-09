import joblib

# Load trained model
model = joblib.load("scam_detector.pkl")

def detect_scam(message):
    prediction = model.predict([message])[0]
    return prediction

# Test the model
test_message = input("Enter a message to check for scams: ")
result = detect_scam(test_message)
print(f"🔍 Scam Detection Result: {result}")