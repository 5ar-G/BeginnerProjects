import random

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)
running = True

print("------ROCK, PAPER, SCISSORS GAME------")
while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        print()
        player = input("Enter a choice (rock / paper / scissors): ").lower()
    print("-------------------------")
    print(f"Player: {player}")
    print(f"Computer: {computer}")
    print("-------------------------")

    if player == computer:
        print("It is a tie!")
        print("-------------------------")
    elif player == "rock" and computer == "scissors":
        print("Player wins!")
        print("-------------------------")
    elif player == "scissors" and computer == "paper":
        print("Player wins!")
        print("-------------------------")
    elif player == "paper" and computer == "rock":
        print("Player wins!")
        print("-------------------------")
    else:
        print("Player loses")
        print("-------------------------")
    
    if not input("PLAY AGAIN?(y/n):").lower() == "y":
        print("-------------------------")
        print("Thank you for playing.")
        running = False
