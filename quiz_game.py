def run_quiz():
    questions = {
        "What is the capital of India? ": "delhi",
        "What is 5 + 3? ": "8",
        "Which language is used for AI? ": "python"
    }

    score = 0

    for question, answer in questions.items():
        user_answer = input(question).lower()
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    print("Your final score:", score)

if __name__ == "__main__":
    run_quiz()