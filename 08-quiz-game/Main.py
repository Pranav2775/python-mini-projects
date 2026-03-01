# Quiz Game

questions = ("how many elements are in periodic table ?:",
             "whih animal lay the largest egg ?:",
             "what are the abundant gas in the atmosphere?:",
             "how many bones in a human body?:",
             "which planet in the solar system is the hottest?:")

options = (("A.116","B.117","C.118","D.119"),
           ("A.whale","B.crocodile","C.elephant","D.ostrich"),
           ("A.nitrogen","B.oxygen","C.carbondioxide","D.hydrogen"),
           ("A.206","B.207","C.208","D.209"),
           ("A.Mercury","B.Venus","C.Earth","D.Mars"))

answers = ("C","D","A","A","B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("enter(A,B,C,D) : ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("correct")
    else:
        print("incorrect")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1


print("--------------------------------------------")
print("result")
print("--------------------------------------------")

print("answers : ",end = " ")
for answer in answers:
    print(answer,end = " ")
print()

print("guesses : ",end = " ")
for guess in guesses:
    print(guess,end = " ")
print()

score = int(score/ len(questions)*100)
print(f"your score is: {score}%")