import random

responses = {
    "greeting": ["Hello! How are you feeling today?", "Hi there! How can I help you today?"],
    "positive": ["That's good to hear!", "Glad to hear you're doing well."],
    "negative": ["I'm sorry to hear that. Would you like to talk about what's bothering you?", "It's okay to not be okay. I'm here to listen."],
    "mental_health_resources": ["Here are some resources that might help:\n1. National Suicide Prevention Lifeline: 1-800-273-TALK (8255)\n2. Crisis Text Line: Text HOME to 741741\n3. NAMI Helpline: 1-800-950-NAMI (6264)"],
    "gratitude": ["You're welcome!", "Anytime. Take care."],
    "farewell": ["Goodbye! Take care of yourself.", "Until next time. Remember, you're not alone."]
}

def get_sentiment(text):
    """
    Perform basic sentiment analysis on the input text.
    Returns: 'positive', 'negative', or 'neutral'
    """
    positive_words = ["happy", "good", "great", "fine", "well"]
    negative_words = ["sad", "bad", "depressed", "anxious", "stressed"]
    
    if any(word in text for word in positive_words):
        return "positive"
    elif any(word in text for word in negative_words):
        return "negative"
    else:
        return "neutral"

def fetch_mental_health_quote():
    """
    Fetch a random mental health quote from a list.
    Returns: Quote string
    """
    quotes = [
        "You are not alone. You are loved.",
        "It's okay to ask for help when you need it.",
        "Your mental health is just as important as your physical health.",
        "Every day may not be good, but there is something good in every day.",
        "Be kind to yourself. You're doing the best you can.",
    ]
    return random.choice(quotes)

def chat():
    print("Welcome to the Mental Health Chatbot!")
    print("Type 'bye' to exit the chat.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "bye":
            print(random.choice(responses["farewell"]))
            break
        sentiment = get_sentiment(user_input)
        if sentiment == "positive":
            print(random.choice(responses["positive"]))
        elif sentiment == "negative":
            print(random.choice(responses["negative"]))
        elif "mental health" in user_input:
            print(random.choice(responses["mental_health_resources"]))
        elif "thank" in user_input or "thanks" in user_input:
            print(random.choice(responses["gratitude"]))
        elif "quote" in user_input:
            print("Here's a mental health quote for you:\n", fetch_mental_health_quote())
        else:
            print("I'm not sure how to respond to that. Can you please rephrase?")

chat()