
class MoodDetector:
    def __init__(self):
        self.questions = {
            "Are you feeling happy?": "happy",
            "Are you feeling sad or depressed?": "sad",
            "Are you feeling anxious or stressed?": "anxious",
            "Are you feeling excited or enthusiastic?": "excited",
            "Are you feeling tired or fatigued?": "tired",
            "Are you feeling angry or irritated?": "angry",
            "Are you feeling bored or unenthusiastic?": "bored",
            "Are you feeling grateful or appreciative?": "grateful",
            "Are you feeling scared or fearful?": "scared",
            "Are you feeling surprised or astonished?": "surprised"
        }

    def detect_mood(self):
        mood_scores = {
            "happy": 0,
            "sad": 0,
            "anxious": 0,
            "excited": 0,
            "tired": 0,
            "angry": 0,
            "bored": 0,
            "grateful": 0,
            "scared": 0,
            "surprised": 0
        }

        for question, mood in self.questions.items():
            answer = input(question + " (yes/no): ")
            while answer.lower() not in ["yes", "no"]:
                answer = input("Invalid input. Please enter 'yes' or 'no': ")
            if answer.lower() == "yes":
                mood_scores[mood] += 1

        max_score = max(mood_scores.values())
        detected_moods = [mood for mood, score in mood_scores.items() if score == max_score]

        if len(detected_moods) == 1:
            return detected_moods[0]
        else:
            return "Mixed emotions"

def main():
    detector = MoodDetector()
    print("Mood Detector")
    print("-------------")
    mood = detector.detect_mood()
    print(f"Detected mood: {mood}")

if __name__ == "__main__":
    main()