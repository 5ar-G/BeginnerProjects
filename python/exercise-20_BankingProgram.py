
def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter the amount to deposit: $"))

    if amount < 0:
        print("-------------------------------------------")
        print("That is not valid amount!")
        print("-------------------------------------------")
        return 0
    else:
        return amount 

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: $"))
    if amount > balance:
        print("-------------------------------------------")
        print("Insufficient funds!")
        print("-------------------------------------------")
        return 0
    elif amount < 0:
        print("-------------------------------------------")
        print("That is not valid amount!")
        print("-------------------------------------------")
        return 0
    else:
        return amount

def main():

    balance = 0
    is_running = True

    while is_running:
        print("--------------Banking Program--------------")
        print("")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("-------------------------------------------")
        print("")
        choice = input("Enter your choice: ")
        print("-------------------------------------------")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("Invalid choice!")
            print("-------------------------------------------")

   
    print("THANK YOU, HAVE A NICE DAY!.")
    print("-------------------------------------------")

if __name__ == '__main__':
    main()