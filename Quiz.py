# Welcome Message
print("Welcome to the Python Quiz Game!")
print("Answer the questions by typing the option letter (a, b, c, or d).")
print("Let's begin!\n")

# Questions, Options, and Answers
quiz = [
    {
        "question": "What is the capital of India?",
        "options": ["a) Mumbai", "b) Delhi", "c) Chennai", "d) Kolkata"],
        "answer": "b"
    },
    {
        "question": "Who developed Python?",
        "options": ["a) Dennis Ritchie", "b) James Gosling", "c) Guido van Rossum", "d) Bjarne Stroustrup"],
        "answer": "c"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["a) func", "b) def", "c) function", "d) create"],
        "answer": "b"
    }
]

# Initialize Score
score = 0

# Quiz Logic
for q in quiz:
    print(q["question"])
    for option in q["options"]:
        print(option)
    user_answer = input("Your answer: ").lower()
    if user_answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was {q['answer']}.\n")

# Final Score
print(f"Quiz Over! You scored {score}/{len(quiz)}.")