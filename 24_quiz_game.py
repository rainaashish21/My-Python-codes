questions = ("What is the temperature of normal human body(In celcius)?",
             "How many bones are in adult human body?",
             "How many Planets are in solar system?",
             "Which colour has maximum wavelength in visible spectrum?",
             "Which is the hardest element on the earth?")
options=(("A.37.2","B.12","C.45","D.20"),
         ("A.300","B.206","C.134","D.210"),
         ("A.10","B.6","C.13","D.8"),
         ("A.Blue","B.Grey","C.Maroon","D.Red"),
         ("A.Wood","B.Steel","C.Iron","D.Diamond"))

answers =("A","B","D","D","D")
guesses =[]
score =0
question_num=0

for question in questions:
    print("------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess= input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+=1
        print("Correct")
    else:
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer")
    question_num+=1

print("---------------------")
print("        Result       ")
print("---------------------")

print("Answers:",end=" ")
for answer in answers:
    print(answer,end=" ")
print()

print("Guesses:",end=" ")
for guess in guesses:
    print(guess,end=" ")
print()

score = int((score/len(questions))*100)
print(f"Your score is : {score}%")
