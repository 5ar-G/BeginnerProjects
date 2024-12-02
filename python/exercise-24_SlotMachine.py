import random

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("----------------")
    print(" | ".join(row))
    print("----------------")

def get_payout(row, bet):
    if row[0] == row[1]  == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet *5
        elif row[0] == "🔔":
            return bet *10
        elif row[0] == "⭐":
            return bet *100
    return 0
        
def main():
    balance = 100
    print("******** PYTHON SLOT MACHINE ********\n")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("***********************************")

    while balance > 0:
        print("_______________________________")
        print(f"Current balance: ${balance}")
        print("-------------------------------")
        bet = input("Place your bet amount: $")
        
        if not bet.isdigit():
            print("Please eneter a valid number!")
            continue

        bet = float(bet)

        if bet > balance:
            print("Insufficient funds!")
            continue

        if bet <= 0:
            print("Bet must be greater than 0!")
            continue
        
        balance -= bet

        row = spin_row()
        print("SPINNING...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
            print("_______________________________")
        else:
            print("Sorry you lost this round")
            print("_______________________________")

        balance += payout

        play_again = input("Do you want to spin again(y/n)?: ").lower()

        if play_again != "y":
            break
    print("***************** GAME OVER! *****************\n")
    print(f"Your final balance is ${balance}")
    print("**********************************************")
    last_input=input("")
if __name__ == '__main__':
    main()