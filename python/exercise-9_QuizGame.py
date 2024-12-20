questions = ( 
    ("What are you?"), 
    ("What is your name?"),
    ("How old are you?"), 
    ("Where were you born?"))


options = (
    ("A: Man", "B: Woman", "C: Dog, Cat, ext..",),
    ("A: Petar", "B: Josip", "C: Luka",),
    ("A: <18", "B: 18", "C: >18",),
    ("A: RH", "B: RS", "C: BiH",)
    )

answers = ("A", "A", "B", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------------")
    print(question)
    print()
    for option in options[question_num]:
        print(option)
    print("----------------------------")
    guess = input("Enter your guess: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        print("----------------------------")
        print("Corret!")
        score+=1
    else:
        print("----------------------------")
        print("Incorrect!")
        print(f"{answers[question_num]} is correct answer.")
    question_num+=1

print("----------------------------")
print("           ANSWERS          ")
print("----------------------------")

print("Answers:", end=" ")
for answer in answers:
    print(answer, end=" ")
print()
print("Guesses:", end=" ")
for guess in guesses:
    print(guess, end= " ")
print()
print("----------------------------")
print("           SCORE            ")
print()
score= int(score / len(questions) * 100)
print(f"Your score is: {score}%")
print("----------------------------")
