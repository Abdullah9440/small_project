import random

questions = [
    "What is 2 + 2?",
    "What is the capital of Bangladesh?",
    "How many days are there in a week?",
    "What is 5 * 5?",
    "What color is the sky?",
    "How many months are there in a year?",
    "What is 10 - 3?",
    "What is the opposite of hot?",
    "How many legs does a cat have?",
    "What is 3 + 4?"
]

answers = [
    "4",
    "Dhaka",
    "7",
    "25",
    "blue",
    "12",
    "7",
    "cold",
    "4",
    "7"
]

score = 0
select = random.sample(range(10),4)
for i in select:
    print(questions[i])
    user_input = input('enter your answer')
    if user_input.lower() == answers[i].lower():
        score +=1
print("You got", score, "out of 4 correct.")