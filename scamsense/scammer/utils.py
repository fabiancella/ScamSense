import requests

def detect_scam(message):
    payload = {"inputs": message, "parameters": {"candidate_labels": ["Scam", "Genuine"]}}
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        classification = result["labels"][0]
        confidence = f"{result['scores'][0] * 100:.2f}%"
        return {"classification": classification, "confidence": confidence}
    else:
        return {"error": f"API Error: {response.status_code}, {response.text}"}

message = input("Enter the message: ")
result = detect_scam(message)
print(f"Message: {message}\nResult: {result}\n")