from django.shortcuts import render
from .utils import detect_scam  

def home(request):
    result = None

    if request.method == "POST":
        message = request.POST.get("message")  
        if message:
            result = detect_scam(message)  
            print("API Response:", result)

    return render(request, "home.html", {"result": result})

def analyze(request):
    result = None
    if request.method == "POST":
        message = request.POST.get("message")
        result = "This looks suspicious!" if "scam" in message.lower() else "Seems safe."

    return render(request, "home.html", {"result": result})

def contact(request):
    context = {}
    return render(request, "contact.html", context)
    