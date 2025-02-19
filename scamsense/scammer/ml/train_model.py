from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Sample dataset (More data = better accuracy)
messages = [
    "You've just won a $500 gift card! Click here to claim it now.",
    "Your account has been locked. Click here to unlock it immediately.",
    "Limited time offer: Claim your free vacation! Click now to reserve your spot.",
    "Your Amazon account has been compromised. Please verify your identity to restore access.",
    "Alert: Unusual activity detected on your bank account. Click here to secure it.",
    "Final notice: Your PayPal account has been suspended. Restore it by clicking here.",
    "Congratulations! You've been selected for a free iPhone. Claim it now before it expires.",
    "Urgent: Your credit card is about to expire. Verify your information immediately.",
    "You’ve been pre-approved for a $10,000 loan! Apply now to receive the funds.",
    "Security alert: Someone has logged into your account. Click here to secure it.",
    "Congratulations! You've been approved for a personal loan. Apply now for instant approval.",
    "Your Google account has been flagged for suspicious activity. Verify your details.",
    "Alert: Your Netflix account has been compromised. Reset your password immediately.",
    "Urgent: Your bank account is at risk. Click here to verify your account details.",
    "We’ve noticed fraudulent charges on your credit card. Click here to dispute them.",
    "Important: Your iCloud account will be deleted soon. Click here to confirm your identity.",
    "Final warning: Your account has been suspended. Click here to reactivate it.",
    "Your email account has been hacked. Reset your password immediately to regain control.",
    "We've detected suspicious activity on your account. Click here to restore access.",
    "Congratulations! You’ve won a prize! Click here to claim your $200 gift card.",
    
    "Your Amazon order has been shipped. You can track it with the provided tracking number.",
    "Thank you for your payment. Your subscription has been successfully renewed.",
    "Your flight booking is confirmed. You will receive your itinerary via email shortly.",
    "You have a new message on LinkedIn. Check it out to see what a recruiter had to say.",
    "Your Netflix subscription has been successfully renewed. Enjoy your streaming experience.",
    "Security alert: A new login to your Google account was detected. Was this you?",
    "Reminder: Your PayPal payment of $75 has been successfully processed.",
    "Your account settings have been updated successfully. If you didn’t make these changes, please contact support.",
    "Your Spotify subscription has been renewed for the next month. Enjoy your music!",
    "Your bank statement is now available. Log in to view your transactions for the month.",
    "Your Amazon package will be delivered tomorrow. Track your shipment using the tracking number.",
    "Your payment to PayPal has been successfully received. You’ve received $50 from John Doe.",
    "Your email account settings have been updated. If you didn’t make this change, please contact support.",
    "Your shipping address has been successfully updated. Your order will be shipped shortly.",
    "You’ve received a refund of $100 for your recent purchase on eBay. Check your account for details.",
    "Your order from Walmart has been successfully processed. Thank you for your purchase.",
    "Your bank account balance is now available. Log in to view your recent transactions.",
    "You have a new profile view on LinkedIn. Check out who is interested in your profile.",
    "Security alert: A new device has signed into your Apple ID. If this wasn’t you, please review your account activity.",
    "Your New York Times subscription has been renewed. Thank you for staying with us!",
    "You’ve successfully signed up for our newsletter. Stay tuned for exciting updates and offers."
]



# Set to align with messages array
labels = [
    "scam",  # "You've just won a $500 gift card! Click here to claim it now."
    "scam",  # "Your account has been locked. Click here to unlock it immediately."
    "scam",  # "Limited time offer: Claim your free vacation! Click now to reserve your spot."
    "scam",  # "Your Amazon account has been compromised. Please verify your identity to restore access."
    "scam",  # "Alert: Unusual activity detected on your bank account. Click here to secure it."
    "scam",  # "Final notice: Your PayPal account has been suspended. Restore it by clicking here."
    "scam",  # "Congratulations! You've been selected for a free iPhone. Claim it now before it expires."
    "scam",  # "Urgent: Your credit card is about to expire. Verify your information immediately."
    "scam",  # "You’ve been pre-approved for a $10,000 loan! Apply now to receive the funds."
    "scam",  # "Security alert: Someone has logged into your account. Click here to secure it."
    "scam",  # "Congratulations! You've been approved for a personal loan. Apply now for instant approval."
    "scam",  # "Your Google account has been flagged for suspicious activity. Verify your details."
    "scam",  # "Alert: Your Netflix account has been compromised. Reset your password immediately."
    "scam",  # "Urgent: Your bank account is at risk. Click here to verify your account details."
    "scam",  # "We’ve noticed fraudulent charges on your credit card. Click here to dispute them."
    "scam",  # "Important: Your iCloud account will be deleted soon. Click here to confirm your identity."
    "scam",  # "Final warning: Your account has been suspended. Click here to reactivate it."
    "scam",  # "Your email account has been hacked. Reset your password immediately to regain control."
    "scam",  # "We've detected suspicious activity on your account. Click here to restore access."
    "scam",  # "Congratulations! You’ve won a prize! Click here to claim your $200 gift card."
    
    "legitimate",  # "Your Amazon order has been shipped. You can track it with the provided tracking number."
    "legitimate",  # "Thank you for your payment. Your subscription has been successfully renewed."
    "legitimate",  # "Your flight booking is confirmed. You will receive your itinerary via email shortly."
    "legitimate",  # "You have a new message on LinkedIn. Check it out to see what a recruiter had to say."
    "legitimate",  # "Your Netflix subscription has been successfully renewed. Enjoy your streaming experience."
    "legitimate",  # "Security alert: A new login to your Google account was detected. Was this you?"
    "legitimate",  # "Reminder: Your PayPal payment of $75 has been successfully processed."
    "legitimate",  # "Your account settings have been updated successfully. If you didn’t make these changes, please contact support."
    "legitimate",  # "Your Spotify subscription has been renewed for the next month. Enjoy your music!"
    "legitimate",  # "Your bank statement is now available. Log in to view your transactions for the month."
    "legitimate",  # "Your Amazon package will be delivered tomorrow. Track your shipment using the tracking number."
    "legitimate",  # "Your payment to PayPal has been successfully received. You’ve received $50 from John Doe."
    "legitimate",  # "Your email account settings have been updated. If you didn’t make this change, please contact support."
    "legitimate",  # "Your shipping address has been successfully updated. Your order will be shipped shortly."
    "legitimate",  # "You’ve received a refund of $100 for your recent purchase on eBay. Check your account for details."
    "legitimate",  # "Your order from Walmart has been successfully processed. Thank you for your purchase."
    "legitimate",  # "Your bank account balance is now available. Log in to view your recent transactions."
    "legitimate",  # "You have a new profile view on LinkedIn. Check out who is interested in your profile."
    "legitimate",  # "Security alert: A new device has signed into your Apple ID. If this wasn’t you, please review your account activity."
    "legitimate",  # "Your New York Times subscription has been renewed. Thank you for staying with us!"
    "legitimate"   # "You’ve successfully signed up for our newsletter. Stay tuned for exciting updates and offers."
]



pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),  # Convert text to numbers
    ('classifier', MultinomialNB()) 
])

# Train the model
pipeline.fit(messages, labels)

# Save the trained model
joblib.dump(pipeline, "scam_detector.pkl")

print("✅ Scam detection model trained & saved as 'scam_detector.pkl'!")


