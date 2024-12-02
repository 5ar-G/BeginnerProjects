import random

high = 100
low = 0
number = random.randint(low, high)
guesses = 0
is_running = True

print("--------PYTHON GUESSING GAME--------")
print()
while is_running:
    guess = input(f"Enter the number between {low} - {high}: ")
   
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < low or guess > high:
            print("-----------------------------")
            print(f"{guess} is out of range!")
            print(f"Please enter the number between {low} - {high}!")
            print("-----------------------------")
        elif guess < number:
            print("-----------------------------")
            print(f"{guess} is too low!")
            print("Please try again")
            print("-----------------------------")
        elif guess > number:
            print("-----------------------------")
            print(f"{guess} is too high!")
            print("Please try again")
            print("-----------------------------")
        else:
            print("-----------------------------")
            print(f"{guess} is CORRECT!")
            print(f"It took you {guesses} tries.")
            print("-----------------------------")
            is_running = False
    else:
        print("Invalid guess!")
        print(f"Please enter the number between {low} - {high}!")

