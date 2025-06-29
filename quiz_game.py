questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 5 + 3?", "answer": "8"},
    {"question": "What is the largest planet in the solar system?", "answer": "Jupiter"}
]

def start_quiz():
    score = 0
    print("Welcome to the Quiz Game!")
    for q in questions:
        print(q["question"])
        user_answer = input("Your answer: ")
        if user_answer.lower() == q["answer"].lower():
            score += 1
            print("Correct!")
        else:
            print("Incorrect!")
    print(f"You got {score}/{len(questions)} correct!")

if __name__ == "__main__":
    start_quiz()
