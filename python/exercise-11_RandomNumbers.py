import random

low = 1
high = 100
guesses = 0
number = random.randint(low, high)

while True:
    guess = int(input(f"Enter the number between {low} - {high}: "))
    guesses +=1

    if guess < number:
        print(f"{guess} is too low!")
    elif guess > number:
        print(f"{guess} is too high!")
    else:
        print("----------------------")
        print()
        print(f"{guess} is correct!")
        break
print()
print("--------RESULT--------")
print(f"It took you {guesses} tries to guess")
print("----------------------")