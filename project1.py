def questions():
    return [
        {
            "question": "what is the capital of Italy?",
            "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
            "answer": "C"
        },
        {
            "question": "What company was originally called 'Cadabra'?",
            "options": ["A. Apple", "B. Amazon", "C. Flipkart", "D. Netflix "],
            "answer": "B"
        },
        {
            "question": "Which planet has the most moons?",
            "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
            "answer": "D"
        }
    ]

def answer():
    while True:
        answer = input("Your answer: ").upper()
        if answer in ["A", "B", "C", "D"]:
            return answer
        else:
            print("Invalid input. Please choose A, B, C, or D.")

def quiz_game():
    question = questions()
    score = 0
    print("Welcome to the Quiz Game!")
    for q in question:
        print(q["question"])
        for opt in q["options"]:
            print(opt)
        user_answer = answer()
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.")
        print()

    print(f"Your final score is {score}/{len(question)}.")

def main():
    quiz_game()

if __name__ == "__main__":
    main()
