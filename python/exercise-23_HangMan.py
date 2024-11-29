import random
#def global variables
words = ("apple", "orange", "bannana", "coconut", "pineapple")
hangman_art = { 0: ("   ",
                    "   ",
                    "   "),
                1: (" o ",
                    "   ",
                    "   "),
                2: (" o ",
                    " | ",
                    "   "),
                3: (" o ",
                    "/| ",
                    "   "),
                4: (" o ",
                    "/|\\",
                    "   "),
                5: (" o ",
                    "/|\\",
                    "/  "),
                6: (" o ",
                    "/|\\",
                    "/ \\"),}

#def functions
def display_man(wrong_guesses):
    print("___________ Hang Man ___________")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("--------------------------------")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

#Main part of program
def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if  guess in guessed_letters:
            print("You have already guessed this letter.")
        elif len(guess) != 1:
            print("Please enter a single letter.")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a letter from the alphabet.")
        else:
            guessed_letters.add(guess)
            if guess in answer:
                for i in range(len(answer)):
                    if answer[i] == guess:
                        hint[i] = guess
            else:
                wrong_guesses += 1
                if wrong_guesses == 6:
                    print("--------------------------------")
                    print("YOU LOST!")
                    print("--------------------------------")
                    is_running = False

        if "_" not in hint:
            print("--------------------------------")
            print("YOU WON!")
            print("--------------------------------")
            is_running = False

    


#run the program
if __name__ == "__main__":
    main()