import json

with open("fileTest/question.json", "r") as file:
    content = file.read()

data = json.loads(content)

for question in data: # print question to the screen
    print(question["question_text"])

    for index, alternatives in enumerate(question["alternatives"]):
        print(f"{index + 1} - {alternatives}")

    user_choice = int(input("Enter your answer (1-4): "))
    question["user_choice"] = user_choice

score = 0


for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score += 1
        result = "Correct"
    else:
        result = "Incorrect"

    print(
    f"Question {index + 1} - "
    f"Your answer is: {question['user_choice']}; "
    f"Correct answer is: {question['correct_answer']} - "
    f"Result: {result}"
)

print(f"Your final score is: {score}/{len(data)}")
print("\n")



        

