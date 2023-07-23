import time

def ask_question(question, answer, choices=None):
    print(question)
    if choices:
        for i, choice in enumerate(choices, 1):
            print(f"{i}. {choice}")
        user_choice = int(input("Your choice (enter the corresponding number): "))
        user_answer = choices[user_choice - 1]
    else:
        user_answer = input("Your answer: ")

    if user_answer.lower() == answer.lower():
        print("Correct!")
        return True
    else:
        print("Wrong!")
        print("correct Answer=",answer)
        return False

def main():
    questions = [
        {
            "question": "What is the capital of France?",
            "answer": "Paris"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "answer": "Mars"
        },
        {
            "question": "What is the largest mammal in the world?",
            "answer": "Blue Whale"
        },
        {
            "question": "What is 12 multiplied by 8?",
            "answer": "96"
        },
        {
            "question": "What is the chemical symbol for water?",
            "answer": "H2O"
        }
    ]

    score = 0

    print("Welcome to the Quiz Game!")
    time.sleep(1)
    print("Answer the following questions:")
    time.sleep(1)

    for question in questions:
        time.sleep(0.5)
        result = ask_question(question["question"], question["answer"])
        if result:
            score += 1

    time.sleep(1)
    print(f"\nYour final score is: {score}/{len(questions)}")
    

if __name__ == "__main__":
    main()
