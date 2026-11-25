# 1. Questions aur answers ko list of dictionaries mein store karna
questions = [
    {
        "question": "Which keyword is used to define a function?",
        "answer": "def"
    },
    {
        "question": "Which data type stores key-value pairs?",
        "answer": "dictionary"
    },
    {
        "question": "Which loop is used to iterate over a sequence?",
        "answer": "for"
    }
]

def run_quiz(question_bank):
    score = 0
    total_questions = len(question_bank)

    print("===== PYTHON QUIZ =====\n")

    # 2. Har question ko for loop se display karna
    for index, item in enumerate(question_bank, start=1):
        print(f"Q{index}: {item['question']}")
        
        # 3. User se answer input lena (.strip() extra spaces hatata hai)
        user_answer = input("Your answer: ").strip()

        # 4. if/else se check karna ke answer correct hai ya wrong
        if user_answer.lower() == item["answer"].lower():
            print("Correct!\n")
            # 5. Har correct answer par score mein 1 add karna
            score += 1
        else:
            print(f"Wrong! Correct answer: {item['answer']}\n")

    # 6. Quiz complete hone par final score display karna
    wrong_answers = total_questions - score
    print("===== QUIZ RESULT =====\n")
    print(f"Correct Answers: {score}")
    print(f"Wrong Answers: {wrong_answers}")
    print(f"Final Score: {score}/{total_questions}")

# Program ko run karna
run_quiz(questions)