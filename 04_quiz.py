quiz = {
    "questions" : ["Who was the violinist at Jake and Amy's wedding?", "Who was the character in the pilot episode who got cut?", "How many episodes were in the final season?"], 
    "answers" : [["mlepnos"],["detective daniels", "daniels"],["10", "ten", "ten episodes", "10 episodes"]]
}

for i in range(len((quiz["questions"]))):
    print(quiz["questions"][i])
    attempted_answer = input("What is the answer?: ")
    if attempted_answer.lower() in quiz["answers"][i]:
        print(f"Correct! the answer was {quiz["answers"][i]}.")