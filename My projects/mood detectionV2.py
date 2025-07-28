import re
from textblob import TextBlob


def detect_mood(text):
    """Detects mood from text input using keyword matching + sentiment analysis"""
    # Preprocess text
    text = text.lower().strip()

    # Mood keyword dictionaries (expandable)
    mood_keywords = {
        "Happy": ["happy", "joy", "excited", "great", "good", "yay", "awesome", "love", "laugh"],
        "Sad": ["sad", "unhappy", "cry", "depressed", "grief", "tear", "lonely"],
        "Angry": ["angry", "mad", "furious", "annoyed", "hate", "rage"],
        "Calm": ["calm", "peaceful", "relax", "chill", "serene", "tranquil"],
        "Anxious": ["anxious", "nervous", "worried", "stressed", "tense", "panic"]
    }

    # Count keyword matches
    mood_scores = {mood: 0 for mood in mood_keywords}
    for mood, keywords in mood_keywords.items():
        for keyword in keywords:
            mood_scores[mood] += len(re.findall(rf"\b{keyword}\b", text))

    # Sentiment analysis
    sentiment = TextBlob(text).sentiment.polarity

    # Determine result
    max_score = max(mood_scores.values())
    if max_score > 0:
        detected = [m for m, s in mood_scores.items() if s == max_score]
        primary_mood = detected[0]
    else:
        primary_mood = "Neutral"

    # Add sentiment nuance
    if sentiment < -0.5 and primary_mood == "Neutral":
        primary_mood = "Slightly Negative"
    elif sentiment > 0.5 and primary_mood == "Neutral":
        primary_mood = "Slightly Positive"

    return primary_mood


# Test the detector
if __name__ == "__main__":
    user_input = input("How are you feeling today? ")
    mood = detect_mood(user_input)
    print(f"Detected mood: {mood}")