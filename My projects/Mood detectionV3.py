def mood_detector():
    """Interactive mood and depression screening tool with yes/no questions"""

    # Introduction
    print("🌼 Welcome to the Mood Detector! 🌼")
    print("Answer these 10 simple yes/no questions about how you've felt OVER THE PAST 2 WEEKS.")
    print("Be honest - this helps me understand you better!\n")

    # Questions based on PHQ-9 depression screening + mood assessment
    questions = [
        "Have you had little interest or pleasure in doing things?",
        "Have you been feeling down, depressed, or hopeless?",
        "Have you had trouble falling/staying asleep or sleeping too much?",
        "Have you been feeling tired or had little energy?",
        "Has your appetite been poor or have you been overeating?",
        "Have you been feeling bad about yourself or like a failure?",
        "Have you had trouble concentrating on things?",
        "Have you been moving/speaking slowly or been extra fidgety?",
        "Have you had thoughts of harming yourself in some way?",
        "Have you experienced moments of joy or happiness?"
    ]

    # Scoring system (points for "yes" answers)
    scores = [1, 1, 1, 1, 1, 1, 1, 1, 3, -2]  # Last question reduces depression score
    depression_levels = [
        "No significant depression",
        "Mild mood disturbance",
        "Mild depression",
        "Moderate depression",
        "Moderately severe depression",
        "Severe depression"
    ]

    total_score = 0
    answers = []

    # Ask questions
    for i, question in enumerate(questions):
        while True:
            answer = input(f"{i + 1}. {question} (y/n): ").lower()
            if answer in ['y', 'n']:
                answers.append(answer == 'y')
                if answers[-1]:  # If answered yes
                    total_score += scores[i]
                break
            print("Please answer with 'y' or 'n'")

    # Depression assessment
    depression_index = min(total_score // 3, 5)  # Convert score to 0-5 index
    depression_result = depression_levels[depression_index]

    # Mood pattern analysis
    mood_pattern = []
    if answers[0] and answers[1]: mood_pattern.append("loss of interest")
    if answers[2] and answers[3]: mood_pattern.append("low energy")
    if answers[4] and answers[6]: mood_pattern.append("appetite/focus issues")
    if answers[5] and answers[7]: mood_pattern.append("self-esteem concerns")
    if answers[9]: mood_pattern.append("positive moments")

    # Generate report
    print("\n🌟 Your Mood Analysis 🌟")
    print(f"Depression screening: {depression_result}")

    if mood_pattern:
        print("\nYour feelings pattern shows:")
        for pattern in mood_pattern:
            print(f"- {pattern.replace('/', ' and ')}")

    # Personalized insights
    print("\n🔍 Key observations:")
    if answers[8]:
        print("⚠️  Critical: You reported self-harm thoughts - please contact a professional immediately")
    elif total_score >= 9:
        print("• You're showing several depression signs - consider speaking with a counselor")
    elif total_score >= 6:
        print("• You're experiencing moderate distress - self-care would be beneficial")
    elif answers[9]:
        print("• You're experiencing positive moments - focus on these feelings")
    else:
        print("• Your mood seems generally stable")

    # Resources
    print("\n💡 Remember:")
    print("- This is not a diagnosis - just a mood snapshot")
    print("- Moods fluctuate normally - this reflects the past 2 weeks")
    print("- If concerned, contact a mental health professional")


# Run the detector
if __name__ == "__main__":
    mood_detector()