from django.shortcuts import render
from .ml.predictor import detect_scam  


def home(request):
    result = None
    confidence = None
    if request.method == "POST":
        message = request.POST.get("message", "").strip()  
        
        if message:  # Ensure message is not empty
            prediction = detect_scam(message)  # Call ML model

            # Ensure prediction is a valid dictionary before using it
            if isinstance(prediction, dict) and "classification" in prediction and "confidence" in prediction:
                result = prediction["classification"]  # "Scam" or "Legitimate"
                confidence = prediction["confidence"]  # Scam probability %
            else:
                result = "Error: Invalid prediction response"
    
    return render(request, "home.html", {"result": result, "confidence": confidence})

def analyze(request):
    result = None
    if request.method == "POST":
        message = request.POST.get("message")
        result = "This looks suspicious!" if "scam" in message.lower() else "Seems safe."

    return render(request, "home.html", {"result": result})

def contact(request):
    context = {}
    return render(request, "contact.html", context)
    