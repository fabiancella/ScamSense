from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Sample dataset (More data = better accuracy)
messages = [
    "You've won a free iPhone! Click here to claim your prize.",
    "Your order has been shipped. Tracking number: 123456.",
    "Verify your bank account now to avoid suspension!",
    "Reminder: Your Netflix subscription has been renewed.",
    "Your PayPal account has been compromised! Reset your password now."
]

# Set to align with messages array
labels = ["Scam", "Legitimate", "Scam", "Legitimate", "Scam"]

pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),  # Convert text to numbers
    ('classifier', MultinomialNB()) 
])

# Train the model
pipeline.fit(messages, labels)

# Save the trained model
joblib.dump(pipeline, "scam_detector.pkl")

print("✅ Scam detection model trained & saved as 'scam_detector.pkl'!")


