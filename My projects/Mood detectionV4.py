def mood_analyzer():
    print("\n🌟 Welcome to the Complete Mood Analyzer 🌟")
    print("I'll help you understand your feelings with different question types\n")

    # Initialize results dictionary
    results = {}

    # Section 1: Multiple-choice questions
    print("--- Lifestyle & Habits ---")
    results["energy"] = input(
        "How's your energy level?\nA) High energy\nB) Normal\nC) Low energy\nD) Completely drained\n> ").upper()

    results["interest"] = input(
        "\nHow interested are you in activities you usually enjoy?\nA) Very interested\nB) Somewhat interested\nC) Little interest\nD) No interest at all\n> ").upper()

    results["appetite"] = input(
        "\nHow has your appetite been?\nA) Normal hunger\nB) Eating more than usual\nC) Eating less than usual\nD) No appetite\n> ").upper()

    # Section 2: 1-10 intensity scale
    print("\n--- Intensity of Feelings (1-10) ---")
    print("1 = Not at all, 10 = Extremely intense")
    results["sadness"] = get_rating("How sad or down have you felt? ")
    results["anxiety"] = get_rating("How anxious or worried have you felt? ")
    results["irritability"] = get_rating("How irritable or easily annoyed? ")
    results["hope"] = get_rating("How hopeful about the future? ", reverse=True)
    results["self_worth"] = get_rating("How positive about yourself? ", reverse=True)

    # Section 3: Yes/No questions
    print("\n--- Recent Experiences (Yes/No) ---")
    results["sleep_issues"] = yes_no("Have you had trouble sleeping? ")
    results["concentration"] = yes_no("Have you had trouble focusing on tasks? ")
    results["crying"] = yes_no("Have you cried more than usual? ")
    results["social"] = yes_no("Have you avoided social interactions? ")
    results["enjoyment"] = yes_no("Have you enjoyed anything recently? ")
    results["self_harm"] = yes_no("Have you had thoughts of harming yourself? ")

    # Calculate depression risk score
    depression_score = calculate_depression_score(results)

    # Generate report
    print("\n\n🔍 Your Complete Mood Analysis 🔍")
    print("-------------------------------")

    # 1. Emotional state summary
    print("\n💭 Your Emotional State:")
    print(f"- Sadness level: {results['sadness']}/10")
    print(f"- Anxiety level: {results['anxiety']}/10")
    print(f"- Hopefulness: {results['hope']}/10")

    # 2. Key patterns
    print("\n📊 Detected Patterns:")
    if results['energy'] in ('C', 'D') and results['interest'] in ('C', 'D'):
        print("- Significant loss of energy and interest")
    if results['sadness'] >= 8 or results['hope'] <= 3:
        print("- Strong feelings of sadness/hopelessness")
    if results['appetite'] in ('C', 'D') and results['sleep_issues']:
        print("- Physical symptoms: Appetite and sleep disturbances")
    if results['enjoyment'] == 'No':
        print("- Lack of enjoyment in activities")

    # 3. Depression risk assessment
    depression_levels = [
        (5, "Minimal depression risk"),
        (10, "Mild depression symptoms"),
        (15, "Moderate depression"),
        (20, "Moderately severe depression"),
        (100, "Severe depression")
    ]
    depression_result = next(level for score, level in depression_levels if depression_score <= score)
    print(f"\n⚠️  Depression Risk: {depression_result} ({depression_score}/27)")

    # 4. Critical alerts
    if results['self_harm'] == 'Yes':
        print("\n🚨 CRITICAL: You reported thoughts of self-harm")
        print("Please contact a professional immediately:")
        print("National Suicide Prevention Lifeline: 1-800-273-8255")
    elif depression_score >= 15:
        print("\n❗ You're showing several depression signs")
        print("Consider speaking with a mental health professional")

    # 5. Personalized recommendations
    print("\n💡 Suggestions for Improvement:")
    if results['social'] == 'Yes' and results['enjoyment'] == 'No':
        print("- Try small social interactions with close friends/family")
    if results['energy'] in ('C', 'D'):
        print("- Light exercise like walking can boost energy")
    if results['sleep_issues'] == 'Yes':
        print("- Establish a regular sleep schedule")
    if depression_score < 10:
        print("- Practice gratitude journaling to maintain positive mindset")

    print("\nRemember: This is not a diagnosis. Seek professional help if concerned.")


def get_rating(prompt, reverse=False):
    """Get 1-10 rating with validation"""
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 10:
                return 11 - value if reverse else value
            print("Please enter a number between 1-10")
        except ValueError:
            print("Invalid input. Enter a number 1-10")


def yes_no(prompt):
    """Get Yes/No answer with validation"""
    while True:
        answer = input(prompt).strip().capitalize()
        if answer in ('Yes', 'Y', 'No', 'N'):
            return 'Yes' if answer in ('Yes', 'Y') else 'No'
        print("Please answer 'Yes' or 'No'")


def calculate_depression_score(results):
    """Calculate depression risk based on responses"""
    score = 0

    # Energy and interest
    score += {'A': 0, 'B': 1, 'C': 2, 'D': 3}[results['energy']]
    score += {'A': 0, 'B': 1, 'C': 2, 'D': 3}[results['interest']]

    # Appetite
    score += {'A': 0, 'B': 1, 'C': 2, 'D': 3}[results['appetite']]

    # Intensity scores
    score += max(0, results['sadness'] - 5) // 2  # 0-2.5 points
    score += max(0, results['self_worth'] - 5) // 2  # Reverse scored
    score += max(0, (10 - results['hope']) - 5) // 2  # Reverse scored

    # Yes/No questions
    score += 2 if results['sleep_issues'] == 'Yes' else 0
    score += 2 if results['concentration'] == 'Yes' else 0
    score += 2 if results['crying'] == 'Yes' else 0
    score += 2 if results['social'] == 'Yes' else 0
    score += -1 if results['enjoyment'] == 'Yes' else 1  # Reverse scoring
    score += 4 if results['self_harm'] == 'Yes' else 0

    return min(27, score)  # Cap at max score


# Run the analyzer
if __name__ == "__main__":
    mood_analyzer()