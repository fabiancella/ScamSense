import os
import requests
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Settings
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
API_KEY = os.getenv("HF_API_KEY")  # Get API key securely

HEADERS = {"Authorization": f"Bearer {API_KEY}"}

def detect_scam(message):
    labels = ["Scam", "Genuine"]  # Categories for classification
    payload = {
        "inputs": message,
        "parameters": {"candidate_labels": labels}
    }

    for attempt in range(5):  # Retry up to 5 times
        response = requests.post(API_URL, headers=HEADERS, json=payload)

        if response.status_code == 200:
            result = response.json()
            print("RAW API RESPONSE:", result)

            if "labels" in result and "scores" in result:
                classification = result["labels"][0]
                confidence = result["scores"][0] * 100  # Convert to percentage
                return {"classification": classification, "confidence": confidence}
            else:
                return {"error": "Unexpected API response format"}

        elif response.status_code == 503:
            try:
                estimated_time = response.json().get("estimated_time", 60)  # Default to 60 sec
                print(f"⚠️ Model is loading... Waiting {estimated_time:.2f} seconds before retrying.")
                time.sleep(estimated_time)  # Wait before retrying
            except Exception:
                time.sleep(60)  # If parsing fails, wait 60 sec

        elif response.status_code == 401:
            return {"error": "❌ Unauthorized! Check API key!"}

        else:
            return {"error": f"Error: {response.status_code}, {response.text}"}

    return {"error": "API failed after 5 attempts"}
